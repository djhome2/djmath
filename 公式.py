#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log

import uuid
import math
import sys
from 乘 import 乘
from 变量 import 变量
from 正弦 import 正弦
from 余弦 import 余弦

from 加 import 加
from mdb_config_set import math_db

import pickle

g_formula_set = math_db['mdb_formula_set']


class 公式(dict):
    mData = []

    def __init__(self):
        log.info('Sin  __init__ --- ')
        # cursor2 = g_formula_set.find()
        # for c2 in cursor2:
        #     y = c2['name']
        #     # y = pickle.loads(y_json)
        #     fx_json = c2['value']
        #     fx = pickle.loads(fx_json)
        #     self[y] = fx
        #     print('{}={}'.format(y, fx))

    # def dumps(self, *args):
    #     y = args[0]
    #     fx = args[1]
    #     self[y] = fx
    #     y_json = pickle.dumps(y)
    #     cond2 = {'y': y_json}
    #     d2 = cond2.copy()
    #     fx_json = pickle.dumps(fx)
    #     d2['fx'] = fx_json
    #     g_formula_set.update(cond2, d2, True)
    #     s = '{}={}'.format(y, fx)
    #     print(s)

    def 注册(self, name, desc, yCallBack, fxCallback, *argsType):
        print(desc)
        v2 = {'name:': name, 'desc': desc, 'argsType': argsType,
              'yCallBack': yCallBack, 'fxCallback': fxCallback}
        print(v2)
        self[name] = v2
        # key_json = pickle.dumps(name)
        cond2 = {'name': name}
        d2 = cond2.copy()
        fx_json = pickle.dumps(v2)
        d2['value'] = fx_json
        d2['desc'] = desc
        g_formula_set.update(cond2, d2, True)

    def 长度(self):
        return len(self.mData)


公式 = 公式()

if __name__ == "__main__":
    # execute only if run as a script
    print(公式)
