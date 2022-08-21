#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 变量 import 变量
from 未知数 import 未知数


class 实数(变量):

    def __init__(self, name=None, x=未知数):
        log.info('variable  __init__ --- ')
        变量.__init__(self, name, x)
        return

    def get(self):
        y = 变量.get(self)
        try:
            return float(y)
        except Exception as e:
            pass
        return y


if __name__ == "__main__":
    # execute only if run as a script
    v = 实数(x=1)
    print(v)
    v.set('a')
    print(v)
