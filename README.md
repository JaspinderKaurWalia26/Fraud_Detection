# Online Payment Fraud Detection System

## 📌 Project Overview
This project is a **Python-based Online Payment Fraud Detection System** that analyzes online payment transaction data to identify **suspicious and potentially fraudulent transactions** using statistical techniques. The system classifies transactions into **Low Risk, Medium Risk, and High Risk** categories based on transaction amounts.

The project follows a **clean and modular folder structure**, making it easy to understand, execute, and maintain for academic purposes.

---

## 🎯 Objectives
- Analyze online payment transaction data
- Identify suspicious transactions using statistical thresholds
- Classify transactions into different risk levels
- Visualize transaction distributions and fraud statistics

---

## 🗂️ Project Folder Structure
```
online-payment-fraud-detection/
│
├── app.py # Main entry point of the application
│
├── src/ # Source code
│ ├── init.py
│ ├── data_loader.py # Loads dataset
│ ├── analysis.py # Statistical analysis
│ ├── risk_model.py # Risk classification logic
│ └── visualization.py # Plot generation
│
├── data/
│ └── raw/
│ └── payment_dataset.csv
│
├── outputs/
│ └── plots/
│ ├── distribution_of_payment_amounts.png
│ └── fraud_vs_non_fraud.png
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used
- **Python 3**
- **Pandas** – data manipulation and analysis
- **Matplotlib** – data visualization

---

## 📊 Methodology
1. Load the online payment transaction dataset
2. Perform basic exploratory data analysis (EDA)
3. Calculate statistical measures such as mean and standard deviation
4. Define a threshold to detect suspicious transactions
5. Classify transactions into risk levels
6. Visualize payment amount distribution and fraud statistics

---

## 🧠 Risk Classification Logic
- **High Risk**: Amount > Mean + Standard Deviation  
- **Medium Risk**: Amount > Mean  
- **Low Risk**: Amount ≤ Mean  

---

## ▶️ How to Run the Project

### Step 1: Install required libraries
```bash
pip install -r requirements.txt
```
### Step 2: Run the application
```bash
python app.py
