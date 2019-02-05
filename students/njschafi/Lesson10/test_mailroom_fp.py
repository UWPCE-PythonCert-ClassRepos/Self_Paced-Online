"""test code for lesson 10 mailroom"""
# NEIMA SCHAFI, LESSON 10 Assignment test code

import pytest
import os
from mailroom_fp import Donors, Donor


def test_init():
    """
    This tests the creation of instance for both the Donor and
    Donors classes.
    """
    d = Donor("Horse Malone")
    d = Donors()


def test_name():
    """
    For Donor Class Object:
    Tests that correct donor name returns when Donor class Function
    is called.
    """
    d = Donor("Horse Malone")
    assert(d.name == "Horse Malone")


def test_donationlist():
    """
    For Donor Class Object:
    Tests historical donation list outputs correct data.
    """
    d = Donor("Horse Malone")
    d.add_donation(50)
    d.add_donation(100.78)
    d.add_donation(99.99)
    assert(d.donationlist == [50.00, 100.78, 99.99])


def test_amount():
    """
    For Donor Class Object:
    Tests sum total of donationlist is correct based on previous
    donations.
    """
    d = Donor("Horse Malone")
    d.add_donation(50)
    d.add_donation(100.78)
    d.add_donation(99.99)
    assert(d.amount == 250.77)


def test_total():
    """
    For Donor Class Object:
    Tests how many donations were given by donor.
    """
    d = Donor("Horse Malone")
    d.add_donation(50)
    d.add_donation(100.78)
    d.add_donation(99.99)
    assert(d.total == 3)


def test_initlist():
    """
    For Donor Class Object:
    Tests setting an initial donation list.
    """
    d = Donor("Horse Malone")
    d.initlist([50, 90.78, 100])
    assert(d.donationlist == [50, 90.78, 100])


def test_average():
    """
    For Donor Class Object:
    Tests class function "average" for correct output.
    """
    d = Donor("Horse Malone")
    d.add_donation(50)
    d.add_donation(100.78)
    d.add_donation(99.99)
    assert(d.average == 83.59)


def test_add_donation():
    """
    For Donor Class Object:
    Tests that a new donation gets added to donors donation list.
    """
    d = Donor("Horse")
    assert(d.donationlist == [])
    d.add_donation(50)
    assert(d.donationlist == [50])
    d.add_donation(100.78)
    assert(d.donationlist == [50.00, 100.78])


def test_email():
    """
    For Donor Class Object:
    Tests class function "average" for correct output.
    """
    d = Donor("Horse Malone")
    d.add_donation(50)
    assert(d.email(50) == ('\nDear Horse Malone, '
                        '\n\tThank you for your generous $50.00 donation.'
                        '\n\tYou are an amazing person. Good job!'))


def test_list_names(capfd):
    """
    For Donors Class Object:
    Tests for the correct list of names from Donors list.
    """
    d = Donors()
    d.list_names()
    out, err = capfd.readouterr()
    assert out == ('List of Donors\n'
                                '--------------\n'
                                'Leon Dechino\n'
                                'Michael Scarn\n'
                                'Lamar Dankers\n'
                                'Horse Malone\n'
                                'Rupert Everton\n\n')


def test_add_donor():
    """
    For Donors Class Object:
    Tests that a new donor gets added to the donors names list.
    """
    c = Donor('Post Malone')
    d = Donors()
    d.add_donor(c)
    assert(c in d.donors)


def test_write_email():
    """
    For Donors Class Object:
    Tests to see if a txt file email is written for specific donor.
    """
    d = Donors()
    d.donors[0].write_email()
    assert os.path.isfile('Leon_Dechino.txt')


def test_send_all():
    """
    For Donors Class Object:
    Tests to see if a txt file email is written for each donor.
    """
    d = Donors()
    d.send_all()
    assert os.path.isfile('Leon_Dechino.txt')
    assert os.path.isfile('Michael_Scarn.txt')
    assert os.path.isfile('Lamar_Dankers.txt')
    assert os.path.isfile('Horse_Malone.txt')
    assert os.path.isfile('Rupert_Everton.txt')

    # Add Donor and check again
    c = Donor('Post Malone')
    d.add_donor(c)
    d.send_all()
    assert os.path.isfile('Leon_Dechino.txt')
    assert os.path.isfile('Michael_Scarn.txt')
    assert os.path.isfile('Lamar_Dankers.txt')
    assert os.path.isfile('Horse_Malone.txt')
    assert os.path.isfile('Rupert_Everton.txt')
    assert os.path.isfile('Post_Malone.txt')

def test_multiply():
    pass

def test_projection():
    pass

def test_alldonations():
    d = Donors()
    assert(d.all_donations()== 1882.83)
