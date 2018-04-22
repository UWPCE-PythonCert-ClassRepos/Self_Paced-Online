# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:43:21 2018

@author: Karl M. Snyder
"""

num = range(1, 101)
for i in num:
    if (i % 3 == 0) and (i % 5 == 0): print('FizzBuzz')
    elif i % 3 == 0: print('Fizz')
    elif i % 5 == 0: print('Buzz')
    else: print(i)