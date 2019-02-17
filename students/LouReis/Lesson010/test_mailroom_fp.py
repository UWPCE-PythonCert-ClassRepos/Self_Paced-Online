#!/usr/bin/env python3.7
# test_mailroom_fp.py
# Coded by LouReis
# Lesson010
# Functional Programming Assignment Lesson10

"""
This program is to test the following program, mailroom4.py:

Write a small command-line script called mailroom4.py.
It should have a data structure that holds a list of your donors and a history
of the amounts they have donated. This structure should be populated at first
with at least five donors, with between 1 and 3 donations each.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”)

Report should look like the following:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Joe Donor                  $  653784.49           2  $   326892.24
John Rich                  $   16396.10           3  $     5465.37
Sally Neighbor             $     877.33           1  $      877.33
Mack Jack                  $     708.42           3  $      236.14

"""

"""

Here are the functions as defined in mailroom4.py:

main_menu(main_prompt,menu_options_dict)
donation_report()
thanks_letter()
thanks_letter_all()
print_letter(donor, amount)
quit()

"""

# referencing all of the functions, names, variables, symbols to import
from mailroom_fp import main_menu, donation_report, thanks_letter
from mailroom_fp import enter_existing_donor, enter_new_donor, challenge
from mailroom_fp import thanks_letter_all, print_letter, quit
from mailroom_fp import main_prompt, menu_options_dict, donations, philanthropy

from io import StringIO
import sys

# GOAL is to test all code not involving "user interaction".
# Functions that contain user interaction have been commented out below.

# Test that the main menu works fine with the default values as assigned.
#def test_1():
#    assert main_menu(main_prompt,menu_options_dict) is not False

# Test that the donation report works fine as default.
def test_2():
    assert donation_report() is not False

# Test that the thanks letter still works as default.
#def test_3():
#    assert thanks_letter() is not False

# Test that this function still works and text files are generated for all.
def test_4():
    assert thanks_letter_all() is not False

# Test that a new donor with a valid donation still works.
def test_5():
    assert print_letter('test name', 5) is not False

# Test that the lower bound donation amount & name still works.
def test_6():
    assert print_letter('', 0) is not False

# Test that a non-numeric value for donation amount is not accepted.
def test_7():
    a = {"Robin Hood": [50000, 50000, 50000], "Tycoon Reis": [25000000, 25000000, 25000000], "Howie Long": [100000], "Joe Neighbor": [25, 25], "Rick Retiree": [0.50, 0.50]}
    assert a == donations

# Test that the user can still prompt for an existing donor list.
def test_8():
    assert print_letter('L', 5) is not False

# Test that adding an existing donor still works.
def test_9():
    assert print_letter('Howie Long', 1000) is not False

# Test that the quit function still terminates gracefully.
#def test_10():
#    assert quit() is True

# Test that a new donor gets added to the dict
def test_11():
    enter_new_donor('test', 10)
    assert 'test' in donations

# Test that another new donor gets added to the dict
def test_12():
    enter_new_donor('other test', .01)
    assert 'other test' in donations

# Test that the output from print_letter is valid.
def test_13():
    # Using StringIO from io...
    # Store the reference, in case you want to show things again in standard output
    old_stdout = sys.stdout
    # This variable will store everything that is sent to the standard output
    result = StringIO()
    sys.stdout = result
    # Here we can call anything we like, like external modules, and everything that they will send to standard output will be stored on "result"
    print_letter('Howie Long', 1000)
    # Redirect again the std output to screen
    sys.stdout = old_stdout
    # Then, get the stdout like a string and process it!
    result_string = result.getvalue()
    assert "Subject: Donation" in result_string
    assert "Dear Howie Long," in result_string
    assert "Thank you for your $1,000.00 donation, it will be used to help meet our goals." in result_string
    assert "We will welcome any future donations and appreciate your support." in result_string
    assert "Sincerely," in result_string
    assert "MDTS Staff" in result_string

# Test that the new challenge function returns proper results based on the donations & parameters
def test_14():
    sample1 = challenge(2,1,100)
    assert sample1 == {'Joe Neighbor': [50, 50], 'test': [20]}

# Test that teh new challenge function returns proper results with larger parameters
def test_15():
    sample2 = challenge(10,1000000,10000000000000)
    print(sample2)
    assert sample2 == philanthropy
