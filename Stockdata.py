### Functions for collecting and handling historical stock price data
from pandas_datareader import data
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime , timedelta

yf.pdr_override()


def get_data_days(ticker, days, col='Adj Close'):
    END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
    WEEK_DATE = datetime.now() - timedelta(days=days)
    WEEK_DATE = WEEK_DATE.strftime('%Y-%m-%d')
    stock_data = data.get_data_yahoo(ticker,start=WEEK_DATE,end=END_DATE)
    clean_data = stock_data[col]
    return clean_data.fillna(method='ffill') # returns only the data about prices