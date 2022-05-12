#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log
from 变量 import 变量
import uuid
import math
import sys

from 实数 import 实数


class 和():
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
        s = ''
        for i in range(0, len(self.args)):
            if(i > 0):
                s = s+'+'
            s = s+'({})'
        s2 = s.format(*self.args)
        return s2

    def 值(self):
        try:
            sum = 0.0
            for x in self.args:
                a = 实数(x)
                if(a == None):
                    return None
                sum += a.值()
            return sum
        except Exception as e:
            pass
        return None


if __name__ == "__main__":
    # execute only if run as a script
    x = 和('2', '1', '3')
    print(x)
    x = 和('a', 'b', 'c')
    print(x)
