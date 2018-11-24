import io
import pytest

from mailroom_lesson_09 import *

def test_show_list():
    assert True
    
def test_add_new_donor():
    c = Donor()
    c.add_donor('Andrew', 300)
    assert 'Andrew' in donors.keys()
    assert donors['Andrew'] == [300]
    
def test_add_donation_to_existing_donor():
    c = Donor()
    c.add_donor('Josh Hoff', 250)
    assert 'Josh Hoff' in donors.keys()
#NOTE: 25 and 75 are existing values for Josh Hoff
    assert donors['Josh Hoff'] == [25, 75, 250]