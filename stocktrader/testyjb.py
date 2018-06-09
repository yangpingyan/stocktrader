# -*- coding: utf-8 -*-
"""
Created on Mon May  7 01:40:41 2018

@author: ypy
"""
import logging
import tushare as ts
import time
import random
import stocktrader
from stocktrader.log import log
from stocktrader.api import use

stockID_g = "002413"
amount_g = 100


log.debug("---Mission start---")

user = use('ths')
user.connect(r'C:\\同花顺软件\\同花顺\\xiadan.exe')
df = ts.get_realtime_quotes('002413')
buy_price = float(df['ask'][0])
sell_price = float(df['bid'][0])
user.buy(stockID_g, price=buy_price, amount=100)
# user.sell(stockID_g, price=sell_price, amount=100)
user.cancel_all_entrusts()

print("Mission Complete")
#    if get is not None:
#            result = getattr(user, do)
#        else:
#            result = getattr(user, do)(*params)
#    try:
#        print(user)
#    except:
#        print("Initial easytrader")
#        user = easytrader.use('ths')
#        user.connect(r'C:\ths\xiadan.exe') # 类似 r'C:\htzqzyb2\xiadan.exe'
#
#    df = ts.get_realtime_quotes('002413')
#    buy_price = float(df['ask'][0])
#    sell_price = float(df['bid'][0])
#    print(buy_price, sell_price)
#
#    print("Mission Complete")


# print(user.balance)

# print(user.position)
# entrust_no = user.buy('002413', price=8.74, amount=3000)
#
# print(entrust_no)


# user2 = easytrader.use('ths')
# user2.connect(r'C:\ths2\xiadan.exe') # 类似 r'C:\htzqzyb2\xiadan.exe'
# print(user2.balance)

# user.position
# user.buy('162411', price=0.55, amount=100)
# user.sell('162411', price=0.55, amount=100)
# user.cancel_entrust('buy/sell 获取的 entrust_no')
# user.today_trades