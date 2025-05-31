import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# downloading stock data for last 6 monmths
msft_data = yf.download('MSFT', period='6mo')

# calculating SMA5 and SMA20
msft_data['SMA5'] = msft_data['Close'].rolling(window=5).mean()
msft_data['SMA20'] = msft_data['Close'].rolling(window=20).mean()

msft_data['Prev_SMA_5'] = msft_data['SMA5'].shift(1)
msft_data['Prev_SMA_20'] = msft_data['SMA20'].shift(1)

# checking crossovers
buy_signals = msft_data[
    (msft_data['Prev_SMA_5'] < msft_data['Prev_SMA_20']) &
    (msft_data['SMA5'] > msft_data['SMA20'])
]

sell_signals = msft_data[
    (msft_data['Prev_SMA_5'] > msft_data['Prev_SMA_20']) &
    (msft_data['SMA5'] < msft_data['SMA20'])
]

# plotting the figure and annotating on the plot where necessary
plt.figure(figsize=(14, 7))
plt.plot(msft_data['Close'], label='Close Price', color='blue')
plt.plot(msft_data['SMA5'], label='SMA 5', color='orange')
plt.plot(msft_data['SMA20'], label='SMA 20', color='green')

plt.scatter(buy_signals.index, buy_signals['Close'], label='Buy Signal', marker='^', color='green', zorder=5)
plt.scatter(sell_signals.index, sell_signals['Close'], label='Sell Signal', marker='v', color='red', zorder=5)

plt.title('MSFT Stock Price with SMA 5 & SMA 20 (Last 6 Months)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
