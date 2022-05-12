#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log

import uuid
import math
import sys
from 乘 import 乘
from 公式 import 公式
from 变量 import 变量
from 正弦 import 正弦
from 余弦 import 余弦

from 加 import 加
from 减 import 减


class 二角和差公式(dict):
    args = None

    def __init__(self, *args):
        log.info('Sin  __init__ --- ')
        self.args = args

    def 正弦和(self):
        z = 加(*self.args)
        k = 正弦(z)
        x = self.args[0]
        y = self.args[1]
        a = 乘(正弦(x), 余弦(y))
        b = 乘(余弦(x), 正弦(y))
        f = 加(a, b)
        return k, f

    def 正弦差(self):
        z = 减(*self.args)
        k = 正弦(z)
        x = self.args[0]
        y = self.args[1]
        a = 乘(正弦(x), 余弦(y))
        b = 乘(余弦(x), 正弦(y))
        f = 减(a, b)
        return k, f

    def 余弦和(self):
        z = 加(*self.args)
        k = 余弦(z)
        x = self.args[0]
        y = self.args[1]
        a = 乘(余弦(x), 余弦(y))
        b = 乘(正弦(x), 正弦(y))
        f = 减(a, b)
        return k, f

    def 余弦差(self):
        z = 减(*self.args)
        k = 余弦(z)
        x = self.args[0]
        y = self.args[1]
        a = 乘(余弦(x), 余弦(y))
        b = 乘(正弦(x), 正弦(y))
        f = 加(a, b)
        return k, f

    def 定义(self):
        公式.dumps(*self.正弦和())
        公式.dumps(*self.正弦差())
        公式.dumps(*self.余弦和())
        公式.dumps(*self.余弦差())


if __name__ == "__main__":
    # execute only if run as a script
    f = 二角和差公式(变量('x'), 变量('y'))
    f.定义()
