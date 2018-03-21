#!/usr/bin/env python3

import mailroom as m
import pytest

choices = {  # Dict of command text and functions in the main menu
'1': {'option': 'Send a thank you', 'function': m.send_thank_you},
'2': {'option': 'Create a report', 'function': m.create_a_report},
'3': {'option': 'Send letters to everyone', 'function': m.send_all_letters},
'4': {'option': 'Quit', 'function': m.exit_screen}
}

# Dict of functions to show donor list or quit when sending a thank you
alt_choices = {  
        '': {'function': m.exit_screen},
        'quit': {'function': m.exit_screen},
        'list': {'function': m.print_donor_list}
}


def test_manage_donors_1():
    with pytest.raises(IOError):
        m.manage_donors()

def test_call_menu_function_1():
    assert m.call_menu_function(
            choices, '0', m.respond_to_bad_main_menu_choice) == False

def test_call_menu_function_2():
    with pytest.raises(IOError):
        m.call_menu_function(choices, '1', m.respond_to_bad_main_menu_choice)

def test_call_menu_function_3():
    assert m.call_menu_function(
            choices, '2', m.respond_to_bad_main_menu_choice) == True

def test_call_menu_function_4():
    with pytest.raises(IOError):
        m.call_menu_function(choices, '3', m.respond_to_bad_main_menu_choice)

def test_call_menu_function_5():
    assert m.call_menu_function(
            choices, '4', m.respond_to_bad_main_menu_choice) == True

def test_call_menu_function_6():
    assert m.call_menu_function(
            choices, '5', m.respond_to_bad_main_menu_choice) == False

def test_call_menu_function_7():
    assert m.call_menu_function(
            choices, 'a', m.respond_to_bad_main_menu_choice) == False



def test_respond_to_bad_main_menu_choice():
    assert m.respond_to_bad_main_menu_choice('any') == None


def test_exit_screen_1():
    assert m.exit_screen() == None


def test_send_thank_you():
    with pytest.raises(IOError):
        m.send_thank_you()

def test_call_menu_function_100():
    assert m.call_menu_function(alt_choices, '', m.get_donation_amount) == True

def test_call_menu_function_101():
    assert m.call_menu_function(alt_choices, 'quit', m.get_donation_amount
            ) == True

def test_call_menu_function_102():
    assert m.call_menu_function(alt_choices, 'list', m.get_donation_amount
            ) == True

def test_call_menu_function_103():
    with pytest.raises(IOError):
        m.call_menu_function(alt_choices, 'C. N. Emone', m.get_donation_amount)


def test_get_donation_amount():
    with pytest.raises(IOError):
        m.get_donation_amount('C. N. Enome')
    
def test_call_menu_function_200():
    donation_choices = alt_choices.copy()
    donation_choices.pop('list')
    assert m.call_menu_function(donation_choices, '', m.add_donation,
            donor_name='C. N. Enome') == True
    
def test_call_menu_function_201():
    donation_choices = alt_choices.copy()
    donation_choices.pop('list')
    assert m.call_menu_function(donation_choices, 'quit', m.add_donation,
            donor_name='C. N. Enome') == True
    
def test_call_menu_function_202():
    donation_choices = alt_choices.copy()
    donation_choices.pop('list')
    assert m.call_menu_function(donation_choices, '50.00', m.add_donation,
            donor_name='C. N. Enome') == False
