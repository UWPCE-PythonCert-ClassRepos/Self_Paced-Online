# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:09:24 2018

@author: Laura.Fiorentino
"""


from mailroom_4 import *


def test_add_donation():
    add_donation('Frank Reynolds', 1000)
    assert donor_list['Frank Reynolds'] == [10, 20, 50, 1000]


