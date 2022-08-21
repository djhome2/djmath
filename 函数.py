#!/usr/bin/python3
# -*- coding: UTF-8 -*-


class 函数():

    def __init__(self, name, *x):
        self.name = name
        self.x = x
        return

    def set(self, *x):
        # log.info('set value=%s', x)
        self.x = x
        return

    def get(self):
        s = '{}{}'.format(self.name, self.x)
        return s

    def __str__(self):
        return str(self.get())


if __name__ == "__main__":
    # execute only if run as a script
    print(函数('f', 1, 2, 3))
    print(函数('f', 'a', 3))
