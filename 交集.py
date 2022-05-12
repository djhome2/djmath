#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log


class 自然数():
    value = None

    def __init__(self, value=None):
        log.info('variable  __init__ --- ')
        self.set(value)

    def set(self, value):
        log.info('set value=%s', value)
        self.value = value

    def get(self):
        log.info('get value=%s', self.value)
        return self.value

    def __str__(self):
        return str(self.value)

    def toInt(self):
        try:
            return int(self.value)
        except Exception as e:
            return None


if __name__ == "__main__":
    # execute only if run as a script
    v = 自然数(1)
    v.set('a')
