#!/usr/bin/env python
# coding: utf-8

import pytest
from mailroom4 import *

import pytest


def test_one():
    with pytest.raises(SystemExit):
        quit_sel()

# in this computer donor_list is the file that contains the donors list and their
# contribution in text file. given that folder name, from any working directory
# test if this function can find it.

def test_two():
    test_values = donor_list_dir("donor_list").split("\\")
    assert "donor_list" == test_values[len(test_values)-1]

# tests if open_donor_file can open the donations by checking the his first
# donation which is 300

def test_three():
    test_path = os.path.join(donor_list_dir("donor_list"), "Paul_Allen.txt")
    test_donations = open_donor_file(test_path).split(", ")
    assert eval(test_donations[0]) == 300
