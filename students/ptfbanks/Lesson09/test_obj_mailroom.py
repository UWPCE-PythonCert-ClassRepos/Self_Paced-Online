#!/usr/bin/env python3
#Lesson09 Objective Mailroom test - ptfbanks

from obj_mailroom import Donor, DonorHistory
import obj_mailroom


def test_donor_name():
    John= Donor('John', 'Alexander', [100])
    assert John.full_name == 'John Alexander'
    
def test_donor_amounts():
    John= Donor('John', 'Alexander', [100])
    assert John.donations == [100]

def test_donor_add_donation():
    John= Donor('John', 'Alexander', [100])
    John.add_donation(300)
    assert John.donations == [100, 300]

def test_donor_total_donation():
    John = Donor('John', 'Alexzander', [100, 600, 200])
    assert sum == 900

def test_donation_reports():
    John = Donor('John', 'Alexzander', [100, 600, 200])
    assert John.reports == ("| John Alexander |       900.00|      3      |       300.00|")

def test_thank_you():
    John = Donor('John', 'Alexzander', [100])
    John.add_donation(500)
    output = ("Dear John Alexander,\n\t Thank you for your very kind donation(s) totaling $  600.0.\n"
                  "It will be put to very good use.\n\n\t\t Sincereley,\n")
    assert letter.format() == output
