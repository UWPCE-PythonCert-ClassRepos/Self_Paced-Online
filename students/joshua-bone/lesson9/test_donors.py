# Joshua Bone - UW Python 210 - Lesson 9
# 02/10/2019
# Assignment: Mailroom, Object Oriented

import pytest
from donor import Donor
from donors import Donors


def test_donor_names():
    donors = Donors()
    d1 = Donor("Mark", 50)
    d2 = Donor("Mary", 80)
    donors.add_donor(d1)
    donors.add_donor(d2)
    assert set(donors.donor_names) == set(["Mark", "Mary"])


def test_get_donor():
    donors = Donors()
    d = Donor("Mark", 50)
    donors.add_donor(d)
    assert donors.get_donor("Mark") == d
    assert donors.get_donor("Mary") is None


def test_add_donation():
    donors = Donors() 
    donors.add_donation("Mark", 10)
    assert donors.get_donor("Mark") == Donor("Mark", 10)
    donors.add_donation("Mark", 20)
    assert donors.get_donor("Mark").donations == (10, 20)
    donors.add_donation("Mary", 30)
    assert donors.get_donor("Mary") == Donor("Mary", 30)
    assert set(donors.donor_names) == set(["Mark", "Mary"]) 
