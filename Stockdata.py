### Functions for collecting and handling historical stock price data
from pandas_datareader import data
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime , timedelta
from statsmodels.tsa.stattools import adfuller

yf.pdr_override()


def get_data_days(ticker, days, col='Adj Close'):
    END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
    WEEK_DATE = datetime.now() - timedelta(days=days)
    WEEK_DATE = WEEK_DATE.strftime('%Y-%m-%d')
    stock_data = data.get_data_yahoo(ticker,start=WEEK_DATE,end=END_DATE)
    clean_data = stock_data[col]
    return clean_data.fillna(method='ffill') # returns only the data about prices


def is_stationary(close_prices):
  """Performs an ADF test on a list of close prices and returns True if it is stationary.

  Args:
    close_prices: A list of close prices for a stock.

  Returns:
    True if the stock prices are stationary, False otherwise.
  """

  # If the p-value < significance level, reject the null hypothesis and conclude that the series is not stationary.
  if adfuller(close_prices)[1] < 0.05: return False

  # Otherwise, we fail to reject the null hypothesis and conclude that the series is stationary.
  else: return True