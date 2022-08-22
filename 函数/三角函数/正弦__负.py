#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import __init__


from 乘 import 乘
from 函数 import 函数
from 变量 import 变量
from 正弦 import 正弦
from 余弦 import 余弦

from 加 import 加
from 实数 import 实数
from 负 import 负


class 正弦__负(函数):

    def __init__(self, 参数1):
        函数.__init__(self, 参数1)
        assert(isinstance(参数1, 负))
        return

    def get(self):
        x = self.x[0]
        assert(isinstance(x, 负))
        a = x.负值()
        b = 负(正弦(a))
        return b.get()


if __name__ == "__main__":
    # execute only if run as a script
    x = 变量('x')
    y = 负(x)
    f = 正弦__负(y)
    print(f)
    x = 实数(1)
    y = 负(x)
    f = 正弦__负(y)
    print(f)
