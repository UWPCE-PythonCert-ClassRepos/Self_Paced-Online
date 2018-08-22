#!/usr/bin/env python3

import sys
from io import StringIO
import mailroom4 as mailroom
import unittest
from unittest import mock
from mock import patch
import pdb
from operator import itemgetter
import os


def test_select_action_dictionary_exit(capsys):
    test_input = ['4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('4', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip()
        assert out == "Before quitting."


def test_select_action_dictionary_lower_bound_invalid(capsys):
    test_input = ['0', '4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('0', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip()
        assert out == ("Please enter only one of the listed options.\n" + "Before quitting.")


def test_select_action_dictionary_upper_bound_invalid(capsys):
    test_input = ['5', '4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('5', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip()
        assert out.startswith("Please enter only one of the listed options.")


def test_tanks_existing_donor(capsys):
    test_input = ['1', 'list', 'Toni Orlando', 1234, '4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('1', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip()
        err = captured.err.strip()
        assert ('Dear {}, Thank you for your generous contribution of ${:.2f} to our program.'.format(test_input[2],
                                                                                                      test_input[
                                                                                                          3])) in out
def test_thanks_new_donor(capsys):
    test_input = ['1', 'list', "Bruno Mars", 450, '4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('1', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip('\n')
        err = captured.err.strip()
        assert 'Dear {}, Thank you for your generous contribution of ${:.2f} to our program.'.format(test_input[2],
                                                                                                     test_input[
                                                                                                         3]) in out


def test_thanks_negative_donation(capsys):
    test_input = ['1', 'list', "Toni Orlando", '-4', '1', '4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('1', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip('\n')
        err = captured.err.strip()
        assert 'Number has to be positive.' in out


def test_thanks_not_numeric_donation(capsys):
    test_input = ['1', 'list', "Toni Orlando", 'ab', '1', '4']
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.select_action_dictionary('1', mailroom.switch_func_dict)
        captured = capsys.readouterr()
        out = captured.out.strip('\n')
        err = captured.err.strip()
        assert 'Input must be a number.' in out


def test_thanks_directly(capsys):
    test_input = ["Marco Polo", 100]
    with mock.patch('builtins.input', side_effect=test_input):
        mailroom.sending_thank_you()
        captured = capsys.readouterr()
        out = captured.out.strip('\n')
        err = captured.err.strip()
        assert 'Dear {}, Thank you for your generous contribution of ${:.2f} to our program.'.format(*test_input) == out


def test_print_report(capsys):
    result_list = mailroom.print_report()
    captured = capsys.readouterr()
    out = captured.out.strip()
    test_list = []
    for k in mailroom.table_dictionary:
        sum_donations = sum(mailroom.table_dictionary[k])
        total_gifts = len(mailroom.table_dictionary[k])
        average_gift = sum_donations / total_gifts
        test_list.append([k, sum_donations, total_gifts, average_gift])
        test_sorted_new_list = sorted(test_list, key=itemgetter(1), reverse=True)
    test_table_header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
    assert test_list == result_list
    for a_header in test_table_header:
        assert a_header in out


def test_send_everyone_letters_directly(capsys):
    mailroom.send_everyone_letters()
    captured = capsys.readouterr()
    out = captured.out.strip('\n')
    err = captured.err.strip()
    file_name_extension = ".txt"
    current_directory = os.getcwd()
    for f_name in mailroom.table_dictionary:
        target_file_path = os.path.join(current_directory,
                                        str(f_name).replace(' ', '_') + mailroom.calculate_date() + file_name_extension)
        assert out == 'Done'
        assert os.path.exists(target_file_path)
