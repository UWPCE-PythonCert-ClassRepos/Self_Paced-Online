#!/usr/bin/env python3
# Ian Letourneau
# 6/18/2018
# Test script for mailroomOO.py

import mailroomOO as m

# Test Donor object creation
LBdonations = [6578921.00, 3.50, 23400.00, 7234.00]
BGdonations = [1235544.00, 456789.50, 2347899.75]
JKdonations = [456.37, 25.67, 999876.00, 2134.78, 3.14]
d1 = m.Donor("LeBron James", LBdonations)
d2 = m.Donor("Bill Gates", BGdonations)
d3 = m.Donor("Jimmy Kimmel", JKdonations)
donors = m.DList(d1, d2, d3)


def test_donor_creation():
    assert d1.name == ("LeBron James")
    assert d1.total == (6609558.5)

# Test send_thank_you donor function


def test_send_thank_you():
    assert d1.send_thank_you(45) == ("Dear LeBron James, we wanted "
                                     "to say thank you for your generous "
                                     "donation of $45.00!")

# Test creation of donor list object


def test_list_creation():
    assert donors[0].name == ("LeBron James")

# Test create_report donor list function


def test_create_report():
    donors.create_report()
    assert donors.out_list[0] == ("LeBron James,6609603.50,5,1321920.70")

# Test send_all donor list function


def test_send_all():
    donors.send_all()


donors.display_report()
