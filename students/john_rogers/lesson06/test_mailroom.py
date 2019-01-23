#!/usr/bin/env python3
"""
Test the various functions in mailroom_L6.py
NOTE: Currently using a fixed date
"""

import pytest
import os


from mailroom_L6 import thank_all
from mailroom_L6 import exit_menu
from mailroom_L6 import save_report
from mailroom_L6 import form_letter


@pytest.fixture
def data():
    db = {'sting': [13.45, 214.34, 123.45, 1433.23, 1243.13],
          'bono': [7843.34, 35.55, 732.34],
          'oprah': [66.34, 32.23, 632.21, 66.67],
          'yoko': [34.34, 4.34],
          'santa': [5334.00, 254.34, 64324.23, 2345.23, 5342.24],
          }
    return db


def test_thank_all(data):
    assert thank_all(data) is None


def test_exit_menu(data):
    with pytest.raises(SystemExit):
        exit_menu(data)


def test_save_report(data):
    save_report(data)
    assert os.path.isfile('sting.2019-01-22.txt')
    assert os.path.isfile('bono.2019-01-22.txt')
    assert os.path.isfile('oprah.2019-01-22.txt')
    assert os.path.isfile('yoko.2019-01-22.txt')
    assert os.path.isfile('santa.2019-01-22.txt')


def test_form_letter():
    name = 'bill'
    amount = 100.01
    assert form_letter(name, amount) == "Hey Bill, thanks for your" \
                                        " donations! As of today, 2019-01-22," \
                                        " you have donated a total of $100.01."


