#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log
import sys


class 那么():

    mData = None

    def __init__(self, argv):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)
        self.mData = argv

    def __str__(self):
        return '那么：{0}\n'.format(self.mData)

    def setValue(self, value):
        self.mData.setValue(value)

    def getValue(self):
        return self.mData.getValue()


if __name__ == "__main__":
    # execute only if run as a script

    print(那么)
