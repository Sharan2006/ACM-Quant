import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# choosing our portfolio
portfolio = {
    "INFY.NS": 15,
    "TCS.NS": 10,
    "RELIANCE.NS": 12
}

tickers = list(portfolio.keys())

# downloading the close prices in the last 30 days
data = yf.download(tickers, period="30d")['Close']

data.fillna(method='ffill', inplace=True)
data.fillna(0, inplace=True)

# calculating values of holdings for each day
for ticker, shares in portfolio.items():
    data[ticker] *= shares

# adds up holdings of all stocks in the portfolio row-wise
portfolio_value = data.sum(axis=1)

# plotting the figure
plt.figure(figsize=(12, 6))
plt.plot(portfolio_value.index, portfolio_value.values, marker='o', linestyle='-')
plt.title("Total Portfolio Value Over Time")
plt.xlabel("Date")
plt.ylabel("Portfolio Value (INR)")
plt.grid(True)
plt.tight_layout()
plt.show()

# calculating the most recent portfolio value
latest_value = portfolio_value.iloc[-1]
print(f"Latest total portfolio value: ₹{latest_value:,.2f}")