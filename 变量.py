#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log


class 变量():
    # x = None

    def __init__(self, x=None):
        log.info('variable  __init__ --- ')
        self.x = x
        print('{}为变量'.format(x))

    def set(self, x):
        log.info('set value=%s', x)
        self.x = x

    def get(self):
        log.info('get x=%s', self.x)
        return self.x

    def __str__(self):
        return str(self.x)

    def 值(self):
        try:
            return self.x.值()
        except Exception as e:
            pass
        return self.x


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('x')
    print(x.值())
