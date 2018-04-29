#!/usr/bin/env python
# James Traub 04-17-18
# Lesson 3 - Mailroom Lab Exercise, Part 1


from datetime import date
today = str(date.today())

if __name__ == "__main__":
    print('')


donors_history = [["Thomas Doyle", [1.00, 2.00, 4.00]], ["Kim Thayill", [200.00, 34999.00]], [
    "Rex Tillerson", [18000000.00, 1.00]], ["Judy Noise", [1000.00]], ["April Brinno", [20000.00, 3000.00, 400.00]]]


mailroom_menu = """
    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\\n
        Mailroom Main Menu\n
    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\\n
    Enter a 1 to - \'Send a Thank You\'\n
    Enter a 2 to - \'Create a Report\'\n
    Enter a 3 to - \'Quit\'\n
"""


def donor_name_list():
    print("This is the complete list of charitable donors as of " + today + ".\n")
    for i in donors_history:
        print(i[0])
        print('')
    thanking()


def thanking():
    name_or_list = input("Enter donor first and last name or the word donors to see a list of names. ")
    donors = ''
    if name_or_list == 'donors':
        donor_name_list()
    else:
        donation_amount = float(input("Please enter a donation amount. No dollar sign needed, thank you. "'\n'))
        for a, b in enumerate(donors_history):
            if name_or_list == b[0]:
                donors_history[a][1].append(donation_amount)
                break
        print(donors_history)
        print("Thank you for your donation!")


def mailing_options():
    menu_input = 0
    while menu_input != '3':
        print(mailroom_menu)
        menu_input = int(input("Please enter an option from the Mailroom Main Menu: "))
        print('')
        if menu_input == 1:
            thanking()
        elif menu_input == 2:
            print("Create a Report")
        elif menu_input == 3:
            print("Good Bye.")
            break
        else:
            print("Entry not recognized. Please try again.")
            break


mailing_options()
