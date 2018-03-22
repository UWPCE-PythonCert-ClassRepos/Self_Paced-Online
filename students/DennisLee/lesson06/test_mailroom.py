#!/usr/bin/env python3

import os
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
    # An I/O error occurs because the function prompts for menu choice
    with pytest.raises(IOError):
        m.manage_donors()

# Simulate and test function calls that occur in the code 
# after the input() function that causes the I/O error
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

def test_call_menu_function_8():
    assert m.call_menu_function(
            choices, '', m.respond_to_bad_main_menu_choice) == False



def test_respond_to_bad_main_menu_choice():
    assert m.respond_to_bad_main_menu_choice('any') == None


def test_exit_screen_1():
    assert m.exit_screen() == None


def test_send_thank_you():
    # An I/O error occurs because the function prompts for donor name,
    # donor list display, or quitting
    with pytest.raises(IOError):
        m.send_thank_you()

# Simulate and test function calls that occur in the code 
# after the input() function that causes the I/O error
def test_call_menu_function_100():
    assert m.call_menu_function(alt_choices, '', m.get_donation_amount) == True

def test_call_menu_function_101():
    assert m.call_menu_function(alt_choices, 'quit', m.get_donation_amount
            ) == True

def test_call_menu_function_102():
    assert m.call_menu_function(alt_choices, 'list', m.get_donation_amount
            ) == True

def test_call_menu_function_103():
    # An I/O error occurs because the function prompts for donation amt
    with pytest.raises(IOError):
        m.call_menu_function(alt_choices, 'C. N. Emone', m.get_donation_amount)

def test_call_menu_function_104():
    # An I/O error occurs because the function prompts for donation amt
    with pytest.raises(IOError):
        m.call_menu_function(alt_choices, 'Papa Smurf', m.get_donation_amount)


def test_get_donation_amount():
    # An I/O error occurs because the function prompts for a donation
    # amount or to quit
    with pytest.raises(IOError):
        m.get_donation_amount('C. N. Enome')
    
# Simulate and test function calls that occur in the code 
# after the input() function that causes the I/O error
def test_call_menu_function_200():
    # re-use the donor name dict, except without the 'list' function
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
    assert m.call_menu_function(donation_choices, '50', m.add_donation,
            donor_name='C. N. Enome') == False
    del m.donor_history['C. N. Enome']  # restore dict for next tests

def test_call_menu_function_203():
    donation_choices = alt_choices.copy()
    donation_choices.pop('list')
    assert m.call_menu_function(donation_choices, '0.00', m.add_donation,
            donor_name='C. N. Enome') == False
    
def test_call_menu_function_204():
    donation_choices = alt_choices.copy()
    donation_choices.pop('list')
    assert m.call_menu_function(donation_choices, '-100.0045', m.add_donation,
            donor_name='C. N. Enome') == False
    
def test_call_menu_function_205():
    donation_choices = alt_choices.copy()
    donation_choices.pop('list')
    assert m.call_menu_function(donation_choices, 'fdasfd', m.add_donation,
            donor_name='C. N. Enome') == False


def test_add_donation_1():
    assert m.add_donation(50, 'C. N. Enome') == 50
    del m.donor_history['C. N. Enome']  # restore dict for next tests

# Non-numeric, zero, or negative donation amounts are not allowed   
def test_add_donation_2():
    assert m.add_donation(0, 'C. N. Enome') == None

def test_add_donation_3():
    assert m.add_donation(-100.0045, 'C. N. Enome') == None

def test_add_donation_4():
    assert m.add_donation('dfjasljdfa', 'C. N. Enome') == None

def test_add_donation_5():
    assert m.add_donation(50, 'Papa Smurf') == 50
    m.donor_history['Papa Smurf'].pop()  # restore dict for next tests

def test_add_donation_6():
    assert m.add_donation(0, 'Papa Smurf') == None

def test_add_donation_7():
    assert m.add_donation(-100.0045, 'Papa Smurf') == None

def test_add_donation_8():
    assert m.add_donation('dfjasljdfa', 'Papa Smurf') == None

def test_add_donation_9():
    m.add_donation(50, 'C. N. Enome')
    assert 'C. N. Enome' in m.donor_history
    del m.donor_history['C. N. Enome']  # restore dict for next tests

# Since non-numeric, zero, or negative donation amounts are not allowed,
# the new donor is not added to the donor history dict
def test_add_donation_10():
    m.add_donation(0, 'C. N. Enome')
    assert 'C. N. Enome' not in m.donor_history

def test_add_donation_11():
    m.add_donation(-100.0045, 'C. N. Enome')
    assert 'C. N. Enome' not in m.donor_history

def test_add_donation_12():
    m.add_donation('dfjasljdfa', 'C. N. Enome')
    assert 'C. N. Enome' not in m.donor_history

def test_add_donation_13():
    m.add_donation(50, 'C. N. Enome')
    assert m.donor_history['C. N. Enome'] == [50]
    del m.donor_history['C. N. Enome']  # restore dict for next tests

def test_add_donation_14():
    m.add_donation(50, 'Papa Smurf')
    assert m.donor_history['Papa Smurf'] == [210.64, 1000, 50]
    m.donor_history['Papa Smurf'].pop()  # restore dict for next tests

def test_add_donation_15():
    m.add_donation(0, 'Papa Smurf')
    assert m.donor_history['Papa Smurf'] == [210.64, 1000]

def test_add_donation_16():
    m.add_donation(-100.0045, 'Papa Smurf')
    assert m.donor_history['Papa Smurf'] == [210.64, 1000]

def test_add_donation_17():
    m.add_donation('dfjasljdfa', 'Papa Smurf')
    assert m.donor_history['Papa Smurf'] == [210.64, 1000]


def test_print_donor_list_1():
    assert m.print_donor_list() == None


def test_create_a_report_1():
    assert m.create_a_report() == None


def test_calc_donor_stats_1():
    assert m.calc_donor_stats('Red Herring') == {
            'name': 'Red Herring',
            'donations': 111946.87, 
            'gifts': 3, 
            'average': 37315.62}

def test_calc_donor_stats_2():
    assert m.calc_donor_stats('Papa Smurf') == {
            'name': 'Papa Smurf',
            'donations': 1210.64, 
            'gifts': 2, 
            'average': 605.32}

def test_calc_donor_stats_3():
    assert m.calc_donor_stats('Pat Panda') == {
            'name': 'Pat Panda',
            'donations': 55324.40, 
            'gifts': 1, 
            'average': 55324.40}

def test_calc_donor_stats_4():
    assert m.calc_donor_stats('Karl-Heinz Berthold') == {
            'name': 'Karl-Heinz Berthold',
            'donations': 14124.51, 
            'gifts': 2, 
            'average': 7062.26}

def test_calc_donor_stats_5():
    assert m.calc_donor_stats('Mama Murphy') == {
            'name': 'Mama Murphy',
            'donations': 176871.62, 
            'gifts': 3, 
            'average': 58957.21}

def test_calc_donor_stats_6():
    assert m.calc_donor_stats('Daphne Dastardly') == {
            'name': 'Daphne Dastardly',
            'donations': 82.00, 
            'gifts': 1, 
            'average': 82.00}

# Nothing is returned from calc fn if an invalid donor is specified
def test_calc_donor_stats_7():
    assert m.calc_donor_stats('Who Me') == None


def test_send_all_letters_1():
    # An I/O error occurs because the function prompts for menu choice
    with pytest.raises(IOError):
        m.send_all_letters()


def save_letters_helper(folder):
    donor_and_last_donation = {
                'Red Herring': 15000,
                'Papa Smurf': 1000,
                'Pat Panda': 55324.4,
                'Karl-Heinz Berthold': 10579.31,
                'Mama Murphy': 12054.33,
                'Daphne Dastardly': 82
            }
    dir_name = m.save_letters(folder)
    assert os.path.isdir(dir_name)
    for donor, gift in donor_and_last_donation.items():
        full_name = os.path.join(dir_name, f'_{donor}.txt')
        assert os.path.isfile(full_name) == True
        with open(full_name, 'r') as f:
            file_content = f.read()
            form_letter = m.create_form_letter(donor, gift)
            assert file_content.splitlines() == form_letter.splitlines() 
            assert len(form_letter) > 500
        os.remove(full_name)

def test_save_letters_1():  # User specifies no directory
    save_letters_helper('')

def test_save_letters_2():  # User tries to save to an illegal directory
    save_letters_helper('u:\\')

def test_save_letters_3():  # User saves to a new dir, relative path
    i = 0
    while os.path.isdir('test' + str(i)) == True:
        i += 1
    folder = 'test' + str(i)
    save_letters_helper(folder)
    os.rmdir(folder)

def test_save_letters_4():  # User saves to a preexisting relative dir
    os.mkdir('PreexistingFolder')
    save_letters_helper('PreexistingFolder')

def test_save_letters_5():  # User saves to a new dir, absolute path
    i = 0
    while os.path.isdir(os.path.join(os.path.expanduser('~'), 'test' + str(i))
            ) == True:
        i += 1
    folder = os.path.join(os.path.expanduser('~'), 'test' + str(i))
    os.mkdir(folder)
    save_letters_helper(folder)
    os.rmdir(folder)

def test_save_letters_6():  # User saves to a preexisting absolute dir
    save_letters_helper(os.path.expanduser('~'))


def test_create_form_letter_1():
    assert m.create_form_letter('Daffy Doo', 1000) == None

def test_create_form_letter_2():
    assert m.create_form_letter('Papa Smurf', -60) == None

def test_create_form_letter_3():
    assert m.create_form_letter('Papa Smurf', 0) == None

def test_create_form_letter_4():
    # Form letter should not be produced if the specified donor amount
    # is not in the donor name's history
    assert m.create_form_letter('Papa Smurf', 75.86) == None

def test_create_form_letter_5():
    # Check that form letter is not be produced if the specified donor
    # amount is in the donor history dict but not for this donor
    assert m.create_form_letter('Papa Smurf', 10579.31) == None

def test_create_form_letter_6():
    result = m.create_form_letter('Papa Smurf', 1000)
    assert isinstance(result, str) == True and len(result) > 500