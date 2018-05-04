#!/usr/bin/env python

import time
import os
from mailroom4 import donors, thank_you, create_report, send_letters, add_user


def test_donors():
    assert isinstance(donors, dict) is True
    for name in donors.keys():
        assert name in list(donors)
    assert 'Amber Allison' not in list(donors)


def test_create_report():
    assert sum(donors['Mary May']) == 1750
    assert donors['Mary May'][0] == 1000
    new_list = []
    for i in donors.values():
        new_list.append(sum(i))
    assert new_list == [495, 1750, 1350, 85, 626]


def test_add_user():
    add_user('scott olsen', 100000)
    assert 'scott olsen' in donors.keys()
    assert 100000 in donors['scott olsen']


def test_send_letters():
    timestr = time.strftime("%Y%m%d")
    os.chdir('/Users/sbolsen/uw_python/Self_Paced-Online/students/sbolsen/lesson06')
    assert os.path.isfile('Mary_May_{}.txt'.format(timestr))
