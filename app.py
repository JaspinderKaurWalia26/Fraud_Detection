from src.data_loader import load_data
from src.analysis import fraud_counts, calculate_stats
from src.risk_model import assign_risk
from src.visualization import plot_amount_distribution, plot_fraud_bar

# Load data
df = load_data("data/raw/payment_dataset.csv")

# Basic info
print(df.head())
print(df.info())

# Fraud statistics
fraud_count = fraud_counts(df)
print("\nFraud counts:\n", fraud_count)

# Stats & threshold
mean, std, threshold = calculate_stats(df)

# Risk & suspicious flag
df['Suspicious'] = df['Amount'] > threshold
df['Risk_level'] = df['Amount'].apply(lambda x: assign_risk(x, mean, std))

# Save plots
plot_amount_distribution(df, "outputs/plots/distribution_of_payment_amounts.png")
plot_fraud_bar(fraud_count, "outputs/plots/fraud_vs_non_fraud.png")

# Print suspicious transactions
print("\nSuspicious Transactions:")
print(df[df['Suspicious']])
