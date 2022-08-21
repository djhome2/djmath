#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 函数 import 函数
from 变量 import 变量
from 实数 import 实数
from 未知数 import 未知数


class 负(函数):

    def __init__(self, 变量1):
        log.info('Sin  __init__ --- ')
        v1 = 变量1
        if(not isinstance(v1, 变量)):
            v1 = 变量(x=变量1)
        函数.__init__(self, '负', v1)
        return

    def get(self):
        y1 = self.x[0].get()
        try:
            return -y1
        except Exception as e:
            pass
        s = '-({})'.format(y1)
        return s

    def 负值(self):
        return self.x[0]


if __name__ == "__main__":
    # execute only if run as a script
    x = 负(实数(x=2))
    print(x)
    x = 负('a')
    print(x)
