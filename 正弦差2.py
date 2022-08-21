#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from 乘 import 乘
from 函数 import 函数
from 变量 import 变量
from 函数.三角函数.正弦 import 正弦
from 函数.三角函数.余弦 import 余弦

from 加 import 加
from 实数 import 实数
from 正弦和2 import 正弦和2
from 负 import 负


class 正弦差2(正弦和2):

    def __init__(self, 参数1, 参数2):
        正弦和2.__init__(self,  参数1, 负(参数2))
        self.name = '正弦差2'
        return


if __name__ == "__main__":
    # execute only if run as a script
    f = 正弦差2(变量('x'), 变量('y'))
    print(f)
    f = 正弦差2(实数(1), 实数(2))
    print(f)
    f = 正弦差2(实数(1), 变量('a'))
    print(f)
