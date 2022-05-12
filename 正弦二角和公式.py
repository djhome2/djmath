#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from FormulaCallback import FormulaCallback
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


def getLeftPart(*args):
    return 正弦(args)


def getRightPart(*args):
    x = args[0]
    y = args[1]
    a = 乘(正弦(x), 余弦(y))
    b = 乘(余弦(x), 正弦(y))
    f = 加(a, b)
    return f


if __name__ == "__main__":
    # execute only if run as a script
    公式.注册('正弦二角和公式', 'sin(x+y)=sinx*cosy+sinx*cosy',
          getLeftPart, getRightPart, type(加))
