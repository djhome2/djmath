#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
from LogApi import log
from 函数 import 函数
from 变量 import 变量
from 实数 import 实数


class 负(函数):

    def __init__(self, 变量1):
        log.info('Sin  __init__ --- ')
        v1 = 变量1
        if(not isinstance(v1, 变量)):
            v1 = 变量(x=变量1)
        函数.__init__(self, v1)
        return

    def get_default_value(self):
        y1 = self.get_x(self.x[0])
        return -y1

    def get_default_str(self):
        return '-({})'.format(self.x[0])

    def 负值(self):
        return self.x[0]


if __name__ == "__main__":
    # execute only if run as a script
    x = 负(实数(x=2))
    print(x)
    x = 负('a')
    print(x)
