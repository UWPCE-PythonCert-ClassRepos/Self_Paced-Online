#!/usr/bin/env python3
"""
Victor Medina
Date: 1/12/2019
Assignment 4: Mailroom Part 2
"""

from mailroom_4 import send_letters
from mailroom_4 import create_report

import sys
import os.path

def test_send_letters():
    donors = {
        'Victor': [100, 20, 30],
        'John': [12],
        'Kevin': [91, 32],
        'Kelly': [5, 21],
        'Matt': [75, 20],
        'Josh': [31, 3],
        'Micah': [120]}
    peoples = list(donors.keys())
    send_letters(donors)
    for people in peoples:
        assert os.path.isfile(people+'.txt')



def test_create_report():
    donors = {
        'Victor': [100, 20, 30],
        'John': [12],
        'Kevin': [91, 32],
        'Kelly': [5, 21],
        'Matt': [75, 20],
        'Josh': [31, 3],
        'Micah': [120]}

    assert create_report(donors) == 'Donor Name      | Total Given |   Num Gifts  | Average Gift\n'\
                                    '------------------------------------------------------------\n'\
                                    'Victor          $          150              3 $        50.00\n'\
                                    'John            $           12              1 $        12.00\n'\
                                    'Kevin           $          123              2 $        61.50\n'\
                                    'Kelly           $           26              2 $        13.00\n'\
                                    'Matt            $           95              2 $        47.50\n'\
                                    'Josh            $           34              2 $        17.00\n'\
                                    'Micah           $          120              1 $       120.00\n'\

