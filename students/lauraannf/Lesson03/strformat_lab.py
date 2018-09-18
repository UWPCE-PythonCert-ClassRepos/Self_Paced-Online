# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:00:52 2018

@author: Laura.Fiorentino
"""
print('----------Task One--------')
testtuple = (2, 123.4567, 10000, 12345.67)
files = 'file_{:03d} :   {:.2f}, {:.2e}, {:.3g}'.format(testtuple[0], testtuple[1], testtuple[2], testtuple[3])
#files = 'file_{:03d} :   {}, {}, {}'.format(testtuple)
print(files)

