"""
test code for donor_models.py

"""

import pytest
import math
from random import shuffle

from donor_models import *
from cli_main import *

def test_donor_init():
    d1 = Donor('Mark','Luckeroth',1000.)
    assert d1.first_name == 'Mark'
    assert d1.last_name == 'Luckeroth'
    assert d1.donations == [1000.]
    d2 = Donor('Raja','Koduri',[60., 60000.])
    assert d2.first_name == 'Raja'
    assert d2.last_name == 'Koduri'
    assert d2.donations == [60., 60000.]

def test_donor_add_donation():
    d = Donor('Mark','Luckeroth',1000.)
    d.add_donation(2000.)
    d.add_donation(3000.)
    assert d.donations == [1000., 2000., 3000.]
    assert d.total == 6000.
    assert d.count == 3
    assert d.average == 2000.

def test_DonorCollection():
    c = DonorCollection()
    assert c.donorlist == None
    c.add_donor('Mark','Luckeroth',1000.)
    c.add_donor('Raja','Koduri',2000.)
    assert c.donorlist[0].first_name == 'Mark'
    assert c.donorlist[1].last_name == 'Koduri'

def test_save():
    c = DonorCollection()
    c.add_donor('Peter','Pan',10.)
    c.add_donor('Paul','Hollywood',5.)
    c.add_donor('Mary','Berry',100.)
    c.add_donor('Jake','Turtle',123.)
    c.add_donor('Raja','Koduri',60.)
    c.donorlist[0].add_donation([10., 10., 10.])
    c.donorlist[1].add_donation([5000., 5., 5.])
    c.donorlist[3].add_donation([456., 789.])
    c.donorlist[4].add_donation(60000.)
    c.save_donors()
    expected = ['Peter;Pan;10.0,10.0,10.0,10.0\n',
                'Paul;Hollywood;5.0,5000.0,5.0,5.0\n',
                'Mary;Berry;100.0\n',
                'Jake;Turtle;123.0,456.0,789.0\n',
                'Raja;Koduri;60.0,60000.0\n']
    with open('donor_list.txt', 'r') as f:
        for i, line in enumerate(f):
            assert line == expected[i]

def test_load():
    c = DonorCollection()
    c.load_donors()
    assert c.donorlist[0].first_name == 'Peter'
    assert c.donorlist[1].last_name == 'Hollywood'
    assert c.donorlist[2].donations == [100.]
    assert c.donorlist[3].last_name == 'Turtle'
    assert c.donorlist[4].last_name == 'Koduri'

def test_names():
    c = DonorCollection()
    c.load_donors()
    expected = [('Pan', 'Peter'), ('Hollywood', 'Paul'), ('Berry', 'Mary'),
                ('Turtle', 'Jake'), ('Koduri', 'Raja')]
    for i, name in enumerate(c.names):
        assert name == expected[i]

def test_find():
    c = DonorCollection()
    c.load_donors()
    assert c.find('Peter','Pan') is c.donorlist[0]
    assert c.find('Paul','Hollywood') is c.donorlist[1]
    assert c.find('Mark','Luckeroth') == False

def test_update():
    c = DonorCollection()
    c.load_donors()
    c.update('Mark','Luckeroth', 1000.)
    c.update('Peter','Pan', 1000.)
    assert c.donorlist[5].first_name == 'Mark'
    assert c.donorlist[5].last_name == 'Luckeroth'
    assert c.donorlist[5].donations == [1000.]
    assert c.donorlist[0].donations == [10., 10., 10., 10., 1000.]
