#!/usr/bin/env python3

import sys

# Data base made of a list containing the donors' information
donor_list = [("William Gates, III", [261514, 392270.49]),
            ("Mark Zuckerberg", [4918.83, 9837.66, 1639.61]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [354.21, 212.53, 141.68])]


def mainloop():
    """Main menu"""
    print('Mailroom Application')
    print()
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
    """Thank You menu"""
    print('You have chosen to Send a Thank You message')
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
    """Generate the formatted report"""
    print("-" * 67)
    sorted_donor_list = donor_list[:]
    sorted_donor_list.sort(key=sum_donation, reverse=True)
    for element in sorted_donor_list:
        print('{:24s} {:>11.2f}  {:>10d}  {:>11.2f}'.format(element[0], sum(element[1]), len(element[1]), avg_donation(element)))
    print()
    mainloop()


def leave():
    """Quit the application"""
    sys.exit()


def names():
    """This function takes no parameters. It allows to refresh the list of the current donors and return it."""
    names = []
    for person in donor_list:
        names.append(person[0])
    return names


def enter_name(name, amount):
    """Add name and/or donation to donors' database"""
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
    """Always executed by the script"""
    mainloop()
