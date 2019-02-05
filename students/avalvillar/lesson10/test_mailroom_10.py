"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    February 2nd 2019
"""


#Small testing file for the new functions in mailroom_10

import mailroom_10 as mr

def test_donor():
    donor = mr.Donor('Adam Alvarez');
    assert donor.name == "Adam Alvarez", ("Test Donor: Name")
    donor.add_donation(1.25)
    assert donor.donations == [1.25], ('Test Donor: Donations')
    donor.add_donation(2.73)
    assert donor.donations == [1.25, 2.73], ('Test Donor: Add Donation')
    donor.add_multiple_donations(list(range(2)))
    assert donor.donations == [1.25, 2.73, 0, 1], ('Test Donor: Add multiple donations')

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

def test_challenge():
    donor1 = mr.Donor('Adam Alvarez')
    donor1.add_donation(1.25)
    donor2 = mr.Donor('Beth Bonnor', 2.73)
    donor2.add_donation(1)
    donor2.add_donation(32.50)
    donors = mr.Donors()
    donors.append(donor1)
    donors.append(donor2)
    donors2 = donors.challenge(3)
    assert str(donors2) == 'Adam Alvarez, Beth Bonnor', ('Test challenge: New Donors but same name')
    assert donors2.get_donor('Adam Alvarez').donations == [3.75], ('Test challege: Donations Multiplied')
    assert donors2.get_donor('Beth Bonnor').donations == [8.19,3,97.5], ('Test challege: Donations Multiplied')
    donors3 = donors.challenge(3, 1, 3)
    assert donors3.get_donor('Beth Bonnor').donations == [8.19], ('Test Challenge: Max Donation')
    donor1.add_multiple_donations([1,2,3,6,7,8])
    donors4 = donors.challenge(5, 1, 6)
    assert donors4.get_donor('Adam Alvarez').donations == [6.25,10,15], ('Test Challenge: Max Donation')