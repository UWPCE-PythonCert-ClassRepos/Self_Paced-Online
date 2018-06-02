from MailroomPt4 import (send_thank_you, create_report, exit_program, file_init)

import unittest
import os.path
import sys
from unittest import mock
from io import StringIO
from contextlib import contextmanager


class mailroomTest(unittest.TestCase):

    def test_exit(self):
        with self.assertRaises(SystemExit):
            exit_program()

    def test_send_thank_you(self):
        def mock_input(prompt):
            if "name" in prompt.lower():
                return 'Tom'
            if "amount" in prompt.lower():
                return 600

        @contextmanager
        def captured_output():
            new_out, new_err = StringIO(), StringIO()
            old_out, old_err = sys.stdout, sys.stderr
            try:
                sys.stdout, sys.stderr = new_out, new_err
                yield sys.stdout, sys.stderr
            finally:
                sys.stdout, sys.stderr = old_out, old_err

        with captured_output() as (out, err):
            with mock.patch('builtins.input', mock_input):
                send_thank_you()
        output = out.getvalue().strip()
        self.assertEqual(output, 'Thank you Tom for your generous donation of 600.0\n\n***File updated!***')

    def test_create_records_file(self):
        file_init()
        self.assertTrue('donors.pkl', os.path.exists('donors.pkl'))

    def test_create_report(self):
        @contextmanager
        def captured_output():
            new_out, new_err = StringIO(), StringIO()
            old_out, old_err = sys.stdout, sys.stderr
            try:
                sys.stdout, sys.stderr = new_out, new_err
                yield sys.stdout, sys.stderr
            finally:
                sys.stdout, sys.stderr = old_out, old_err

        with captured_output() as (out, err):
            create_report()
        output = out.getvalue().strip().split('\n', 1)[0]
        self.assertEqual(output, 'Donor Name |   Total Given | Num Gifts |   Average Gift')


if __name__ == '__main__':
    unittest.main()