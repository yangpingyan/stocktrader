# -*- coding: utf-8 -*-

import pywinauto
import time



class CommonConfig:
    DEFAULT_EXE_PATH = None
    TITLE = '网上股票交易系统5.0'


    TRADE_SECURITY_CONTROL_ID = 1032
    TRADE_PRICE_CONTROL_ID = 1033
    TRADE_AMOUNT_CONTROL_ID = 1034

    TRADE_SUBMIT_CONTROL_ID = 1006

    TRADE_MARKET_TYPE_CONTROL_ID = 1541

    COMMON_GRID_CONTROL_ID = 1047

    COMMON_GRID_LEFT_MARGIN = 10
    COMMON_GRID_FIRST_ROW_HEIGHT = 30
    COMMON_GRID_ROW_HEIGHT = 16

    BALANCE_MENU_PATH = ['查询[F4]', '资金股票']
    POSITION_MENU_PATH = ['查询[F4]', '资金股票']
    TODAY_ENTRUSTS_MENU_PATH = ['查询[F4]', '当日委托']
    TODAY_TRADES_MENU_PATH = ['查询[F4]', '当日成交']

    BALANCE_CONTROL_ID_GROUP = {
        '资金余额': 1012,
        '可用金额': 1016,
        '可取金额': 1017,
        '股票市值': 1014,
        '总资产': 1015
    }

    POP_DIALOD_TITLE_CONTROL_ID = 1365

    GRID_DTYPE = {
        '操作日期': str,
        '委托编号': str,
        '申请编号': str,
        '合同编号': str,
        '证券代码': str,
        '股东代码': str,
        '资金帐号': str,
        '资金帐户': str,
        '发生日期': str
    }

    CANCEL_ENTRUST_ENTRUST_FIELD = '合同编号'
    CANCEL_ENTRUST_GRID_LEFT_MARGIN = 50
    CANCEL_ENTRUST_GRID_FIRST_ROW_HEIGHT = 30
    CANCEL_ENTRUST_GRID_ROW_HEIGHT = 16

    AUTO_IPO_SELECT_ALL_BUTTON_CONTROL_ID = 1098
    AUTO_IPO_BUTTON_CONTROL_ID = 1006
    AUTO_IPO_MENU_PATH = ['新股申购', '批量新股申购']




config = CommonConfig
connect_path = r'C:\\同花顺软件\\同花顺\\xiadan.exe'
if connect_path is None:
    raise ValueError('参数 exe_path 未设置，请设置客户端对应的 exe 地址,类似 C:\\客户端安装目录\\xiadan.exe')

app = pywinauto.Application().connect(path=connect_path, timeout=10)
#close_prompt_windows()
time.sleep(1)
for w in app.windows(class_name='#32770'):
    if w.window_text() != config.TITLE:
        w.close()
time.sleep(1)
    
main = app.top_window()

#path = ['查询[F4]', '资金股票']
path = ['买入[F1]']
#path = ['卖出[F2]']
#path = ['查询[F4]']


#找到左侧菜单
while True:
    try:
        handle = main.child_window(control_id=129, class_name='SysTreeView32')
        # sometime can't find handle ready, must retry
        handle.wait('ready', 2)
        break
    except:
        pass
            


handle.get_item(path).click()
time.sleep(0.2)
security = "002413"
code = security[-6:]


main.window(control_id=config.TRADE_SECURITY_CONTROL_ID, class_name='Edit').set_edit_text(code)
# wait security input finish
time.sleep(0.1)
main.window(control_id=config.TRADE_PRICE_CONTROL_ID, class_name='Edit').set_edit_text("6.68")
main.window(control_id=config.TRADE_AMOUNT_CONTROL_ID, class_name='Edit').set_edit_text("200")

     
time.sleep(0.05)
main.window(control_id=config.TRADE_SUBMIT_CONTROL_ID, class_name='Button').click()
        


while main.wrapper_object() != app.top_window().wrapper_object():
    time.sleep(0.2)
    title = app.top_window().window(control_id=config.POP_DIALOD_TITLE_CONTROL_ID).window_text()

    app.top_window().type_keys('%Y')
    time.sleep(0.2)
    app.top_window()['确定'].click()

        
#可用金额
#fund_available = main.child_window(control_id=1016, class_name='Static')
#fund_available.print_control_identifiers()

print("Mission Complete")
    
    







