"""
Unit testing for mailroom
"""

import mailroom_4 as mr
import pytest

def test_main_menu_prompt():
    assert mr.main_prompt == "\nWelcome to the Main Menu! What would you like to do?\n1 - Send a Thank You\n2 - Create a Report\n3 - Send letters to everyone\nq - Quit and exit\n--> "


def test_thank_you_prompt():
    assert mr.thank_you_prompt == "\nPlease choose one of the following:\n1 - Add a donation and send thank you message\n2 - Display list of current donors\nq - Return to main menu\n--> "


def test_main_menu():
    assert mr.main_menu == {
        "1": mr.send_thank_you,
        "2": mr.print_report,
        "3": mr.write_letters,
        "q": mr.quit_menu,
    }


def test_thank_you_menu():
    assert mr.thank_you_menu == {
        "1": mr.prompt_for_donation,
        "2": mr.print_donors,
        "q": mr.quit_menu,
    }


def test_donor_list():
    donations = {"Chris": 100.00, "Joe": 10.99}
    assert mr.list_donors(donations) == '\nList of donors:\nChris\nJoe\n'


def test_create_donor_email():
    assert mr.create_email("Chris", 100.00) == '\nDear Chris,\n\nThank you so very much for your kind donation of $100.0. We can assure you that it will be put to great use.\n\nBest,\nChris'


def test_create_report_header():
    assert mr.create_report_header() == 'Donor Name          |  Total Given  |   Num Gifts   |   Average Gift\n---------------------------------------------------------------------'


def test_create_report_data():
    donations = {"Chris": [10.00, 20.00, 100.00]}
    data = mr.create_report_data(donations)
    assert data[0][0] == "Chris"
    assert data[0][1] == sum(donations["Chris"])
    assert data[0][2] == len(donations["Chris"])
    assert data[0][3] == data[0][1] / data[0][2]


def test_create_report_rows():
    donations = {"Chris": [10.00, 20.00, 100.00]}
    data = mr.create_report_data(donations)
    assert mr.create_report_rows(data) == 'Chris                         130.00               3           43.33\n'


def test_compose_letter():
    donations = {"Chris": [10.00, 20.00, 100.00]}
    assert mr.compose_letter("Chris", donations) == "Dear Chris,\n\n        Thank you very much for your generosity! Your most recent gift of $100.0 will be put to great use. So far, you've donated a total of $130.0!\n\n        Sincerely,\n        The Team"


def test_add_donation_to_existing_donor():
    donations = {"Chris": [10.00, 20.00, 100.00]}
    mr.add_donation("Chris", 15.15, donations)
    assert donations["Chris"][-1] == 15.15


def test_add_new_donor():
    donations = {"Chris": [10.00, 20.00, 100.00]}
    mr.add_donation("Joe", 100.00, donations)
    assert donations["Joe"][0] == 100.00


def test_quit_menu_function():
    assert mr.quit_menu() == "quit"
