import unittest
import mailroom4
from unittest.mock import patch
import io
import sys

donors = {  'Alice Adams Ron': [20] ,
            'Charles Cruz': [30, 50, 10]
            }
            
expected_close = '\nClosing Program\n\n'

def print_screen():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    return capturedOutput

def clear_screen():
    sys.stdout = sys.__stdout__

class TestMailRoom4(unittest.TestCase):

    def test_close_program(self):
        mailroom4.close_program(donors) == '\nClosing Program\n'

    @patch('mailroom4.input', side_effect = ["list"])
    def test_send_ty(self, mock_input):
        capture_print = print_screen()
        mailroom4.send_ty(donors)
        clear_screen()
        self.assertEqual(capture_print.getvalue(), 'Alice Adams Ron\nCharles Cruz\n')

    @patch('mailroom4.input', side_effect = [1, "Bob", 100, 'no', 4])
    def test_main(self, mock_input):
        capture_print = print_screen()
        mailroom4.main()
        clear_screen()
        expected = 'Thank you Bob for your donation of $100.00\n'
        self.assertEqual(capture_print.getvalue(), expected + expected_close)
    
    @patch('mailroom4.input')
    def test_report(self, mock_input):
        capture_print = print_screen()
        mailroom4.report(donors)
        clear_screen()
        table_contents = 'Donor Name           | Total Given   | Num Gifts     | Average Gift  |\n'
        table_contents += '----------------------------------------------------------------------\n'
        for name, donations in donors.items():
            total = sum(donations)
            num = len(donations)
            table_contents += "|{:<20}|{:>15.2f}|{:>15}|{:>15.2f}|\n".format(name, total, num, total/num)
        self.assertEqual(capture_print.getvalue(), table_contents)

    @patch('mailroom4.input', side_effect = [1])
    def test_use_input(self, mock_input):
        action = mailroom4.user_input()
        self.assertEqual(action, 1)
    
    @patch('mailroom4.input', side_effect = [5])
    def test_use_input2(self, mock_input):
        capture_print = print_screen()
        action = mailroom4.user_input()
        clear_screen()
        expected = "\nEnter 1 to 'Send a Thank You', 2 to 'Create a Report',\n3 to 'Send Letter to Everyone', or 4 to 'Quit'\n\n"
        self.assertEqual(capture_print.getvalue(), expected)

    @patch('mailroom4.input')
    def test_letters(self, mock_input):
        capture_print = print_screen()
        action = mailroom4.letters(donors)
        clear_screen()
        expected = ''
        for name, donations in donors.items():
            expected += 'Printing Letter to {a}\n'.format(a = name)
        self.assertEqual(capture_print.getvalue(), expected)

        for name, donations in donors.items():
            f = open('{a}.txt'.format(a = name))
            text = f.read()
            self.assertEqual(text, """Dear Ms./Mrs./Mr./Dr. {x}, \n
              We are thankful for your donation of ${y}.
              Your donation will be used for (insert harmful activity here).
              We hope you donate again soon!""".format(x = name,
              y = sum(donations)))
            f.close()
        
if __name__ == '__main__':
    unittest.main()
