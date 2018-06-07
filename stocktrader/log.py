# coding:utf8
import logging

logging.getLogger("stocktrader").handlers = []
log = logging.getLogger('stocktrader')
log.setLevel(logging.DEBUG)
log.propagate = False

fmt = logging.Formatter('[%(levelname)s] %(filename)s %(lineno)s: %(message)s')
ch = logging.StreamHandler()

ch.setFormatter(fmt)
log.handlers.append(ch)
