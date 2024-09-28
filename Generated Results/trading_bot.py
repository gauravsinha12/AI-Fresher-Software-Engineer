
import pandas as pd
import yfinance as yf

# Download historical data for HUL
data = yf.download('HINDUNILVR.NS', start='2010-01-01', end='2022-02-26')

# Calculate daily returns
data['Return'] = data['Close'].pct_change()

# Calculate mean and standard deviation of returns
mean_return = data['Return'].mean()
std_dev = data['Return'].std()

# Calculate z-score
data['Z-Score'] = (data['Return'] - mean_return) / std_dev

# Generate entry and exit signals
data['Signal'] = 0
data.loc[data['Z-Score'] < -2, 'Signal'] = 1  # Buy signal
data.loc[data['Z-Score'] > 2, 'Signal'] = -1  # Sell signal
