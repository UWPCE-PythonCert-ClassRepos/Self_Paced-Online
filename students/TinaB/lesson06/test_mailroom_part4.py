#!/usr/bin/env python

import pytest
import mailroom_part4 as mailroom

'''Bringing over dictionaries for testing.!!! Look into a better way to do this!!'''
MAIN_MENU = {
    "1": {'menu_prompt': 'Send a Single Thank You', 'menu_dispatch': mailroom.single_print_menu},
    "2": {'menu_prompt': 'Create a Report', 'menu_dispatch': mailroom.print_report},
    "3": {'menu_prompt': 'Send Letters to Everyone', 'menu_dispatch': mailroom.send_letters_everyone},
    "4": {'menu_prompt': 'Print Letters to Everyone', 'menu_dispatch': mailroom.print_letters_to_everyone},
    "q": {'menu_prompt': 'Quit Program', 'menu_dispatch': mailroom.quit_menu}
}
SINGLE_PRINT_SUB_MENU = {
    "1": {'menu_prompt': 'Lookup Donor By Name', 'menu_dispatch': mailroom.send_single_thank_you},
    "2": {'menu_prompt': 'Print List of donors', 'menu_dispatch': mailroom.print_donors_names},
    "3": {'menu_prompt': 'Print Donors list with donations', 'menu_dispatch': mailroom.print_donors_and_donations},
    "q": {'menu_prompt': 'Quit to Main Menu', 'menu_dispatch': mailroom.quit_menu}}

#---------------Testing expected User Choices for Main Menu----------------
def test_main_menu_inputs_1():
    '''Test 1 entry from menu prompt- requires user promp'''
    with pytest.raises(IOError):
        mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, '1')

def test_main_menu_inputs_2():
    '''Test 2 entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, '2') is True

def test_main_menu_inputs_3():
    '''Test 3 entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, '3') is True

def test_main_menu_inputs_4():
    '''Test 4 entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, '4') is True

def test_main_menu_inputs_q():
    '''Test 'q' entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, 'q') is True

#------Test Bad Expected User Behavior for error handling for main menu-------

def test_main_menu_inputs_0():
    '''Test 0 entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, 0) is False

def test_main_menu_inputs_alph_aupper():
    '''Test capitol letter entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, 'T') is False

def test_main_menu_inputs_alpha_lower():
    '''Test lower case letter (NOT 'q') entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, 't') is False

def test_main_menu_inputs_5():
    '''Testing number not in dictionary entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, '5') is False

def test_main_menu_inputs_enter():
    '''Test '' (enter or other key) entry from menu prompt'''
    assert mailroom.menu_selection(MAIN_MENU, '') is False

#------Testing expected User Choices for Sub Menu - Single Print----------------
def test_single_print_sub_menu_inputs_1():
    '''Test 1 entry from menu prompt- requires user promp'''
    with pytest.raises(IOError):
        mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, '1')

def test_single_print_sub_menu_inputs_2():
    '''Test 2 entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, '2') is True

def test_single_print_sub_menu_inputs_3():
    '''Test 3 entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, '3') is True

def test_single_print_sub_menu_inputs_q():
    '''Test 'q' entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, 'q') is True

#------Test Bad Expected User Behavior for error handling for main menu-------

def test_single_print_sub_menu_inputs_0():
    '''Test 0 entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, 0) is False

def test_single_print_sub_menu_inputs_alphaUpper():
    '''Test capitol letter entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, 'T') is False

def test_single_print_sub_menu_inputs_alphaLower():
    '''Test lower case letter (NOT 'q') entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, 't') is False

def test_single_print_sub_menu_inputs_5():
    '''Testing number not in dictionary entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, '5') is False

def test_single_print_sub_menu_inputs_enter():
    '''Test '' (enter or other key) entry from menu prompt'''
    assert mailroom.menu_selection(SINGLE_PRINT_SUB_MENU, '') is False

def test_quit_menu_function():
    '''tests the return from the quit'''
    assert mailroom.quit_menu() == "exit menu"


def test_single_thank_you_print():
    assert mailroom.print_thank_you(
        "Kevin", 250.50) == "\nDear Kevin,\n \tThank you for your generous donation of $250.50\nSincerely, \nThe ChickTech Donations Department\n"


def test_print_total():
    #"Justin Timberlake": [999658.25, 1233, 123]
    assert mailroom.print_thank_you_total("Justin Timberlake") == '''\n\nDear Justin Timberlake

Thank you for your most recent generous donation of $123.00. You're support of $1,001,014.25
over the years has helped us fund many great programs!We wanted to write you to thank you and that we 
look forward to your continued support!

Sincerely,


The ChickTech Donations Department'''
