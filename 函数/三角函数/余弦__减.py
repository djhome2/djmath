#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import __init__


from 乘 import 乘
from 减 import 减
from 函数 import 函数
from 变量 import 变量
from 正弦 import 正弦
from 余弦 import 余弦


from 实数 import 实数
from 负 import 负
from 余弦__加 import 余弦__加


class 余弦__减(余弦__加):

    def __init__(self, 参数1, 参数2):
        余弦__加.__init__(self, 参数1, 负(参数2))
        return


if __name__ == "__main__":
    # execute only if run as a script
    f = 余弦__减(变量('x'), 变量('y'))
    print(f)
    f = 余弦__减(实数(1), 实数(2))
    print(f)
    f = 余弦__减(实数(1), 变量('a'))
    print(f)
