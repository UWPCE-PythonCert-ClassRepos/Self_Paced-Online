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

def test_calc_donor_stats_7():
    assert m.calc_donor_stats('Who Me') == None


def test_send_all_letters():
    with pytest.raises(IOError):
        m.send_all_letters()


def test_create_form_letter_1():
    assert m.create_form_letter('Daffy Doo', 1000) == None

def test_create_form_letter_2():
    assert m.create_form_letter('Papa Smurf', -60) == None

def test_create_form_letter_3():
    assert m.create_form_letter('Papa Smurf', 0) == None

def test_create_form_letter_3():
    # Form letter should not be produced if the specified donor amount
    # is not in the donor name's history
    assert m.create_form_letter('Papa Smurf', 75.86) == None

def test_create_form_letter_4():
    result = m.create_form_letter('Papa Smurf', 1000)
    assert isinstance(result, str) == True and len(result) > 500