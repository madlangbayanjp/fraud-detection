import streamlit as st
import pandas as pd
import joblib

model = joblib.load('random_forest_fraud_model.pkl')

st.title("Fraud Detection Prediction")
st.markdown("Enter the transaction details below:")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=0.0)

if st.button("Predict"):
    # Create the base input data
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])
    
    # Add the engineered features that the model expects
    input_data['amount_to_oldbalanceOrg'] = input_data['amount'] / (input_data['oldbalanceOrg'] + 1)
    input_data['amount_to_newbalanceOrig'] = input_data['amount'] / (input_data['newbalanceOrig'] + 1)
    input_data['newbalanceOrig_zero_transfer_cashout'] = ((input_data['newbalanceOrig'] == 0) & 
                                                          (input_data['type'].isin(['TRANSFER', 'CASH_OUT']))).astype(int)
    input_data['newbalanceDest_zero_transfer_cashout'] = ((input_data['newbalanceDest'] == 0) & 
                                                          (input_data['type'].isin(['TRANSFER', 'CASH_OUT']))).astype(int)
    input_data['transfer_amount'] = input_data['amount'] * (input_data['type'] == 'TRANSFER').astype(int)
    input_data['cashout_amount'] = input_data['amount'] * (input_data['type'] == 'CASH_OUT').astype(int)

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result: '{int(prediction)}'")

    if prediction == 1:
        st.success("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")