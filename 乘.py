#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log
from 变量 import 变量
import uuid
import math
import sys
from 实数 import 实数


class 乘():
    args = None

    def __init__(self, *args):
        log.info('Sin  __init__ --- ')
        self.args = args

    def get(self):
        log.info('get value=%s', self.args)
        return self.args

    def __str__(self):
        v = self.值()
        if(v != None):
            return str(v)
        x = self.args[0]
        y = self.args[1]
        s = '({})*({})'.format(x, y)
        return s

    def 值(self):
        try:
            x = self.args[0]
            y = self.args[1]
            a = 实数(x)
            if(a == None):
                return None
            b = 实数(y)
            if(b == None):
                return None
            return a.值() * b.值()
        except Exception as e:
            pass
        return None


if __name__ == "__main__":
    # execute only if run as a script
    x = 乘('1', '2')
    print(x)
    x = 乘('a', 'b')
    print(x)
