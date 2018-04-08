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

# @pytest.fixture
# def 

# @patch(m.add_amount)  # Fail
# @unittest.mock.patch(m.add_amount)    # Fail
# @unittest.mock.patch('m.add_amount')    # Fail
# @unittest.mock.patch('add_amount')   # Fail 
def test_add():
# def test_add(mock_add_amount):
    test_names = ['berta', 'nobody']
    for name in test_names:
        with unittest.mock.patch('builtins.input') as fake_input:
            fake_input.return_value = name
            '''
            It seems to be necessary to mock / fake m.add_amount() here to return True or something
            arbitrary when running this test. Otherwise m.add_amount() will be executed 
            in real and the test will be caught in m.add_amount's while loop.

            # m.add_amount = unittest.mock.MagicMock(return_value = 'BUBU')   # OK1
            # assert m.add() == 'BUBU'                                        # OK1

            Drawback: from here on m.add_amount() is faked. If used further below from here,
            e.g. in test_add_amount(), it won't be executed in real but just represent
            the faked state.
            '''
            
            # mock_add_amount.return_value = True
            m.add_amount = unittest.mock.MagicMock(return_value = True)   # OK2
            assert m.add() is True                                        # OK2
            '''
            # This version (OK2) let test_add_amount() succeed also, but that is then only some
            # kind of 'false positive', because m.add_amount() is NOT really executed / tested
            # in test_add_amount() anymore. So, if the code of m.add_amount() would have 
            # changed to something wrong, this would not be detected my test_add_amount() 
            # anymore.

            # m.add_amount = unittest.mock.MagicMock(name)
            # assert m.add() == m.add_amount(name)

            # unittest.mock.patch(m.add_amount, return_value = 'BUBU')
            # assert m.add() == 'BUBU'                                        
            '''
            # with unittest.mock.patch('m.add_amount') as fake_am:      # Fail
            # with unittest.mock.patch('add_amount') as fake_am:          # Fail
            # with unittest.mock.patch(m.add_amount) as fake_am:      # Fail
            # with unittest.mock.MagicMock(m.add_amount, return_value = True) as fake_am:   # Fail
            # with unittest.mock.MagicMock('m.add_amount', return_value = True) as fake_am:   # Fail
            #     assert fake_am() is True

            # with m.add_amount = unittest.mock.MagicMock(return_value = True) as bla: # Fail
            #     assert m.add() is True                                        # Fail

            # with unittest.mock.patch('m.add_amount') as fake_am:      # Fail
            # with unittest.mock.patch(m.add_amount) as fake_am:        # Fail
            # with unittest.mock.MagicMock(m.add_amount, return_value = True) as fake_am:   # Fail
            # with unittest.mock.patch(add_amount) as fake_am:      # Fail
                # fake_am.return_value = True
                # assert m.add() is True


def test_add_amount():
    test_donor = 'steve'
    with unittest.mock.patch('builtins.input') as fake_input:
        # fake_input.return_value = '100'
        fake_input.return_value = '-100'    # puts you in while loop, thereby proving that
                                              # m.add_amount really is executed here
        # fake_input.return_value = 'abc'     # dito
        '''
        Note: depending on the code in test_add() above, m.add_amount might be still 
        mocked / patched at this point and return a faked return value instead of 
        being executed / tested here once again in real. 
        This can lead to misleading test results at this point!
        Possible workaround: put test_add_amount() before test_add().
        '''
        assert m.add_amount(test_donor) is True


def test_report():
    assert m.report() is True


def test_efunc_1():
    assert m.efunc() == 'exiting'

# def test_menu():
