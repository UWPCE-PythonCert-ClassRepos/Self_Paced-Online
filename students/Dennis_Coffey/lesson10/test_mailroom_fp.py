# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:48:02 2018

@author: dennis
"""

import os
import pytest
from mailroom_fp import *

# Test create report
def test_create_report():
    assert donors.create_report() == f'\nDonor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------\n\
Paul Allen                 $    54000.00           2  $   27000.00\n\
Dennis Coffey              $     4300.00           3  $    1433.33\n\
Ethan Coffey               $     2050.00           3  $     683.33\n\
Bill Gates                 $      770.00           2  $     385.00\n\
Jeff Bezos                 $        3.00           1  $       3.00\n'
    
# Test add_donation by adding donation to existing donor
def test_add_donation_existing_donor(donor='Dennis Coffey', amount=5000.00):
    donor = donors.set_donor(donor)
    donor.add_donation(amount)
    assert donor.donations == [2500.00,400.00,1400.00,amount]

# Test add_donation by adding donation from new donor
def test_add_donation_new_donor(new_donor='Bill Nye', amount=777.00):
    donor = donors.set_donor(new_donor)
    donor.add_donation(amount)
#    donorlist = donors.donor_list
#    assert new_donor in str(donorlist) == True
    assert donor.donations == [amount]
    
# Test create email output
def test_create_email(donor='Tyler Coffey', amount=999):
    donor = donors.set_donor(donor)
    email_result = donor.create_email(amount)
    expected_result = '\nDear Tyler Coffey,\n\nThank you so much for generous donation of $999.\n\n\t\t\tSincerely,\n\t\t\tPython Donation Team'
    # Check email matches the expected result
    assert email_result == expected_result

# Test send email function
def test_send_email():
    donors.send_letters()
    path = os.getcwd()
    # Number of emails sent (files in directory)
    num_files = sum([len(files) for r, d, files in os.walk(path)])
    # Number of donors in dictionary
    num_donors = len(donors.donors)
    # Check that number of emails in directory equals number of donors sent emails
    assert num_donors == num_files
    
# Test multiply donations function
def test_multiply_donations(factor=3):
    donor = donors.set_donor('Ethan Coffey')
    d = donor.multiply_donations(int(factor))
    assert d == [2400.00,450.00,3300.00]
    
# Test filter donations function
def test_filter_donations(min_donation=200, max_donation=5000):
    donor = Donor('Bill Nye', [2500.00,400.00,1400.00, 5.00])
    d = donor.filter_donations(min_donation, max_donation)
    assert d == [2500.00,400.00,1400.00]
    
    
    