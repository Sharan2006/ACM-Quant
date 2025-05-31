import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# downloading the stock data for the last 6 months
aapl_data = yf.download('AAPL', period='6mo')

# calculating the SMA_7, 7 day std deviation and % change
aapl_data['SMA_7'] = aapl_data['Close'].rolling(window=7).mean()
aapl_data['7_day_rolling_std'] = aapl_data['Close'].rolling(window=7).std()
aapl_data['pct_change'] = aapl_data['Close'].pct_change()

# creating the plot as 2 subplots to better observe percent changes as seperate plot % changes are near zero
fig, x1 = plt.subplots(figsize = (10,6))

x1.plot(aapl_data['SMA_7'], label = '7-day rolling avg')
x1.plot(aapl_data['7_day_rolling_std'], label = '7-day rolling std')
x1.set_xlabel('Date')
x1.set_ylabel('Value')
x1.legend(loc = 'upper left')
x1.grid(True)

x2 = x1.twinx()
x2.plot(aapl_data['pct_change'],color = 'black',label = '% change')
x2.set_ylabel('% change')
x2.legend(loc = 'upper right')

plt.title('Apple 7-day rolling avg, 7-day std deviation & % change')

plt.show()