#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import __init__


from LogApi import log


import math
from 函数 import 函数

from 变量 import 变量
from 实数 import 实数
from 未知数 import 未知数
from 正弦__加 import 正弦__加


class 正弦2x(正弦__加):

    def __init__(self, x):
        log.info('Sin  __init__ --- ')
        正弦__加.__init__(self, x, x)
        return


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('1')
    y = 正弦2x(x)
    print(y)
    x = 变量('x')
    y = 正弦2x(x)
    print(y)
    x = 实数(1)
    y = 正弦2x(x)
    print(y)
