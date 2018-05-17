#!/usr/bin/env python

"""Test file for mailroom.py"""
import mailroom
import os
import pytest


def test_update_tot_avg():
    test_dict = {'name': 'Testy McTestFace',
                 'donations': [789.25, 87561.75, 125000.00],
                 'last_don': 125000
                 }
    mailroom.update_tot_avg(test_dict)
    assert test_dict['tot_don'] == 213351
    assert test_dict['num_don'] == 3
    assert test_dict['avg_don'] == 71117


def test_gen_email():
    expected = ('FROM: Your friendly local charity mailroom.\n'
                'TO: {name}\n'
                'RE: Your recent donation\n\n'
                '\nThank you so much for your recent donation of'
                ' ${last_don:,.2f}. This will go a long way towards helping to'
                ' save the pythons. Your generosity is most appreciated!'
                '\n\nBest Regards,\nSave The Pythons\n'
                )
    assert mailroom.gen_email() == expected


def test_create_report():
    mailroom.donors = {'abe lincoln': {'avg_don': 2.6666666666666665,
                                       'donations': [5, 2, 1],
                                       'last_don': 1,
                                       'name': 'Abe Lincoln',
                                       'num_don': 3,
                                       'tot_don': 8
                                       },
                       'bill gates': {'avg_don': 71117.15666666666,
                                      'donations': [789.25, 87562.22, 125000],
                                      'last_don': 125000,
                                      'name': 'Bill Gates',
                                      'num_don': 3,
                                      'tot_don': 213351.47
                                      },
                       'jeff bezos': {'avg_don': 1793.445,
                                      'donations': [3456.89, 130],
                                      'last_don': 130,
                                      'name': 'Jeff Bezos',
                                      'num_don': 2,
                                      'tot_don': 3586.89
                                      },
                       'jimmy buffett': {'avg_don': 85000.0,
                                         'donations': [85000],
                                         'last_don': 85000,
                                         'name': 'Jimmy Buffett',
                                         'num_don': 1,
                                         'tot_don': 85000
                                         },
                       'yankee doodle': {'avg_don': 67.0,
                                         'donations': [67],
                                         'last_don': 67,
                                         'name': 'Yankee Doodle',
                                         'num_don': 1,
                                         'tot_don': 67
                                         }
                       }
    expected = [('\n     Donor Name     | Total Given | Num Gifts | '
                 'Average Gift'),
                '------------------------------------------------------------',
                'Bill Gates            $  213351.47           3  $   71117.16',
                'Jimmy Buffett         $   85000.00           1  $   85000.00',
                'Jeff Bezos            $    3586.89           2  $    1793.44',
                'Yankee Doodle         $      67.00           1  $      67.00',
                'Abe Lincoln           $       8.00           3  $       2.67'
                ]
    assert mailroom.gen_report_text() == expected


def test_add_donation():
    mailroom.donors = {'abe lincoln': {'avg_don': 2.6666666666666665,
                                       'donations': [5, 2, 1],
                                       'last_don': 1,
                                       'name': 'Abe Lincoln',
                                       'num_don': 3,
                                       'tot_don': 8
                                       }
                       }
    mailroom.add_donation('Abe Lincoln', 8)
    assert mailroom.donors['abe lincoln']['last_don'] == 8
    assert mailroom.donors['abe lincoln']['num_don'] == 4


def test2_add_donation():
    mailroom.donors = {'abe lincoln': {'avg_don': 2.6666666666666665,
                                       'donations': [5, 2, 1],
                                       'last_don': 1,
                                       'name': 'Abe Lincoln',
                                       'num_don': 3,
                                       'tot_don': 8
                                       }
                       }
    mailroom.add_donation('Testy McTestFace', 50000)
    assert 'testy mctestface' in mailroom.donors
    assert mailroom.donors['testy mctestface']['name'] == 'Testy McTestFace'
    assert mailroom.donors['testy mctestface']['last_don'] == 50000
    assert mailroom.donors['testy mctestface']['num_don'] == 1
    assert mailroom.donors['testy mctestface']['tot_don'] == 50000
    assert mailroom.donors['testy mctestface']['avg_don'] == 50000


def test_write_letters_to_file():
    mailroom.donors = {'abe lincoln': {'avg_don': 2.6666666666666665,
                                       'donations': [5, 2, 1],
                                       'last_don': 1,
                                       'name': 'Abe Lincoln',
                                       'num_don': 3,
                                       'tot_don': 8
                                       },
                       'yankee doodle': {'avg_don': 67.0,
                                         'donations': [67],
                                         'last_don': 67,
                                         'name': 'Yankee Doodle',
                                         'num_don': 1,
                                         'tot_don': 67
                                         }
                       }
    mailroom.write_letters_to_file('.')
    assert os.path.isfile('Abe Lincoln.txt')
    assert os.path.isfile('Yankee Doodle.txt')

    with open('Abe Lincoln.txt', 'r') as f:
        actual = f.read()

    expected = ('FROM: Your friendly local charity mailroom.\n'
                'TO: Abe Lincoln\n'
                'RE: Your recent donation\n'
                '\n'
                '\n'
                'Thank you so much for your recent donation of $1.00. This '
                'will go a long way towards helping to save the pythons. '
                'Your generosity is most appreciated!\n'
                '\n'
                'Best Regards,\n'
                'Save The Pythons\n'
                )
    assert expected == actual
