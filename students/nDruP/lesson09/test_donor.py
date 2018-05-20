from pytest import *
from donor import *
from donor_dict import *

#def test_donor_init():
andrew = Donor("Andrew", [12])
someone = Donor("Someone", [384.23])
people = Donor("People", [937472.909, 379.243])

def test_donor_name():
    assert andrew.name == "Andrew"
    assert someone.name == "Someone"
    assert people.name == "People"

def test_donor_history():
    assert andrew.history == [12]
    assert someone.history == [384.23]
    assert people.history == [937472.91, 379.24]

def test_donor_add_donation():
    andrew.add_gift(14)
    andrew.add_gift(24.05)
    assert andrew.history == [12, 14, 24.05]

def test_donor_sum_donation():
    assert andrew.sum_gift == 50.05
    assert someone.sum_gift == 384.23
    assert people.sum_gift == 937852.15

def test_donor_avg_donation():
    assert andrew.avg_gift == sum([12, 14, 24.05])/3
    assert someone.avg_gift == 384.23
    assert people.avg_gift == 937852.15/2

def test_donor_info():
    assert andrew.info == ("Andrew", 3, sum([12, 14, 24.05])/3, sum([12, 14, 24.05]))
    assert someone.info == ("Someone", 1, 384.23, 384.23)
    assert people.info == ("People", 2, 937852.15/2, 937852.15)

def test_challenge():
    a = andrew.challenge(2, 13, 24)
    s = someone.challenge(4)
    p = people.challenge(1.5, 0, 400)
    assert a.history == [28, 12, 24.05]
    assert s.history == [384.23*4]
    assert p.history == [379.24*1.5, 937472.91]
