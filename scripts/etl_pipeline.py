import pandas as pd
import sqlite3
import json
from pathlib import Path

# Base project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# JSON file path
json_path = BASE_DIR / "data" / "raw" / "nav_data.json"

# Read JSON
with open(json_path, "r") as f:
    data = json.load(f)

# Extract NAV data
nav_data = data["data"]

# Convert to DataFrame
df = pd.DataFrame(nav_data)

# Rename columns
df.columns = ["date", "nav"]

# Convert datatypes
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df["nav"] = pd.to_numeric(df["nav"])

# Sort by date
df = df.sort_values("date")

# Save cleaned CSV
processed_path = BASE_DIR / "data" / "processed" / "nav_data.csv"

df.to_csv(processed_path, index=False)

# SQLite database path
db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"

# Connect database
conn = sqlite3.connect(db_path)

# Load into SQLite
df.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("ETL completed successfully")