"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 26th 2019
"""


#Small testing file for the new classes in mailroom_9

import mailroom_9 as mr

def test_donor():
    donor = mr.Donor('Adam Alvarez');
    assert donor.name == "Adam Alvarez", ("Test Donor: Name")
    donor.add_donation(1.25)
    assert donor.donations == [1.25], ('Test Donor: Donations')
    donor.add_donation(2.73)
    assert donor.donations == [1.25, 2.73], ('Test Donor: Add Donation')

def test_donors():
    donor1 = mr.Donor('Adam Alvarez')
    donor1.add_donation(1.25)
    donor2 = mr.Donor('Beth Bonnor', 2.73)
    donors = mr.Donors()
    donors.append(donor1)
    donors.append(donor2)
    assert donor1.name == "Adam Alvarez", ('Test Donors: Adam\'s Name')
    assert donor2.name == "Beth Bonnor", ('Test Donors: Beth\'s Name')
    assert str(donors) == 'Adam Alvarez, Beth Bonnor', ('Test Donors: Donor List')
    assert donors.get_donor('Beth Bonnor') == donor2, ('Test Donors: Donor Get')