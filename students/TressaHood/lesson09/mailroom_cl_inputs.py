#!/usr/bin/env python3

"""lesson 09, Mail room 5 Assignment, OO programming!
This mail room version is now a module that has donor, and donor collections classes.
As well as a base functions file.
"""

# import modules
import pathlib
import mailroom_donors
from mailroom_base_functions import *
from functools import partial


def menu():
    """
    This function lists all the menu items and calls the appropriate
    functions based on the user input to response. It also deals with
    exceptions from user input.
    """

    # set up menu selection prompts
    response = None
    while response != 4:

        # the introduction
        print("\nWelcome to the mail room, please choose an action: ")

        # print menu items
        for item in menu_items:
            print(item, menu_items[item][0])

        # add try/catch block
        try:
            # get the  user's response and convert it to an integer, then call
            # the appropriate function
            response = int(
                input("\nWhat action would you like to choose?").strip())

            if int(response) not in [1, 2, 3, 4]:
                print("\nYou must ONLY choose 1, 2, 3, or 4, please try again")
                continue

        except ValueError:
            print("\nYour entry must be INTEGERS 1,2,3,4, please try again")
            continue

        else:
            menu_items[response][1](donors)


def thank_you(donor_data):
    """
    Prompt the user for more information to create the thank you, then
    call the email function to write it. Also deal with exceptions from user input.
    """
    print("\nYou have chosen to create a Thank You Note: ")
    print("\nPlease give the full name of the donor, or type 'list' to see all current donors. Remember you can always type 'quit' to go to the main menu.")

    # create the selection
    while True:

        response = input("\nFull name of the donor or type 'list': ").strip()

        # if list print the list of donors
        if response.lower() == "list":
            donor_data.list_donors()
            continue

        # if they type 4, go back to the menu
        elif response.lower() == "quit":
            print("Going back to main menu")
            menu()

        # if they give a bunch of white spaces
        elif response.strip() == "":
            print("You did not type anything, going back to main menu")
            menu()

        # if they give a numeric
        elif response.replace(".", "").isdigit() == True:
            print("You did not type a string, going back to the main menu")
            menu()

        # if the person is in the donors database, add the donation - adding
        # try/catch block here
        elif response in donor_data.get_all_donors():
            while True:
                try:
                    amount = float(input("\nHow much did they donate? "))

                except ValueError:
                    print("Please enter a numeric value!!")
                    continue

                else:
                    # add the donations and then create the email
                    donor_data.add_to_database(response, amount)
                    print(email(response, amount))
                    menu()

        else:

            while True:
                    # there is a new donor
                print(
                    "\nGreat! A new donor! Adding to {} database now...".format(
                        response.title()))
                try:
                    amount = float(input("How much did they donate? "))

                except ValueError:
                    print("Please enter a numeric value!!")
                    continue

                else:
                    # add them to the database and email
                    donor_data.add_new_donor(
                        mailroom_donors.Donor(
                            response.title(), [amount]))
                    print(email(response, amount))
                    menu()


def main():
    """
    This is the main function that calls the the main selection program and sets up the donor starting list.
    :global donors: global variable for the donor database
    :global menu_items: global variable for the menu selection items
    """

    # Set global variables
    global donors
    global menu_items

    # donor names and data, easier to update this way using comprehension
    d1 = mailroom_donors.Donor("Sarah Sanderson", [3000, 367, 1000])
    d2 = mailroom_donors.Donor("Amy Anderson", [300, 256])
    d3 = mailroom_donors.Donor("Erin Eckoff", [12536.26, 10, 12536.26])
    d4 = mailroom_donors.Donor("Cassandra Cooper", [234.34, 234, 117.17])
    d5 = mailroom_donors.Donor("Debbie Danger", [9809.56])

    donors = mailroom_donors.DonorCollection([d1, d2, d3, d4, d5])

    # create the menu items
    menu_items = {1: ("- Send a Thank You",
                      thank_you),
                  2: ("- Create a Report",
                      report),
                  3: ("- Send letters to everyone",
                      send_all_letters),
                  4: ("- Quit",
                      quit)}

    # call the menu function to get started
    menu()

# call the main function
if __name__ == '__main__':
    main()
