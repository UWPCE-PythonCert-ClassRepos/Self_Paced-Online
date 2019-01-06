from donors import Donor
from donors import Donors


def test_donor_init():
    d = Donor("Bill", 100)
    assert d.name == "Bill"
    assert d.donations == [100]


def test_donor_init_w_multiple_donations():
    d = Donor("Bill", [1, 2, 3])
    assert d.name == "Bill"
    assert d.donations == [1, 2, 3]


def test_donor_add_donation():
    d = Donor("Bill", 100)
    d.add_donation(200)
    d.add_donation(300)
    assert d.donations == [100, 200, 300]


def test_donor_donation_calculations():
    d = Donor("Bill", 100)
    d.add_donation(200)
    d.add_donation(300)
    assert d.num_donations() == 3
    assert d.sum_donations() == 600
    assert d.avg_donation() == 200


def test_donor_thank_you_letter():
    d = Donor("Bill", 100)
    d.add_donation(200)
    d.add_donation(300)
    expected = f"Dear Bill,\n" \
               f"Thank you very much for your generous donation of $300.00.\n" \
               f"Sincerely,\n" \
               f"PYTHON210 Class of 2018"
    assert d.thank_you_letter() == expected


def test_donors_init():
    db = Donors()
    assert db == {}


def test_donors_list_donors_empty_db():
    db = Donors()
    expected = ""
    assert db.list_donors() == expected


def test_donors_list_donors_one_item_in_db():
    db = Donors({"one": [1, 2, 3]})
    expected = "   one"
    assert db.list_donors() == expected


def test_donors_list_donors_multiple_items_in_db():
    db = Donors({"one": [1, 2, 3],
                 "two": [4, 5, 6],
                 "three": [7, 8, 9]})
    expected = "   one\n   two\n   three"
    assert db.list_donors() == expected


def test_donors_list_donors_empty_value_lists():
    db = Donors({"one": [], "two": [], "three": []})
    expected = "   one\n   two\n   three"
    assert db.list_donors() == expected


def test_donors_add_donor():
    db = Donors()
    db.add_donor(Donor("Bill", 100))
    assert db["Bill"].name == "Bill"
    assert db["Bill"].donations == [100]


def test_donors_add_donor_w_multiple_donations():
    db = Donors()
    db.add_donor(Donor("Bill", [1, 2, 3]))
    assert db["Bill"].name == "Bill"
    assert db["Bill"].donations == [1, 2, 3]


def test_donors_add_donations_empty_db():
    db = Donors()
    db.add_donation("A Name", 1)
    expected = "   A Name"
    assert db.list_donors() == expected
    assert db["A Name"].name == "A Name"
    assert db["A Name"].donations == [1]


def test_donors_add_donations_name_not_in_db():
    db = Donors({"A Name": [1]})
    db.add_donation("B Name", 2)
    expected = "   A Name\n   B Name"
    assert db.list_donors() == expected


def test_donors_add_donations_name_in_db():
    db = Donors({"A Name": [1], "B Name": [2]})
    db.add_donation("A Name", 3)
    expected = "   A Name\n   B Name"
    assert db.list_donors() == expected
    assert db["A Name"].donations == [1, 3]
    assert db["B Name"].donations == [2]


def test_donors_add_donations_empty_value_list():
    db = Donors({"A Name": [], "B Name": []})
    db.add_donation("A Name", 3)
    expected = "   A Name\n   B Name"
    assert db.list_donors() == expected
    assert db["A Name"].donations == [3]
    assert db["B Name"].donations == []


def test_donors_summary_report_empty_db():
    db = Donors()
    expected = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n"
    assert db.summary_report() == expected


def test_donors_summary_report_one_name_one_value():
    db = Donors({"A Name": [0]})
    expected = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
               "A Name                 $        0.00   1               $       0.00\n"
    assert db.summary_report() == expected


def test_donors_summary_report_one_name_multiple_values():
    db = Donors({"A Name": [1, 2, 3, 4, 5]})
    expected = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
               "A Name                 $       15.00   5               $       3.00\n"
    assert db.summary_report() == expected


def test_donors_summary_report_multiple_names_multiple_values():
    db = Donors({"A Name": [6.75, 7.75, 8.50],
                 "B Name": [1, 2, 3, 4, 5]})
    expected = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
               "A Name                 $       23.00   3               $       7.67\n" \
               "B Name                 $       15.00   5               $       3.00\n"
    assert db.summary_report() == expected


def test_donors_summary_report_multiple_names_multiple_values_sorting():
    db = Donors({"A Name": [1, 2, 3, 4, 5],
                 "B Name": [6.75, 7.75, 8.50],
                 "C Name": [20.6789]})
    expected = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
               "B Name                 $       23.00   3               $       7.67\n" \
               "C Name                 $       20.68   1               $      20.68\n" \
               "A Name                 $       15.00   5               $       3.00\n"
    assert db.summary_report() == expected


def test_donors_get_second_from_list():
    elem = ["A Name", 1, 2, 3]
    assert Donors.get_second(elem) == 1


def test_donors_get_second_from_dict():
    db = {"A Name": [1, 2, 3],
          "B Name": [4, 5, 6]}
    assert Donors.get_second(db["B Name"]) == 5


def test_donors_get_second_does_not_exist():
    elem = [1]
    assert Donors.get_second(elem) is None
