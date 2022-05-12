#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log
import sys

from 证明过程 import 证明过程


class 如果():
    mData = None

    def __init__(self, argv):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)
        self.mData = argv

    def __str__(self):
        return '如果：{0}\n'.format(self.mData)

    def setValue(self, value):
        # 证明过程.set(self, value)
        self.mData.setValue(value)

    def getValue(self):
        return self.mData.getValue()


if __name__ == "__main__":
    # execute only if run as a script
    pass
