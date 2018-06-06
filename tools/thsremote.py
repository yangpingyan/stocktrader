# -*- coding: utf-8 -*-
"""
Created on Mon May  7 01:40:41 2018

@author: ypy
"""
import logging
import easytrader
import tushare as ts
import time

stockID_g= '002413'
amount_g = 5000
host_g = '192.168.1.5'
port_g = 1430

from easytrader import remoteclient


if __name__ == '__main__' :
    print("---Mission start---")
    logging.info("debug logging test")
    print("Initial easytrader")
    user = remoteclient.use('ths', host=host_g, port=port_g)
#    user.connect(r'C:\同花顺软件\同花顺\xiadan.exe')

    while(True) :
        input_str = input("THS Command:")
#        print(input_str)

        do, *params = input_str.split(" ")
        if(do == 'exit') :
            break
        #get default amount and price
        amount = amount_g
        df = ts.get_realtime_quotes('002413')
        buy_price = float(df['ask'][0])
        sell_price = float(df['bid'][0])
        print(buy_price, sell_price)
        if(do == 'buy'):
            price = buy_price
        else:
            price = sell_price

        for arg in params:
            print(arg)
            arg_tmp = float(arg)
            if arg_tmp < 20:
                price = arg_tmp
            if arg_tmp >= 100 and arg_tmp < 500000:
                amount = arg_tmp

        print(do, price, amount)


        result = getattr(user, do)(stockID_g, price=price, amount=amount)


        print(result)


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






#print(user.balance)

#print(user.position)
#entrust_no = user.buy('002413', price=8.74, amount=3000)
#
#print(entrust_no)




#user2 = easytrader.use('ths')
#user2.connect(r'C:\ths2\xiadan.exe') # 类似 r'C:\htzqzyb2\xiadan.exe'
#print(user2.balance)

#user.position
#user.buy('162411', price=0.55, amount=100)
#user.sell('162411', price=0.55, amount=100)
#user.cancel_entrust('buy/sell 获取的 entrust_no')
#user.today_trades