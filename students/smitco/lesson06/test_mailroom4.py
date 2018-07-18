# lesson 06 testing for mailroom4
# implemented using pytest
# !/usr/bin/env python3


import os
import datetime
import mailroom4 as m
import pytest
import sys
from unittest import mock


def test_donor_name(capsys):
    user_inputs = ["James Bond", "5000", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.donor_name()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "James Bond" and "5000" in out


def test_donation_amount(capsys):
    with mock.patch("builtins.input", return_value="2000"):
        m.donation_amount("James Bond")
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert out == ("\nThank you, James Bond, for your generous donation of $2000 to the Brave Heart Foundation.\n")


def test_donation_amount_exit():
    m.donors["Jimmy Dean"] = []
    with mock.patch("builtins.input", return_value="exit"):
        m.donation_amount("Jimmy Dean")
        assert "Jimmy Dean" not in m.donors


def test_donation_amount_invalid_entry(capsys):
    m.donors["Jimmy Dean"] = []
    with mock.patch("builtins.input", return_value="dksjsh"):
        m.donation_amount("Jimmy Dean")
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Jimmy Dean" not in m.donors


def test_email(capsys):
    m.email("James Bond", 8000)
    sys.stderr.write("error")
    out, err = capsys.readouterr()
    assert out == ("\nThank you, James Bond, for your generous donation of $8000 to the Brave Heart Foundation.\n")


def test_report(capsys):
    m.report()
    sys.stderr.write("error")
    out, err = capsys.readouterr()
    assert "James Bond" in out


def test_letters():
    current = datetime.datetime.now()
    date = str(current.month) + "_" + str(current.day) + "_" + str(current.year)
    file_name = "James Bond" + " " + date + ".txt"
    m.letters()
    assert os.path.isfile(file_name)


def test_menu_valid_choice(capsys):
    with mock.patch("builtins.input", return_value="2"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "James Bond" in out


def test_menu_invalid_entry(capsys):
    with mock.patch("builtins.input", return_value="5"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert out == ("\nThere was an error. Please try again.\n\n")


def test_quit():
    with pytest.raises(SystemExit) as py_se:
        m.quit()
    assert py_se.type == SystemExit
