#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log

import sys

from 二元关系 import 二元关系

from 命题 import 命题
from 如果 import 如果
from 猜想 import 猜想


from 任意 import 任意
from 那么 import 那么
from 集合 import 集合
from 属于 import 属于
from 元素 import 元素


class 子集(二元关系):

    def __init__(self):
        二元关系.__init__(self)
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)

    def __str__(self):
        assert(self.mData != None)
        assert(isinstance(self.mData, list))
        assert(len(self.mData) == 2)
        return '{0}是{1}的{2}'.format(self.mData[0], self.mData[1], self.__class__.__name__)

    def setValue(self, value):
        二元关系.setValue(self, value)
        # d = 猜想()
        # d.loadName('子集')
        # d.如果.setValue(True)
        # d.那么.setValue(True)


def 定义():
    A = 集合()
    a = 元素(任意(A))
    # a.属于(A)
    B = 集合()
    # a.属于(B)
    # cond1 = {a: {属于: A}}
    # cond2 = {a: {属于: B}}
    # a1 = 命题(属于(), [a, A])
    a2 = 命题(属于(), [a, B])
    a3 = 命题(子集(), [A, B])
    猜想('子集', 如果(a2), 那么(a3)).save()


def 推论1():
    A = 集合()
    a = 元素(任意(A))
    # a.属于(A)
    B = 集合()
    # a.属于(B)
    # cond1 = {a: {属于: A}}
    # cond2 = {a: {属于: B}}
    # a1 = 命题(属于(), [a, A])
    a1 = 命题(子集(), [A, B])
    a2 = 命题(属于(), [a, B])
    d = 猜想('子集-推论1', 如果(a1), 那么(a2))
    assert(d.证明())
    d.save()


if __name__ == "__main__":
    # execute only if run as a script
    定义()
    推论1()
