#!/usr/bin/env python

"""
Lesson1, Task 1: Explore Errors
"""


def name_error():
    print(error)


def type_error():
    d = {'a': 0, 'b': 1}
    s = {1, 2, 3}
    print(d[s])


def syntax_error():
    try:
        eval('x === x')
    except SyntaxError as the_error:
        print(the_error)
        the_error
        raise


def attribute_error():
    d = {'first_name': 'Chris', 'last_name': 'Barker'}
    print(d.lastname)
