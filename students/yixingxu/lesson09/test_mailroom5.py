from mailroom5 import Donor, Donors_Collection, donation_history_initialization

def test_Donor():
    new_donor = Donor('New')
    assert (new_donor.name == 'New') is True

    new_donor.add_donation(40)
    assert (new_donor.donations == [40]) is True


def test_Donors_Collection_add_new_donor():
    donors_collection = donation_history_initialization()
    new_donor = Donor('New')
    new_donor.add_donation(40)
    donors_collection.add_new_donor(new_donor)
    assert( donors_collection.donors[-1].name == 'New') is True
    assert( donors_collection.donors[-1].donations == [40]) is True


def test_Donors_Collection_add_donation_amount():
    donors_collection = donation_history_initialization()
    donors_collection.add_donation_amount('Ethan',50)
    assert( donors_collection.donors[-1].name == 'Ethan') is True
    assert( donors_collection.donors[-1].donations == [10, 20, 50]) is True