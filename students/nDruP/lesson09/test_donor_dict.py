from pytest import *
from donor import *
from donor_dict import *

andrew = Donor("Andrew", [12])
someone = Donor("Someone", [384.23])
people = Donor("People", [937472.909, 379.243])
d = Donor_Dict(andrew, someone, people)
e = Donor_Dict(Donor("blah", [100]))
e.add_donor("some", [1, 2, 3])
e.add_donor("be", [3, 4])
a = Donor_Dict.from_file("easy_dict_init.txt")
b = Donor_Dict.from_file("med_dict_init.txt")
andrew.add_gift(14)
andrew.add_gift(24.05)

def test_donor_dict_names():
    assert d.names == ["Andrew", "Someone", "People"]
    assert e.names == ["blah", "some", "be"]
    
def test_donor_dict_histories():
    assert d.histories == [[12, 14, 24.05], [384.23], [937472.91, 379.24]]
    assert e.histories == [[100], [1,2,3], [3, 4]]

def test_donors():
    assert andrew in d.donors
    assert someone in d.donors
    assert people in d.donors

def test_donor_dict_add():
    d.add_donor("me", [8000])
    d.add_donor("you", [7000, 2000])
    assert "me" in d.names
    assert "you" in d.names

def test_all_donor_info():
    assert e.all_donor_info == [("blah", 1, 100.0, 100), ("some", 3, 2.0, 6), ("be", 2, 3.5, 7)]

def test_sort_by_name():
    assert e.sort_all_donor_info() == [("be", 2, 3.5, 7), ("blah", 1, 100.0, 100), ("some", 3, 2.0, 6)]

def test_sort_by_hist():
    assert e.sort_all_donor_info(1) == [("some", 3, 2.0, 6), ("be", 2, 3.5, 7), ("blah", 1, 100.0, 100)]

def test_sort_by_avg():
    assert e.sort_all_donor_info(2) == [("blah", 1, 100.0, 100), ("be", 2, 3.5, 7), ("some", 3, 2.0, 6)]

def test_sort_by_sum():
    assert e.sort_all_donor_info(3) == [("blah", 1, 100.0, 100), ("be", 2, 3.5, 7), ("some", 3, 2.0, 6)]

def test_getitem():
    assert d["andrew"] == andrew

def test_len():
    assert len(e) == 3
    assert len(d) == 5

def test_keys():
    assert d.keys == ['andrew', 'someone', 'people', 'me', 'you']
    assert e.keys == ['blah', 'some', 'be']


def test_init_from_file():
    assert "andrew" in a.keys
    assert "someone" in b.keys
    assert "thinker" in b.keys
    assert a["andrew"].history == [1234.6]
    assert b["someone"].history == [9843.23, 483.24]
    assert b["thinker"].history == [45632.39]

def test_save_dict():
    assert a.dict_to_txt() == "andrew;1234.6\n"
    assert b.dict_to_txt() == "someone;9843.23,483.24\nthinker;45632.39\n"


def test_challenge():
    aang = a.challenge(2, -1.0, -1.0)
    bang = b.challenge(3, 9000, -1.0) 
    assert aang.histories == [[round(1234.6*2,2)]]
    assert bang.histories == [[round(9843.23*3,2), 483.24], [round(45632.39*3,2)]]
