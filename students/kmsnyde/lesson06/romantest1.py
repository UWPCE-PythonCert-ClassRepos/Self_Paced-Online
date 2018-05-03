# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:57:20 2018

@author: Karl M. Snyder
"""

import roman1
import unittest

class KnownValues(unittest.TestCase):
    #for test case, subclass TestCase of unittest module
    know_values = ((1, 'I'),
                   (2, 'II'),
                   (3, 'III'),
                   (4, 'IV'),
                   (5, 'V'),
                   (6, 'VI'),
                   (7, 'VII'),
                   (8, 'VIII'),
                   (9, 'IX'),
                   (10, 'X'),
                   (50, 'L'),
                   (100, 'C'),
                   (500, 'D'),
                   (1000, 'M'),
                   (31, 'XXXI'),
                   (148, 'CXLVII'),
                   (294, 'CCXCIV'),
                   (312, 'CCCXII'),
                   (421, 'CDXXI'),
                   (528, 'DXXVII'),
                   (621, 'DCXXI'),
                   (782, 'DCCLXXXII'),
                   (870, 'DCCCLXX'),
                   (941, 'CMXLI'),
                   (1043, 'MXLII'),
                   (1110, 'MCX'),
                   (1226, 'MCCXXVI'),
                   (1301, 'MCCI'),
                   (1485, 'MCDLXXXV'),
                   (1509, 'MDIX'),
                   (1607, 'MDCVII'),
                   (1754, 'MDCCLIV'),
                   (1832, 'MDCCCXXXII'),
                   (1993, 'MCMXCII'),
                   (2074, 'MMLXXIV'),
                   (2152, 'MMCLII'),
                   (2212, 'MMCCXII'),
                   (2343, 'MMCCCXLII'),
                   (2499, 'MMCDXCIX'),
                   (2574, 'MMDLXXIV'),
                   (2646, 'MMDCXLVI'),
                   (2723, 'MMDCCXXIII'),
                   (2892, 'MMDCCCXCII'),
                   (2975, 'MMCMLXXV'),
                   (3051, 'MMMLI'),
                   (3185, 'MMMCLXXXV'),
                   (3250, 'MMMCCL'),
                   (3313, 'MMMCCCXII'),
                   (3408, 'MMMCDVII'),
                   (3501, 'MMMDI'),
                   (3610, 'MMMDCX'),
                   (3743, 'MMMDCCXLIII'),
                   (3844, 'MMMDCCCXLIV'),
                   (3888, 'MMMDCCCLXXXVIII'),
                   (3940, 'MMMCMXL'),
                   (3999, 'MMMCMXCIX'))
 
#Each test is its own method
#it takes no params, returns no value, and name must begin with "test"
#if test exits normally, no result; else, raises an exception and failed
def test_to_roman_known_values(self):
    '''to_roman should give known result with known input'''
    for integer, numeral in self.known_values:
        #call to_roman func; defines its argument as integer
        result = roman1.to_roman(integer)
        #check if conversion is correct; no output if correct
        self.assertEqual(numeral, result)
        
if __name__ == '__main__':
    unittest.main()
    