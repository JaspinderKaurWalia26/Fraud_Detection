def assign_risk(amount, mean, std):
    if amount > mean + std:
        return "High Risk"
    elif amount > mean:
        return "Medium Risk"
    return "Low Risk"
