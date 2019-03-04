#Lesson 6 Assignment 1
#Mailroom Part 4 Assignment
#Jason Virtue 03/02/2019
#UW Self Paced Python Course

"""
Unit test code for the mailroom_ut.py
"""

#Import Mailroom package
import pytest
import mailroom_ut as m
import os
import datetime

#Test main menu is INT
test_donor_db = {'Fred Flintstone': [100,200],'Wilma Flintstone': [300],'Bamm-Bamm Rubble': [50,30,40],'Barney Rubble' : [75],'Pebbles Flintstone': [500]}

#List out Valid donors from List function
def test_donor_list():
    test_donors = ['Fred Flintstone','Wilma Flintstone','Bamm-Bamm Rubble','Barney Rubble','Pebbles Flintstone']
    donors = m.donor_list(test_donor_db)
    assert donors == test_donors

#Inputs correct amount into donors_db dict{}
def test_donor_amount():
    amount = m.amount_add('Jason', 100, test_donor_db)
    assert 'Jason' in test_donor_db
    assert test_donor_db['Jason'][-1] == 100

def test_report():
    test_case = [['Fred Flintstone', 300, 2, 150.0],
 ['Wilma Flintstone', 300, 1, 300.0],
 ['Bamm-Bamm Rubble', 120, 3, 40.0],
 ['Barney Rubble', 75, 1, 75.0],
 ['Pebbles Flintstone', 500, 1, 500.0],
 ['Jason', 100, 1, 100.0]]

    assert test_case == m.crunch_numbers(test_donor_db)

def test_letters():
        m.thanks_file(test_donor_db)
        assert os.path.isfile("Fred_Flintstone.txt")
        assert os.path.isfile("Wilma_Flintstone.txt")
        assert os.path.isfile("Bamm-Bamm_Rubble.txt")
        assert os.path.isfile("Barney_Rubble.txt")
        assert os.path.isfile("Pebbles_Flintstone.txt")
        assert os.path.isfile("Jason.txt")