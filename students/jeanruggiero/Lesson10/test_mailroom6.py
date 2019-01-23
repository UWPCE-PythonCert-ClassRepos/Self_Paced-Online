#!/usr/bin/env python

"""This module contains test functions for the mailroom4 assignment."""

import pytest
import datetime
import mailroom6
from mailroom6 import DonorDict
from mailroom6 import Donor

don = Donor('Name Zero',[50, 1])
donors = DonorDict()
donors.add_donor('name one', [1,2])
donors.add_donor('name two', [3,4,5])
donors.add_donor('name three', [6])
donors2 = DonorDict([Donor('name one', [1,2]), Donor('name two', [3,4,5])])


# Donor class tests
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

# DonorDict class tests
def test_dd_init():
    dd = DonorDict([don])
    assert list(dd.donors.values()) == [don]

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

def test_sub():
    assert donors - donors2 == 0

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

def test_total_donations():
    assert donors.total_donations == 15

def test_add_donor():
    global donors
    donors.add_donor('name four')
    assert donors['name four'] == Donor('name four', [])

def test_add_donation():
    global donors
    donors.add_donation('name four', 77)
    assert donors['name four'] == Donor('name four', [77])

# Test FP sub-functions
def test_thank_donor():
    assert mailroom6.thank_donor(donors, 'name four', 77) == \
        mailroom6.thank(Donor('name four', [77]), 77)

def test_thank():
    assert mailroom6.thank(don, 6) == "Dear Name Zero,\n\n" + \
            "Thank you so much for your generous donation of " + \
            "$6.00.\n\nWe really appreciate your donations " + \
            "totalling $51.00.\n" + \
            f"You are ${1000000000-51:.2f} away from a" + \
            " gift of Spaceballs: The Flamethrower!\n\n" + \
            "Sincerely, The Wookie Foundation"

def test_filename():
    d = datetime.date.today()
    assert mailroom6.filename(don) == '_'.join(['Name_Zero', str(d.month),
            str(d.day), str(d.year)])+'.txt'

def test_challenge():
    assert mailroom6.challenge(donors, 2) == \
        DonorDict([
            Donor('name one', [2,4]),
            Donor('name two', [6,8,10]),
            Donor('name four', [154])
            ])
    assert mailroom6.challenge(donors, 2, min_donation=4) == \
        DonorDict([
            Donor('name one', [1,2]),
            Donor('name two', [3,8,10]),
            Donor('name four', [154])
            ])
    assert mailroom6.challenge(donors, 3, max_donation=2) == \
        DonorDict([
            Donor('name one', [3,6]),
            Donor('name two', [3,4,5]),
            Donor('name four', [77])
            ])
    assert mailroom6.challenge(donors, 4, min_donation=2, max_donation=5) == \
        DonorDict([
            Donor('name one', [1,8]),
            Donor('name two', [12,16,20]),
            Donor('name four', [77])
            ])
