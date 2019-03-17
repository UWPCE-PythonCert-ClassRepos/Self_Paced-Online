#Lesson 9 Assignment 1
#Mailroom Part 5 Assignment
#Jason Virtue 03/13/2019
#UW Self Paced Python Course

"""
Unit test code for the mailroom.py
"""

#Import Mailroom package
import pytest
import mailroom as m
import os
import datetime

#Test main menu is INT
def test_donation_read():
    donors_collection = m.donation_read()
    donors_collection = {'Fred Flintstone': [100,200],'Wilma Flintstone': [300],'Bamm-Bamm Rubble': [50,30,40],'Barney Rubble' : [75],'Pebbles Flintstone': [500]}

#List out Valid donors from List function
def test_donor_list():
    donors_collection = m.donation_read()
    test_donors = ['Fred Flintstone','Wilma Flintstone','Bamm-Bamm Rubble','Barney Rubble','Pebbles Flintstone']
    donors = m.Donor_Collections.donor_list(donors_collection)
    assert donors == test_donors

#Test report from DICT{}
def test_report():
    donors_collection = m.donation_read()
    test_case = [['Pebbles Flintstone', 500.0, 1, 500.0],
        ['Fred Flintstone', 300.0, 2, 150.0],
 ['Wilma Flintstone', 300.0, 1, 300.0],
 ['Bamm-Bamm Rubble', 120.0, 3, 40.0],
 ['Barney Rubble', 75.0, 1, 75.0]]
 #['Jason', 100, 1, 100.0]]

    assert test_case == m.Donor_Collections.crunch_numbers(donors_collection)

#Test Letter names and genertion
def test_letters():
        donors_collection = m.donation_read()
        m.Donor_Collections.thanks_file(donors_collection)
        assert os.path.isfile("Fred_Flintstone.txt")
        assert os.path.isfile("Wilma_Flintstone.txt")
        assert os.path.isfile("Bamm-Bamm_Rubble.txt")
        assert os.path.isfile("Barney_Rubble.txt")
        assert os.path.isfile("Pebbles_Flintstone.txt")