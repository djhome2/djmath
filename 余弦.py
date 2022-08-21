#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 函数 import 函数
from 变量 import 变量
from 实数 import 实数
from 未知数 import 未知数


class 余弦(函数):

    def __init__(self, x):
        log.info('Sin  __init__ --- ')
        函数.__init__(self, x)
        return

    def set(self, x):
        log.info('set argv=%s', x)
        函数.set(self, x)
        return

    def __str__(self):
        y = self.get()
        if(y != 未知数):
            return str(y)
        s = 'cos({})'.format(self.x[0])
        return s

    def 值(self):
        try:
            y = self.x[0].get()
            return math.cos(y)
        except Exception as e:
            pass
        return 未知数


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('1')
    y = 余弦(x)
    print(y)
    x = 变量('x')
    y = 余弦(x)
    print(y)
    x = 实数(1)
    y = 余弦(x)
    print(y)
