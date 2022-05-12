#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

__author__ = 'dj'

print('Content-type:text/plain; charset=utf-8')
print('')

import sys, platform
# print(sys.platform)
# print(platform.system())

if('win32' == sys.platform):
    args_spilt_array = sys.argv[0].rsplit('\\', 1)
else:
    args_spilt_array = sys.argv[0].rsplit('/', 1)

directory = args_spilt_array[0]
pathname = args_spilt_array[1]
pgname, suffix = pathname.split('.', 1)


def has_argv(argv):
    for i in range(1, len(sys.argv)):
        k = sys.argv[i]
        if(argv == k):
            return True
    return False


def get_argv_value(argv):
    for i in range(1, len(sys.argv)):
        kv = sys.argv[i]
        s = kv.split('=')
        if(argv == s[0]):
            return s[1]
    return None


def is_sim():
    return has_argv('sim')
    

def is_logfile():
    return has_argv('logfile')


def is_once():
    return has_argv('once')


def is_clear():
    return has_argv('clear')


def get_risk():
    return get_argv_value('risk')


def get_pyname():
    print('sys.argv: ', sys.argv)
    name = sys.argv[0]
    print('name: ', name)
    dirs = name.split('/')
    print('dirs: ', dirs)
    pg = dirs[len(dirs) - 1]
    print('pg: ', pg)
    d, n = pg.split('.', 1)
    print('d: ', d)
    print('n: ', n)
    return d


def is_orderable():
    return has_argv('is_orderable')


def is_debug():
    return has_argv('debug')

