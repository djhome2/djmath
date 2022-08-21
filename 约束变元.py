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
from 公式 import 公式
from 逻辑词 import 逻辑词

g_formula_set = math_db['mdb_formula_set']


class 约束变元():

    def __init__(self) -> None:
        pass
