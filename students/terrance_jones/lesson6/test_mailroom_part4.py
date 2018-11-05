
import mailroom_part4
from mailroom_part4 import donor_list
from mailroom_part4 import donor_exists
from mailroom_part4 import add_or_update_donor
from mailroom_part4 import thank_you_letter

import pytest

def test_donor_exists():
    assert donor_exists('Carlos Santos') is True
    assert donor_exists('Unknown Name') is False

def test_add_or_update_donor():
    mailroom_part4.add_or_update_donor('Carlos Santos', 10) 
    assert donor_list['Carlos Santos'] == [25,50,100,10]

    mailroom_part4.add_or_update_donor('New Donor', 100)
    assert donor_list['New Donor']==[100]

def test_thank_you_letter():
    assert thank_you_letter('Carlos Santos', 500) == "Dear Carlos Santos, \n Thank you for your $500.00 donation. \nSincerely, Mailroom."
