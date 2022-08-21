#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from 乘 import 乘
from 函数 import 函数
from 变量 import 变量
from 函数.三角函数.正弦 import 正弦
from 函数.三角函数.余弦 import 余弦

from 加 import 加
from 实数 import 实数


class 正弦和2(函数):

    def __init__(self, 参数1, 参数2):
        函数.__init__(self, '正弦和2', 参数1, 参数2)
        return

    def get(self):
        a = self.x[0].get()
        b = self.x[1].get()
        c1 = 乘(正弦(a), 余弦(b))
        c2 = 乘(余弦(a), 正弦(b))
        f = 加(c1, c2)
        return f.get()


if __name__ == "__main__":
    # execute only if run as a script
    f = 正弦和2(变量('x'), 变量('y'))
    print(f)
    f = 正弦和2(实数(1), 实数(2))
    print(f)
    f = 正弦和2(实数(1), 变量('a'))
    print(f)
