# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:01:16 2018

@author: Karl M. Snyder
"""

"""Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

# import definition
from not_string import not_string

def test_1():
    assert not_string("This is not candy") == "not This is not candy"

def test_2():
    assert not_string("not does not need 'not' prepended") == \
    "not does not need 'not' prepended"
    
def test_3():
    assert not_string("Does not get prepended?") == \
    "not Does not get prepended?"
    
def test_4():
    assert not_string("not handy candy") == "not handy candy"