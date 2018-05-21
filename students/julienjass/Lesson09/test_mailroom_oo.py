from mailroom_oo import Donor, DonorDB


def test_donor_init():
    d = Donor('William Gates III')
    assert d.name == 'William Gates III'
    assert d.donations == []
    d.add_donation(100)
    d.add_donation(200)
    assert d.total_donations == 300


def test_donors():
    d = Donor('Paul Allen')
    d.add_donation(600)
    db = DonorDB()
    db.add_donor(d)
    assert db.get_total_from_donor('Paul Allen') == 600
    e = Donor('Jeff Bezos')
    e.add_donation(100)
    e.add_donation(200)
    db.add_donor(e)
    assert db.get_total_from_donor('Jeff Bezos') == 300
    assert db.count_donors == 2
    assert db.count_donations == 3
    assert db.total_donations == 900
    assert db.average_total_donation == 450
    assert db.average_single_donation == 300
    test_list = db.donor_list()
    assert test_list.startswith('Paul Allen')
    assert test_list.endswith('Jeff Bezos')
