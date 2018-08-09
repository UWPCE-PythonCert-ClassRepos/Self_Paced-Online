# lesson 09 testing for mailroom object oriented
# implemented using pytest
# !/usr/bin/env python3


import os
import datetime
import mailroomOO as m
import pytest
import sys
from unittest import mock


def test_donor_email(capsys):
    d = m.Donor("JK Rowling")
    d.donor_email("JK Rowling", 8752)
    sys.stderr.write("error")
    out, err = capsys.readouterr()
    assert "JK Rowling" and "8752" in out


def test_donor_append():
    ad = m.AllDonors()
    ad.donor_append("Jim Carrey", 3425)
    assert "Jim Carrey" in ad.donors


def test_donor_details():
    ad = m.AllDonors()
    ad.donor_details()
    assert ("Joey Tribbiani", [9000, 1, 9000.0]) in ad.details
    assert ad.details[0][1] > ad.details[1][1]
    assert ad.details[1][1] > ad.details[2][1]


def test_donor_report(capsys):
    ad = m.AllDonors()
    ad.donor_report()
    sys.stderr.write("error")
    out, err = capsys.readouterr()
    assert "Joey Tribbiani" in out
    assert "9000.00" in out


def test_donor_letters():
    ad = m.AllDonors()
    ad.donor_letters()
    current = datetime.datetime.now()
    date = [str(current.month), str(current.day), str(current.year)]
    current_date = "_".join(date)
    letter_name = ("Joey Tribbiani" + " " + current_date + ".txt")
    test_file = open(letter_name, "r")
    assert "Joey Tribbiani" and "9000" in test_file.read()


def test_menu_valid_choice(capsys):
    with mock.patch("builtins.input", return_value="3"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Files completed" in out


def test_menu_invalid_number(capsys):
    with mock.patch("builtins.input", return_value="5"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert out == ("\nThere was an error. Please try again.\n\n")


def test_menu_invalid_entry(capsys):
    with mock.patch("builtins.input", return_value="sdgdfg"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert out == ("\nThere was an error. Please try again.\n\n")


def test_thank_you(capsys):
    user_inputs = ["George Washington", "4295", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "George Washington" and "4295" in out

def test_thank_you_list_exit(capsys):
    user_inputs = ["List", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "George Washington" and "Exiting" in out


def test_thank_you_donation_exit(capsys):
    user_inputs = ["James Bond", "exit", "list", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Exiting" in out
        assert "James Bond" not in out


def test_thank_you_large_donation(capsys):
    user_inputs = ["James Bond", "42954356804343", "list", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "too large" in out
        assert "James Bond" not in out


def test_thank_you_invalid_entry(capsys):
    user_inputs = ["James Bond", "sdhfdhfd", "list", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Invalid entry" in out
        assert "James Bond" not in out


def test_report(capsys):
    m.report()
    sys.stderr.write("error")
    out, err = capsys.readouterr()
    assert "George Washington" and "Judy Blume" in out


def test_letters():
    current = datetime.datetime.now()
    date = [str(current.month), str(current.day), str(current.year)]
    current_date = "_".join(date)
    file_name = "George Washington" + " " + current_date + ".txt"
    m.letters()
    assert os.path.isfile(file_name)


def test_quit():
    with pytest.raises(SystemExit) as py_se:
        m.quit()
    assert py_se.type == SystemExit
