### Mean Reversion Trading Algorithm

####### Strategy Theory

# Bollinger lines (+- some x * std, on SMA20)
# Buy -> lower bound
# Sell -> Upper bound


import sys
sys.path.append("..")

import numpy as np
import matplotlib.pyplot as plt
import Stockdata


def calculate_moving_average(close_prices, window):
    """Calculates an array of moving averages for the given close prices in a given window

    Args:
        close_prices (list): List of close prices
        window (int): Window size

    Returns:
        list: List of moving averages
    """

    weights = np.repeat(1.0, window) / window
    moving_averages = np.convolve(close_prices, weights, 'valid')
    return moving_averages


def close_prices(ticker, days):
    """Returns array of close prices for a given amount of days for a given ticker

    Args:
        ticker (String): The stock ticker
        days (int): Number of days

    Returns:
        List: List of close prices
    """

    data = Stockdata.get_data_days(ticker, days)
    close_prices = []
    for i in data:
        close_prices.append(i)
    
    return close_prices


def MeanReversion(sma_trade, lower_bollinger, upper_bollinger):

    """Generates buy / sell lists containing index(s) of when to buy or sell (index of time series list) 

    Returns:
        (List, List): Two lists (buy / sell)
    """

    buy = []
    sell = []
    active = False # True if algo has a position

    if sma_trade[0] > upper_bollinger[0]: smaPosition = 'Above'
    elif sma_trade[0] < lower_bollinger[0]: smaPosition = 'Below'
    else: smaPosition = 'Between'

    for i in range(0, len(sma_trade)):
        
        if smaPosition == 'Above':
            if sma_trade[i] < upper_bollinger[i]: # ABOVE -> MIDDLE (SELL)
                smaPosition = 'Between'
                if active:
                    sell.append(i)
                    active = False

        elif smaPosition == 'Between':

            if sma_trade[i] > upper_bollinger[i]:
                smaPosition = 'Above'
            
            if sma_trade[i] < lower_bollinger[i]:
                smaPosition = 'Below'

        elif smaPosition == 'Below':
            if sma_trade[i] > lower_bollinger[i]: # BELOW -> MIDDLE (BUY)
                smaPosition = 'Between'
                buy.append(i)
                active = True

    return buy, sell


##### VARIABLES #####

ticker = 'AMZN'
days = 1000 / 5 * 7

# Optimization
SMABollinger = 200
SMATrade = 20
stdMult = 1

##### CALCULATIONS #####

# create moving average lists
close_prices = close_prices(ticker, days+200)

sma_bollinger = calculate_moving_average(close_prices, SMABollinger)
sma_trade = calculate_moving_average(close_prices, SMATrade)

# formatting for plot - so that they all start at the same point (where the SMA Trade starts)
close_prices = close_prices[SMABollinger-1:]
sma_trade = sma_trade[SMABollinger - SMATrade:]

# Bollinger Bands
std = np.std(sma_bollinger)
lower_bollinger = [element - stdMult * std for element in sma_bollinger]
upper_bollinger = [element + stdMult * std for element in sma_bollinger]


buy, sell = MeanReversion(sma_trade, lower_bollinger, upper_bollinger)


##### PLOTTING #####

plt.figure(figsize=(10, 6))

# plt.plot(close_prices, label='Closing Prices')
# plt.plot(sma_bollinger, label=f'SMA {SMABollinger}', color='orange')

plt.plot(sma_trade, label=f'SMA {SMATrade}', color='orange') # The lower SMA (e.g: SMA20)
plt.plot(lower_bollinger, color='blue')
plt.plot(upper_bollinger, color='blue')

plt.vlines(buy, ymin=min(close_prices), ymax=max(close_prices), color='green')
plt.vlines(sell, ymin=min(close_prices), ymax=max(close_prices), color='red')

plt.xlabel('Period')
plt.ylabel('Price')
plt.title(f'Closing Prices and Moving Averages - {ticker}')
plt.legend()
plt.grid(True)
plt.show()