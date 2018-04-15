#!/usr/bin/env python3

# test_utest_printfunc.py

# Test /  capture print output of a function

from io import StringIO
# from unittest import main
# from unittest import TestCase
# from unittest.mock import patch

import unittest
import unittest.mock
import printfunc 

class MeineTests(unittest.TestCase):

    def test_printfunc(self):
        expected = 'JACKSON'    # Festlegung des erwarteten Outputs
        
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_stdout:  
            # Ab obiger Zeile ist STDOUT umgebogen auf ein StringIO Objekt namens fake_stdout.
            # Jetzt muss die Original-Funktion auch noch ausgefuehrt werden, damit deren Output 
            # dann auch in diesem Objekt landet: 
            printfunc.printfunc()

            # Jetzt wird geprueft ob das was ans StringIO Objekt fake_stdout geschrieben wurde 
            # mit unserer Vorgabe 'expected' uebereinstimmt:
            self.AssertEqual(fake_stdout(getvalue(), expected))


if __name__ == '__main__':
    unittest.main()

