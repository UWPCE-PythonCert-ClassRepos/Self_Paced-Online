#!/usr/bin/python
# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Exception Exercise - Lesson 05
# PURPOSE: Working with Exception Handling
# DATE: 06/23/2018
#
# DESCRIPTION: Inserting Try/Except blocks to allow except_exercise.py to run using functions from
#  except_test.py
# ----------------------------------------------------------------------------------------------------------------------
"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""
# Figure out what the exception is: Line 15 - joke = fun(first_try[0])
# catch it and while still in that catch block, try again with the
# second item in the list.
# What did that do? : Resolved line 15 error 'Spam' was accepted
# You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

from except_test import fun, more_fun, last_fun       # import functions from except_test.py file

first_try = ['spam', 'cheese', 'mr death']            # list values
try:                                                  # attempt this, on error, go to except block
    joke = fun(first_try[0])                          # first value

except Exception as e:
    print('Whoops! There is no joke for: {}'.format(first_try[0]))

# Here is a try/except block. Add an else that prints not_joke
try:                                                    # check last element of first_try list
    not_joke = fun(first_try[2])

except Exception as e:
    print('Run Away!', e)

else:
    print(not_joke)                                    # if not error, print result

# Figure out what the exception is, catch it and in that same block
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
# If there are no exceptions, call the more_fun function with the last
# language in the list
# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']                   # new list
try:
    # more_joke = more_fun(langs[0])              # test list val 1, index out of range
    more_joke = more_fun(langs[1])                # test list val 2

except IndexError as e:
    pass

else:
    more_joke = more_fun(langs[2])                # test list val 3

finally:
    end_me = last_fun()
