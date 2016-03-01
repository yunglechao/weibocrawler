# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:18:23 2015

@author: YungLeChao
"""

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo('MSFT', start, today)
attributes=['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS, columns= attributes)
list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfMS.index = list
quotesdfMS = quotesdfMS.drop(['date'], axis = 1)
list = []
quotesdfMS14 = quotesdfMS['14/01/01':'14/12/31']
for i in range(0, len(quotesdfMS14)):
    list.append(int(quotesdfMS14.index[i][3:5])) #get month just like '02'
quotesdfMS14['month'] = list
print (quotesdfMS14.groupby('month').mean().close)
openMS = quotesdfMS14.groupby('month').mean().open
listopen = []
for i in range(1, 13):
    listopen.append(openMS[i])
plt.plot(openMS.index, listopen)