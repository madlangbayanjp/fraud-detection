# Fraud Detection

![Python](https://img.shields.io/badge/Python-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange?logo=scikit-learn)

I optimized a machine learning project that I've found on youtube
https://www.youtube.com/watch?v=4Od5_z28iIE

In this project, he created a Fraud Detection using Logistic Regression with 96% accuracy **BUT** 2% precision
This means that it will be classified as a fraud even though it is not

What I did is that I optimized this fraud detection project. I experimented and used different algorithms to make the metrics as accurate as possible

Using different algorithms, I found out that the best one to use for this project is Random Forest since  it can handle **large** imbalances in data

## 🚀 Features

- **Real-time Fraud Detection**: Predict fraudulent transactions instantly
- **Interactive Web Interface**: Easy-to-use Streamlit dashboard
- **Multiple Transaction Types**: Supports PAYMENT, TRANSFER, CASH_OUT, DEBIT, CASH_IN
- **Advanced Feature Engineering**: Uses engineered features for better accuracy

## 🛠️ Technologies Used

- **Python**
- **Scikit-learn** 
- **Streamlit** 
- **Pandas**
- **Joblib**

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
