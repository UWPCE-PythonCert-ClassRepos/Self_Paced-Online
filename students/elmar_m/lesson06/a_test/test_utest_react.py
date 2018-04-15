#!/usr/bin/env python3

import react as rc
from unittest import TestCase
from unittest import main as utmain
from unittest.mock import patch
from unittest.mock import MagicMock
from io import StringIO
import os
import sys


class MeineTests(TestCase):
    '''
    Test a function which prints to STDOUT. 
    Catch the print output into a StringIO object and compare to
    a certain value.
    '''
    def test_simple(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            rc.simple()
            self.assertEqual(fake_output.getvalue(), 'simple\n')

    def test_reactcorrect(self):
    '''
    Test a function which expects STDIN input from users.
    Simulate several inputs by manipulating the builtin function input    
    with unittest.mock.patch(). Use the side_effect parameter to
    pass in the fake input you want to test.
    side_effect expects a list as it's argument.
    '''
        # se = ['yes', 'yes']
        # se = ['yes', 'no']
        # se = ['no', 'yes']
        with patch('builtins.input', side_effect=['yes']) as fake_input:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                rc.react_correct()
                self.assertEqual(fake_output.getvalue(), 'JAAA\n')

        with patch('builtins.input', side_effect=['no']) as fake_input:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                rc.react_correct()
                self.assertEqual(fake_output.getvalue(), 'NOOO\n')

    def test_funcsix(self):
    '''
    Test a function which should return / call another function, 
    but without really executing this second function during the test.
    '''
        rc.funcseven = MagicMock(return_value=True)
        rc.funcsix()
        # self.assertTrue(mock_fourth.called)
        assert rc.funcseven.called 
        
    


if __name__ == '__main__':
    utmain()

