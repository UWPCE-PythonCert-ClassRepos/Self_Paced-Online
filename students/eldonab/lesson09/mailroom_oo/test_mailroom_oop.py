#!/usr/bin/python

import pytest
from mailroom_oop import *

def test_donor():
    Bill = Donor('Bill Gates', [300])
    assert Bill.name == 'Bill Gates'
    Bill.add_donation(400)
    assert Bill.donations == [300, 400]

def test_add_donation():
    Bill = Donor('Bill Gates', [300, 400])
    Bill.add_donation(450)
    assert Bill.donations == [300, 400, 450]


def test_total_donations():
    Bill = Donor('Bill Gates', [300, 400])
    assert Bill.total_donations == 700


def test_donations_number():
    Bill = Donor('Bill Gates', [300, 400])
    assert Bill.donations_number == 2


def test_average_donation():
    Bill = Donor('Bill Gates', [300, 400])
    assert Bill.average_donation == 350

def test_repr():
    Bill = Donor('Bill Gates', [300])
    assert str(Bill) == '[Bill Gates, [300]]'

def test_lt():
    Bill = Donor('Bill Gates', [300])
    Jeff = Donor('Jeff Bezos', [100])
    assert Bill.donations > Jeff.donations

def test_gt():
    Bill = Donor('Bill Gates', [300])
    Jeff = Donor('Jeff Bezos', [100])
    assert Jeff.donations < Bill.donations


def test_donor_collection():
    Jeff = Donor('Jeff Bezos', [100])
    donors = DonorCollection(Jeff)
    assert str(donors) == ("[[Jeff Bezos, [100]]]")

def test_donor_repr():
    donors = DonorCollection(Donor('Jeff Bezos', [100]))
    assert str(donors) == '[[Jeff Bezos, [100]]]'

def test_is_in_list():
    donors = DonorCollection(Donor('Jeff Bezos', [100]))
    assert donors.is__in_list('Jeff Bezos') == True

def test_add_donation_to_list():
    donors = DonorCollection(Donor('Jeff Bezos', [100]))
    donors.add_donation_to_list('Jeff Bezos', 300)
    print(donors)
    assert str(donors) == '[[Jeff Bezos, [100, 300]]]'

def test_add_new_donor():
    donors = DonorCollection(Donor('Jeff Bezos', [100]))
    donors.add_new_donor('Bill Gates', 400)
    print(donors)
    assert str(donors) == '[[Jeff Bezos, [100]], [Bill Gates, [400]]]'

def test_list(capsys):
    Bill = Donor('Bill', [300])
    donors = DonorCollection(Bill)
    donors.list()
    captured = capsys.readouterr()
    assert captured.out == 'Bill\n'

def test_donors():
    Bill = Donor("Bill", [500])
    Jeff = Donor("Jeff", [10000])
    donors = DonorCollection(Bill, Jeff)
    assert str(donors) == ('[[Bill, [500]], [Jeff, [10000]]]')
