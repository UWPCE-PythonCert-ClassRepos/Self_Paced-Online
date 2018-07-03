"""
Sean Tasaki
6/29/2018
Lesson09.oo_mailroom
"""


from oo_mailroom import *

sean = Donor('Sean', 'Tasaki', [5000, 1000, 2000])
donor_dict = defaultdict(list, {'Bob Dylan': [2000.00, 500.00, 3.00], 'Italo Calvino': [1001.00, 333.00]})

def test_name():
    assert sean.full_name == 'Sean Tasaki'

def test_donations():
    sean.add_donation(100)
    assert 8100 == sean.total_donation
    assert 4 == sean.num_of_donations

# this test is failing because sean.add_donor() is not adding sean to donor_dict. Not sure why.
def test_add_donor():
    dc = DonorCollection(donor_dict)
    dc.add_donor(sean)
    lis = list(donor_dict.keys())
    assert lis[-1] == 'Sean Tasaki'

def test_thank_you_message():
    dc = DonorCollection(donor_dict)
    #Test new donor
    s1 = dc.thank_you_message('Sean Tasaki', 100.00, 0) 
    assert s1 == 'Thank you Sean Tasaki for becoming a new donor to our charity! Your genereous donation of $100.00 is much appreciated.'
    #Test previous donor
    s2 =  dc.thank_you_message('Feisty Burger', 99.00, 1)
    assert s2 == 'Thank you Feisty Burger for your loyal support to our charity! Your genereous donation of $99.00 is much appreciated.'

def test_thank_you_letter_template():
     dc = DonorCollection(donor_dict)
     newDonor = Donor('Karl', 'Jaspers', [5.00])
     dc.add_donor(newDonor)
     #Test new donor
     s2 = dc.thank_you_letter_template('Karl Jaspers')
     assert s2 == 'Dear Karl Jaspers,''\n''Thank you for your generous donation of $5.00. Your support helps our charity stay in business.''\n\n''Sincerely,''\n''-The Team'
     s1 = dc.thank_you_letter_template('Bob Dylan')
     assert s1 == 'Dear Bob Dylan,''\n''Thank you for your 3 generous donations of $2503.00. Your support helps our charity stay in business.''\n\n''Sincerely,''\n''-The Team'



