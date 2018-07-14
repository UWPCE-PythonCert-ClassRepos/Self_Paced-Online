#!/usr/bin/env python
from io import StringIO
from datetime import date
from contextlib import redirect_stdout
import ast
import pytest
from mailroomOO import *
from mailroomOO import input_dollars

def make_group_for_testing():
    gd1 = Group_Donors()
    gd1.add_donor(Individual_Donor('John Doe', 500.05))
    gd1.add_donor(Individual_Donor('Jane Doe', 333.33))
    return gd1


# Individual_Donor class
def test_Individual_Donor_create_donor():
    id1 = Individual_Donor('John Doe', 500.05)
    assert (id1.name == 'John Doe' and id1.donations == {str(date.today()): [500.05]})


def test_Individual_Donor_create_donor_with_date():
    id1 = Individual_Donor('John Doe', 500.05, donation_date='2017-03-21')
    assert (id1.name == 'John Doe' and id1.donations == {'2017-03-21': [500.05]})


def test_Individual_Donor_getter_and_property_name():
    id1 = Individual_Donor('John Doe', 500.05)
    assert id1[str(date.today())] == [500.05]


def test_Individual_Donor_setter_does_not_work():
    id1 = Individual_Donor('John Doe', 500.05)
    id1[str(date.today())] == [1.23]
    assert id1[str(date.today())] == [500.05]


def test_Individual_Donor_property_donations():
    id1 = Individual_Donor('John Doe', 500.05)
    assert id1.donations == {str(date.today()): [500.05]}


def test_Individual_Donor_add_dollars():
    id1 = Individual_Donor('John Doe', 500.05)
    id1.add_dollars(1.23)
    assert (id1.name == 'John Doe' and id1.donations == {str(date.today()): [500.05, 1.23]})


def test_Individual_Donor_add_dollars_with_date():
    id1 = Individual_Donor('John Doe', 500.05, donation_date='2017-03-21')
    id1.add_dollars(1.23, donation_date='2017-03-21')
    assert (id1.name == 'John Doe' and id1.donations == {'2017-03-21': [500.05, 1.23]})


def test_Individual_Donor_add_dollars_with_two_dates():
    id1 = Individual_Donor('John Doe', 500.05, donation_date='2017-03-21')
    id1.add_dollars(1.23)
    assert (id1.name == 'John Doe' and id1.donations == {'2017-03-21': [500.05], str(date.today()): [1.23]})


def test_Individual_Donor_calc_total_donation():
    id1 = Individual_Donor('John Doe', 500.05)
    id1.add_dollars(1.23, donation_date='2017-03-21')
    id1.add_dollars(3.72)
    testdata = id1.report_total_donations()
    assert testdata == 505.00


def test_Individual_Donor_calc_num_donations():
    id1 = Individual_Donor('John Doe', 500.05)
    id1.add_dollars(1.23, donation_date='2017-03-21')
    id1.add_dollars(3.72)
    testdata = id1.report_total_num_gifts()
    assert testdata == 3


def test_Individual_Donor_latest_donation():
    id1 = Individual_Donor('John Doe', 500.05)
    id1.add_dollars(1.23, donation_date='2017-03-21')
    id1.add_dollars(3.72)
    testdata = id1.latest_donation()
    assert testdata == str(date.today())


# Group_Donors class
def test_Group_Donors_add_Donor():
    gd1 = Group_Donors()
    id1 = Individual_Donor('John Doe', 500.05)
    id2 = Individual_Donor('Jane Doe', 333.33)
    gd1.add_donor(id1)
    gd1.add_donor(id2)
    assert gd1.donor_list == ['John Doe', 'Jane Doe']


def test_Group_Donors_add_Donor_2():
    gd1 = make_group_for_testing()
    assert gd1.donor_list == ['John Doe', 'Jane Doe']


def test_Group_Donors_find_Donor():
    gd1 = Group_Donors()
    id1 = Individual_Donor('John Doe', 500.05)
    gd1.add_donor(id1)
    assert 'John Doe' in gd1

def test_Group_Donors_get_Donor():
    gd1 = Group_Donors()
    id1 = Individual_Donor('John Doe', 500.05)
    gd1.add_donor(id1)
    assert 'John Doe' == gd1[0]


def test_Group_Donors_save_data():
    gd1 = Group_Donors()
    id1 = Individual_Donor('John Doe', 500.05)
    id2 = Individual_Donor('Jane Doe', 333.33)
    gd1.add_donor(id1)
    gd1.add_donor(id2)
    id1.add_dollars(1.23, donation_date='2017-03-21')
    id1.add_dollars(3.72)
    gd1.save_donor_list('temp')
    testdata = open('temp').read()
    assert testdata == f"{{'John Doe': {{'{date.today()}': [500.05, 3.72], '2017-03-21': [1.23]}}, 'Jane Doe': {{'{date.today()}': [333.33]}}}}"


def test_Group_Donors_parse_data():
    temp_str = open('temp').read()
    testdata = ast.literal_eval(temp_str)
    assert testdata == {'Jane Doe': {str(date.today()): [333.33]}, 'John Doe': {'2017-03-21': [1.23], str(date.today()): [500.05, 3.72]}}


def test_Group_Donors_load_data():
    gd1 = Group_Donors()
    gd1.load_donor_list('temp')
    testdata = {}
    for obj in gd1.donor_obj_list:
        testdata[obj.name] = obj.donations
    assert testdata == {'Jane Doe': {str(date.today()): [333.33]}, 'John Doe': {'2017-03-21': [1.23], str(date.today()): [500.05, 3.72]}}


# User interactions
# mode 1 - add a donation and send a thank you
# test input_name()
def test_input_name_list(monkeypatch):  # tests "list"
    monkeypatch.setattr('builtins.input', lambda x: "list")
    gd1 = make_group_for_testing()
    f = StringIO()
    with redirect_stdout(f):
        input_name(gd1)
    testdata = f.getvalue()
    assert testdata == "\n\nJohn Doe\nJane Doe\n\n\n"


def test_input_name_blank(monkeypatch):  # tests ""
    monkeypatch.setattr('builtins.input', lambda x: "")
    gd1 = make_group_for_testing()
    testdata = input_name(gd1)
    assert testdata == None


def test_input_name_donorname(monkeypatch):  # tests name
    monkeypatch.setattr('builtins.input', lambda x: "John")
    gd1 = make_group_for_testing()
    testdata = input_name(gd1)
    assert testdata == "John"


# test input_dollars():
def test_input_dollars_gt_0(monkeypatch):  # tests name from dict with dollars > 0
    monkeypatch.setattr('builtins.input', lambda x: "500")
    gd1 = make_group_for_testing()
    testdata = input_dollars('John Doe', gd1)
    assert testdata == 500


def test_input_dollars_error(monkeypatch):  # tests name from dict with value error
    monkeypatch.setattr('builtins.input', lambda x: "a")
    gd1 = make_group_for_testing()
    with pytest.raises(ValueError):
        testdata = input_dollars('John Doe', gd1)


def test_input_dollars_lt_1(monkeypatch):  # tests name from dict with dollars <= 0
    monkeypatch.setattr('builtins.input', lambda x: "0")
    gd1 = make_group_for_testing()
    testdata = input_dollars('John Doe', gd1)
    assert testdata == None


def test_input_dollars_gt_0_new_name(monkeypatch):  # tests new name with dollars > 0
    monkeypatch.setattr('builtins.input', lambda x: "500")
    gd1 = make_group_for_testing()
    testdata = input_dollars('JD', gd1)
    assert testdata == 500


def test_input_dollars_error_new_name(monkeypatch):  # tests new name with value error
    monkeypatch.setattr('builtins.input', lambda x: "a")
    gd1 = make_group_for_testing()
    with pytest.raises(ValueError):
        testdata = input_dollars('JD', gd1)


def test_input_dollars_lt_1_new_name(monkeypatch):  # tests new name with dollars <= 0
    monkeypatch.setattr('builtins.input', lambda x: "0")
    gd1 = make_group_for_testing()
    testdata = input_dollars('JD', gd1)
    assert testdata == None


# test thank_you():
def test_thank_you():
    f = StringIO()
    with redirect_stdout(f):
        thank_you('John', 500.00)
    testdata = f.getvalue()
    print(testdata)
    assert testdata == "Dear John,\n\nThank you for your donation of 500.00.\n\nLove,\nThe Charity Org\n"


def add_donation_to_list(obj):
    while True:
        name = input_name(obj)
        if not name:
            break
        dollars = input_dollars(name, obj)
        if name and dollars:
            thank_you(name, dollars)

def add_donation_to_list(obj):
    while True:
        name = input_name(obj)
        if not name:
            break
        dollars = input_dollars(name, obj)
        if name and dollars:
            thank_you(name, dollars)



# mode 2 - "create a report"
# test sort_by_dollars():
def test_sort_by_dollars():
    donor_lists = [['John Doe', 873.33, 3, 291.11],['Jane Doe', 3500.04, 2, 1750.02]]
    sort_by_dollars(donor_lists)
    testdata = donor_lists
    assert testdata == [['Jane Doe', 3500.04, 2, 1750.02],['John Doe', 873.33, 3, 291.11]]


# test create_donor_list():
def test_create_donor_list():
    gd1 = make_group_for_testing()
    testdata = create_donor_list(gd1)
    assert testdata == [['John Doe', 500.05, 1, 500.05], ['Jane Doe', 333.33, 1, 333.33]]


# test print_donor_report():
def test_print_donor_report():
    temp_data = [['Jane Doe', 6124.48, 2, 3062.24], ['John Doe', 1373.33, 4, 343.33]]
    f = StringIO()
    with redirect_stdout(f):
        print_donor_report(temp_data)
    testdata = f.getvalue()
    assert testdata == "\n\nDonor Name                | Total Given |   Num Gifts |  Average Gift\n---------------------------------------------------------------------\nJane Doe                          6124.48             2       3062.24\nJohn Doe                          1373.33             4        343.33\n\n\n"


# mode 3 - "send letters"
# test plural_donate():
def test_plural_donate_1():
    assert plural_donate(1) == 'donation of'


def test_plural_donate_2():
    assert plural_donate(2) == 'donations totaling'


# mode 6 - "quit"
# test end_program():
def test_end_program():
    gd1 = make_group_for_testing()
    with pytest.raises(SystemExit):
        end_program(gd1)

