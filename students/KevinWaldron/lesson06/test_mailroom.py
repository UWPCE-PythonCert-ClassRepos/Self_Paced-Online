#!/usr/bin/env python3

from mailroom import quit_menu, list_donors, create_thank_you, mail_everyone, create_report, create_flattened_sorted_donors_list, total_donations, add_donation

import os

def test_quit_menu():
    assert quit_menu() == 'Quit'

def test_list_donors():
    assert list_donors().strip() == "---------- Donors ----------\nBill Ted\nFrank Fred\nLaura Todd\nSteve Lincoln\nLisa Grant"

def test_mail_everyone():
    mail_everyone()
    dir_files = os.listdir()
    assert 'bill_ted.txt' in dir_files
    assert 'frank_fred.txt' in dir_files
    assert 'laura_todd.txt' in dir_files
    assert 'steve_lincoln.txt' in dir_files
    assert 'lisa_grant.txt' in dir_files

    with open('bill_ted.txt') as in_file:
        file_contents = in_file.read()
        assert file_contents.strip() == ("Dear Bill Ted,\nThank you for your very generous donation of $726.63.  "
            "It \nwill go very far in supporting the Human Fund, \"Money for \nPeople.\"\n"
            "                               Sincerely\n                                      Art Vandelay")

def test_create_report():
    assert create_report().strip() == (
        "Donor Name          | Total Given | Num Gifts | Average Gift\n"
        "-------------------------------------------------------------\n"
        "Bill Ted            | $    726.63 |         3 | $     242.21\n"
        "Lisa Grant          | $    209.70 |         2 | $     104.85\n"
        "Frank Fred          | $    178.76 |         3 | $      59.59\n"
        "Steve Lincoln       | $    165.28 |         2 | $      82.64\n"
        "Laura Todd          | $      5.75 |         1 | $       5.75"
        )

def test_create_thank_you():
    assert create_thank_you({'name':"Bill Ted", 'amount':5}) == ("Dear Bill Ted,\nThank you for your very generous donation of $5.00.  "
        "It \nwill go very far in supporting the Human Fund, \"Money for \nPeople.\"\n"
        "                               Sincerely\n                                      Art Vandelay")

def test_add_donation():
    assert add_donation("Test1", 55.55) == [55.55, 55.55]
    assert add_donation("Test1", 4) == [59.55, 55.55, 4]
    assert add_donation("Laura Todd", 99) == [104.75, 5.75, 99]

def test_total_donations():
    assert total_donations(["fred", 33]) == 33
    assert total_donations(["bill", 3, 5]) == 3
    try:
        total_donations(["bill"])
    except IndexError:
        pass
    else:
        assert False

def test_create_flattened_sorted_donors_list():
    add_donation("Smallest", 1)
    add_donation("Biggest", 9999)
    flat_list = create_flattened_sorted_donors_list()
    assert flat_list[0] == ['Biggest', 9999, 9999]
    assert flat_list[len(flat_list)-1] == ['Smallest', 1, 1]