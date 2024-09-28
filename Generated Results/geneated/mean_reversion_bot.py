
import numpy as np
import pandas as pd
import requests
import json

# Define API keys and other constants
nse_api_key = "YOUR_NSE_API_KEY"
alpha_vantage_api_key = "YOUR_ALPHA_VANTAGE_API_KEY"

# Define the mean reversion strategy
def mean_reversion_strategy(symbol, short_window, long_window):
    # Fetch historical data using NSE API
    response = requests.get(f"https://nseapi.com/api/stock/{symbol}", headers={"api-key": nse_api_key})
    data = json.loads(response.content)
    df = pd.DataFrame(data["data"])

    # Calculate short and long moving averages
    df["short_ma"] = df["close"].rolling(window=short_window).mean()
    df["long_ma"] = df["close"].rolling(window=long_window).mean()

    # Generate trading signals
    df["signal"] = np.where(df["short_ma"] > df["long_ma"], 1, -1)

    return df

# Backtest the strategy
def backtest_strategy(symbol, short_window, long_window):
    df = mean_reversion_strategy(symbol, short_window, long_window)
    # Calculate returns and plot the strategy
    returns = df["signal"].cumsum()
    print(returns)

# Run the backtest
backtest_strategy("SBIN", 20, 50)
