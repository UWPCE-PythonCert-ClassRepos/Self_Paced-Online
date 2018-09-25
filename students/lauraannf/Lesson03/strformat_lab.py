# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:00:52 2018

@author: Laura.Fiorentino
"""
print('----------Task One--------')
test_tuple = (2, 123.4567, 10000, 12345.67)
files1 = 'file_{:03d} :   {:.2f}, {:.2e}, {:.3g}'.format(*test_tuple)
print(files1)
print()

print('----------Task Two--------')
files2 = 'file_{key1:03d} :   {:.2f}, {:.2e}, {:.3g}'.format(*test_tuple[1:],
                                                            key1=test_tuple[0])
print(files2)
print()
files3 = f"file_{test_tuple[0]: 03d} :   {test_tuple[1]: .2f}, \
    {test_tuple[2]: .2e}, {test_tuple[3]: .3g}"
print(files3)
print()

print('----------Task Three--------')


def formatter(in_tuple):
    form_string = 'the {num:d} numbers are: ' + '{}, '*(len(in_tuple)-1) + '{}'
    return form_string.format(*in_tuple[0:-1], in_tuple[-1], num=len(in_tuple))


print('run formatter with a tuple of arbitrary length')
print()

print('----------Task Four--------')
test_tuple2 = (4, 30, 2017, 2, 27)
files4 = '{:02d} {} {} {:02d} {}'.format(test_tuple2[-2], test_tuple2[-1],
                                         test_tuple2[2], test_tuple2[0],
                                         test_tuple2[1])
print(files4)
print()
print('----------Task Five--------')
testlist = ['oranges', 1.3, 'lemons', 1.1]
teststring = f"The weight of an {testlist[0][:-1]} is {testlist[1]} and \
        the weight of a {testlist[2][:-1]} is {testlist[3]}."
teststring2 = f"The weight of an {testlist[0][:-1].upper()} is \
    {testlist[1]*1.2} and the weight of a {testlist[2][:-1].upper()} \
    is {testlist[3]*1.2}."
print(teststring)
print(teststring2)
print()

print('----------Task Six--------')
Names = ('Erik', 'Zooey', 'Lacey')
Ages = ('28', '9', '10')
Cost = ('200.10', '10.00', '5000.15')
n1 = len(max(Names))
n2 = len(max(Ages))
n3 = len(max(Cost))
for it in range(len(Names)):
    print('{:{n1}}{:{n2}} ${:{n3}}'.format(Names[it], Ages[it], Cost[it],
                                           n1=n1+2, n2=n2+2, n3=n3+2))
tuple10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:5}'*10).format(*tuple10))
