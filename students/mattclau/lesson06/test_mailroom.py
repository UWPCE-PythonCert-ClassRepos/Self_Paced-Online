#Test script for mailroom program for lesson 6
from operator import itemgetter
import pytest
import mailroom4
import os

#replication of starting donor list
test_donors = {"Douglas Adams":[1000],
            "Bruce Lee":[9876.55],
            "Charles Barkley":[999999.99,55555.55,7777.77],
            "Scottie Pippen":[1, 5],
            "Ursula K Le Guin":[1234567.89]
        }


def test_create_letter():
    assert mailroom4.create_letter("Charles Barkley") == 'Dear Charles Barkley,\n\tThank you for your donation of $7,777.77 to the foundation.\tWe also thank you for your continuing support and appreciate that you are a repeat giver.\tYour generous gift will make a tremendous difference in the coming years.\n\nSincerely,\n\tDirector of the Foundation\n'

def test_aggregate_donations():
    assert mailroom4.aggregate_donations(test_donors) == [['Douglas Adams', 1000, 1, 1000.0], ['Bruce Lee', 9876.55, 1, 9876.55], ['Charles Barkley', 1063333.31, 3, 354444.4366666667], ['Scottie Pippen', 6, 2, 3.0], ['Ursula K Le Guin', 1234567.89, 1, 1234567.89]]

def test_order_donations():
    assert mailroom4.order_donations(test_donors) == [['Ursula K Le Guin', 1234567.89, 1, 1234567.89], ['Charles Barkley', 1063333.31, 3, 354444.4366666667], ['Bruce Lee', 9876.55, 1, 9876.55], ['Douglas Adams', 1000, 1, 1000.0], ['Scottie Pippen', 6, 2, 3.0]]

def test_add_donation_newName():
    mailroom4.add_donation("New Person", 12456)

    assert mailroom4.create_letter("New Person") =='Dear New Person,\n\tThank you for your donation of $12,456.00 to the foundation.\tYour generous gift will make a tremendous difference in the coming years.\n\nSincerely,\n\tDirector of the Foundation\n'

def test_add_donation_oldName():
    mailroom4.add_donation("Charles Barkley", 12456)

    assert mailroom4.create_letter("Charles Barkley")== 'Dear Charles Barkley,\n\tThank you for your donation of $12,456.00 to the foundation.\tWe also thank you for your continuing support and appreciate that you are a repeat giver.\tYour generous gift will make a tremendous difference in the coming years.\n\nSincerely,\n\tDirector of the Foundation\n'

def test_export_letter():
    mailroom4.export_letter('', "Charles Barkley")
    assert os.path.isfile("Charles_Barkley.txt")

