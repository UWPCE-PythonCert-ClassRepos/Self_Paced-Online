#!/usr/bin/env python
import pytest
from mailroom import format_currency_str
from mailroom import list_donors, sort_donors, donor_key_search
from mailroom import add_donation, add_donor_name, append_donation
from mailroom import donor_email, thank_donor, get_donor_summary, print_report


def test_list_donors(capsys):
    list_donors()
    captured = capsys.readouterr()
    assert captured.out == ('Jim Halpert\n'
                            'Pam Beesley\n'
                            'Dwight Shrute\n'
                            'Michael Scott\n'
                            'Andy Bernard\n')


def test_sort_donors():
    donors = [('Pam Beesley', [1000.0, 2000.0, 3000.0]),
              ('Andy Bernard', [500.0]),
              ('Michael Scott', [10.0, 20.0, 30.0]),
              ('Dwight Shrute', [2.0, 3.0]),
              ('Jim Halpert', [1.0])]
    assert sort_donors() == donors


def test_donor_key_missing():
    with pytest.raises(KeyError):
        donor_key_search('')


def test_donor_key_found():
    assert donor_key_search('Jim Halpert') is True


def test_format_currency_str():
    assert format_currency_str('1.00') == '$1.00'


def test_donor_not_empty():
    with pytest.raises(ValueError):
        add_donor_name('')


def test_donor_added_done():
    assert add_donor_name('John Doe') is True


def test_donation_value():
    with pytest.raises(ValueError):
        add_donation('John Doe', 'abc')


def test_append_donation_value():
    with pytest.raises(ValueError):
        append_donation('Jim Halpert', 'z')


def test_append_donation_done():
    assert append_donation('Jim Halpert', 1.00) is True


def test_donation_added():
    assert add_donation('Jim Halpert', 1.00) is True


def test_thank_single(capsys):
    str1 = ('Dear Jim Halpert,\n\n'
            '        Thank you for your very kind donation of $1.00.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team\n')
    thank_donor('Jim Halpert', 1.00)
    captured = capsys.readouterr()
    assert captured.out == str1


def test_donor_email(capsys):
    str1 = ('Dear Jim Halpert,\n\n'
            '        Thank you for your very kind donation of $1.00.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team\n')
    donor_email('Jim Halpert', 1.00, False)
    captured = capsys.readouterr()
    assert captured.out == str1


def test_get_donor_summary():
    donors = [('Pam Beesley', [1000.0, 2000.0, 3000.0]),
              ('Andy Bernard', [500.0]),
              ('Michael Scott', [10.0, 20.0, 30.0]),
              ('Dwight Shrute', [2.0, 3.0]),
              ('Jim Halpert', [1.0])]
    summary = [['Pam Beesley', '$6000.00', '3', '$2000.00'],
               ['Andy Bernard', '$500.00', '1', '$500.00'],
               ['Michael Scott', '$60.00', '3', '$20.00'],
               ['Dwight Shrute', '$5.00', '2', '$2.50'],
               ['Jim Halpert', '$1.00', '1', '$1.00']]
    assert get_donor_summary(donors) == summary


def test_print_report(capsys):
    summary = [['Pam Beesley', '$6000.00', '3', '$2000.00'],
               ['Andy Bernard', '$500.00', '1', '$500.00'],
               ['Michael Scott', '$60.00', '3', '$20.00'],
               ['Dwight Shrute', '$5.00', '2', '$2.50'],
               ['Jim Halpert', '$1.00', '1', '$1.00']]
    r = ('Donor Name                | Total Given | Num Gifts | Average Gift\n'
         'Pam Beesley                $   $6000.00 |         3  $    $2000.00\n'
         'Andy Bernard               $    $500.00 |         1  $     $500.00\n'
         'Michael Scott              $     $60.00 |         3  $      $20.00\n'
         'Dwight Shrute              $      $5.00 |         2  $       $2.50\n'
         'Jim Halpert                $      $1.00 |''         1  $       $1.00'
         '\n')
    print_report(summary)
    captured = capsys.readouterr()
    assert captured.out == r
