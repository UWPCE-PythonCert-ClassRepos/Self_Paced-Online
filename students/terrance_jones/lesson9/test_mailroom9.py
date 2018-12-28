from mailroom9 import *


def test_Donor():
    b = Donor('Zu Xi', 750)
    assert isinstance(b, Donor)
    assert b.name == 'Zu Xi'
    assert b.donations == [750]
    b.append_donations(500)
    assert b.donations == [750,500]
    b.thank_you_letter('Zu Xi', 500) == "Dear Zu Xi, \n Thank you for your generous donation of $500. \nSincerely, Mailroom."

def test_DonorCollection():
    assert DonorCollection.donor_exists('Carlos Santos') is True
    assert DonorCollection.donor_exists('Alien Galaxy') is False
