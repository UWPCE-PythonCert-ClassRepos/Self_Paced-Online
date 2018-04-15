#!/usr/bin/env python3

from io import StringIO
import unittest
import unittest.mock

# from unittest import TestCase
# from unittest.mock import patch

import mymodule

# class TestURLPrint(unittest.TestCase):
class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)
        
        self.AssertTrue(mymodule.urlprint()) 

        # with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_out:
        #     mymodule.urlprint(protocol, host, domain)
        #     self.AssertEqual(fake_out.getvalue(), expected_url) 


if __name__ == '__main__':
    unittest.main()
