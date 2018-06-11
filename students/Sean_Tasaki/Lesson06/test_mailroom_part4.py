#!/usr/bin/env python3
"""
Sean Tasaki
5/27/2018
Lesson06.test_mailroom_part_4
"""
import mailroom_part4 as mailroom 
from mailroom_part4 import donor_dict
from collections import defaultdict
import pytest

@pytest.fixture()
def resource_a():
    s = 'Sean Tasaki'
    return s

def test_add_donor_amount():
    # test for new donor with donor amount
    mailroom.add_donor_amount('Sean', 5)
    # test for a donor already in donor_dict with donor amount
    mailroom.add_donor_amount('Bob Dylan', .01)
    assert mailroom.donor_dict.get('Sean') == [5.00, 1, 5.00]
    assert mailroom.donor_dict.get('Bob Dylan') == [20000.01, 4, 5000.0025]

def test_thank_you_letter_template(resource_a):
    # test a letter to a new donor
    mailroom.donor_dict[resource_a]= [5.00, 1, 5.00]
    mailroom.thank_you_letter_template(resource_a)

    # test a letter to a donor already in the donor_dict
    mailroom.thank_you_letter_template('Bob Dylan')
    assert "Dear Sean Tasaki,\nThank you for your {} generous donation of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format('Sean Tasaki', donor_dict['Sean Tasaki'][1], donor_dict['Sean Tasaki'][0])
    assert "Dear {},\nThank you for your {} generous donations of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format('Bob Dylan', donor_dict['Bob Dylan'][1], donor_dict['Bob Dylan'][0])


