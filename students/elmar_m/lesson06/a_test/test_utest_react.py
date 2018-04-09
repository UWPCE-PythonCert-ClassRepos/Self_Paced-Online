#!/usr/bin/env python3

import react as rc
import unittest


class MeineTests(unittest.TestCase):
    
    def testthirdfunc(self):
        self.assertEqual(rc.thirdfunc(8, 2), 10)
    
    def testfuncfive(self):
        self.assertTrue(rc.funcfive(11))
        self.assertFalse(rc.funcfive(9))
    

if __name__ == '__main__':
    unittest.main()

