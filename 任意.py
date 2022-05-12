#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log


class 任意():
    mData = None

    def __init__(self, value=None):
        log.info('Sin  __init__ --- ')
        self.mData = value


if __name__ == "__main__":
    # execute only if run as a script
    # a=元(任意)
    print(任意)
