import pandas as pd

# Load CSVs
sentiment_df = pd.read_csv("analytics_ready_sentiment.csv")
stock_df = pd.read_csv("NVDA_stock.csv")  # or whichever stock CSV

# Convert date columns to datetime
sentiment_df["published_at"] = pd.to_datetime(sentiment_df["published_at"])
stock_df["Date"] = pd.to_datetime(stock_df["Date"])  # keep as is if CSV has 'Date'

# Merge on the date
merged_df = pd.merge(
    sentiment_df, stock_df,
    left_on="published_at", right_on="Date",
    how="left"
)

# Save merged CSV
merged_df.to_csv("merged_sentiment_stock.csv", index=False)

print("✅ Merged CSV saved: merged_sentiment_stock.csv")