# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:00:17 2018

@author: Karl M. Snyder
"""

"""Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
    if str[0:3] == "not":
        return str
    else:
        return "not " + str
