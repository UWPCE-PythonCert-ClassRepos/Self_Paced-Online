#!/usr/bin/env python3

# from mailroom import efunc
import mailroom as m
import unittest.mock
import pytest

def test_writefile():
    content = 'This is a test\n'
    assert m.writefile('test', content) is True


def test_mail():
    assert m.mail() is True


# def test_thankyou():
    

def test_list_donors():
    # a = m.list_donors()
    # assert type(m.list_donors) is list 
    # assert m.list_donors is list 
    # assert type(a) is list 
    # assert type(a) is str
    assert m.list_donors() is True


@pytest.mark.parametrize("test_input, expected", [('johndoe', m.add_amount('johndoe') )])

# def test_add():
def test_add(test_input, expected):
    # @pytest.mark.parametrize("test_input, expected", [(1, fun1()), (2, fun2()), (3, fun3())])
    # # ---------------------------------------
    # # test_input |   1    |   2    |   3    |
    # # ---------------------------------------
    # #   expected | fun1() | fun2() | fun3() |
    # # ---------------------------------------
    # def test_my_fun(test_input, expected):
    #     assert my_fun(test_input) == expected

    assert m.add() == expected 
    # assert m.add() is True


#def test_add_amount():
#    assert m.add_amount('testdonor') is True


def test_report():
    assert m.report() is True


def test_efunc_1():
    assert m.efunc() == 'exiting'

# def test_menu():
