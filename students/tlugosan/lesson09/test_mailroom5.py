#!/usr/bin/env python3

import sys
from io import StringIO
import pytest

import mailroom5 as mailroom


def test_Donor_init():
    d = mailroom.Donor("Angela", [245])
    assert d.name == "Angela"
    assert d.donation == [245]


def test_Donor_init_int():
    d = mailroom.Donor("Angela", 33)
    assert d.donation == [33]


def test_donor_init_donation_null():
    d = mailroom.Donor('', [44])
    assert d.name == 'Anonymous'


def test_donation_addition():
    d = mailroom.Donor("Angela", [245])
    d.add_donation(77)
    assert d.donation == [245, 77]


def test_donation_addition_int():
    d = mailroom.Donor("Angela", 55)
    d.add_donation(77)
    assert d.donation == [55, 77]


def test_donation_addition_negative():
    d = mailroom.Donor("Angela", 55)
    with pytest.raises(ValueError):
        d.add_donation(-77)


def test_set_name():
    d = mailroom.Donor("Angela", 55)
    d.name = "Bob"
    assert d.name == "Bob"
    d.name = 34
    assert d.name == "34"


def test_donation_stats():
    donation_list = [75, 22, 34]
    d = mailroom.Donor("Angela", donation_list)
    assert d.total_donation_amount() == 75 + 22 + 34
    assert d.donation_occurrences() == 3
    assert d.average_total_donor_amount() == (75 + 22 + 34) / 3
    assert d.stats() == [75 + 22 + 34, 3, (75 + 22 + 34) / 3]


def test_donor_list_add_donor():
    d = mailroom.Donor("Angela", [245])
    c = mailroom.Donor("Bob", [34, 22])
    ab = mailroom.DonorList([d, c])
    e = mailroom.Donor("Adam", [34, 22])
    ab.add_donor_list(e)
    assert ab.donors == [d, c, e]


def test_names_only_list():
    d = mailroom.Donor("Angela", [245])
    c = mailroom.Donor("Bob", [34, 22])
    e = mailroom.Donor("Adam", [34, 22])
    ab = mailroom.DonorList([d, c, e])
    names_only_list = ab.names_only_list()
    assert names_only_list == ['Angela', 'Bob', 'Adam']


def test_find_donor():
    d = mailroom.Donor("Angela", [245])
    c = mailroom.Donor("Bob", [34, 22])
    e = mailroom.Donor("Adam", [34, 22])
    ab = mailroom.DonorList([d, c, e])
    b = ab.find_donor_history("Bob")
    assert b.name == c.name
    assert b.donation == c.donation


"""def test_select_action_dictionary_exit(capsys):
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
        assert os.path.exists(target_file_path)"""
