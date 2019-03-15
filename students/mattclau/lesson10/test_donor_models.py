import pytest

from donor_models import *

def test_init_donor():
    """test that donor is initialized with name and with donation if sent"""
    d1 = Donor('Micheal Jordan')
    d2 = Donor('Lebron James', [12345.67])

    assert d1.name == 'Micheal Jordan'
    assert d1.donations == []
    assert d2.name == 'Lebron James'
    assert d2.donations == [12345.67]

def test_add_donation():
    """test that donations are properly added to list"""
    d1 = Donor('Micheal Jordan')
    d2 = Donor('Lebron James', [12345.67])

    d1.add_donation(12345)
    d2.add_donation(123456)

    assert d1.donations == [12345]
    assert d2.donations == [12345.67,123456]

def test_compare_donors():
    """test that donors can be properly compared by their total donations"""
    d1 = Donor('Micheal Jordan',[12345])
    d2 = Donor('Lebron James',[12345])
    d3 = Donor('Micheal Jordan',[12345])

    assert d1 != d2
    assert d1 == d3

    d2.add_donation(1)

    assert d1 < d2
    assert d2 > d1

def test_sort_donors():
    """test that donors can be properly sorted by sum, average, and number of donations"""
    d1 = Donor('Micheal Jordan',[12345, 1])
    d2 = Donor('Lebron James',[12344])
    d3 = Donor('The Snake',[1,2,3])

    donor_list = [d1, d2, d3]

    donor_list.sort(key=Donor.sort_avg, reverse=True)

    assert donor_list == [d2, d1, d3]

    donor_list.sort(key=Donor.sort_sum, reverse=True)

    assert donor_list == [d1, d2, d3]

    donor_list.sort(key=Donor.sort_len, reverse=True)

    assert donor_list == [d3, d1, d2]


def test_init_collection():
    """test that collection of donors can be initialized by passing list of donors"""
    d1 = Donor('Micheal Jordan',[12345, 1])
    d2 = Donor('Lebron James',[12344])
    d3 = Donor('The Snake',[1,2,3])
    d4 = Donor('Rincewind',[1,2,3])

    donor_list = DonorCollection([d1, d2, d3])


    assert d1 in donor_list.return_donors()
    assert d2 in donor_list.return_donors()
    assert d3 in donor_list.return_donors()
    assert d4 not in donor_list.return_donors()

def test_add_donor():
    """test a donor can be added to an existing collection"""
    d1 = Donor('Micheal Jordan',[12345, 1])
    d2 = Donor('Lebron James',[12344])
    d3 = Donor('The Snake',[1,2,3])
    d4 = Donor('Rincewind',[1,2,3])

    donor_list = DonorCollection([d1, d2, d3])

    assert d1 in donor_list.return_donors()
    assert d2 in donor_list.return_donors()
    assert d3 in donor_list.return_donors()
    assert d4 not in donor_list.return_donors()

    donor_list.add_donor(d4)

    assert d4 in donor_list.return_donors()

def test_aggregate_donors():
    """test that collection of donors is aggregated correctly"""
    d1 = Donor("Douglas Adams",donations = [1000])
    d2 = Donor("Bruce Lee",donations = [9876.55])
    d3 = Donor("Charles Barkley",donations = [999999.99,55555.55,7777.77])
    d4 = Donor("Scottie Pippen",donations = [1, 5])
    d5 = Donor("Ursula K Le Guin",donations = [534567.89])

    donor_list = DonorCollection([d1, d2, d3, d4, d5])

    assert donor_list.aggregate_donations(True, 'sum') == [['Charles Barkley', 1063333.31, 3, 354444.4366666667], ['Ursula K Le Guin', 534567.89, 1, 534567.89], ['Bruce Lee', 9876.55, 1, 9876.55], ['Douglas Adams', 1000, 1, 1000.0], ['Scottie Pippen', 6, 2, 3.0]]

def test_match_min():
    """tests that matches are properly calculated with a minimum donation set"""
    d1 = Donor("Douglas Adams",donations = [1000])
    d2 = Donor("Bruce Lee",donations = [20])
    d3 = Donor("Charles Barkley",donations = [100])
    d4 = Donor("Scottie Pippen",donations = [50])

    donor_list = DonorCollection([d1, d2, d3, d4])

    new_donor_list, projected_total = donor_list.match_donations(2,min_don=100)

    d1 = Donor("Douglas Adams",donations = [2000])
    d3 = Donor("Charles Barkley",donations = [200])

    assert d1 in new_donor_list.return_donors()
    assert d2 not in new_donor_list.return_donors()
    assert d3 in new_donor_list.return_donors()
    assert d4 not in new_donor_list.return_donors()

def test_match_max():
    """tests that matches are properly calculated with a maximum donation set"""
    d1 = Donor("Douglas Adams",donations = [1000])
    d2 = Donor("Bruce Lee",donations = [20])
    d3 = Donor("Charles Barkley",donations = [100])
    d4 = Donor("Scottie Pippen",donations = [50])

    donor_list = DonorCollection([d1, d2, d3, d4])

    new_donor_list, projected_total = donor_list.match_donations(2,max_don=99)

    d2 = Donor("Bruce Lee",donations = [40])
    d4 = Donor("Scottie Pippen",donations = [100])

    assert d1 not in new_donor_list.return_donors()
    assert d2 in new_donor_list.return_donors()
    assert d3 not in new_donor_list.return_donors()
    assert d4 in new_donor_list.return_donors()

def test_match_both():
    """tests that matches are properly calculated with both min and max donation set"""
    d1 = Donor("Douglas Adams",donations = [1000])
    d2 = Donor("Bruce Lee",donations = [20])
    d3 = Donor("Charles Barkley",donations = [100])
    d4 = Donor("Scottie Pippen",donations = [50])

    donor_list = DonorCollection([d1, d2, d3, d4])

    new_donor_list, projected_total = donor_list.match_donations(2, min_don=50,max_don=99)

    d4 = Donor("Scottie Pippen",donations = [100])

    assert d1 not in new_donor_list.return_donors()
    assert d2 not in new_donor_list.return_donors()
    assert d3 not in new_donor_list.return_donors()
    assert d4 in new_donor_list.return_donors()

def test_projection():
    """tests that match projection is caclulated properly"""
    d1 = Donor("Douglas Adams",donations = [1000])
    d2 = Donor("Bruce Lee",donations = [20])
    d3 = Donor("Charles Barkley",donations = [100])
    d4 = Donor("Scottie Pippen",donations = [50])

    donor_list = DonorCollection([d1, d2, d3, d4])

    new_donor_list, projected_total = donor_list.match_donations(2, projection=True)


    assert projected_total == 1170