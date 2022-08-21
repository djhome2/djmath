#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import sys
import os


path_0 = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path_0)

path_1 = os.path.abspath(os.path.join(path_0, '..'))
sys.path.append(path_1)

path_2 = os.path.abspath(os.path.join(path_1, '..'))
sys.path.append(path_2)
