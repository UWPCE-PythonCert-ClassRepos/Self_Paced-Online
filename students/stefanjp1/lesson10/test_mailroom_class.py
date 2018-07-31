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
    
    
def test_challenge():
    db = Donor_DB()
    db.add_donor(Donor(name='Stefan', donations=[100,200]))
    db.add_donor(Donor(name='Mason', donations=[150]))
    
    db_2 = db.challenge(2)
    
    assert db_2.donors[0].donations == [200,400]
    
    db_3 = db.challenge(2, min_donation=110)
    
    assert db_3.donors[0].donations == [400]
    
    db_4 = db.challenge(2, max_donation=110)
    
    assert db_4.donors[0].donations == [200]
    
    db_5 = db.challenge(2, min_donation = 110, max_donation=175)
    
    assert db_5.donors[0].donations == []
    assert db_5.donors[1].donations == [300]
    
def test_projection():
    db = Donor_DB()
    db.add_donor(Donor(name='Stefan', donations=[100,200]))
    db.add_donor(Donor(name='Mason', donations=[150]))
    
    assert db.run_projection(2, 110, 210) == 700