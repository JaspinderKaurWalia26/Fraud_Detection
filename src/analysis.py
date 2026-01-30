def fraud_counts(df):
    return df['Fraud'].value_counts()

def calculate_stats(df):
    mean = df['Amount'].mean()
    std = df['Amount'].std()
    threshold = mean + std
    return mean, std, threshold
