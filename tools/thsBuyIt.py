# -*- coding: utf-8 -*-
"""
Created on Mon May  7 01:40:41 2018

@author: ypy
"""
import logging
import easytrader
import tushare as ts
import time
import random

stockID_g= '002413'
amount_g = 5000
logger = logging.getLogger()



logger.debug("---Mission start---")
logger.info("Initial easytrader")
user = easytrader.use('ths')
user.connect(r'C:\\同花顺软件\\同花顺\\xiadan.exe')

while(True) :


    amount = random.randint(5, 10) * 100
    df = ts.get_realtime_quotes('002413')
    buy_price = float(df['ask'][0])
    sell_price = float(df['bid'][0])
    print(buy_price, sell_price)
    do = 'buy'
    price = buy_price
    print(do, price, amount)

    result = getattr(user, do)(stockID_g, price=price, amount=amount)

    print(result)
    time.sleep(1)