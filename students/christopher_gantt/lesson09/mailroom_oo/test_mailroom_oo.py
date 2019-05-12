#!/usr/bin/env pYThon3

"""Testing for OO Mailroom and Modules"""

from donor_models import Donor, DonorCollection
from cli_main import DONOR_DB


def test_donor_init():
    c = Donor("Chris Gantt")
    assert c.name == "Chris Gantt"
    assert c.donations == []
    j = Donor("john jacob")
    assert j.name == "John Jacob"


def test_donor_add_donation():
    c = Donor("Chris Gantt")
    c.add_donation(12345.67)
    assert c.donations[0] == 12345.67
    c.add_donation(9876.54)
    assert c.donations == [12345.67, 9876.54]


def create_test_donor():
    c = Donor("Chris")
    c.add_donation(12345.67)
    c.add_donation(9876.54)
    return c


def test_donor_str_repr():
    c = create_test_donor()
    assert str(c) == "Name: Chris\nDonations: [12345.67, 9876.54]"
    assert repr(c) == "Donor('Chris')"


def test_donor_number_of_donations():
    c = create_test_donor()
    assert c.number_of_donations == 2
    c.add_donation(1)
    assert c.number_of_donations == 3


def test_donor_sum_donations():
    c = create_test_donor()
    assert c.sum_donations == 22222.21
    c.add_donation(1)
    assert c.sum_donations == 22223.21


def test_donor_thank_you_letter():
    c = create_test_donor()
    thanks = "".join(('\nDear Chris,\n\n\tThank you for your donation of $9876.54.',
                      '\n\n\t\tSincerely,\n\t\t-The Mailroom'))
    assert c.thank_you_letter() == thanks


def test_donorcollection_init():
    a = Donor("Abe")
    b = Donor("Bob")
    c = Donor("Chris")
    collection = DonorCollection(a, b, c)
    assert collection.donors == [a, b, c]


def test_donorcollection_add_donor():
    a = Donor("Abe")
    collection = DonorCollection(a)
    d = Donor("Dan")
    collection.add_donor(d)
    assert collection.donors == [a, d]


def test_get_donor():
    assert DONOR_DB.get_donor("Wassily Kandinsky") == DONOR_DB.donors[0]
    assert DONOR_DB.get_donor("Yves Tanguy") == DONOR_DB.donors[-1]


def test_generate_report():
    report = "\n".join(["Donor Name                | Total Given | Num Gifts | Average Gift",
                        "------------------------------------------------------------------",
                        "Richard Serra              $  1475665.99          3  $   491888.66",
                        "Mark Rothko                $   135353.33          1  $   135353.33",
                        "Wassily Kandinsky          $    45987.47          3  $    15329.16",
                        "Yves Tanguy                $     4076.42          2  $     2038.21",
                        "Jasper Johns               $     3287.77          2  $     1643.88"])
    assert DONOR_DB.generate_report() == report


def test_generate_name_list():
    names = ["Wassily Kandinsky",
             "Jasper Johns",
             "Mark Rothko",
             "Richard Serra",
             "Yves Tanguy"]
    assert DONOR_DB.generate_name_list() == names
