#!/usr/bin/env python
from io import StringIO
import sys
from contextlib import redirect_stdout
import pytest


# test input_name():
from  mailroom3 import input_name
def test_1(monkeypatch):  # tests "list"
    monkeypatch.setattr('builtins.input', lambda x: "list")
    f = StringIO()
    with redirect_stdout(f):
        input_name()
    testdata = f.getvalue()
    assert testdata == "\n\nJohn Doe\nJane Doe\nJohn Smith\nJane Smith\nBilly Jo Jones\n\n\n"

def test_2(monkeypatch):  # tests ""
    monkeypatch.setattr('builtins.input', lambda x: "")
    testdata = input_name()
    assert testdata == None

def test_3(monkeypatch):  # tests name
    monkeypatch.setattr('builtins.input', lambda x: "John")
    testdata = input_name()
    assert testdata == "John"


#test input_dollars():
from  mailroom3 import input_dollars
def test_4(monkeypatch):  # tests name from dict with dollars > 0
    monkeypatch.setattr('builtins.input', lambda x: "500")
    testdata = input_dollars('John Doe')
    assert testdata == 1

def test_5(monkeypatch):  # tests name from dict with value error
    monkeypatch.setattr('builtins.input', lambda x: "a")
    with pytest.raises(ValueError):
        testdata = input_dollars('John Doe')

def test_6(monkeypatch):  # tests name from dict with dollars <= 0
    monkeypatch.setattr('builtins.input', lambda x: "0")
    testdata = input_dollars('John Doe')
    assert testdata == None

def test_7(monkeypatch):  # tests new name with dollars > 0
    monkeypatch.setattr('builtins.input', lambda x: "500")
    testdata = input_dollars('JD')
    assert testdata == 1

def test_8(monkeypatch):  # tests new name with value error
    monkeypatch.setattr('builtins.input', lambda x: "a")
    with pytest.raises(ValueError):
        testdata = input_dollars('JD')

def test_9(monkeypatch):  # tests new name with dollars <= 0
    monkeypatch.setattr('builtins.input', lambda x: "0")
    testdata = input_dollars('JD')
    assert testdata == None


#test sort_by_dollars():
from mailroom3 import sort_by_dollars
def test_11():
    donor_lists = [['John Doe', 873.33],['Jane Doe', 3500.04]]
    sort_by_dollars(donor_lists)
    testdata = donor_lists
    assert testdata == [['Jane Doe', 3500.04],['John Doe', 873.33]]


#test create_donor_list():
from mailroom3 import create_donor_list
def test_12():
    testdata = create_donor_list()
    assert testdata == [['Jane Doe', 6124.48], ['John Doe', 1373.33], ['JD', 500], ['John Smith', 462.53], ['Billy Jo Jones', 300.00], ['Jane Smith', 2.00]]


#test def create_gift_list():
from mailroom3 import create_gift_list
def test_13():
    temp_donor_lists = create_donor_list()
    testdata = create_gift_list(temp_donor_lists)
    assert testdata == [['Jane Doe', 6124.48, 2, 3062.24], ['John Doe', 1373.33, 4, 343.33], ['JD', 500.00, 1, 500.00], ['John Smith', 462.53, 3, 154.18], ['Billy Jo Jones', 300.00, 3, 100.00], ['Jane Smith', 2.00, 1, 2.00]]


#test print_donor_report():
from mailroom3 import print_donor_report
def test_14():
    temp_data = [['Jane Doe', 6124.48, 2, 3062.24], ['John Doe', 1373.33, 4, 343.33]]
    f = StringIO()
    with redirect_stdout(f):
        print_donor_report(temp_data)
    testdata = f.getvalue()
    assert testdata == "\n\nDonor Name                | Total Given |   Num Gifts |  Average Gift\n---------------------------------------------------------------------\nJane Doe                          6124.48             2       3062.24\nJohn Doe                          1373.33             4        343.33\n\n\n"


#test plural_donate():
from mailroom3 import plural_donate
def test_15():
    assert plural_donate(1) == 'donation of'

def test_16():
    assert plural_donate(2) == 'donations totaling'


#test total_donate():
from mailroom3 import total_donate
def test_17():
    assert total_donate([120.00, 353.33, 400.00]) == 873.33

def test_18():
    assert total_donate([1, 100.00]) == 101.00


#test end_program():
from mailroom3 import end_program
def test_19():
    with pytest.raises(SystemExit):
        end_program()


