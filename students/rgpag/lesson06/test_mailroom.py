import datetime
import os
from mailroom import (don_in, donors, new_donor, update_don, menu_sel_1,
                      menu_sel_2, menu_sel_3, menu_switch_dict)


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


def test_menu_sel_1():
    # check new donor
    assert menu_sel_1('Robbie', 100) == ('Robbie', 1, 100)
    # check returning donor
    assert menu_sel_1('Robbie', 100) == ('Robbie', 2, 200)
    assert menu_sel_1('menu') is False
    x = 'Jeff Bezos\nMark Zuckerberg\nBill Gates\nPaul Allen\nRobbie'
# not sure if this approach is what I want to do here...
    assert menu_sel_1('list') == print(x)


# unsure how to test_menu_sel_2() at this time...
# related to above, unsure how to approach testing stdout and stdin


def test_menu_sel_3():
# this checks if file was created and first 4 lines were written as expected
# unsure if need to be more thorough in testing files written
# e.g. need to check that all files exist, or entire msg was written
    menu_sel_3()
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
    assert menu_switch_dict.get('1') == menu_sel_1
    assert menu_switch_dict.get('2') == menu_sel_2
    assert menu_switch_dict.get('3') == menu_sel_3

# unsure how to test __name__=="__main__" block at this time
