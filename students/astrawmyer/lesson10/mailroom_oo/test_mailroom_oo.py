#!/usr/bin/env python3

import mailroom_oo as m
import mailroom_oo_classes as mc
import pytest
import os


# Adding this to import preset data.
a = mc.Donor("James Hinchcliffe", [12.2,2.51,3.20])
b = mc.Donor("Robert Wickens", [1024.14,22.21,323.45])
c = mc.Donor("Sam Schmidt", [3.2,5.55,4.20])
donor_set = mc.Donors()
donor_set.new_donor(a)
donor_set.new_donor(b)
donor_set.new_donor(c)


def test_display_list(capsys):
    donor_set.display_list()
    out, err = capsys.readouterr()
    assert out == "James Hinchcliffe\nRobert Wickens\nSam Schmidt\n"


def test_write_letter():
    expected = "Dear James,\nThank you for donating $5.00 to the Human Fund. " \
            "Your money will be used appropriately."
    assert donor_set.write_letter("James",5) == expected


def test_write_report(capsys):
    expected_1 = 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
    expected_2 = '-------------------------------------------------------------------\n'
    expected_3 = 'Robert Wickens             $    1369.80           3  $      456.60\n'
    expected_4 = 'James Hinchcliffe          $      17.91           3  $        5.97\n'
    expected_5 = 'Sam Schmidt                $      12.95           3  $        4.32\n'
    expected = expected_1 + expected_2 + expected_3 +expected_4 + expected_5
    donor_set.write_report()
    out, err = capsys.readouterr()
    assert out == expected


def test_thank_you_add_donation():
    donor_set.add_donation('James Hinchcliffe',42)
    assert donor_set.data == {'James Hinchcliffe': [12.2, 2.51, 3.2, 42.0],
                        'Robert Wickens': [1024.14, 22.21, 323.45],
                        'Sam Schmidt': [3.2, 5.55, 4.2]}
    

def test_thank_you_new_donor():
    AR = mc.Donor("Alexander Rossi",[1])
    donor_set.new_donor(AR)
    assert donor_set.data == {'James Hinchcliffe': [12.2, 2.51, 3.2, 42.0],
                        'Robert Wickens': [1024.14, 22.21, 323.45],
                        'Sam Schmidt': [3.2, 5.55, 4.2],
                        'Alexander Rossi': [1]}


def test_all_letters():
    donor_set.letter_files()
    assert os.path.isfile('James Hinchcliffe.txt')
    assert os.path.isfile('Robert Wickens.txt')
    assert os.path.isfile('Sam Schmidt.txt')