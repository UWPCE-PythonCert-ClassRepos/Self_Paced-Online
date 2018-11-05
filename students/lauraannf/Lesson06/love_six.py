# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:24:32 2018

@author: Laura.Fiorentino
"""


def love_six(a, b):
    if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
        return True
    else:
        return False
