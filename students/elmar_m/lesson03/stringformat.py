#!/usr/bin/env python3

'''
file: stringformat_lab.py
elmar_m / 22e88@mailbox.org
Lesson03: String Formatting Lab Exercise
'''

a_tuple = ( 2, 123.4567, 10000, 12345.67)
b_tuple = ( 999, 123.4567, 10000, 12345.67)
l_tuple = ( 999, 123.4567, 10000, 12345.67, 28282, 5, 34.0887, 1)
x_tuple = ( 999, 123.4567, 10000, 12345.67, 28282, 5, 34.0887, 1, 'abc', 'def', 12)



def task1(t):
    '''
    Task 1
    '''
    # print('file_{} {} {} {}'.format(*t))  # OK
    # print('file_{:0>3d} {:.2f} {:.2e} {:.3e}'.format(*t))
    return 'file_{:0>3d} {:.2f} {:.2e} {:.3e}'.format(*t)


def task2(t):
    '''
    Task 2
    '''
    filename, n1, n2, n3 = t
    print(filename, n1, n2, n3)
    # return 'file_{:0>3d} {:.2f} {:.2e} {:.3e}'.format(*t)     # OK
    # return 'file_{filename:0>3d} {n1:.2f} {n2:.2e} {n3:.3e}'.format(filename, n1, n2, n3)  # not ok
    return 'file_{pos1:0>3d} {pos2:.2f} {pos3:.2e} {pos4:.3e}'.format(pos1=filename, pos2=n1, pos3=n2, pos4=n3)


def task3(t):
    '''
    Task 3
    '''
    flist= []
    for i in t:
        # print('item:', i)
        # print('{:d}', i)
        # flist.append('{:d}')
        flist.append('{}')
    # print(' '.join(fstring))
    fstring = ' '.join(flist)
    return fstring.format(*t)



'''
Task 4
'''




'''
Task 5
'''




'''
Task 6
'''






if __name__ == '__main__':
    print('This file contains functions for the stringformatting lab exercises, please import it to use them')
