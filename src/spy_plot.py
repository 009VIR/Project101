# Updated for clarity
git add spy_plot.py
git commit -m "Add clarification comment to spy_plot.py"

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download 1 year of SPY data
spy = yf.download("SPY", period="1y", interval="1d")

# Save to CSV
spy.to_csv("../data/spy_1y.csv")

# Plot OHLC
plt.figure(figsize=(14, 7))
plt.plot(spy['Open'], label='Open')
plt.plot(spy['High'], label='High')
plt.plot(spy['Low'], label='Low')
plt.plot(spy['Close'], label='Close')
plt.title("SPY - Last 1 Year OHLC")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../notebooks/spy_ohlc_plot.png")  # Save screenshot
plt.show()
