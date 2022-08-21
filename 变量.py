#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
import uuid
from LogApi import log

from 未知数 import 未知数


class 变量():

    def __init__(self,  x=未知数, name=None):
        log.info('variable  __init__ --- ')
        if(name == None):
            name = str(uuid.uuid1())
        else:
            assert(isinstance(name, str))
        self.name = name
        self.x = x
        print('变量: {} = {}'.format(name, x))
        return

    def set(self, x=未知数):
        log.info('set value=%s', x)
        self.x = x
        return

    def __str__(self):
        return str(self.get())

    def get(self):
        try:
            return self.x.get()
        except Exception as e:
            pass
        return self.x


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量(name='x')
    print(x)
    x = 变量(name='y', x=1)
    print(x)
