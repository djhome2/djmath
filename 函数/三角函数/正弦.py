#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import __init__


from LogApi import log


import math
from 函数 import 函数

from 变量 import 变量
from 实数 import 实数
from 未知数 import 未知数


class 正弦(函数):

    def __init__(self, x):
        log.info('Sin  __init__ --- ')
        函数.__init__(self, x)
        return

    def set(self, x):
        log.info('set argv=%s', x)
        函数.set(self, x)
        return

    def get_default_value(self):
        y1 = self.get_x(self.x[0])
        return math.sin(y1)

    def get_default_str(self):
        s = 'sin({})'.format(self.x[0])
        return s


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('1')
    y = 正弦(x)
    print(y)
    x = 变量('x')
    y = 正弦(x)
    print(y)
    x = 实数(1)
    y = 正弦(x)
    print(y)
