#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import sys
from LogApi import log


class 集合():

    def __init__(self):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)


if __name__ == "__main__":
    # execute only if run as a script
    print(集合)
