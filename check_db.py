import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

df = pd.read_sql("SELECT * FROM nav_history LIMIT 10", conn)

print(df)

conn.close()