#!/usr/bin/env python3
# Lesson 6, Mailroom unit tests

import mailroom as m
import os

def test_get_total():
    """
    Test the mailroom get_total function
    """
    assert m.get_total([100.05, 200.10, 300.15, 400.20]) == 1000.50
    
def test_get_avg():
    """
    Test the mailroom get_avg function
    """
    assert m.get_avg([100.05, 200.10, 300.15, 400.20]) == 250.125
    
def test_donor_functions():
    """
    Test the mailroom record_donation functionality with various additions
    """
    m.donors.clear()
    m.record_donation("Bob Smith", 100.00)
    assert "Bob Smith" in m.donors.keys()
    assert len(m.donors) == 1
    assert len(m.donors["Bob Smith"]) == 1
    assert 100.00 in m.donors["Bob Smith"]
    
    m.record_donation("Bob Smith", 200.00)
    assert len(m.donors) == 1
    assert len(m.donors["Bob Smith"]) == 2
    assert 100.00 in m.donors["Bob Smith"]
    assert 200.00 in m.donors["Bob Smith"]
    
    m.record_donation("Sally Jones", 300.33)
    assert "Sally Jones" in m.donors.keys()
    assert len(m.donors) == 2
    assert len(m.donors["Sally Jones"]) == 1
    assert 300.33 in m.donors["Sally Jones"]
    
def test_thank_all():
    """
    Test the mailroom thank_all function, which records letters to donors
    """
    m.donors.clear()
    m.record_donation("Notmy Realname", 100.00)
    m.thank_all()
    assert os.path.isfile("Notmy_Realname.txt")
    # clean up test thank you file, for cleanliness
    os.remove("Notmy_Realname.txt")
    