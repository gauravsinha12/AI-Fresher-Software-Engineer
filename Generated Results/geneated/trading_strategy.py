import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Define the ticker symbol
ticker = 'NSE:BANKNIFTY'

# Download the historical data
data = yf.download(ticker, start='2010-01-01', end='2023-02-26')

# Calculate the daily returns
data['Returns'] = data['Close'].pct_change()

# Calculate the mean and standard deviation of the returns
mean_return = data['Returns'].mean()
std_return = data['Returns'].std()

# Define the z-score
data['Z-Score'] = (data['Returns'] - mean_return) / std_return