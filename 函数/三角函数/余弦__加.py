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


class 余弦__加(函数):

    def __init__(self, 参数1, 参数2):
        函数.__init__(self, 参数1, 参数2)
        return

    def get(self):
        a = self.get_x(self.x[0])
        b = self.get_x(self.x[1])
        c1 = 乘(余弦(a), 余弦(b))
        c2 = 乘(正弦(a), 正弦(b))
        f = 减(c1, c2)
        return f.get()


if __name__ == "__main__":
    # execute only if run as a script
    f = 余弦__加(变量('x'), 变量('y'))
    print(f)
    f = 余弦__加(实数(1), 实数(2))
    print(f)
    f = 余弦__加(实数(1), 变量('a'))
    print(f)
