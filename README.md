# Fraud Detection with Random Forest

A machine learning-powered fraud detection system built with Random Forest algorithm and deployed using Streamlit.

## 🚀 Features

- **Real-time Fraud Detection**: Predict fraudulent transactions instantly
- **Interactive Web Interface**: Easy-to-use Streamlit dashboard
- **Multiple Transaction Types**: Supports PAYMENT, TRANSFER, CASH_OUT, DEBIT, CASH_IN
- **Advanced Feature Engineering**: Uses engineered features for better accuracy

## 🛠️ Technologies Used

- **Python 3.12**
- **Scikit-learn 1.6.1** (Random Forest)
- **Streamlit** (Web Interface)
- **Pandas** (Data Processing)
- **Joblib** (Model Serialization)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fraud-detection-random-forest.git
cd fraud-detection-random-forest
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📊 Dataset

The dataset used for training the model is not included in this repository due to its large size. You can download the dataset from the following link:

- [Financial Transaction Dataset](https://www.kaggle.com/datasets/dalpozz/creditcard-fraud)

After downloading the dataset, place it in the project directory and update the file path in the code accordingly.

## 🚀 Usage

1. Run the Streamlit app:
```bash
streamlit run fraud_detection.py
```

2. Open your browser and go to `http://localhost:8501`

3. Enter transaction details and click "Predict" to get fraud detection results

## 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: Financial transaction dataset with engineered features
- **Features Used**:
  - Transaction type, amount, account balances
  - Engineered ratios and flags
  - Transaction-specific amounts

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
