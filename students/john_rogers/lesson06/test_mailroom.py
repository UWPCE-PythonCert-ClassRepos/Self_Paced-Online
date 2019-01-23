#!/usr/bin/env python3
"""
Test the various functions in mailroom_L6.py
"""

from mailroom_L6 import thank_all


db = {'sting': [13.45, 214.34, 123.45, 1433.23, 1243.13],
          'bono': [7843.34, 35.55, 732.34],
          'oprah': [66.34, 32.23, 632.21, 66.67],
          'yoko': [34.34, 4.34],
          'santa': [5334.00, 254.34, 64324.23, 2345.23, 5342.24],
          }


def test_thank_all(db):
    assert thank_all(db) == 

