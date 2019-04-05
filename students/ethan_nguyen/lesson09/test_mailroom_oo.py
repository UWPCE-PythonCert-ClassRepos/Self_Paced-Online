from mailroom9 import *

D0 = Donor("Paul Allen", 5000)
donor_db = DonorCollection()
donor_db.add_donor(D0)

def test_donnor_object():
    assert "Donor: Paul Allen" in str(D0)

def test_donnor_amount():
    assert D0.amount == 5000

def test_donor_donation_count():
    donor_db.add_donor(Donor("Paul Allen", 3000))
    assert D0.count_donation == 2

def test_donor_average_donation():
    assert D0.cal_average() == 4000

def test_get_report_count():

    result = donor_db.prepare_report()     
    assert len(result) == 1

def test_get_letter_text():
    D1 = Donor("World", 300.00)

    expected = "Dear World, \n Thank you for your very kind donation of $300.00 \n \
            It will be put to very good use. \n Sincerely, \n -UW"
    
    print(D1.create_thank_you_note())
    
    assert D1.create_thank_you_note() == expected

def test_create_letter():
    donor_db.add_donor(D0)
    expected = os.path.join(os.getcwd(), "World.txt")
    donor_db.create_letter(os.getcwd(), "World", "Dear World, \n Thank you for your very kind donation of $300.00 \n \
            It will be put to very good use. \n Sincerely, \n -UW")
    assert os.path.isfile(expected)

def test_add_new_donor():
    D1 = Donor("Ethan", 5000.24)
    donor_db.add_donor(D1)
    D2 = Donor('Ethan', 10000)
    donor_db.add_donor(D2)
    expected_key, expected_value =  "Ethan", 15000.24

    assert expected_key in donor_db and expected_value == donor_db[expected_key].amount
