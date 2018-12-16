#!/usr/bin/python3
"""
mailroom part 4: adding unit testing

modules to test:
    list_donors(db)
    add_donation(db, name, amount)
    thank_you_letter(db, name)
    summary_report(db)
    get_second(elem)
    
modules not tested:
    send_thank_you(db) - user input
    send_all_letters(db) - user input
    create_a_report(db) - no logic
    main_menu_error(_) - no logic
    quit_program(_) - no logic
"""

from mailroom import list_donors
from mailroom import add_donation
from mailroom import thank_you_letter
from mailroom import summary_report
from mailroom import get_second


# test list_donors(db) - 4 tests
def test_list_donors_empty_db():
    db = {}
    res_string = ""
    assert list_donors(db) == res_string
    
    
def test_list_donors_one_item_in_db():
    db = {"one": [1, 2, 3]}
    res_string = "   one"
    assert list_donors(db) == res_string
    
    
def test_list_donors_multiple_items_in_db():
    db = {"one": [1, 2, 3],
          "two": [4, 5, 6],
          "three": [7, 8, 9]}
    res_string = "   one\n   two\n   three"
    assert list_donors(db) == res_string
    
    
def test_list_donors_empty_value_lists():
    db = {"one": [], "two": [], "three": []}
    res_string = "   one\n   two\n   three"
    assert list_donors(db) == res_string


# test add_donations(db, name, amount) - 4 tests
def test_add_donations_empty_db():
    db = {}
    add_donation(db, "A Name", 1)
    res_db = {"A Name": [1]}
    assert db == res_db
    
    
def test_add_donations_name_not_in_db():
    db = {"A Name": [1]}
    add_donation(db, "B Name", 2)
    res_db = {"A Name": [1], "B Name": [2]}
    assert db == res_db
    
    
def test_add_donations_name_in_db():
    db = {"A Name": [1], "B Name": [2]}
    add_donation(db, "A Name", 3)
    res_db = {"A Name": [1, 3], "B Name": [2]}
    assert db == res_db
    
    
def test_add_donations_empty_value_list():
    db = {"A Name": [], "B Name": [2]}
    add_donation(db, "A Name", 3)
    res_db = {"A Name": [3], "B Name": [2]}
    assert db == res_db


# test thank_you_letter(db, name) - 5 tests
def test_thank_you_letter_one_name_in_db():
    db = {"A Name": [1]}
    res_string = "Dear A Name,\n" \
                 "Thank you very much for your generous donation of $1.00.\n" \
                 "Sincerely,\n" \
                 "PYTHON210 Class of 2018"
    assert thank_you_letter(db, "A Name") == res_string


def test_thank_you_letter_multiple_names_in_db():
    db = {"A Name": [1], "B Name": [2.5]}
    res_string = "Dear B Name,\n" \
                 "Thank you very much for your generous donation of $2.50.\n" \
                 "Sincerely,\n" \
                 "PYTHON210 Class of 2018"
    assert thank_you_letter(db, "B Name") == res_string


def test_thank_you_letter_multiple_values_for_name():
    db = {"A Name": [1.1, 2.2], "B Name": [3.3, 4.4]}
    res_string = "Dear B Name,\n" \
                 "Thank you very much for your generous donation of $4.40.\n" \
                 "Sincerely,\n" \
                 "PYTHON210 Class of 2018"
    assert thank_you_letter(db, "B Name") == res_string


def test_thank_you_letter_value_that_rounds_down():
    db = {"A Name": [1.1, 2.2], "B Name": [3.3, 4.444]}
    res_string = "Dear B Name,\n" \
                 "Thank you very much for your generous donation of $4.44.\n" \
                 "Sincerely,\n" \
                 "PYTHON210 Class of 2018"
    assert thank_you_letter(db, "B Name") == res_string


def test_thank_you_letter_value_that_rounds_up():
    db = {"A Name": [1.1, 2.2], "B Name": [3.3, 4.445]}
    res_string = "Dear B Name,\n" \
                 "Thank you very much for your generous donation of $4.45.\n" \
                 "Sincerely,\n" \
                 "PYTHON210 Class of 2018"
    assert thank_you_letter(db, "B Name") == res_string


# test summary_report(db) - 5 tests
def test_summary_report_empty_db():
    db = {}
    res_string = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n"
    assert summary_report(db) == res_string


def test_summary_report_one_name_one_value():
    db = {"A Name": [0]}
    res_string = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
                 "A Name                 $        0.00   1               $       0.00\n"
    assert summary_report(db) == res_string


def test_summary_report_one_name_multiple_values():
    db = {"A Name": [1, 2, 3, 4, 5]}
    res_string = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
                 "A Name                 $       15.00   5               $       3.00\n"
    assert summary_report(db) == res_string


def test_summary_report_multiple_names_multiple_values():
    db = {"A Name": [6.75, 7.75, 8.50],
          "B Name": [1, 2, 3, 4, 5]}
    res_string = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
                 "A Name                 $       23.00   3               $       7.67\n" \
                 "B Name                 $       15.00   5               $       3.00\n"
    assert summary_report(db) == res_string


def test_summary_report_multiple_names_multiple_values_sorting():
    db = {"A Name": [1, 2, 3, 4, 5],
          "B Name": [6.75, 7.75, 8.50],
          "C Name": [20.6789]}
    res_string = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n" \
                 "B Name                 $       23.00   3               $       7.67\n" \
                 "C Name                 $       20.68   1               $      20.68\n" \
                 "A Name                 $       15.00   5               $       3.00\n"
    assert summary_report(db) == res_string


# test get_second(elem) - 3 tests
def test_get_second_from_list():
    elem = ["A Name", 1, 2, 3]
    assert get_second(elem) == 1


def test_get_second_from_dict():
    db = {"A Name": [1, 2, 3],
          "B Name": [4, 5, 6]}
    assert get_second(db["B Name"]) == 5


def test_get_second_does_not_exist():
    elem = [1]
    assert get_second(elem) is None

