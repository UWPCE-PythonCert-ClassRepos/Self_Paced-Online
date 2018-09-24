# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:30:51 2018

@author: Laura.Fiorentino
"""

Names = ('Erik', 'Zooey', 'Lacey')
Ages = ('28', '9', '10')
Cost = ('200.10', '10.00', '5000.15')
n1 = len(max(Names))
n2 = len(max(Ages))
n3 = len(max(Cost))
for it in range(len(Names)):
    print('{:{n1}}{:{n2}} ${:{n3}}'.format(Names[it], Ages[it], Cost[it], n1 = n1+2, n2 = n2+2, n3 = n3+2))