#!/usr/bin/env python
# coding: utf-8

import pytest
from mailroom4 import *

import pytest


def test_exit():
    with pytest.raises(SystemExit):
        quit_sel()

# test if directory_path can find the directory path of donor_list (
# folder containing all donor text files)
def test_directory_path():
    test_path = directory_path("donor_list")
    directories = test_path.split("\\")
    assert "donor_list" == directories[-1]

# test if open_donor_file can open and extract list of donations form a donor
def test_open_donor_file():
    dir_path = directory_path("donor_list")
    file_path = os.path.join(dir_path, "Paul_Allen.txt")
    donation_info = open_donor_file(file_path)
    test_donations = donation_info.split(", ")
    assert eval(test_donations[0]) == 300


# given folder name holding the text files of donors, test if directory_path can find the whole path in the machine

def test_one_donor_info():
# get directory information
    dir_path = directory_path("donor_list")
    file_name = "Paul_Allen.txt"
    donor_dict = one_donor_info(file_name = file_name, donor_folder = dir_path)
    donor_first_name = list(donor_dict.values())[0][0]
    assert donor_first_name == "Paul"



def test_all_donors_info():
    # get directory information
    dir_path = directory_path("donor_list")
    all_donors = all_donors_info(dir_path)
    donor_list = list(all_donors.keys())
    assert "Paul Allen" in donor_list
