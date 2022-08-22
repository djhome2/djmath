#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import inspect


class 函数():

    def __init__(self,  *x):
        self.x = x
        return

    def set(self, *x):
        # log.info('set value=%s', x)
        self.x = x
        return

    def get(self):
        cls = self.__class__
        name = cls.__name__
        n2 = cls.__qualname__
        # print(dir(cls))
        # print(cls.__dict__)
        # stack = inspect.stack()
        # s1 = stack[1]
        # name = inspect.stack()[1][3]
        s = '{}{}'.format(name, self.x)
        return s

    def __str__(self):
        return str(self.get())

    def get_expand(self):
        if(len(self.x) != 1):
            return None
        x = self.x[0]
        if(not isinstance(x, 函数)):
            return None
        try:
            m1 = self.__module__
            m2 = x.__module__
            m3 = '{}__{}'.format(m1, m2)
            m4 = __import__(m3)
            class2 = getattr(m4, m3)
            cls_obj = class2(x)
            return cls_obj.get()
        except Exception as e:
            pass
        return None


if __name__ == "__main__":
    # execute only if run as a script
    print(函数(1, 2, 3))
    print(函数('a', 3))
