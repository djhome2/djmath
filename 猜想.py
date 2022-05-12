#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from LogApi import log


from mdb_config_set import math_db

import pickle


g_guess_set = math_db['猜想']
g_proof_set = math_db['证明过程']


class 猜想():
    name = None
    如果 = None
    那么 = None

    def __init__(self, name=None, 如果=None, 那么=None):
        log.info('Sin  __init__ --- ')
        self.name = name
        self.如果 = 如果
        self.那么 = 那么

    # def loadName(self, name):
    #     c2 = g_define_set.find_one({'name': name})
    #     self.如果 = pickle.loads(c2['if'])
    #     self.那么 = pickle.loads(c2['then'])
    #     return

    def save(self):
        # cond2 = {'if:': 如果, 'then': 那么}
        # print(cond2)
        # self[如果] = 那么
        # key_json = pickle.dumps(name)
        # cond2 = {'if': 如果}
        # d2 = cond2.copy()
        if_json = pickle.dumps(self.如果)
        then_json = pickle.dumps(self.那么)
        value2 = {'name': self.name, 'if': if_json, 'then': then_json}
        cond2 = {'name': self.name}
        # d2['value'] = fx_json
        # d2['desc'] = desc
        g_guess_set.update_one(cond2, {'$set': value2}, True)
        return

    def 证明(self):
        # s1 = str(self.如果)
        # s2 = str(self.那么)
        print('求证：\n{0}，{1}'.format(self.如果, self.那么))
        g_proof_set.delete_many({})
        print('导入所有已知定义：\n')
        cursor2 = g_guess_set.find()
        for c2 in cursor2:
            print('导入定义  ---  {0}：\n'.format(c2['name']))
            # y = c2['name']
            # y = pickle.loads(y_json)
            # fx_json = c2['value']
            # fx = pickle.loads(fx_json)
            if_json = pickle.loads(c2['if'])
            then_json = pickle.loads(c2['then'])
            if_json.setValue(True)
            then_json.setValue(True)
            print('\n')
        print('证明：\n')
        self.如果.setValue(True)
        return self.那么.getValue()

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

    # def 注册(self, name, desc, yCallBack, fxCallback, *argsType):
    #     print(desc)
    #     v2 = {'name:': name, 'desc': desc, 'argsType': argsType,
    #           'yCallBack': yCallBack, 'fxCallback': fxCallback}
    #     print(v2)
    #     self[name] = v2
    #     # key_json = pickle.dumps(name)
    #     cond2 = {'name': name}
    #     d2 = cond2.copy()
    #     fx_json = pickle.dumps(v2)
    #     d2['value'] = fx_json
    #     d2['desc'] = desc
    #     g_define_set.update(cond2, d2, True)

    # def 长度(self):
    #     return len(self.mData)


# 定义 = 定义()
if __name__ == "__main__":
    # execute only if run as a script
    print(猜想)
