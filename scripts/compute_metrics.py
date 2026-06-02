import pandas as pd

df = pd.read_csv("data/processed/nav_data.csv")

df["daily_return"] = df["nav"].pct_change()

sharpe = (
    df["daily_return"].mean()
    /
    df["daily_return"].std()
) * (252 ** 0.5)

volatility = (
    df["daily_return"].std()
) * (252 ** 0.5)

print("Sharpe Ratio:", sharpe)
print("Volatility:", volatility)