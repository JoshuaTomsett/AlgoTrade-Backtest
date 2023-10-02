# Momentum Trading Algorithm

####### Strategy Theory

# IDEA - use linear regression to determine up trend, and max point (using shorter timeframe)

# buy when angle above 30 degress (for example)

# sell when angle is cloe to zero (e.g: between 5 < angle <= -5)

# tweak the angles to find opptimal performance, both with in and out of sample testing




import sys
sys.path.append("..")

import Stockdata
import matplotlib.pyplot as plt
import numpy as np


def calcRegressionLine(x, y):
    """
    Calculates the regression line using the least squares method.

    Args:
        x: Array of x values
        y: Array of y values

    Returns:
        a,b
        The slope (a) and intercept (b) of the regression line (y = ax+ b)
    """

    n = len(x)
    Sx = sum(x)
    Sx2 = sum(i*i for i in x)
    Sy = sum(y)
    Sxy = sum(a * b for a, b in zip(x, y))

    a = (n*Sxy - Sx*Sy) / (n*Sx2 - Sx**2)
    b = (Sx2*Sy - Sx*Sxy) / (n*Sx2 - Sx**2)

    return a,b

            ## XXXXXXXXXXXXXXXXX ##

# ticker = 'TSLA'
# days = 8
# data = Stockdata.get_data_days(ticker, days)
# x = []
# for i in data:
#     x.append(i)

# y = list(range(1, len(x)+1))

# a,b = calcRegressionLine(x, y)

# colour = ''
# if a > 0 : colour = 'green'
# else: colour = 'red'

# # Plot the data and the regression line
# plt.plot(y, x, 'o')
# plt.plot(y, x)
# plt.plot([a*i + b for i in x], x, '-', color = colour)
# plt.show()


def calcAngleList(ticker, days, time_frame):

    def calcAngle(a): # a = gradient
        return np.rad2deg(np.arctan(a))


    angles = []

    data = Stockdata.get_data_days(ticker, time_frame)

    prices = []
    for i in data:
        prices.append(i)

    for i in range(len(prices)-days):
        x = prices[i:i+days]
        y = list(range(1, 11))
        a, b = calcRegressionLine(x,y)
        angles.append(calcAngle(a))
    
    return angles



ticker = 'TSLA'
days = 100
data = Stockdata.get_data_days(ticker, days)
x = []
for i in data:
    x.append(i)

y = list(range(1, len(x)+1))

angles = calcAngleList('TSLA', 10, 100)

buy = []
sell = []
mode = 'Buy'

for i in angles:
    if i > -2 and i < 2 and mode == 'Buy':
        buy.append(angles.index(i)+1)
        mode = 'Sell'
    
    elif i > -2 and i < 2 and mode == 'Sell':
        sell.append(angles.index(i)+1)
        mode = 'Buy'

for index, value in enumerate(angles):
    print(index+1, value)


plt.vlines(buy, ymin=min(x), ymax=max(x), color='green')
plt.vlines(sell, ymin=min(x), ymax=max(x), color='red')
plt.plot(y, x)
plt.show()






def Momentum(ticker, time_frame):
    pass