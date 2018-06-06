# -*- coding: utf-8 -*-
"""
Created on Mon May  7 01:40:41 2018

@author: ypy
"""

import easytrader
import tushare as ts

print(easytrader.__version__)
print(ts.__version__)

print("Missioin Start")
stockID = '002413'
user = easytrader.use('ths')
user.connect(r'C:\\同花顺软件\\同花顺\\xiadan.exe')

#df = ts.get_realtime_quotes(stockID)
#buy_price = float(df['ask'][0])
#sell_price = float(df['bid'][0])
#print(buy_price, sell_price)
##print(user.balance)
#stock_amounts = 100


#entrust_no = user.sell(stockID, price=sell_price, amount=stock_amounts)
print(user.balance)




#user2 = easytrader.use('ths')
#user2.connect(r'C:\ths2\xiadan.exe') # 类似 r'C:\htzqzyb2\xiadan.exe'
#print(user2.balance)

#user.position
#user.buy('162411', price=0.55, amount=100)
#user.sell('162411', price=0.55, amount=100)
#user.cancel_entrust('buy/sell 获取的 entrust_no')
#user.today_trades