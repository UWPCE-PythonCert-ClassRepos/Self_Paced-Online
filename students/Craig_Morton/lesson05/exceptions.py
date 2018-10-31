# ------------------------------------------------- #
# Title: Lesson 5, pt 1/2, Exceptions
# Dev:   Craig Morton
# Date:  8/28/2018
# Change Log: CraigM, 8/28/2018, Exceptions
# ------------------------------------------------- #

# !/usr/bin/env python

from except_test import fun, more_fun, last_fun

first_try = ['spam', 'cheese', 'mr death']
langs = ['java', 'c', 'python']

try:
    joke = fun(first_try[0])
except NameError:
    joke = fun(first_try[1])

try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)

try:
    more_joke = more_fun(langs[0])
except IndexError:
    next_joke = more_fun(langs[1])
else:
    more_fun(langs[2])
finally:
    last_fun()
