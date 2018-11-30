# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:17:11 2018

@author: Laura.Fiorentino
"""

from mailroom_oo import *


def test_donor():
    donor = Donor('donor', [1, 2, 3])
    assert donor.name == 'donor'
    assert donor.donations == [1, 2, 3]


def test_donor_numbers():
    donor = Donor('donor', [1, 2, 3])
    assert donor.total_donation == 6
    assert donor.number_donation == 3
    assert donor.avg_donation == 2


def test_add_donor():
    donor = Donor('donor', [1, 2, 3])
    donor.add_donation(100)
    assert donor.donations == [1, 2, 3, 100]


def test_list_donor(capsys):
    donor = Donor('donor', [1, 2, 3])
    donor.list_donations
    out, err = capsys.readouterr()
    test_string = 'donor Donations: $1, $2, $3\n'
    assert out == test_string



def test_donor_list():
    donor_list = Donor_List()
    donor_list.add_donation('donor', [1, 2, 3])
    assert donor_list.donors['donor'].donations == [1, 2, 3]
    donor_list.add_donation('donor', 2)
    assert donor_list.donors['donor'].donations == [1, 2, 3, 2]


def test_list_donors(capsys):
    donor_list = Donor_List()
    donor_list.add_donation('donor', [1, 2, 3])
    donor_list.add_donation('donor2', [1, 2, 3])
    list_donors(donor_list)
    out, err = capsys.readouterr()
    test_string = 'donor\ndonor2\n'
    assert out == test_string

