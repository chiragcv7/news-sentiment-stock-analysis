import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect("news_sentiment.db")

# Read the analytics-ready table
df = pd.read_sql_query("SELECT * FROM ANALYTICS_READY_SENTIMENT", conn)

# Save to CSV
df.to_csv("analytics_ready_sentiment.csv", index=False)

conn.close()
print("✅ CSV saved: analytics_ready_sentiment.csv")