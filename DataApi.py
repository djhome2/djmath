#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from LogApi import log
import time
import datetime
import math
from math import modf

__author__ = 'chengzhi'


def ctp_upround(a, z):
    log.info('ctp_upround - a: %s, z: %s', a, z)
    n = 1.0 / z
#     a = round(a * n + 0.9999)
    f2, n2 = modf(a * n + 0.9999)
    log.info('f2=%s, n2=%s', f2, n2)
    a = n2 / n
    log.info('result: %f', a)
    return a


def ctp_downround(a, z):
    log.info('ctp_downround - a: %s, z: %s', a, z)
    n = 1.0 / z
    f2, n2 = modf(a * n)
    log.info('f2=%s, n2=%s', f2, n2)
    a = n2 / n
#     a = round(a * n - 0.9999)
#     a /= n
    log.info('result: %f', a)
    return a


def getdict(dict2, key, default_value):
    v = dict2.get(key, None)
    if(v == None):
        v = default_value;
        dict2[key] = v
    return v


def format_time(seconds):
    timeArray = time.localtime(seconds)  # 1970秒数
    log.info(timeArray)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    datetime1 = datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    log.info('datetime1: %s', datetime1)
    return datetime1


def format_trade_date_time(trade_date_time):
    ns = trade_date_time
    us = ns / 1000.0
    ms = us / 1000.0
    s = ms / 1000.0
    timeArray = time.localtime(s)
    t = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    log.info('time: %s', t)
    return t


def get_float(v):
    if(isinstance(v, float)):
        if(math.isnan(v)):
            return 0.0
    return float(v)


def update_dict(self, data, prefix=''):
    # log.info('update_dict - %s', prefix)
    # log.info('data - %s', data)
    for k in data:
        v = data[k]
        # log.info('k=%s, v=%s, type=%s', k, v, type(v))
        if(isinstance(v, float)):
            # log.info('v is float')
            if(math.isnan(v)):
                # log.info('v is nan')
                v = 0.0
        self[prefix + k] = v
    # log.info('result - %s', self)

    
def is_weekend():
    t2 = time.localtime()
    log.info('t2: %s', t2)
    wday = t2[6]
    if(wday < 0 or wday > 4):
        return True
    return False

    
if __name__ == "__main__":
    ctp_upround(20100, 5)
    ctp_downround(20100, 5)
    
