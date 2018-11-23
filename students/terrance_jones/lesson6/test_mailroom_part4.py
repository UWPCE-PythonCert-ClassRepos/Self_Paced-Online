
import mailroom_part4
from mailroom_part4 import donor_list
from mailroom_part4 import donor_exists
from mailroom_part4 import add_or_update_donor
from mailroom_part4 import thank_you_letter
from mailroom_part4 import letter
from mailroom_part4 import letters_everyone
from mailroom_part4 import get_report


import pytest
import os

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


def test_letters_everyone():
    """Test creation of files"""
    letters_everyone()
    assert os.path.isfile('Carlos Santos.txt')
    assert os.path.isfile('Esperanza Gomez.txt')
    assert os.path.isfile('Paul Jackson.txt')
    assert os.path.isfile('Karl Black.txt')
    assert os.path.isfile('Charles Exx.txt')
    
def test_letters_everyone_2():
    """Test the content of the letter"""
    expected = '''Dear Esperanza Gomez,\n
    \tThank you for your most recent donation of $30.00.
    \tYour total support of $60.00 has been used to assist many people.\n
    Thank you,\n
    -The Mailroom'''

    assert letter('Esperanza Gomez') == expected


    def test_get_report():
        donor_list = {'Jay Jones': [2,2,2]}
        expected = "{:<25} ${:^10} {:^10} ${:^10}".format('Jay Jones', 6, 3, 2)
        assert get_report(donor_list) == expected





