#-------------------------------------------------#
# Title: Mail Room Part 4 Unit Testing
# Dev:   LDenney
# Date:  November 7, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 11/7/18, Started MailRoom Part 4
#-------------------------------------------------#

from mailroom_part4 import *

def test_1():
    assert len(sort_by_amount()) >= 5
    assert type(sort_by_amount()) is list

def test_2():
    assert quit() == 'quit'