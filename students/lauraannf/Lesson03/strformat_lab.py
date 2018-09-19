# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:00:52 2018

@author: Laura.Fiorentino
"""
print('----------Task One--------')
testtuple = (2, 123.4567, 10000, 12345.67)
# files1 = 'file_{:03d} :   {:.2f}, {:.2e}, {:.3g}'.format(testtuple[0], testtuple[1], testtuple[2], testtuple[3])
files1 = 'file_{:03d} :   {:.2f}, {:.2e}, {:.3g}'.format(*testtuple)
print(files1)
print()


print('----------Task Two--------')
files2 = 'file_{key1:03d} :   {:.2f}, {:.2e}, {:.3g}'.format(*testtuple[1:], key1=testtuple[0])
print(files2)
print()
files3 = f"file_{testtuple[0]:03d} :   {testtuple[1]:.2f}, {testtuple[2]:.2e}, {testtuple[3]:.3g}"
print(files3)
print()

print('----------Task Three--------')
def formatter(in_tuple):
    form_string = 'the {num:d} numbers are: ' + '{}, '*(len(in_tuple)-1) + '{}'
    return form_string.format(*in_tuple[0:-1], in_tuple[-1], num = len(in_tuple))
print('run formatter with a tuple of arbitrary length')
print()

print('----------Task Four--------')
testtuple2=(4,30,2017,2,27)
files4 = '{:02d} {} {} {:02d} {}'.format(testtuple2[-2], testtuple2[-1], testtuple2[2],
          testtuple2[0], testtuple2[1])
print(files4)
print()

print('----------Task Five--------')
