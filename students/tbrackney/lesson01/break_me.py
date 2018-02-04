"""
File Name: break_me.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 2/3/2018
Python Version: 3.6.4
"""


def name_error():
    # returns an uninitialized name
    return(b)


def type_error():
    # attempts to divide a string by an integer.
    a = "string"
    b = a / 5
    return b


def syntax_error():
    # mimics bad syntax for equality operator.
    if a = b:
        return "True"


def assertion_error():
    # Asserts a false statement.
    assert 0 == 1
