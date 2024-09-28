import yfinance as yf
import pandas as pd

ticker = yf.download("^NSEBANK", start="2020-01-01", end="2022-02-26")
ticker["20d_ma"] = ticker["Close"].rolling(window=20).mean()
ticker["Upper"] = ticker["20d_ma"] + 2 * ticker["Close"].rolling(window=20).std()
ticker["Lower"] = ticker["20d_ma"] - 2 * ticker["Close"].rolling(window=20).std()
ticker["Signal"] = 0
ticker.loc[ticker["Close"] > ticker["Upper"], "Signal"] = -1
ticker.loc[ticker["Close"] < ticker["Lower"], "Signal"] = 1
print(ticker.head())
