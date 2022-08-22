#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log
from 加 import 加
from 变量 import 变量
import uuid
import math
import sys

from 实数 import 实数
from 负 import 负


class 减(加):

    def __init__(self,  变量1, 变量2):
        log.info('Sin  __init__ --- ')
        加.__init__(self, 变量1, 负(变量2))
        return


if __name__ == "__main__":
    # execute only if run as a script
    x = 减(实数(x=2), 实数(x=1))
    print(x)
    x = 减('a', 'b')
    print(x)
    x = 减('a', 实数(x=1))
    print(x)
