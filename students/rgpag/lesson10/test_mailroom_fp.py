import datetime
import os
from mailroom_fp import (don_in, donors, new_donor, update_don, challenge,
                         donors_sum, challenge_demo, thank_you, report,
                         send_letters, menu_switch_dict)


def test_challenge():
    test_dict = {'Jeff Bezos': [], 'Mark Zuckerberg': [10, 10],
                 'Bill Gates': [], 'Paul Allen': [10, 10, 10, 10, 10]}

    assert challenge(1, 0, 10) == test_dict


def test_donors_sum():
    assert donors_sum() == 43692


def test_don_in():
    assert don_in(100) == 100


def test_new_donor():
    assert new_donor('Barack Obama', 1000) == ('Barack Obama', 1, 1000)
    assert 'Barack Obama' in donors
    assert donors['Barack Obama'] == [1000]


def test_update_don():
    test_name = 'Mark Zuckerberg'
    pre_cnt = len(donors[test_name])
    pre_amt = sum(donors[test_name])
    assert update_don(test_name, 5000) == (test_name, pre_cnt+1, pre_amt+5000)


def test_thank_you():
    # check new donor
    assert thank_you('Robbie', 100) == ('Robbie', 1, 100)
    # check returning donor
    assert thank_you('Robbie', 100) == ('Robbie', 2, 200)
    assert thank_you('menu') is False


def test_send_letters():
# this checks if file was created and first 4 lines were written as expected
# unsure if need to be more thorough in testing files written
# e.g. need to check that all files exist, or entire msg was written
    send_letters()
    date = datetime.datetime.now()
    donor = 'Mark Zuckerberg'
    file_name = '{}_{}_{}_{}.txt'.format(donor, date.month, date.day,
                                         date.year)
    with open(file_name, 'r') as file:
        x = file.readlines(4)
    assert x == ['\n', '\n', 'Dear Mark Zuckerberg,\n']
    # need to find better way to "cleanup" after test
    for donor in donors:
        file_name = '{}_{}_{}_{}.txt'.format(donor, date.month, date.day,
                                             date.year)
        os.remove(file_name)


def test_menu_switch_dict():
    assert menu_switch_dict.get('1') == thank_you
    assert menu_switch_dict.get('2') == report
    assert menu_switch_dict.get('3') == send_letters
    assert menu_switch_dict.get('4') == challenge_demo
