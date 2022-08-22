#!/usr/bin/python3
# -*- coding: UTF-8 -*-


class 函数():

    def __init__(self, *x):
        self.x = x
        return

    def set(self, *x):
        # log.info('set value=%s', x)
        self.x = x
        return

    def get(self):
        # cls = self.__class__
        # name = cls.__name__
        # n2 = cls.__qualname__
        # # print(dir(cls))
        # # print(cls.__dict__)
        # # stack = inspect.stack()
        # # s1 = stack[1]
        # # name = inspect.stack()[1][3]
        # s = '{}{}'.format(name, self.x)
        v1 = self.get_expand_f_g()
        if(v1 != self):
            return v1
        try:
            return self.get_default_value()
        except Exception as e:
            return self

    def get_default_value(self):
        return self

    def __str__(self):
        s1 = self.get()
        if(s1 != self):
            return str(s1)
        return self.get_default_str()

    def get_default_str(self):
        s = '{}{}'.format(self.__class__.__name__, self.x)
        return s

    def get_expand_f_g(self):
        if(len(self.x) != 1):
            return self
        x = self.x[0]
        if(not isinstance(x, 函数)):
            return self
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
        return self

    def is_number(self, x):
        return isinstance(x, float) or isinstance(x, int) or isinstance(x, complex)

    def get_x(self, x):
        try:
            return x.get()
        except Exception as e:
            return x


if __name__ == "__main__":
    # execute only if run as a script
    print(函数(1, 2, 3))
    print(函数('a', 3))
