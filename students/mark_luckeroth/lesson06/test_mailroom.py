import pytest
import os
from mailroom4 import totals
from mailroom4 import count
from mailroom4 import averages
from mailroom4 import update_records
from mailroom4 import create_report
from mailroom4 import doner_dict
from mailroom4 import letters


DONATIONS = {
    'Peter Pan': [10., 10., 10.],
    'Paul Hollywood': [5., 50000., 5., 5.],
    'Mary Berry': [100.],
    'Jake': [123., 456., 789.],
    'Raj': [60., 600000.]}


def test_totals():
    sum_dict = {
        'Peter Pan': 30.,
        'Paul Hollywood': 50015.,
        'Mary Berry': 100.,
        'Jake': 1368.,
        'Raj': 600060.}
    assert totals(DONATIONS) == sum_dict


def test_count():
    count_dict = {
        'Peter Pan': 3,
        'Paul Hollywood': 4,
        'Mary Berry': 1,
        'Jake': 3,
        'Raj': 2}
    assert count(DONATIONS) == count_dict


def test_avg():
    avg_dict = {
        'Peter Pan': 10.,
        'Paul Hollywood': 12503.75,
        'Mary Berry': 100.,
        'Jake': 456.,
        'Raj': 300030.}
    assert averages(totals(DONATIONS), count(DONATIONS)) == avg_dict


def test_update1():
    updated = {
        'Peter Pan': [10., 10., 10.],
        'Paul Hollywood': [5., 50000., 5., 5.],
        'Mary Berry': [100.],
        'Jake': [123., 456., 789.],
        'Raj': [60., 600000.],
        'alph': [123456.]}
    update_records('alph', 123456.)
    assert doner_dict() == updated


def test_update2():
    updated = {
        'Peter Pan': [10., 10., 10., 10.],
        'Paul Hollywood': [5., 50000., 5., 5.],
        'Mary Berry': [100.],
        'Jake': [123., 456., 789.],
        'Raj': [60., 600000.],
        'alph': [123456.]}
    update_records('Peter Pan', 10.)
    assert doner_dict() == updated


def test_create_report():
    report = ['Donor Name          | Total Given | Num Gifts | Average Gift',
              '------------------------------------------------------------',
              'Raj                  $    600060.0           2 $    300030.0',
              'alph                 $    123456.0           1 $    123456.0',
              'Paul Hollywood       $     50015.0           4 $    12503.75',
              'Jake                 $      1368.0           3 $       456.0',
              'Mary Berry           $       100.0           1 $       100.0',
              'Peter Pan            $        40.0           4 $        10.0']
    assert create_report() == report


def test_letters1():
    letters()
    donations_dict = doner_dict()
    expected_letters = [donor.replace(' ', '_')
                        for donor in donations_dict.keys()]
    found_letters = [f[:-4] for f in os.listdir('.') if f.endswith('.txt')]
    assert expected_letters.sort() == found_letters.sort()
