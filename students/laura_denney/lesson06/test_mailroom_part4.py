#-------------------------------------------------#
# Title: Mail Room Part 4 Unit Testing
# Dev:   LDenney
# Date:  November 7, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 11/7/18, Started MailRoom Part 4
#   Laura Denney, 11/12/18, Completed work on MailRoom Part 4
#-------------------------------------------------#

from mailroom_part4 import *

#tests sort_by_amount
def test_1():
    assert len(sort_by_amount()) >= 5
    assert type(sort_by_amount()) is list

#tests the quit function
def test_2():
    assert quit() == 'quit'

def test_3():
    assert get_list() == '\nWe have 5 current donors: John Doe, Laura Denney, Bill Gates, Samuel Jackson, Mr. Bean'

#tests the validation of donation amounts
def test_4():
    assert validate_donation(400) == 400.0

def test_4_5():
    assert validate_donation('four hundred') == 0.0

#tests the function to create a string for report
def test_7():
    assert create_string_report() == '\nDonor Name                | Total Given | Num Gifts | Average Gift\n---------------------------------------------------\
---------------'

def test_7_5():
    assert create_string_report(sort_by_amount()) > create_string_report()


#tests checking if entered donor is current donor or not
def test_5():
    assert check_current_donor("laura denney", 5.0) == '\nLaura Denney is a current donor, we will update their donations.'

def test_6():
    assert check_current_donor("chuck norris", 500.00) == '\nChuck Norris is not a current donor, we will add them to our system.'



#tests whether to print to screen or save in txt file
def test_8():
    assert send_email('Laura Denney', 500) == '\n    Dear Laura Denney,\n\n    We would like to thank you for your generous donation\n    of $500.00\
. It will be put to great use!\n\n    Thank you!\n    <3 The MailRoom\n    '

def test_9():
    assert send_email('Laura Denney', 500, "home.txt") == 1
