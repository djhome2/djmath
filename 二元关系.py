#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log
import sys
from n元谓词 import n元谓词


class 二元关系(n元谓词):

    def __init__(self):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)

    def __str__(self):
        assert(self.mData != None)
        assert(isinstance(self.mData, list))
        assert(len(self.mData) == 2)
        return '{0}{1}{2}'.format(self.mData[0], self.__class__.__name__, self.mData[1])


if __name__ == "__main__":
    # execute only if run as a script
    print(二元关系)
