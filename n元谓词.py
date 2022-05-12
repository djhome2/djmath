#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log
import sys

from 证明过程 import 证明过程


class n元谓词():
    mData = []
    mValue = None

    def __init__(self):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)

    def setData(self, argv):
        self.mData = argv

    def setValue(self, value):
        self.mValue = value
        证明过程.setValue(self, value)

    def getValue(self):
        print('{0}判定为{1}\n'.format(self, self.mValue))
        if(self.mValue != None):
            return self.mValue
        # assert(False)
        return self.mValue

    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__, self.mData)


if __name__ == "__main__":
    # execute only if run as a script
    print(n元谓词)
