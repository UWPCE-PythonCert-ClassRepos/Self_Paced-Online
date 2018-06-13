import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from mailroom5 import Donor, Donors_Collection

def test_Donor():
    new_donor = Donor('New')
    assert (new_donor.name == 'New') is True

    new_donor.add_donation(40)
    assert (new_donor.donations == [40]) is True

# def test_Donors_Collection():
#     donors_collection = donation_history_initialization()
#     new_donor = Donor('New')
#     new_donor.add_donation(40)
#     donors_collection.add_new_donor(new_donor)
#     assert( donors_collection.donors[-1].name == 'New') is True
#     assert( donors_collection.donors[-1].donations == [40]) is True