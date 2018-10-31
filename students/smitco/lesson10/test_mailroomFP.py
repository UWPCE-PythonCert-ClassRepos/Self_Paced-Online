# lesson 10 testing mailroom functional programming
# based on testing mailroom 4 file
# implemented using pytest
# !/usr/bin/env python3


import os
import datetime
import mailroomFP as m
import pytest
import sys
from unittest import mock


def test_thank_you(capsys):
    user_inputs = ["James Bond", "5200", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "James Bond" and "5,200" in out
        assert "James Bond" in m.donors


def test_thank_you_list(capsys):
    user_inputs = ["list", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Judy Blume" in out
        assert "Joey Tribbiani" in out


def test_thank_you_exit(capsys):
    with mock.patch("builtins.input", return_value="exit"):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Exiting" in out


def test_thank_you_invalid_entry(capsys):
    user_inputs = ["Jimmy Dean", "dksjsh", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "Invalid" in out
        assert "Jimmy Dean" not in m.donors


def test_thank_you_large_donation(capsys):
    user_inputs = ["Jimmy Dean", "10000000000", "exit"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.thank_you()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "too large" in out
        assert "Jimmy Dean" not in m.donors


def test_report(capsys):
    m.report()
    sys.stderr.write("error")
    out, err = capsys.readouterr()
    assert "James Bond" and "5,200" in out


def test_letters():
    current = datetime.datetime.now()
    date = [str(current.month), str(current.day), str(current.year)]
    current_date = "_".join(date)
    letter_name = "James Bond" + " " + current_date + ".txt"
    m.letters()
    assert os.path.isfile(letter_name)
    test_file = open(letter_name, "r")
    assert "James Bond" and "5,200" in test_file.read()


def test_matching(capsys):
    user_inputs = ["3000", "4000", "3"]
    with mock.patch("builtins.input", side_effect=user_inputs):
        m.match()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "6,500" in out
        assert "19,500" in out


def test_menu_valid_choice(capsys):
    with mock.patch("builtins.input", return_value="2"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert "James Bond" in out


def test_menu_invalid_number(capsys):
    with mock.patch("builtins.input", return_value="9"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert out == ("\nThere was an error. Please try again.\n\n")


def test_menu_invalid_entry(capsys):
    with mock.patch("builtins.input", return_value="sdlhgdsgs"):
        m.menu()
        sys.stderr.write("error")
        out, err = capsys.readouterr()
        assert out == ("\nThere was an error. Please try again.\n\n")


def test_quit():
    with pytest.raises(SystemExit) as py_se:
        m.quit()
    assert py_se.type == SystemExit
