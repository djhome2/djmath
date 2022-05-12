#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 变量 import 变量


class 实数():
    x = None

    def __init__(self, x=None):
        log.info('variable  __init__ --- ')
        self.set(x)

    def set(self, x):
        log.info('set value=%s', x)
        self.x = x

    def get(self):
        log.info('get value=%s', self.x)
        return self.x

    def __str__(self):
        return str(self.x)

    def 值(self):
        try:
            y = self.x.值()
            return float(y)
        except Exception as e:
            pass
        try:
            return float(self.x)
        except Exception as e:
            pass
        return None


if __name__ == "__main__":
    # execute only if run as a script
    v = 实数(1)
    v.set('a')
