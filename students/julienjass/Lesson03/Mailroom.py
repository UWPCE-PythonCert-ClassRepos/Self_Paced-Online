#!/usr/bin/env python3

import sys

# Data base made of a list containing the donors' information
donor_list = [("William Gates, III", [261514, 392270.49]),
            ("Mark Zuckerberg", [4918.83, 9837.66, 1639.61]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [354.21, 212.53, 141.68])]

def mainloop():
    """This function takes no parameters. It contains the main menu prompt which allows the user: with choice 1 to
    send a Thank You message (calling the function thank_you), with choice 2 to display a report with the donors'
    information (calling the function report), and with choice 3 to leave the application (calling the function
    leave)."""
    print('Mailroom Application')
    print()
    response = ''
    while True:
        print('Please select one of the 3 options:')
        print('''
        1) Send a Thank You
        2) Create a Report
        3) Quit''')
        print()
        response = input('Your answer: ')
        print()
        if response not in ('1', '2', '3'):
            print('This is not a valid response. Please type either 1, 2, or 3\n')
            continue
        elif response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            leave()

def thank_you():
    """This function takes no parameters. A menu prompt allows the user: with choice 1 to enter a donor name and a
    donation amount (calling the function enter_name), with choice 2 to see the list of all the donors, and with
    choice 3 to return to the previous menu (calling the function mainloop)."""
    print('You have chosen to Send a Thank You message')
    choice_user = ''
    while True:
        print('''
        1) Enter the name of the donor
        2) See the list of donors
        3) Return''')
        print()
        choice_user = input('Your choice: ')
        if choice_user not in ('1', '2', '3'):
                print('This is not a valid choice. Please either type 1, 2, or 3\n')
                continue
        elif choice_user == '1':
            print()
            print('Enter the name of the donor:')
            donor_name = input('Name: ')
            print('Enter an amount:')
            donor_amount = input('Amount: ')
            print()
            enter_name(donor_name, donor_amount)
        elif choice_user == '2':
            print()
            print('List of all the donors:')
            for name in names():
                print(name)
            print()
            continue
        elif choice_user == '3':
            print()
            mainloop()

def report():
    """This function takes no parameters. It allows to display in a table the formatted information on donations:
    donor name, total given, number of gifts, and average gifts, ordered by the total amount given."""
    print("{:24s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 67)
    sorted_donor_list = donor_list[:]
    sorted_donor_list.sort(key=sum_donation, reverse=True)
    for element in sorted_donor_list:
        print('{:24s} {:>11.2f}  {:>10d}  {:>11.2f}'.format(element[0], sum(element[1]), len(element[1]), avg_donation(element)))
    print()
    mainloop()

def leave():
    """This function takes no parameters. It allows the user to end the application."""
    sys.exit()

def names():
    """This function takes no parameters. It allows to refresh the list of the current donors and return it."""
    names = []
    for person in donor_list:
        names.append(person[0])
    return names

def enter_name(name, amount):
    """This function takes 2 parameters: a donor name and a donation amount. If the name already exists in the donors'
    database, it will add the donation amount to an existing donor name. If it doesn't already exist, it will add a new
    donor name with the corresponding donation amount. Then it will display a nicely formatted thank you message with
    the donor name and the donation amount."""
    amount = float(amount)
    if name in names():
        donor_list[names().index(name)][1].append(amount)
    else:
        donor_list.append((name, [amount]))
    print("Dear {:s},\nThank you for your donation of ${:.2f}".format(name, amount))
    print("Best regards,")
    print("The Organization")
    print()
    mainloop()

def avg_donation(donation):
    """This function takes 1 parameter: a list of numbers. It computes the average and returns it."""
    return sum(donation[1]) / len(donation[1])

def sum_donation(donation):
    """This function takes 1 parameter: a list of numbers. It computes the total sum and returns it."""
    return sum(donation[1])


if __name__ == '__main__':
    """This area is always executed by the script. It is calling the mainloop function displaying the main menu
    prompt."""
    mainloop()
