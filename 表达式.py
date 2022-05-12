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


class 表达式():
    args = None

    def __init__(self, *args):
        log.info('Sin  __init__ --- ')
        self.args = args

    def 形如(self, *new_args):
        n1 = len(self.args)
        n2 = len(new_args)
        if(n1 != n2):
            return False
        for i in range(0, n1):
            p1 = self.args[i]
            p2 = new_args[i]
            t2 = type(p2)
            if(not isinstance(p1, t2)):
                return False
        return True


if __name__ == "__main__":
    # execute only if run as a script
    f = 表达式(变量('x'), 变量('y'))
    f.形如(变量('a'), 变量('b'))
