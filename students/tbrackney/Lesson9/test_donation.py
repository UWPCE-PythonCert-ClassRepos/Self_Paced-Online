#!/usr/bin/env python3
"""
File Name: test_donation.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/16/2018
Python Version: 3.6.4
"""
from donation_tracker import Donor, Donorlist
import pytest

init_donors = ['Tom Selleck', 'Burt Reynolds', 'Nick Offerman', 'Sam Elliot', 'John Waters']
init_donations = [[2000.00, 1500.00, 500.00], [45.00], [1000.00, 1000.00], [1200.00, 550.00], [20.00, 20.00, 20.00]]
init_dict = dict(zip(init_donors, init_donations))


def test_donor_init():
    d = Donor('Tom', [13, 17])
    assert d.name == 'Tom'
    assert d.donations == [13, 17]


def test_init_one_value():
    d = Donor('Tim')
    assert d.name == 'Tim'
    assert d.donations == []


def test_add_donation():
    d = Donor('Tom', [13, 17])
    d.add_donation(15)
    assert d.donations == [13, 17, 15]
    with pytest.raises(TypeError):
        d.add_donation('words')
    with pytest.raises(ValueError):
        d.add_donation(-12)


def test_total():
    d = Donor('Tom', [13, 17])
    assert d.total == 30.0


def test_donation_count():
    d = Donor('Tom', [1, 2, 3, 4, 5])
    assert d.count == 5


def test_avg_donation():
    d = Donor('Tom', [13, 17])
    assert d.average == 15


def test_donation_list_init():
    dl = Donorlist(**init_dict)
    for d in init_donors:
        assert d in dl._donors.keys()


def test_get_donor():
    dl = Donorlist(**init_dict)
    d = dl.get_donor('Tom Selleck')
    assert isinstance(d, Donor)
