#!/usr/bin/env python3
from unittest import TestCase, mock
import pytest
import mailroom_v4
import unittest
from io import StringIO
from testfixtures import tempdir, compare
import os


@pytest.mark.parametrize('name, amount, expected', [
    ("dan", '50', "Thank you dan for donating 50 dollars generously."),
    ("jeff", '60', "Thank you jeff for donating 60 dollars generously.")
])
def test_thank_you_letter_positive(name, amount, expected):
    result = str(mailroom_v4.thank_you_letter(name, amount))
    assert expected == result


@pytest.mark.parametrize('name, amount, expected', [
    ("dan", 50, "Thank you sam for donating 50 dollars generously."),
    ("jeff", 60, "Thank you  for donating 60 dollars generously.")
])
def test_thank_you_letter_negitive(name, amount, expected):
    result = str(mailroom_v4.thank_you_letter(name, amount))
    assert expected != result


testing_donors_data = {"testname1": [200, 20, 35.5],
                   "testname2": [500, 20],
                   "Susan": [1000, 20, 70],
                   "Rob": [250, 20],
                   }


@unittest.mock.patch('mailroom_v4.donor_details')
def test_donor_details(mock_donor_details):
    mailroom_v4.donor_details(testing_donors_data)
    mock_donor_details.assert_called_with(testing_donors_data)


def test_amount_validate_positive():
    assert mailroom_v4.amount_validate(float(20))


@unittest.mock.patch('mailroom_v4.amount_validate')
def test_amount_validate_negitive(mock_amount_validate):
    mailroom_v4.amount_validate(-10)
    mock_amount_validate.assert_called_with(-10)


@unittest.mock.patch('mailroom_v4.update_data_print_thanks')
def test_thank_you(mock_update_data_print_thanks):
    mailroom_v4.update_data_print_thanks(float(10), "name1")
    assert mock_update_data_print_thanks.called


@unittest.mock.patch('sys.stdout', new_callable=StringIO)
def test_create_report(mock_stdout,):
    mailroom_v4.create_report()
    assert mock_stdout.getvalue() == '''Donor Name           |         Total Given |Num Gifts            |                Aver
------------------------------------------------------------------------------------------
John                 $               255.5                    3 $     85.17
Jeff                 $                 520                    2 $     260.0
Susan                $                1090                    3 $     363.3
Rob                  $                 270                    2 $     135.0
Ross                 $                 200                    1 $     200.0\n'''


@unittest.mock.patch('mailroom_v4.send_letters_all')
def test_send_letters_all_call(mock_send_letters_all_call):
    test_send_donors_data = {"testname3": [200, 20, 35.5],
                           "testname2": [500, 20],
                           "Susan": [1000, 20, 70],
                           "Rob": [250, 20],
                           }
    mailroom_v4.send_letters_all(**test_send_donors_data)
    assert mock_send_letters_all_call.called
    #compare(dir.read('Susan.txt'), b'some  thing')


test_send_letters_all_call()


# @unittest.mock.patch('mailroom_v4.send_letters_all')
# def test_send_letters_all(mock_test_send_letters_all_call):
#     test_send_donors_data = {"testname3": [200, 20, 35.5],
#                              "testname2": [500, 20],
#                              "Susan": [1000, 20, 70],
#                              "Rob": [250, 20],
#                              }
#     print(mock_test_send_letters_all_call(**test_send_donors_data))
#     print(mailroom_v4.send_letters_all(**test_send_donors_data))
#
#     assert os.path.isfile("testname3.txt") == 1



#test_send_letters_all
