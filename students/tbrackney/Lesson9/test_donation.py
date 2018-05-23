#!/usr/bin/env python3
"""
File Name: test_donation.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/16/2018
Python Version: 3.6.4
"""
from donation_tracker import Donor, Donorlist
from io import StringIO
import pytest

init_donors = ['Tom Selleck', 'Burt Reynolds', 'Nick Offerman', 'Sam Elliot', 'John Waters']
init_donations = [[2000.00, 1500.00, 500.00], [45.00], [1000.00, 1000.00], [1200.00, 550.00], [20.00, 20.00, 20.00]]
init_tuple = tuple(zip(init_donors, init_donations))


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
    dl = Donorlist(init_tuple)
    for d in init_donors:
        assert d in dl._donor_objects.keys()
    for v in dl._donor_objects.values():
        assert isinstance(v, Donor)


def test_get_donor():
    dl = Donorlist(init_tuple)
    d = dl.get_donor('Tom Selleck')
    assert isinstance(d, Donor)
    assert d.name == 'Tom Selleck'
    assert d.donations == [2000.00, 1500.00, 500.00]


def test_list_donors():
        dl = Donorlist(init_tuple)
        assert type(dl.list_donors()) == list
        assert dl.list_donors() == ['Burt Reynolds', 'John Waters', 'Nick Offerman', 'Sam Elliot', 'Tom Selleck']


def test_add_donor():
    dl = Donorlist(init_tuple)
    dl.add_donor('Gene Shallit')
    assert 'Gene Shallit' in dl.list_donors()
    assert isinstance(dl.get_donor('Gene Shallit'), Donor)
    assert dl.list_donations('Gene Shallit') == []
    with pytest.raises(ValueError):
        dl.add_donor('Tom Selleck')


def test_contains():
    dl = Donorlist(init_tuple)
    assert 'Tom Selleck' in dl
    assert 'Freddie Mercury' not in dl


def test_list_donation():
    dl = Donorlist(init_tuple)
    assert dl.list_donations('John Waters') == [20.0, 20.0, 20.0]
    with pytest.raises(ValueError):
        dl.list_donations('Freddie Mercury')


def test_add_donation():
    dl = Donorlist(init_tuple)
    dl.add_donation('Nick Offerman', 250)
    dl.add_donation('Nick Offerman', 55)
    assert 250 in dl.list_donations('Nick Offerman')
    assert 55 in dl.list_donations('Nick Offerman')
    with pytest.raises(KeyError):
        dl.add_donation('Nobody', 20)


def test_thankyou():
    dl = Donorlist(init_tuple)
    email = 'Dear Test User, thank you for your generous donation of $77.77\n'
    assert dl.send_thankyou('Test User', 77.77) == email


def test_thankyou2():
    email = ('Dear Test User,\n'
             '\n'
             '        Thank you for your kind donations totaling $77.77\n'
             '\n'
             '        Your gifts will be put to very good use.\n\n'
             '                            Sincerely\n'
             '                                -The Team\n'
             )

    dl = Donorlist(init_tuple)
    assert dl.send_thankyou('Test User', 77.77, template='long') == email


def test_report():
    dl = Donorlist(init_tuple)
    report = ('Donor Name          | Total Given |  Num Gifts | Average Gift\n'
              'Tom Selleck          $    4000.00          3     $    1333.33\n'
              'Nick Offerman        $    2000.00          2     $    1000.00\n'
              'Sam Elliot           $    1750.00          2     $     875.00\n'
              'John Waters          $      60.00          3     $      20.00\n'
              'Burt Reynolds        $      45.00          1     $      45.00\n'
              )
    out = StringIO()
    dl.create_report(out)
    assert report == out.getvalue()


def test_get_total():
    dl = Donorlist(init_tuple)
    assert dl.get_total('Tom Selleck') == 4000.0
    with pytest.raises(KeyError):
        dl.get_total('Fake Name')
