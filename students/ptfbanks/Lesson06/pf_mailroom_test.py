#!/usr/bin/env python3
#unit testing exercise- lesson06

import unittest
import os
import sys
from io import StringIO

from pf_mailroom4 import d_dict, letter, send_where, new_don, add_new, hist_rpt, thank_you

n_name = 'New Mann'
amt_1 = 1000.00
amt_2 = 4000.00

class MyTestCase(unittest.TestCase):

    def test_1(self):  # Tests donors and donations
        self.assertEqual(['Bob Williams', 'Tom Haskell', 'Earl Jackson',
                          'Les Thomas', 'James Black', 'Ed Jones'], list(d_dict.keys()))
        self.assertTrue(d_dict['Bob Williams'] == [5580.00, 3245.50, 1000])
        print("End Test 1---------------------------------------------")
        
        
    def test_2(self):  # Tests add donors and donations             
        d_dict[n_name]=[float(amt_1)]
#        print(d_dict)  #Diagnostic insert
        self.assertTrue(d_dict['New Mann'] == [1000.0])
        print("End Test 2---------------------------------------------")
       
    def test_3(self):  # Tests add donation            
        d_dict[n_name].append(float(amt_2))
#        print(d_dict)    #Diagnostic insert
        self.assertTrue(d_dict['New Mann'] == [1000.0, 4000.0])
        print("End Test 3---------------------------------------------")        
        
    def test_4(self):# Confirm letter is properly prepared
        amt = sum(d_dict[n_name])
        output = ("Dear New Mann,\n\t Thank you for your very kind donation(s) totaling $ 5000.0.\n"
                  "It will be put to very good use.\n\n\t\t Sincereley,\n"
                  "\t\t   -The Team")
#        print(n_name, amt, "\n",output)      #Diagnostic insert
#        print (letter.format(n_name, amt))   #Diagnostic insert
        self.assertTrue(letter.format(n_name, amt) == output)
        print("End Test 4---------------------------------------------")        
        
    def test_5(self): # Confirm .txt file is generated
        send_where (n_name, 'y', "")
        assert os.path.isfile('New Mann.txt')
        print("End Test 5---------------------------------------------")        
       
if __name__ == '__main__':
    unittest.main()