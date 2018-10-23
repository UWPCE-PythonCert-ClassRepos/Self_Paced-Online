import oo_mailroom


d1 = oo_mailroom.Donor("kim schultz", [10, 100, 1000, 10000])
d2 = oo_mailroom.Donor("ann schultz", [9, 99, 999])
d3 = oo_mailroom.Donor("bill schultz", [222, 2222])
donors = oo_mailroom.DonorCollection([d1, d2, d3])

#DONOR TESTS
def test_name():
    assert d1.name == "kim schultz"
    assert d2.name == "ann schultz"
    assert d3.name == "bill schultz"

def test_total_given():
    assert d1.total_given == 11110
    assert d2.total_given == 1107
    assert d3.total_given == 2444

def test_num_gifts():
    assert d1.num_gifts == 4
    assert d2.num_gifts == 3
    assert d3.num_gifts == 2

def test_average_gift():
    assert d1.average_gift == 2777.5
    assert d2.average_gift == 369
    assert d3.average_gift == 1222

def test_donations():
    assert d1.donations == [10, 100, 1000, 10000]
    assert d2.donations == [9, 99, 999]
    assert d3.donations == [222, 2222]

def test_average_gift():
    assert d1.average_gift == 2777.5
    assert d2.average_gift == 369
    assert d3.average_gift == 1222

def test_append_donation():
    d3.append_donation(d3, d3, 420)
    assert len(d3.donations) == 3

def test_new_donor():
    d4 = oo_mailroom.Donor("sammy schultz", [222, 2222])
    assert d4.name == "sammy schultz"



