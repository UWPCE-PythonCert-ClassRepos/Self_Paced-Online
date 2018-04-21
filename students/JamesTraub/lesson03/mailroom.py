#!/usr/bin/env python3.6
# James Traub 04-17-18
# Lesson 3 - Mailroom Lab Exercise, Part 1


from datetime import date
today = str(date.today())

if __name__ == "__main__":
    print()


donors_history = [["Thomas Doyle", [1.00, 2.00, 4.00]], ["Kim Thayill", [200.00, 34999.00]], [
    "Rex Tillerson", [18000000.00, 1.00]], ["Judy Noise", [1000.00]], ["April Brinno", [20000.00, 3000.00, 400.00]]]


mailroom_menu = "    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\\n        Mailroom Main Menu    \\ \\ \\ \\ \\ \\ \\      \\ \\ \\ \\ \\ \\ \\\n    Option 1: \'Send a Thank You\'\n    Option 2: \'Create a Report\'\n    Option 3: \'Quit\'\n"



def donor_name_list():
    print("This is the complete list of charitable donors as of " + today + ". ")
    for i in donors_history:
        print(i[0])
    thanking()


def thanking():
    thanks_for = input("Please enter the first and last name of the donor to thank. \nIf you would like to a list of the donor names enter the word 'list'. ")
    if thanks_for.lowercase() = 'list':
        donor_name_list()
    else:
        if thanks_for in donors_history:
            input("please eter a donation amount: ")
        else:



def mailing_options():
    menu_input = ''
    while menu_input != '3':
        print(mailroom_menu)
        menu_input = input("Please enter an option from the Mailroom Main Menu: ")
        if menu_input == '1':
            thanking()
        elif menu_input == '2':
            print("Create a Report")
        elif menu_input == '3':
            print("Good Bye.")
        else:
            print("Entry not recognized. Please try again.")
        break


mailing_options()
