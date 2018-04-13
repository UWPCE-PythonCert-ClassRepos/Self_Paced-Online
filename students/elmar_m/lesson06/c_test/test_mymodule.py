#!/usr/bin/env python3

from io import StringIO
from unittest import TestCase
from unittest import main as utmain
from unittest.mock import patch
import mymodule

# import unittest

class TestURLPrint(TestCase):
# class TestURLPrint(unittest.TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
        # with unittest.patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)
            

if __name__ == '__main__':
    # unittest.main()
    utmain()
