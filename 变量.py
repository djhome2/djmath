#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
import uuid
from LogApi import log

from 未知数 import 未知数


class 变量():
    # x = None

    def __init__(self, name=None, x=未知数):
        log.info('variable  __init__ --- ')
        if(name == None):
            name = uuid.uuid1()
        self.name = str(name)
        self.x = x
        print('变量: {} = {}'.format(name, x))

    def set(self, x=未知数):
        log.info('set value=%s', x)
        self.x = x

    def get(self):
        log.info('get x=%s', self.x)
        if(self.x == 未知数):
            self.x = self.值()
        return self.x

    def __str__(self):
        return str(self.get())

    def 值(self):
        try:
            return self.x.值()
        except Exception as e:
            pass
        return 未知数


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('x')
    print(x)
    x = 变量('y', 1)
    print(x)
