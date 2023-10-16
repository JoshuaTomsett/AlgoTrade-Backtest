# Random Trading Algorithm

####### Strategy Theory


# Just decides random when to buy and sell - Purpose: to compare to the other strategies


import sys
sys.path.append("..")

import Stockdata
import random
import matplotlib.pyplot as plt


def RandomTrade(ticker, days):
    
    data = Stockdata.get_data_days(ticker, days)
    x = [] # price series
    for i in data:
        x.append(i)

    y = list(range(1, len(x)+1))


    buy = []
    sell = []
    chance = 30

    for i in range(1, len(x)):
        
        if random.randint(1,chance) == chance:
            if len(buy) == len(sell):
                buy.append(i)
            elif len(buy) > len(sell):
                sell.append(i)

    if len(buy) > len(sell):
        del buy[-1]


    ##          RETURN CALCULATION       ##


    pairs = zip(buy,sell)
    total = 1000

    for i in pairs:
        total = total * (x[i[1]] / x[i[0]])

    print(total)

    plt.vlines(buy, ymin=min(x), ymax=max(x), color='green')
    plt.vlines(sell, ymin=min(x), ymax=max(x), color='red')
    plt.plot(y, x)
    plt.show()



RandomTrade('TSLA', 200)