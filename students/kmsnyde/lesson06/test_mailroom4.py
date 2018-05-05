# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 13:19:54 2018

@author: Karl M. Snyder
"""

"""
Define tests that will work againsts mailroom4.py.
"""

import mailroom4 as mail
import os.path

def test_1():
    donors = mail.donor_dict
    assert "Karl Stick" in donors
    
#IPython will display "Donor Amount:", input same as below for pass, or diff
# to fail
def test_2():
    assert mail.donations() == 50.00


#In IPython promp after Donor Amount: from above test, type "May West" and then any number.
#If you type May West, no error; else AssertionError
def test_3():
    mail.send_thanks()
    assert "May West" in mail.donor_dict
    
def test_4():
    mail.send_letters_all()
    assert os.path.isfile("Thank_You - karl_stick.txt")

    
if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()