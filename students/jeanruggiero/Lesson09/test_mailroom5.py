#!/usr/bin/env python

"""This module contains test functions for the mailroom4 assignment."""

import pytest
import datetime
import mailroom5
from mailroom5 import DonorDict
from mailroom5 import Donor

don = Donor('Name Zero',[50, 1])
donors = DonorDict()
donors.add_donor('name one', [1,2])
donors.add_donor('name two', [3,4,5])
donors.add_donor('name three', [6])

def test_init():
    assert don.name == 'Name Zero'
    assert don.donations == [50, 1]

def test_repr():
    assert don.__repr__() == 'Donor(Name Zero, [50, 1])'

def test_str():
    assert don.__str__() == 'Donor(Name: Name Zero, Donations: [50, 1])'

def test_eq():
    assert don == Donor('Name Zero',[50, 1])

def test_name():
    assert don.name == 'Name Zero'

def test_donations():
    assert don.donations == [50, 1]

def test_count_conations():
    assert don.count_donations == 2

def test_total_donations():
    assert don.total_donations == 51

def test_average_donation():
    assert don.average_donation == (50 + 1)/2

def test_add_donation():
    global don
    don.add_donation(6)
    assert don.donations == [50, 1, 6]

def test_thank():
    assert don.thank(6) == "Dear Name Zero,\n\n" + \
            "Thank you so much for your generous donation of " + \
            "$6.00.\n\nWe really appreciate your donations " + \
            "totalling $51.00.\n" + \
            f"You are ${1000000000-51:.2f} away from a" + \
            " gift of Spaceballs: The Flamethrower!\n\n" + \
            "Sincerely, The Wookie Foundation"

def test_filename():
    d = datetime.date.today()
    assert don.filename == '_'.join(['Name_Zero', str(d.month),
            str(d.day), str(d.year)])+'.txt'

def test_dd_str():
    assert donors.__str__() == "{'name one': Donor(Name One, [1, 2]), 'name two': Donor(Name Two, [3, 4, 5]), 'name three': Donor(Name Three, [6])}"

def test_dd_len():
    assert len(donors) == 3

def test_getitem():
    assert donors['name one'] == Donor('name one', [1,2])

def test_delitem():
    del donors['name three']
    assert 'name three' not in donors

def test_iter():
    assert list(iter(donors)) == [Donor('name one', [1,2]),
        Donor('name two', [3,4,5])]

def test_contains():
    assert 'name one' in donors
    assert 'blah' not in donors

def test_names_by_donations():
    assert donors.names_by_donations() == [Donor('name two', [3,4,5]),
        Donor('name one', [1,2])]

def test_sort_key():
    assert donors.sort_key(Donor('name', [7,8])) == 15

def test_donors():
    assert donors.donors == {'name one': Donor('name one', [1,2]),
        'name two': Donor('name two', [3,4,5])}

def test_names():
    assert donors.names == ['Name One', 'Name Two']

def test_add_donor():
    global donors
    donors.add_donor('name four')
    assert donors['name four'] == Donor('name four', [])

def test_add_donation():
    global donors
    donors.add_donation('name four', 77)
    assert donors['name four'] == Donor('name four', [77])

def test_thank_donor():
    assert donors.thank_donor('name four',77) == \
        Donor('name four', [77]).thank(77)
