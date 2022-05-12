#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log
from 变量 import 变量
import uuid
import math
import sys


class 除():
    value = None

    def __init__(self, value=None):
        log.info('Sin  __init__ --- ')
        self.set(value)

    def set(self, argv):
        log.info('set argv=%s', argv)
        self.value = argv

    def get(self):
        log.info('get value=%s', self.value)
        return self.value

    def __str__(self):
        if(self.value != None):
            return str(self.value)
        return '-' + str(self.value)


if __name__ == "__main__":
    # execute only if run as a script
    if(len(sys.argv) == 1):
        print('Usage: Jian.py [double]')
        sys.exit(0)
    x = 除(sys.argv[1])
    print(x)
