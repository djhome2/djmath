#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log


class 符号():
    mData = None

    def __init__(self, value=None):
        log.info('variable  __init__ --- ')
        self.set(value)

    def set(self, value):
        log.info('set value=%s', value)
        self.mData = value

    def get(self):
        log.info('get value=%s', self.mData)
        return self.mData

    def __str__(self):
        return str(self.mData)

    def toInt(self):
        try:
            return int(self.mData)
        except Exception as e:
            return None


if __name__ == "__main__":
    # execute only if run as a script
    v = 符号(1)
    v.set('a')
