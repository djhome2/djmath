#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log

import uuid
import math
import sys

from 变量 import 变量
from 实数 import 实数


class 正弦():
    x = None

    def __init__(self, x=None):
        log.info('Sin  __init__ --- ')
        self.set(x)

    def set(self, x):
        log.info('set argv=%s', x)
        self.x = x

    def get(self):
        log.info('get value=%s', self.x)
        return self.x

    def __str__(self):
        y = self.值()
        if(y != None):
            return str(y)
        s = 'sin({})'.format(self.x)
        return s

    def 值(self):
        y = 实数(self.x)
        try:
            return math.sin(y.值())
        except Exception as e:
            pass
        return None


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('1')
    y = 正弦(x)
    print(y)
    x = 变量('x')
    y = 正弦(x)
    print(y)
