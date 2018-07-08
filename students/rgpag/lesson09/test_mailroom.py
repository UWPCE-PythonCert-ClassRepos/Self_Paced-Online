import datetime
import pytest
import os
from mailroom import (Donor, Donor_collect, don_in,
                      ind_thanks, all_thanks)

a = Donor("Jeff Bezos", [100])
b = Donor("Elon Musk", [500, 200])
c = Donor("Bill Gates", [50])
donor_list = [a, b, c]
D = Donor_collect(donor_list)


def test_Donor():
    test_donor = Donor('bob', [10, 20, 30])
    test_donor2 = Donor('joe', [20])
    assert test_donor.name == 'bob'
    assert test_donor.donations == [10, 20, 30]
    assert test_donor.total == 60
    assert test_donor.avg == 20
    assert test_donor.cnt == 3
    assert test_donor2 < test_donor


def test_Donor_collect():
    assert 'Jeff Bezos' in D.donor_dict


def test_DC_bad_input():
    with pytest.raises(TypeError):
        Donor_collect([10, 20, 30])


def test_DC_new_donor():
    D.new_donor('Devin', 10)
    assert 'Devin' in D.donor_dict
    assert D.donor_dict['Devin'].total == 10


def test_DC_update():
    D.update_donor('Devin', 10)
    assert D.donor_dict['Devin'].total == 20


def test_DC_search():
    assert D.search_donor('Jeff Bezos') is True
    assert D.search_donor('Not Donor') is False


def test_DC_get_msg_vars():
    assert D.get_msg_vars('Devin') == ('Devin', 2, 20)


def test_don_in():
    assert don_in(20) == 20


def test_ind_thanks():
    assert ind_thanks('menu') is False


def test_all_thanks():
    # this checks if file was created and first 4 lines were written as expected
    # unsure if need to be more thorough in testing files written
    # e.g. need to check that all files exist, or entire msg was written
    e = Donor('Mark Zuckerberg', [10])
    E = Donor_collect([e])
    date = datetime.datetime.now()
    donor = 'Mark Zuckerberg'
    file_name = '{}_{}_{}_{}.txt'.format(donor, date.month, date.day,
                                         date.year)
    all_thanks(E)
    with open(file_name, 'r') as file:
        x = file.readlines(1000)
    assert x == ['\n',
                 '\n',
                 'Dear Mark Zuckerberg,\n',
                 '\n',
                 'Thank you for your recent donation, did you realize you have now made 1 lifetime donations? Wow, look at you all star! We are most grateful for your total donation amount of $10.\n',
                 '\n',
                 "I will personally ensure these funds are put towards purchase of yummy donuts! Also, any additional contributions you make in the next 24 hours will be matched up to $1000. What a deal! Don't delay.\n",
                 '\n',
                 'Humbly yours,\n',
                 '\n',
                 'Dime for Donuts\n',
                 '\n']
    os.remove(file_name)
