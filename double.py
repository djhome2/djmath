#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from LogApi import log
from variable import Variable
import uuid


class double():
    value = None
    
    def __init__(self, value=None):
        log.info('Double  __init__ --- ')
        self.value = value
        
    def set(self, value):
        log.info('set value=%s', value)
        self.value = value
        
    def get(self):
        log.info('get value=%s', value)
        return self.value 


if __name__ == "__main__":
    # execute only if run as a script
    x = double('1')
    print(x)

