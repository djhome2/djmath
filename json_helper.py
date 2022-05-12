#!/usr/bin/env python3


import json
from 集合 import 集合
from 元素 import 元素
from 任意 import 任意


__author__ = 'dj'


def get_id(obj):
    id2 = id(obj)
    # print(':0x{:x}'.format(id2))
    return id2


def json_dumps(clsObj, map2={}):
    key = ':{}'.format(get_id(clsObj))
    map_result = {}
    map_result[key] = type(clsObj)
    if(map2.get(key)):
        return map_result
    map2[key] = type(clsObj)
    # map2['self:{}'.format(get_id(clsObj))] = type(clsObj)
    for k, v in clsObj.__dict__.items():
        # a = getattr(clsObj, k)
        # map2[':{}'.format(get_id(a))] = type(a)
        # map2['{}:{}'.format(k, get_id(a))] = type(a)
        map_result[k] = json_dumps(v, map2)
    # print(dir(clsObj))
    # print(clsObj.__class__)
    # # print(clsObj.__delattr__)
    # print(clsObj.__dict__)
    # # print(clsObj.__dir__)
    # print(clsObj.__doc__)
    # print(vars(clsObj))
    # print(id(clsObj))
    # str = '{}:{:x}'.format(clsObj, id(clsObj))
    # print(str)
    # print(map_result)
    return map_result


if __name__ == "__main__":
    # execute only if run as a script
    A = 集合()
    a = 元素(任意(A))
    map2 = json_dumps(a)
    s2 = str(map2)
    print(s2)
