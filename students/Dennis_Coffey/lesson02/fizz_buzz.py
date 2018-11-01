# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:28:33 2018

@author: dennis
"""

for i in range(100):
    if i % 5 + i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)