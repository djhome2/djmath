#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log
from 变量 import 变量
import uuid
import math
import sys

from 实数 import 实数


class 减():
    x = None

    def __init__(self, *args):
        log.info('Sin  __init__ --- ')
        self.x = args

    def get(self):
        log.info('get value=%s', self.x)
        return self.x

    def __str__(self):
        v = self.值()
        if(v != None):
            return str(v)
        s = '({})-({})'.format(self.x[0], self.x[1])
        return s

    def 值(self):
        try:
            a = 实数(self.x[0])
            if(a == None):
                return None
            b = 实数(self.x[1])
            if(b == None):
                return None
            return a.值() - b.值()
        except Exception as e:
            pass
        return None


if __name__ == "__main__":
    # execute only if run as a script
    x = 减('2', '1')
    print(x)
    x = 减('a', 'b')
    print(x)
