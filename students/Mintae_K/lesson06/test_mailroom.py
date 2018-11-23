from mailroom4 import *
import os.path

donors = {'William Gates, III': [54842.49, 48965.25],
            'Mark Zuckerberg': [7852.25, 48652.0, 3548.0],
            'Jeff Bezos': [5486.0, 58794.02, 7412.1],
            'Paul Allen': [46872.02]}


def test_check_name_exist():
    (yes_exist, s) = check_name_exist('Starbucks Coffee', donors)
    assert 0 is yes_exist


def test_check_error():
    x = check_error('not_a_number')
    assert x is 0


def test_append_donation():
    answer = append_donation('Paul Allen', 9999.0, 1, donors)
    assert answer['Paul Allen'][1] is 9999.0
