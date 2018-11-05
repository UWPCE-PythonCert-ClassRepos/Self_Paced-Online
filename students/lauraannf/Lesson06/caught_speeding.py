# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:35:09 2018

@author: Laura.Fiorentino
"""


def caught_speeding(speed, birthday):
    if birthday is False:
        a = 61
        b = 80
    else:
        a = 66
        b = 85
    if speed < a:
        ticket = 0
    elif speed >= a and speed <= b:
        ticket = 1
    else:
        ticket = 2
    return ticket
