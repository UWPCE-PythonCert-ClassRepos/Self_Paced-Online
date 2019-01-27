#!/usr/bin/python 3

from except_test import fun, more_fun, last_fun

def main():
    first_try = ['spam', 'cheese', 'mr death']

    # Exception handles NameError by printing string.
    try:
        joke = fun(first_try[0])
    except NameError:
        print("Whoops!  There is no joke for: " + first_try[0])

    # prints opening dialogue between customer and shopkeeper (lines 1-2)
    joke = print(fun(first_try[2]))

    langs = ['java', 'c', 'python']

    # prints conclusion question (line 3)
    try:
        more_joke = more_fun(langs[0])
    except IndexError:
        more_joke = more_fun(langs[1])

    # prints the two lines of the joke (lines 4-5)
    last_joke = last_fun() 

main()