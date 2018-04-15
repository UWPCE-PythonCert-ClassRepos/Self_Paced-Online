#!/usr/bin/env python3

'''
file: test_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson06: Mailroom Exercise Part 4/ unittesting
'''

import mailroom as m
from unittest import TestCase
from unittest import main as utmain
from unittest.mock import patch
from unittest.mock import MagicMock
from io import StringIO
import os
import sys

def test_writefile():
    content = 'This is a test\n'
    assert m.writefile('test', content) is True


def test_mail():
    assert m.mail() is True


def test_list_donors():
    assert m.list_donors() is True


class mytestclass(TestCase):
    def test_add(self):
        '''
        Test a function which expects STDIN input from users.
        Simulate several inputs by manipulating the builtin function input    
        with unittest.mock.patch(). Use the side_effect parameter to
        pass in the fake input you want to test.
        side_effect expects a list as it's argument.
        '''
        with patch('builtins.input', side_effect=['berta']) as fake_input:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                m.add_amount = MagicMock(return_value=True)
                m.add()                
                self.assertEqual(fake_output.getvalue(), '>> berta already in list\n')

        with patch('builtins.input', side_effect=['nobody']) as fake_input:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                m.add_amount = MagicMock(return_value=True)
                m.add()
                self.assertEqual(fake_output.getvalue(), '>> nobody not in list, adding it\n')


def test_add_amount():
    test_donor = 'steve'
    with patch('builtins.input') as fake_input:
        fake_input.return_value = '100'
        # fake_input.return_value = '-100'      # should put you in while loop, thereby proving that
                                              # m.add_amount really is executed here
        # fake_input.return_value = 'abc'     # dito
        '''
        Note: because of the code in mytestclass.test_add() above, m.add_amount is still 
        mocked / patched at this point and returns a faked return value instead of 
        being executed / tested here once again in real. 
        This leads to misleading test results at this point!
        Possible workaround: put test_add_amount() before mytestclass.test_add().
        '''
        assert m.add_amount(test_donor) is True


def test_report():
    assert m.report() is True


def test_efunc_1():
    assert m.efunc() == 'exiting'


if __name__ == '__main__':
    utmain()
