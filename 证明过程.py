#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log


from mdb_config_set import math_db

import pickle
import sys


g_define_set = math_db['定义']
g_proof_set = math_db['证明过程']


class 证明过程():

    def __init__(self):
        log.info('entering %s.%s --- ',
                 self.__class__.__name__, sys._getframe().f_code.co_name)

    def get(self, key):
        key_json = pickle.dumps(key)
        cond2 = {'key': key_json}
        result2 = g_proof_set.find_one(cond2)
        if(result2 != None):
            return None
        value_json = result2['value']
        return pickle.loads(value_json)

    def setValue(self, key, value):
        if(value == True):
            print('{0}'.format(key, value))
        elif(value == False):
            print('设置{0}为{1}'.format(key, value))
        else:
            print('设置{0}为{1}'.format(key, value))
        key_json = pickle.dumps(key)
        value_json = pickle.dumps(value)
        value2 = {'key': key_json, 'value': value_json}
        cond2 = {'key': key_json}
        g_proof_set.update_one(cond2, {'$set': value2}, True)
        return


证明过程 = 证明过程()

if __name__ == "__main__":
    # execute only if run as a script
    print(证明过程)
