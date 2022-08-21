#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from 未知数 import 未知数


class 函数():

    def __init__(self, *x):
        self.x = x
        self.y = 未知数
        return

    def set(self, *x):
        # log.info('set value=%s', x)
        self.x = x
        self.y = 未知数
        return

    def get(self):
        # log.info('get x=%s', self.x)
        if(self.y == 未知数):
            self.y = self.值()
        return self.y

    def __str__(self):
        return str(self.get())

    def 值(self):
        return 未知数


if __name__ == "__main__":
    # execute only if run as a script
    print(函数())
