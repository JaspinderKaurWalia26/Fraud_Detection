import matplotlib.pyplot as plt

def plot_amount_distribution(df, save_path):
    plt.figure(figsize=(8,5))
    plt.hist(df['Amount'], bins=20, edgecolor='black')
    plt.xlabel("Payment Amount")
    plt.ylabel("Frequency")
    plt.title("Distribution of Payment Amounts")
    plt.savefig(save_path)
    plt.close()

def plot_fraud_bar(fraud_counts, save_path):
    fraud_counts.plot(kind='bar')
    plt.xlabel("Fraud Status")
    plt.ylabel("Number of Transactions")
    plt.title("Fraud vs Non-Fraud Transactions")
    plt.savefig(save_path)
    plt.close()
