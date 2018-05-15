"""
Unit testing for mailroom
"""

import mailroom_4 as mr
import pytest
import sys

donations = {"Bill Gates": [10.50, 123.45, 1111.11],
             "Jeff Bezos": [7.65, 1000.00],
             "Paul Allen": [145.90],
             "John Nordstrom": [45.67, 6519.65],
             "Mark Zuck": [789.12]}

def test_main_menu_prompt():
    assert mr.main_prompt == "\nWelcome to the Main Menu! What would you like to do?\n1 - Send a Thank You\n2 - Create a Report\n3 - Send letters to everyone\nq - Quit and exit\n--> "

def test_thank_you_prompt():
    assert mr.thank_you_prompt == "\nPlease choose one of the following:\n1 - Add a donation and send thank you message\n2 - Display list of current donors\nq - Return to main menu\n--> "

def test_main_menu():
    assert mr.main_menu == {
        "1": mr.send_thank_you,
        "2": mr.create_report,
        "3": mr.write_letters,
        "q": mr.quit_menu,
    }

def test_thank_you_menu():
    assert mr.thank_you_menu == {
        "1": mr.add_donation,
        "2": mr.list_donors,
        "q": mr.quit_menu,
    }

def test_send_thank_you_prompt(capfd):
    mr.send_thank_you()
    out, err = capfd.readouterr()
    assert out == "\nPlease choose one of the following:\n1 - Add a donation and send thank you message\n2 - Display list of current donors\nq - Return to main menu\n--> "


# def test_prompt():
#     mr.prompt(mr.main_prompt, mr.main_menu)


# def test_list_donors_function(capfd):
#     mr.list_donors()
#     out, err = capfd.readouterr()



def test_quit_menu_function():
    assert mr.quit_menu() == "quit"
