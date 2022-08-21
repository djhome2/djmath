#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from 函数 import 函数
from 变量 import 变量
from 实数 import 实数


class 乘(函数):

    def __init__(self, 变量1, 变量2):
        v1 = 变量1
        if(not isinstance(v1, 变量)):
            v1 = 变量(x=变量1)
        v2 = 变量2
        if(not isinstance(v2, 变量)):
            v2 = 变量(x=变量2)
        函数.__init__(self, '乘', v1, v2)
        return

    def get(self):
        y1 = self.x[0].get()
        y2 = self.x[1].get()
        try:
            return y1 * y2
        except Exception as e:
            pass
        if(isinstance(y1, float)):
            return '{} * ({})'.format(y1, y2)
        if(isinstance(y2, float)):
            return '({}) * {}'.format(y1, y2)
        return '({}) * ({})'.format(y1, y2)


if __name__ == "__main__":
    # execute only if run as a script
    x = 乘(实数(x=2), 实数(x=1))
    print(x)
    x = 乘('a', 'b')
    print(x)
    x = 乘('a', 实数(x=1))
    print(x)
