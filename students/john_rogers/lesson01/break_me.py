#!/usr/bin/env python3
"""
write four python functions that cause an exception
UW python lesson01
Author: JohnR
"""


# ZeroDivisionError
def div(a, b):
    try:
        print(a/b)
    except ZeroDivisionError as err:
        print('Error:', err)


div(5, 0)


# TypeError
def add(x, y):
    try:
        print(x + y)
    except TypeError as err:
        print('Error:', err)


add('2', 4)


# NameError
# Question: While this throws a NameError, it doesn't appear to be
# caught by the except statement; not sure why?
def name(z, w):
    try:
        print(z + w)
    except NameError as err:
        print('Error:', err)


name('Tony', Stark)


# AttributeError
def foo(a):
    try:
        a.append(2)
    except AttributeError as e:
        print('Error:', e)


foo(4)


# SyntaxError
# Same as NameError, can create one but cannot capture one
# with the try/except clause
def syntax(value):
    try:
        print(value))
    except SyntaxError as e:
        print('Error:', e)


syntax('no error')

