# Momentum Trading Algorithm

####### Strategy Theory

# IDEA - use linear regression to determine up trend, and max point (using shorter timeframe)





import sys
sys.path.append("..")

import Stockdata
import matplotlib.pyplot as plt


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


ticker = 'TSLA'
days = 20
data = Stockdata.get_data_days(ticker, days)
x = []
for i in data:
    x.append(i)

y = list(range(1, len(x)+1))

a,b = calcRegressionLine(x, y)

colour = ''
if a > 0 : colour = 'green'
else: colour = 'red'

# Plot the data and the regression line
plt.plot(y, x, 'o')
plt.plot(y, x)
plt.plot([a*i + b for i in x], x, '-', color = colour)
plt.show()








def Momentum(ticker, time_frame):
    pass