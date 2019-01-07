#!/usr/bin/env python3.7
# test_mailroom4.py
# Coded by LouReis


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
from mailroom4 import main_menu, donation_report, thanks_letter
from mailroom4 import thanks_letter_all, print_letter, quit
from mailroom4 import main_prompt, menu_options_dict, donations

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
#def test_7():
#    assert print_letter('test name', x) is not True

# Test that the user can still prompt for an existing donor list.
def test_8():
    assert print_letter('L', 5) is not False

# Test that adding an existing donor still works.
def test_9():
    assert print_letter('Howie Long', 1000) is not False

# Test that the quit function still terminates gracefully.
#def test_10():
#    assert quit() is True
