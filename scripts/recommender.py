risk = input("Enter risk level: ")

if risk.lower() == "low":
    print("Recommended: Debt Funds")

elif risk.lower() == "medium":
    print("Recommended: Hybrid Funds")

else:
    print("Recommended: Equity Funds")