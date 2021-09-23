import pandas as pd


def sma(prices: pd.Series, window: int):
    return prices.rolling(window).mean()


def ema(prices: pd.Series, window: int):
    return prices.ewm(span=window).mean()
