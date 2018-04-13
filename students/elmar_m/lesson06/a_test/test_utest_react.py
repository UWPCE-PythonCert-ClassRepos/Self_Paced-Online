#!/usr/bin/env python3

import react as rc
from unittest import TestCase
from unittest import main as utmain
from unittest.mock import patch
from io import StringIO
import os
import sys


class MeineTests(TestCase):
    def test_simple(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            rc.simple()
            self.assertEqual(fake_output.getvalue(), 'simple\n')

    def test_reactcorrect(self):
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


if __name__ == '__main__':
    utmain()

