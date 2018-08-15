import pytest
import os
from mailroom_class import *

def test_donor_class():
    d = Donor(name='Stefan', donations=[100,100])
    assert d.name == 'Stefan'
    
    d.new_donation(100)
    assert d.donations == [100, 100, 100]
    
    assert d.donations_sum == 300
    assert d.donations_count == 3
    assert d.donations_avg == 100

    
def test_donor_db_class():
    db = Donor_DB()
    d = Donor(name='Stefan', donations=[100,100])
    
    db.add_donor(d)
    
    assert db.display_names() == ['Stefan']
    
    db.add_donor(Donor(name='Mason', donations=[150]))
    
    assert db.donors[0] > db.donors[1]
    assert db.create_report() == "report printed successfully"
    
def test_donor_db_send_letters():
    db = Donor_DB()
    db.add_donor(Donor(name='Stefan', donations=[100,100]))
    db.add_donor(Donor(name='Mason', donations=[150]))
    db.send_letters()
    
    files = os.listdir()
    new_txt_files = [f.endswith('.txt') for f in files]
    assert sum(new_txt_files) > 0