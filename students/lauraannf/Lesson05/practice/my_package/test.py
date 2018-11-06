# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:25:58 2018

@author: Laura.Fiorentino
"""

try:
    f = open('missing.txt')
except FileNotFoundError:
    print("couldn't open missing.txt")
finally:
    print('a')
