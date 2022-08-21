#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 变量 import 变量
from 未知数 import 未知数


class 实数(变量):

    def __init__(self, x=未知数, name=None):
        log.info('variable  __init__ --- ')
        变量.__init__(self, x, name)
        return

    def 值(self):
        try:
            y = self.x.get()
            return float(y)
        except Exception as e:
            pass
        try:
            return float(self.x)
        except Exception as e:
            pass
        return 未知数


if __name__ == "__main__":
    # execute only if run as a script
    v = 实数(x=1)
    print(v.get())
    v.set('a')
    print(v.get())
