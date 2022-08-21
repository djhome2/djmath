#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log

import uuid
import math
import sys
from 乘 import 乘
from 二角和差公式 import 二角和差公式
from 公式 import 公式
from 变量 import 变量
from 和 import 和
from 函数.三角函数.正弦 import 正弦
from 函数.三角函数.余弦 import 余弦

from 加 import 加
from 减 import 减


class 三角和公式(dict):
    args = None

    def __init__(self, *args):
        log.info('Sin  __init__ --- ')
        self.args = args

    def 正弦和(self):
        k = 正弦(和(*self.args))
        print(k)
        k1 = 二角和差公式(加(self.args[0], self.args[1]), self.args[2])
        print(k1)
        v2 = k1.正弦和()
        print(v2)
        fx = v2[1]
        print(fx)
        return k, fx

    def 余弦和(self):
        k = 余弦(和(*self.args))
        print(k)
        k1 = 二角和差公式(加(self.args[0], self.args[1]), self.args[2])
        print(k1)
        v2 = k1.余弦和()
        print(v2)
        fx = v2[1]
        print(fx)
        return k, fx

    def 定义(self):
        公式.dumps(*self.正弦和())
        公式.dumps(*self.余弦和())


if __name__ == "__main__":
    # execute only if run as a script
    f = 三角和公式(变量('x'), 变量('y'), 变量('z'))
    f.定义()
