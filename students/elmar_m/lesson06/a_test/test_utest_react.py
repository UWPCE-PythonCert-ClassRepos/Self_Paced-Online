#!/usr/bin/env python3

import react as rc
import unittest
import unittest.mock
from io import StringIO
import os
import sys

def redirect_stdout():
    redirect = StringIO()
    sys.stdout = redirect
    return redirect     # redirect ist ein StringIO objekt

class MeineTests(unittest.TestCase):

    def test_reactcorrect(self):
        # with unittest.mock.patch('builtins.input', side_effect=["yes", "no"]) as fake_input:
        #     fake_input.return_value == True

        # with unittest.mock.patch('builtins.input', side_effect=['yes']) as fake_input:
        with unittest.mock.patch('builtins.input', side_effect='yes') as fake_input:
            captured_print = redirect_stdout()      # danach ist captured_print ein StringIO objekt
            print(captured_print.getvalue())
            self.assertTrue(captured_print.getvalue() == ('JAAA'))


'''    
#    def testthirdfunc(self):
#        self.assertEqual(rc.thirdfunc(8, 2), 10)
#    
#    def testfuncfive(self):
#        self.assertTrue(rc.funcfive(11))
#        self.assertFalse(rc.funcfive(9))
#    
############################################################################################


#def redirect_stdout():
#    redirect = StringIO()
#    sys.stdout = redirect
#
#    return redirect
        
#  # Test invalid input type
#         se = ['two', 1]
#         with mock.patch('builtins.input', side_effect=se) as mock_input:
#             captured_print = redirect_stdout()
#             mr.get_usr_input()
#             reset_stdout()
# 
#             self.assertTrue(captured_print.getvalue() == (f'\nPlease try again. '
#                                                           f'Valid options are: '
#                                                           f'{mr.PROMPT_OPTS}\n'))
# 
'''

if __name__ == '__main__':
    unittest.main()

