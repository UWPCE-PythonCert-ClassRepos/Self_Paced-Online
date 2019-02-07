"""

Notes for mail room class testing:

1. Class for individual donor
    a. contains, first name, last name, donation amount
    b. method to append to donations
    c. method to send a thank you
    
2. Class for collection of donors
    a. has list of donors and sum of donotion amount
    b. method to create report
    c. method to create letters

"""

import sys
sys.path.append("C:\\Users\\Jared\\Documents\\IntroToPython\\Self_Paced-Online\\students\\jared_mulholland\\lesson_10")

import pytest
import numpy as np
import os
from mail_room_class_2 import Donor, DonorGroup

#Donor tests
#a. test donor can be created
#b. test that donation can be added to donor

def test_donor_create():
    d = Donor("Mookie Betts",1000)
    assert d.first == "Mookie"
    assert d.last == "Betts"

def test_donor_donation_append():
    d = Donor("Chris Cornell", 200)
    d.add_donation = 100
    d.add_donation = 300
    assert sum(d.donation) == 600

"""wanted to check thank_you method - after passed, changed method from return to print"""
#def test_thank_you():
#    d = Donor("Chris Cornell")
#    d.add_donation = 2000
#    note = d.thank_you
#    assert '$2,000.00' in note

#DonorGroup tests
#a. test that donor is in list of donors
    #i. input into Class is dictonary: donor, summation of donations
    #ii. getter will be created to get list of donors - check to see if name is in donor list
#b. that report can be created from class

def test_add_donor():
    """created two donors to insert into DonorGroup"""
    jared = Donor("Jared Mulholland", 10000)    
    dg = DonorGroup(jared)
    
    assert len(dg.donor_list) == 1

    """test that new donor gets correctly added to dg"""
    chris = Donor("Chris Cornell", 50000)
    dg.add_donor = chris

    assert "Chris Cornell" in dg.donor_list 

def test_create_report():
    """test that report is actually created"""
    jared = Donor("Jared Mulholland", 10000) 
    chris = Donor("Chris Cornell", 50000)

    dg = DonorGroup(jared)
    dg.add_donor = chris

    x = dg.create_report
    assert x == "report created"

def test_send_letters():
    """test that the letters are sent by checking number of files in folder after function is run"""
    jared = Donor("Jared Mulholland", 10000) 
    chris = Donor("Chris Cornell", 50000)
    ben = Donor("Ben Shepard", 4000)
    kim = Donor("Kim Thayil", 3400)

    dg = DonorGroup(jared)
    dg.add_donor = chris
    dg.add_donor = kim
    dg.add_donor = ben

    donor_count = len(dg.donor_list)

    letter_dir = "C:\\Users\\Jared\\Documents\\IntroToPython\\Self_Paced-Online\\students\\jared_mulholland\\lesson_9\\donor_letters"
    dg.send_letters = letter_dir
    assert donor_count == len(os.listdir(letter_dir))

    filelist = [f for f in os.listdir(letter_dir)]
    for f in filelist:
        os.remove(os.path.join(letter_dir, f))


"""test functions in mail room:
    1. send_thankyou()
    2. create_report(): create report tested in DonorGroup class tests
    3. send_letters(): send letters testing in DonorGroup class tests """

#def test_send_letters():
#    input = lambda input: ['Eddie Vedder', 10000]
#    assert 'Eddie' in send_thankyou()


#Lesson 10 additions
"""
1.
Add a new feature to Mailroom using map so that each donation on record can be doubled, tripled or indeed multiplied by any 
arbitrary factor based on the whims of philanthropists who would like to support our cause.

This will require a new function (or method in your donor database class) called challenge(factor) that takes a multiplier (factor), 
and multiplies all the donations of all the donors by the factor. The function returns a NEW donor database, with the new data.

2. 
Add a new feature to Mailroom using filter so that donations either above or below a specified dollar amount are included in the map operations of #1 above.
You can do this by adding min_donation and max_donation optional keyword parameters to your challenge function. You’ll want to filter the donations before 
passing them to map.
"""


def test_factor_donation():
    """tests challenge function to see if factor works correctly"""

    billy = Donor("Billy Corgan", [10,20])
    james = Donor("James Iha", [30,100])
    mark = Donor("Mark Lanegan", [50, 150, 40])

    dg_test = DonorGroup(billy)
    dg_test.add_donor = james
    dg_test.add_donor = mark
    factor = 2
    factored_amount = 800
    assert factored_amount ==  dg_test.projection(factor)


def test_factored_donation_min_max():

    factor = 2
    min_don = 11
    max_don = 99
    factored_amount = 280
    assert factored_amount == dg_test.projection(factor, min_don, max_don)









