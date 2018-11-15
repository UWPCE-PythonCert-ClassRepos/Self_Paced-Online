#!/usr/bin/env python3
# Lesson 10, Functional Programming Mailroom unit tests

from mailroom_fp import Donor, DonationRecords
import os

def test_donor():
    d = Donor("Quincy Adams", [100, 200, 300, 400])
    assert(d.name == "Quincy Adams")
    assert(d.donations == [100, 200, 300, 400])
    assert(d.num_donations == 4)
    assert(d.total_donations == 1000)
    assert(d.avg_donation == 250)
    d.donate(500)
    assert(d.num_donations == 5)
    assert(d.total_donations == 1500)
    assert(d.avg_donation == 300)

def test_compare():
    d1 = Donor("Bob Smith", [100, 100, 200])
    d2 = Donor("John Doe", [150, 250])
    d3 = Donor("Sally Jones", [250, 250])
    assert(d1 == d2)
    assert(d3 > d1)
    assert(d2 != d3)
    
def test_donation_records():
    d1 = Donor("Bob Smith", [100, 100, 200, 300])
    d2 = Donor("John Doe", [150, 250])
    d3 = Donor("Sally Jones", [250, 250])
    dr = DonationRecords([d1, d2, d3])
    num_donors = len(dr.donors)
    assert(num_donors == 3)
    assert(dr.get_donor("John Doe") is not None)
    assert(dr.get_donor("No Name") is None)
    dr.add_donor(Donor("Bill Nye", [100]))
    num_donors = len(dr.donors)
    assert(num_donors == 4)
    report_text = dr.create_report()
    assert "Bob Smith" in report_text
    assert "175.00" in report_text        # Bob's average
    assert "700.00" in report_text        # Bob's total
    assert "Sally Jones" in report_text
    assert "250.00" in report_text        # Sally's average
    assert "Bill Nye" in report_text
    assert "100.00" in report_text        # Bill's average
    
def test_thank_all():
    d1 = Donor("Bob Smith", [100, 100, 200, 300])
    dr = DonationRecords([d1])
    dr.thank_all()
    assert os.path.isfile("Bob_Smith.txt")
    # clean up test thank you file, for cleanliness
    os.remove("Bob_Smith.txt")
    
def test_challenge():
    d1 = Donor("Bob Smith", [100, 100, 200, 300])
    assert(d1.challenge(2) == [200, 200, 400, 600])
    d2 = Donor("John Doe", [150, 250])
    assert(d2.challenge(3, min=200, max=300) == [750])
    d3 = Donor("Sally Jones", [250, 250])
    assert(d3.challenge(4, min=100, max=200) == [])
    dr = DonationRecords([d1, d2, d3])
    assert(dr.challenge(3) == 4800)
    assert(dr.challenge(2, min=200, max=500) == 2500)
    assert(dr.challenge(5, max=200) == 2750)
    
    