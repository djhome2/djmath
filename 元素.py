#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log
import sys


class 元素():
    mData = None

    def __init__(self, value=None):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)
        self.mData = value


if __name__ == "__main__":
    # execute only if run as a script
    print(元素)
