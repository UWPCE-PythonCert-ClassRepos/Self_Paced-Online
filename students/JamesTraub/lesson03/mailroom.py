#!/usr/bin/env python
# James Traub 04-17-18
# Lesson 3 - Mailroom Lab Exercise, Part 1


from datetime import date
today = str(date.today())

if __name__ == "__main__":
    print('')


donors_history = [["thomas doyle", [1.00, 2.00, 4.00]], ["kim thayill", [200.00, 34999.00]], [
    "rex tillerson", [18000000.00, 1.00]], ["judy noise", [1000.00]], ["april brinno", [20000.00, 3000.00, 400.00]]]


mailroom_menu = """
    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\\n
        Mailroom Main Menu\n
    \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\\n
    Enter a 1 to - \'Send a Thank You\'\n
    Enter a 2 to - \'Create a Report\'\n
    Enter a 3 to - \'Quit\'\n
"""


def donor_name_list():
    print('\n'"This is the complete list of charitable donors as of " + today + ".\n")
    for i in donors_history:
        print(i[0].title())
        print('')
    thanking()


def thanking():
    name_or_list = input("Enter donor first and last name or the word donors to see a list of names. ")
    name_or_list = name_or_list.lower()
    donors = ''
    if name_or_list == 'donors':
        donor_name_list()
    else:
        donation_amount = float(input('\n'"Please enter a donation amount. No dollar sign needed, thank you. "'\n'))
        for a, b in enumerate(donors_history):
            if name_or_list == b[0]:
                donors_history[a][1].append(donation_amount)
                break
            else:
                donors_history.append([name_or_list, [donation_amount]])
                break
        print(donors_history)
        print('\n'"Thank you for the donation in {}'s name!".format(name_or_list.title()))


def donor_report():
    print('\n'"This is the Donor History report listing Donor and Donation Amount.")
    print("-------------------------------------------------------------------")
    for list_entry in donors_history:
        total_donation = sum(list_entry[1])
        print("|{:>32}|{:>32}|".format(list_entry[0].title(), total_donation))

def mailing_options():
    menu_input = 0
    while menu_input != '3':
        print(mailroom_menu)
        menu_input = int(input("Please enter an option from the Mailroom Main Menu: "))
        if menu_input == 1:
            thanking()
        elif menu_input == 2:
            donor_report()
        elif menu_input == 3:
            print('\n'"Good Bye."'\n')
            break
        else:
            print("Entry not recognized. Please try again.")
            break


mailing_options()
