#!/usr/bin/env python3

import os
from new_mailroom import add_donor, donors, thank_you_msg, save_report


def test_add_donor():
    add_donor('User1', 300)
    assert 'User1' in donors.keys()
    assert 300 in donors['User1']


def test_thank_you_msg():
    msg = thank_you_msg('Ford')
    assert msg == 'Thank you Ford for your generous donation of 3400'


def test_save_report():
    save_report()
    os.chdir('/Users/galmamar/git_repo/Self_Paced-Online/students/ghassan/lesson06')  # noqa: E501
    assert os.path.isfile('Jessie.txt')
    assert os.path.isfile('James.txt')
    assert os.path.isfile('Ford.txt')
