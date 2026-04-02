import yfinance as yf
import pandas as pd

# Choose your company ticker
ticker = "NVDA"  # NVIDIA example

# Download last 30 days of stock prices
data = yf.download(ticker, period="30d")

# Keep only Date and Close price
data = data.reset_index()[["Date", "Close"]]

# Save to CSV
data.to_csv("NVDA_stock.csv", index=False)
print("✅ Stock CSV saved: NVDA_stock.csv")