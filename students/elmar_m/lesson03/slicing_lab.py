#!/usr/bin/env python3

'''
file: slicing_lab.py
elmar_m / 22e88@mailbox.org
Lesson03: Slicing Lab Exercise
Functions for slicing sequences.
'''

# mystr = "this is a string"
# t = (2, 54, 13, 12, 5, 32)

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exfl(a):
    '''
    return a given sequence with the first and last item exchanged
    '''
    # print(a)
    # print(a[-1:])
    # print(a[1:-1])
    # print(a[0])
    # print(a[-1] + a[1:-1] + a[0])

    # print(a[-1:] + a[1:-1] + a[:1])
    return a[-1:] + a[1:-1] + a[:1]

    # print(a[-1:] + a[1:-1] + a[:1])
    # return a[-1:] + a[1:-1] + a[:1]


def onlyfl(a):
    '''
    return only the first and last item, remove everything in between 
    '''
    return a[:1] + a[-1:]

def withoutfl4(a):
    '''
    remove the first 4 and the last 4 items of a given sequence and 
    return everything in between
    '''
    return a[4:-4]

def reverse(a):
    '''
    return the sequence with the elements reversed:
    '''
    return a[::-1]

def third(a):
    '''
    with the middle third, then last third, then the first third in the new order.
    '''
    # thrd = len(a) // 3
    n = len(a) // 3
    return a[n:-n] + a[-n:] + a[:n]


'''
Assertions:
'''
assert exfl(a_string) == "ghis is a strint"
assert exfl(a_tuple) == (32, 54, 13, 12, 5, 2)


if __name__ == '__main__':
    # print('__name__ is set to "__main__", you executed this directly as a script.')
    exfl(a_string)
    exfl(a_tuple)
    
