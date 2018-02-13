#!/usr/bin/env python3

'''
file: slicing_lab.py
elmar_m / 22e88@mailbox.org
Lesson03: Slicing Lab Exercise
Functions for slicing sequences.
'''

mystr = "this is a string"
t = (2, 54, 13, 12, 5, 32)


def exfl(a):
    '''
    return a given sequence with the first and last item exchanged
    '''
    # print(a[-1] + a[1:-1] + a[0])
    return a[-1:] + a[1:-1] + a[:0]


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
# assert exchange_first_last(a) == "ghis is a strint"
assert exfl(mystr) == "ghis is a strint"
# assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exfl(t) == (32, 54, 13, 12, 5, 2)


if __name__ == '__main__':
    print('__name__ is set to "__main__", you executed this directly as a script.')
    print(exfl(mystr))
    
