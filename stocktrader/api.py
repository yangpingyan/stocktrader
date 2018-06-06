# coding=utf-8
import logging
import six

from .log import log

if six.PY2:
    raise TypeError('不支持 Python2，请升级 Python3 ')


def use(broker, debug=True, **kwargs):
    """用于生成特定的券商对象
    :param broker:券商名支持 ['yh_client', '银河客户端'] ['ht_client', '华泰客户端']
    :param debug: 控制 debug 日志的显示, 默认为 True
    :param initial_assets: [雪球参数] 控制雪球初始资金，默认为一百万
    :return the class of trader

    Usage::

        >>> import easytrader
        >>> user = easytrader.use('xq')
        >>> user.prepare('xq.json')
    """
    if not debug:
        log.setLevel(logging.INFO)
    elif broker.lower() in ['ths', '同花顺客户端']:
        from .clienttrader import ClientTrader
        return ClientTrader()

