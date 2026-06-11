import pandas as pd

perf = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

risk = input("Enter risk appetite (Low/Moderate/High): ")

if risk.lower() == "low":
    filtered = perf[perf['risk_grade'].str.contains("Low", case=False)]

elif risk.lower() == "moderate":
    filtered = perf[perf['risk_grade'].str.contains("Moderate", case=False)]

else:
    filtered = perf[perf['risk_grade'].str.contains("High", case=False)]

top3 = filtered.sort_values(by='sharpe_ratio', ascending=False).head(3)

print("\nTop Recommended Funds:\n")
print(top3[['scheme_name', 'fund_house', 'sharpe_ratio', 'risk_grade']])