### Mean reversion trading 
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


plt.figure(figsize=(10, 6)) # create plot figure

ticker = 'AAPL'
days = 365*3

close_prices = close_prices(ticker, days+200)
moving_averages_20 = calculate_moving_average(close_prices, 20)
moving_averages_200 = calculate_moving_average(close_prices, 200)

close_prices = close_prices[199:]
moving_averages_20 = moving_averages_20[180:]

print(len(close_prices))
print(len(moving_averages_20))
print(len(moving_averages_200))

plt.plot(close_prices, label='Closing Prices')
plt.plot(moving_averages_20, label='SMA20')
plt.plot(moving_averages_200, label='SMA200')

plt.xlabel('Period')
plt.ylabel('Price')
plt.title(f'Closing Prices and Moving Averages - {ticker}')
plt.legend()
plt.grid(True)
plt.show()