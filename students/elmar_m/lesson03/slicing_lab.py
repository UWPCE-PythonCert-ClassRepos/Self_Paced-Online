#!/usr/bin/env python3

'''
file: slicing_lab.py
elmar_m / 22e88@mailbox.org
Lesson03: Slicing Lab Exercise
Functions for slicing sequences.
'''

a_string = "this is a string"
al_string = "this is an even longer string and it still goes on"
a_tuple = (2, 54, 13, 12, 5, 32)
al_tuple = (2, 54, 13, 12, 5, 32, 48, 102, 9, 11, 2056, 299)

def exfl(a):
    '''
    return a given sequence with the first and last item exchanged
    '''
    return a[-1:] + a[1:-1] + a[:1]

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
    n = len(a) // 3
    return a[n:-n] + a[-n:] + a[:n]


'''
Assertions:
'''
assert exfl(a_string) == "ghis is a strint"
assert exfl(a_tuple) == (32, 54, 13, 12, 5, 2)
 
assert onlyfl(a_string) == "tg"
assert onlyfl(a_tuple) == (2, 32)
 
assert withoutfl4(a_string) == " is a st"
assert withoutfl4(a_tuple) == ()
 
assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

assert third(a_string) == "is a stringthis "
assert third(al_tuple) == (5, 32, 48, 102, 9, 11, 2056, 299, 2, 54, 13, 12)

if __name__ == '__main__':
    print('__name__ is set to "__main__", you executed this directly as a script.')
