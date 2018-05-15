#!/usr/bin/env python3
"""
File Name: test_mailroom4.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/8/2018
Python Version: 3.6.4
"""

import mailroom4


user = 'Test User'
donation = 77.77


def test_quit():
    assert mailroom4.quit() == 'exit menu'


def test_dict():
    assert 'Tom Selleck' in mailroom4.donors.keys()


def test_add_donor():
    mailroom4.add_donor(user)
    assert user in mailroom4.donors.keys()
    assert mailroom4.donors[user] == []


def test_add_donation():
    mailroom4.add_donor(user)
    mailroom4.add_donation(user, donation)
    assert donation in mailroom4.donors[user]


def test_print():
    email = 'Dear Test User, thank you for your generous donation of $77.77\n'
    assert mailroom4.print_email(user, donation) == email


def test_sort():
    '''Asserts values in list are sorted'''
    list = mailroom4.sort_donors()
    for i in range(len(list) - 1):
        assert list[i][1] >= list[i+1][1]
