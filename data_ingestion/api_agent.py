import requests
import pandas as pd
import os

class AlphaVantageAPI:
    def __init__(self, api_key: str = "7NF7AZF66EWQ6UXR"):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_daily_stock_data(self, symbol: str, outputsize: str = "compact") -> pd.DataFrame:
        """
        Fetch daily adjusted stock data for a given symbol.

        Args:
            symbol: Stock symbol (e.g., 'AAPL', 'MSFT').
            outputsize: 'compact' (last 100 data points) or 'full' (20+ years).

        Returns:
            DataFrame with OHLCV and adjusted close.
        """
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "outputsize": outputsize,
            "apikey": self.api_key
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        if "Time Series (Daily)" not in data:
            raise ValueError(f"Unexpected response format: {data}")

        time_series = data["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(time_series, orient="index")
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()

        return df
