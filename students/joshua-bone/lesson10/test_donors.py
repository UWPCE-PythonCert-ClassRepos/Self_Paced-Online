# Joshua Bone - UW Python 210 - Lesson 10
# 03/08/2019
# Assignment: Functional Mailroom

import pytest
from donor import Donor
from donors import Donors


def test_donor_names():
    donors = Donors()
    d1 = Donor("Mark", 50)
    d2 = Donor("Mary", 80)
    donors.add_donor(d1)
    donors.add_donor(d2)
    assert set(donors.names) == set(["Mark", "Mary"])


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
    assert set(donors.names) == set(["Mark", "Mary"])


def test_challenge():
    donors = Donors()
    d1 = Donor("Mark", 50)
    d1.add_donation(90)
    d1.add_donation(110)
    d2 = Donor("Mary", 80)
    d2.add_donation(95)
    d2.add_donation(115)
    donors.add_donor(d1)
    donors.add_donor(d2)
    copy = donors.challenge(3, min_amt=85, max_amt=100)
    assert copy.get_donor("Mark").donations == (270,)
    assert copy.get_donor("Mary").donations == (285,)
