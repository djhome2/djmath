#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from 函数 import 函数
from 变量 import 变量
from 实数 import 实数


class 除(函数):
    def __init__(self, 变量1, 变量2):
        v1 = 变量1
        if(not isinstance(v1, 变量)):
            v1 = 变量(x=变量1)
        v2 = 变量2
        if(not isinstance(v2, 变量)):
            v2 = 变量(x=变量2)
        函数.__init__(self, v1, v2)
        return

    def get_default_value(self):
        y1 = self.get_x0()
        y2 = self.get_x1()
        if(self.is_number(y1) and self.is_number(y2)):
            return y1 / y2
        return self

    def get_default_str(self):
        s = '({}) / ({})'.format(self.x[0], self.x[1])
        return s


if __name__ == "__main__":
    # execute only if run as a script
    x = 除(实数(x=2), 实数(x=1))
    print(x)
    x = 除('a', 'b')
    print(x)
    x = 除('a', 实数(x=1))
    print(x)
