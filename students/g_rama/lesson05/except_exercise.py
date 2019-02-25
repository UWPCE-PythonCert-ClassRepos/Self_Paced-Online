#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun

first_try = ['spam', 'cheese', 'mr death']
for ft in range(len(first_try)):
    try:
        joke = fun(first_try[ft])
        # if ft == 2:
        #     print(joke)
    except NameError:
        print(f"Whoops! there is no joke for:{first_try[ft]}")

langs = ['java', 'c', 'python']

for lang in range(len(langs)):
    try:
        if lang == 1:
            more_joke = more_fun(langs[lang])
    except IndexError:
        print("This Language is not found")
    finally:
        last_fun()



