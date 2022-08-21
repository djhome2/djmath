#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from LogApi import log

import uuid
import math
import sys
from 乘 import 乘
from 变量 import 变量
from 函数.三角函数.正弦 import 正弦
from 函数.三角函数.余弦 import 余弦

from 加 import 加
from mdb_config_set import math_db

import pickle

g_formula_set = math_db['mdb_formula_set']


class FormulaCallback():
    name = None
    desc = None
    argsType = None

    def __init__(self):
        log.info('Sin  __init__ --- ')

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def getArgsType(self):
        return self.argsType

    def getFullMethod(self, *args):
        return None

    def getValue(self, *args):
        return None


if __name__ == "__main__":
    # execute only if run as a script
    print('公式')
