#!/usr/bin/env python3

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
    assert m.list_donors() is True


# @pytest.mark.parametrize("test_input, expected", [('johndoe', m.add_amount('johndoe') )])
# def test_add(test_input, expected):
#    # @pytest.mark.parametrize("test_input, expected", [(1, fun1()), (2, fun2()), (3, fun3())])
#    # # ---------------------------------------
#    # # test_input |   1    |   2    |   3    |
#    # # ---------------------------------------
#    # #   expected | fun1() | fun2() | fun3() |
#    # # ---------------------------------------
#    # def test_my_fun(test_input, expected):
#    #     assert my_fun(test_input) == expected
# 
#     assert m.add() == expected 
    # assert m.add() is True


# def test_add():
#     # action_result= {'yes' : 'BUBU', 'no' : 'NOOO', 'wiwiwi' : 'BULLSHIT' }
#     test_names = ['berta', 'nobody']
#     # for key in action_result:
#     for name in test_names:
#         with unittest.mock.patch('builtins.input') as fake_input:
#             # fake_input.return_value = key 
#             fake_input.return_value = name
#             # if key == 'yes':
#             if name == 'berta':
#                 # r.secondfunc = unittest.mock.MagicMock(return_value = 'BUBU') 
#                 m.add_amount(name) = unittest.mock.MagicMock(return_value = 'BUBU')
#                 # assert r.react_correct() == action_result[key]
#                 assert m.add() == action_result[key]
#             else:
#                 assert r.react_correct() == action_result[key]


def test_add():
    test_names = ['berta', 'nobody']
    for name in test_names:
        with unittest.mock.patch('builtins.input') as fake_input:
            '''
            Mocking m.add_amount to return True or something arbitrary prevents it from
            actually being executed when running this test. Executing it would result
            in being caught in m.add_amount's while loop (until i find out how 
            to use this 'side_effect' parameter of mock.patch ...:)
            '''
            m.add_amount = unittest.mock.MagicMock(return_value = 'BUBU')
            # m.add_amount = unittest.mock.MagicMock(return_value = True)
            fake_input.return_value = name
            assert m.add() is True


def test_add_amount():
    test_donor = 'berta'
    with unittest.mock.patch('builtins.input') as fake_input:
        fake_input.return_value = '100'
        '''
        Note: m.add_amount is still mocked / patched to return the faked return_value 
        from the stanza above !!
        '''
        assert m.add_amount(test_donor) is True


def test_report():
    assert m.report() is True


def test_efunc_1():
    assert m.efunc() == 'exiting'

# def test_menu():
