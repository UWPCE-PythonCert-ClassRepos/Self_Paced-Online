import pytest
import os
from mailroom import *

donor_db = {'William Gates, III': [1000, 2000, 8000],
            'Mark Zuckerberg': [666],
            'Jeff Bezos': [9000, 1500],
            'Paul Allen': [16000],
            'Donald Trump': [2]}

def test_donor_names():
    assert type(donor_names()) == list
    assert len(donor_names()) >= 1
    
def test_thank_you_letter():
    assert thank_you_letter(thanks_dict = {'Stefan': 100})['Stefan'] == "Dear Stefan,\n\n\tThank you for your kind donation of $100.00.\n\n\tIt will go a long way to feed the needy. \n\n\t\tSincerely, \n\n\t\t  -The Team"

def test_send_letters():
    send_letters()
    files = os.listdir()
    new_txt_files = [f.endswith('.txt') for f in files]
    assert sum(new_txt_files) > 0

def test_create_report():
    assert create_report() == "report printed successfully"