#!/usr/bin/env python3

# import pytest
# from mailroom import _donors
# from mailroom import Helpers
from mailroom import Donors
from mailroom import Donor

"""
Lesson9 - Object Oriented Mailroom Unit Test
"""


def test_list_donors(capsys):
    D = Donors()
    D.list_donors()
    captured = capsys.readouterr()
    donors = ('Jim Halpert\n'
              'Pam Beesley\n'
              'Dwight Shrute\n'
              'Michael Scott\n'
              'Andy Bernard\n')
    assert captured.out == donors


def test_sort_donors():
    D = Donors()
    sl = [('Pam Beesley', [1000.0, 2000.0, 3000.0]),
          ('Andy Bernard', [500.0]),
          ('Michael Scott', [10.0, 20.0, 30.0]),
          ('Dwight Shrute', [2.0, 3.0]),
          ('Jim Halpert', [1.0])]
    assert D.sort_donors() == sl


def test_donor_key_found():
    D = Donors()
    D.donor_key_found('Jim Halpert') is True


def test_get_donors_summary():
    D = Donors()
    sl = D.sort_donors()
    summary = [['Pam Beesley', '$6000.00', '3', '$2000.00'],
               ['Andy Bernard', '$500.00', '1', '$500.00'],
               ['Michael Scott', '$60.00', '3', '$20.00'],
               ['Dwight Shrute', '$5.00', '2', '$2.50'],
               ['Jim Halpert', '$1.00', '1', '$1.00']]

    assert D.get_donor_summary(sl) == summary


def test_donor_email_total(capsys):
    D = Donors()
    name = 'Pam Beesley'
    donations = sum([1000.00, 2000.00, 3000.00])
    dstr = ('\n\nDear Pam Beesley,\n\n'
            '        Thank you for your very kind'
            ' donations totalling $6000.00.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team\n\n\n')
    D.donor_email(name, donations)
    captured = capsys.readouterr()
    assert captured.out == dstr


def test_generate_letters(capsys):
    D = Donors()
    D.generate_letters()
    str1 = '\n\n========== Letters Created ==========\n\n\n'
    captured = capsys.readouterr()
    assert captured.out == str1


def test_create_report(capsys):
    D = Donors()
    D.create_report()
    str1 = ('Donor Name                | Total Given | Num Gifts | Average Gift\n'
            'Pam Beesley                $   $6000.00 |         3  $    $2000.00\n'
            'Andy Bernard               $    $500.00 |         1  $     $500.00\n'
            'Michael Scott              $     $60.00 |         3  $      $20.00\n'
            'Dwight Shrute              $      $5.00 |         2  $       $2.50\n'
            'Jim Halpert                $      $1.00 |         1  $       $1.00\n')
    captured = capsys.readouterr()
    assert captured.out == str1


def test_donations_total():
    D = Donors()
    D.donations_total('Pam Beesley') == '$6000.00'


def test_donations_count():
    D = Donors()
    D.donations_total('Pam Beesley') == 3


def test_donations_average():
    D = Donors()
    D.donations_total('Pam Beesley') == '$2000.00'


def test_donor_email_single(capsys):
    d = Donor()
    name = 'Pam Beesley'
    donation = 100.00
    dstr = ('\n\nDear Pam Beesley,\n\n'
            '        Thank you for your very kind'
            ' donation of $100.00.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team\n\n\n')
    d.donor_email(name, donation)
    captured = capsys.readouterr()
    assert captured.out == dstr
