#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from pymongo.mongo_client import MongoClient
from LogApi import log
import ctp_argv
import sys

__author__ = 'dj'


# if('win32' == sys.platform):
#     mdb_conn = MongoClient('192.168.30.128', 27017)
# else:
#     mdb_conn = MongoClient('localhost', 27017)

mdb_conn = MongoClient('localhost', 27017)

math_db = mdb_conn.math_db
g_config_set = math_db['mdb_config_set']


def getConfig(name, default):
    result = g_config_set.find_one({'name': name})
    log.info('result: %s', result)
    if result:
        return result['value']
    return default


def setConfig(name, value):
    data = {'name': name, 'value': value}
    result = g_config_set.update({'name': name}, data, True)
    log.info('result: %s', result)


def import_mdb(tname, data):
    log.info('import_mdb: tname=%s', tname)
    tset = math_db[tname]
    tset.delete_many({})
    for d in data:
        tset.insert(d)


log.info('end')

if __name__ == "__main__":
    # execute only if run as a script
    log.info('test')
