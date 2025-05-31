import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# choosing our stocks
nifty_20 = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "LT.NS", "SBIN.NS", "KOTAKBANK.NS", "AXISBANK.NS", "HINDUNILVR.NS",
    "ITC.NS", "BHARTIARTL.NS", "BAJFINANCE.NS", "ASIANPAINT.NS", "HCLTECH.NS",
    "WIPRO.NS", "ULTRACEMCO.NS", "SUNPHARMA.NS", "MARUTI.NS", "NESTLEIND.NS"
]

# downloading the close prices of the listed stocks
data = yf.download(nifty_20, period="1mo")['Close']
data.ffill(inplace=True)

# calculating % changes
start_prices = data.iloc[0]
end_prices = data.iloc[-1]
percent_change = ((end_prices - start_prices) / start_prices) * 100

# storing them in a dataframe
percent_change_df = percent_change.reset_index()
percent_change_df.columns = ['Ticker', 'Percent Change']

# storing them in a csv file
percent_change_df.to_csv('percent_change.csv', index=False)

# finding the top gainers and top losers
top_gainers = percent_change.sort_values(ascending = False).head(5)
top_losers = percent_change.sort_values(ascending = True).head(5)
combined = pd.concat([top_gainers, top_losers])

# plotting the figure 
plt.figure(figsize=(10, 6))
combined.plot(kind='bar')
plt.title('Top 5 Gainers & Top 5 Losers')
plt.xlabel('Stock')
plt.ylabel('Percentage Change')
plt.xticks(rotation=90)

plt.grid(axis='y')
plt.tight_layout()
plt.show()
