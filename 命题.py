#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 证明过程 import 证明过程


class 命题():
    n元谓词 = None
    个体词 = []
    mValue = None

    def __init__(self, n元谓词=None, 个体词=[]):
        log.info('variable  __init__ --- ')
        self.n元谓词 = n元谓词
        self.个体词 = 个体词
        self.n元谓词.setData(self.个体词)

    def __str__(self):
        return '{0}'.format(self.n元谓词)

    def setValue(self, value):
        self.mValue = value
        self.n元谓词.setValue(value)
        证明过程.setValue(self, value)

    def getValue(self):
        if(self.mValue != None):
            return self.mValue
        return self.n元谓词.getValue()

    def toInt(self):
        try:
            return int(self.value)
        except Exception as e:
            return None

    def 证明(self, *argv):
        return True


if __name__ == "__main__":
    # execute only if run as a script
    v = 命题(1)
    v.set('a')
