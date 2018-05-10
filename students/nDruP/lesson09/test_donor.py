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

#def test_donor_dict_init():
d = Donor_Dict(andrew, someone, people)

def test_donor_dict_names():
    assert d.names == ["Andrew", "Someone", "People"]

def test_donor_dict_avgs():
    assert d.avgs == [sum([12, 14, 24.05])/3, 384.23, 937852.15/2]

def test_donor_dict_sums():
    assert d.sums == [50.05, 384.23, 937852.15]

def test_donor_dict_add():
    d.add_donor("me", [8000])
    d.add_donor("you", [7000, 2000])
    assert "me" in d.names
    assert "you" in d.names

def test_donor_info():
    assert d.donor_info("me") == ("me", [8000], 8000.0, 8000)
    assert d.donor_info("you") == ("you", [7000, 2000], 4500.0, 9000)


e = Donor_Dict(Donor("blah", [100]))
e.add_donor("some", [1, 2, 3])
e.add_donor("be", [3, 4])
def test_all_donor_info():
    assert e.all_donor_info() == [("blah", [100], 100.0, 100), ("some", [1, 2, 3], 2.0, 6), ("be", [3, 4], 3.5, 7)]

def test_sort_by_name():
    assert e.sort_all_donor_info() == [("be", [3, 4], 3.5, 7), ("blah", [100], 100.0, 100), ("some", [1, 2, 3], 2.0, 6)]

def test_sort_by_hist():
    assert e.sort_all_donor_info(1) == [("some", [1, 2, 3], 2.0, 6), ("be", [3, 4], 3.5, 7), ("blah", [100], 100.0, 100)]

def test_sort_by_avg():
    assert e.sort_all_donor_info(2) == [("blah", [100], 100.0, 100), ("be", [3, 4], 3.5, 7), ("some", [1, 2, 3], 2.0, 6)]

def test_sort_by_sum():
    assert e.sort_all_donor_info(3) == [("blah", [100], 100.0, 100), ("be", [3, 4], 3.5, 7), ("some", [1, 2, 3], 2.0, 6)]
