#!/usr/bin/env python3

import pytest
import os
import Mailroom4 as m


test_donors = {
    'William Gates, III': [261514, 392270],
    'Mark Zuckerberg': [4918, 9837, 1639],
    'Jeff Bezos': [877],
    'Paul Allen': [354, 212, 141]
    }


def test_add_donation():
    m.add_donation('Pete John', 100, test_donors)
    assert 'Pete John' in test_donors
    assert test_donors['Pete John'][-1] == 100


def test_donor_list():
    donors = m.donor_list(test_donors)
    assert donors.startswith('William Gates, III')
    assert donors.endswith('Pete John\n')


def test_avg_donations():
    test_donations = ['Pete John', [100, 200]]
    assert m.avg_donations(test_donations) == 150


def test_sum_donations():
    test_donations = ['Pete John', [100, 200]]
    assert m.sum_donations(test_donations) == 300
    

def test_gen_letter():
    test = ('Pete John', 100)
    assert m.gen_letter(*test) == 'Dear Pete John,\n\nThank you for your donation of $100.00.\n\nBest regards,\nThe Organization'
    assert 'Pete John' in m.gen_letter(*test)
    assert '$100.00' in m.gen_letter(*test)


def test_filename():
    assert m.filename('Pete John') == 'Pete John.txt'


def test_write_letters_on_disk():
    m.write_letters_on_disk(test_donors)
    assert os.path.isfile('Pete John.txt')
    with open('Pete John.txt') as f:
        size = len(f.read())
    assert size > 0
