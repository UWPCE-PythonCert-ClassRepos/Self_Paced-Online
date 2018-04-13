#!/usr/bin/env python3
"""
File Name: mailroom.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 4/9/2018
Python Version: 3.6.4
"""


'''List of donors and list of lists of donations.  Both share an index '''
donors = ["Tom Selleck", "Burt Reynolds", "Nick Offerman", "Sam Elliot", "John Waters"]
donations = []
donations.append([2000.00, 1500.00, 500.00])
donations.append([45.00])
donations.append([1000.00, 1000.00])
donations.append([1200.00, 550.00])
donations.append([20.00, 20.00, 20.00])


def list_donors():
    ''' Prints list of donors '''
    for d in donors:
        print(d)
    return


def add_donor(d_name):
    '''Adds a new donor to donors'''
    print("")
    donors.append(d_name)
    donations.append([])
    add_donation(d_name)
    return


def add_donation(d_name):
    '''Appends a donation to existing donor '''
    print(f"{d_name}")
    # Formats float to 2 decimal places"
    d_amount = round(float(input("Enter a Donation amount: ")), 2)
    # Using same index for donors and donations
    donations[donors.index(d_name)].append(d_amount)
    print_email(d_name, d_amount)
    return


def print_email(name, amount):
    template = "Dear {}, thank you for your generous donation of ${}"
    print(template.format(name, amount))
    print('\n')
    return


def t_menu():
    ''' Prints Thank You menu'''
    while True:
        print("Type list to see a list of donors. Type quit to exit")
        prompt = "Please enter donor name: "
        entry = input(prompt)
        if entry == "list":
            list_donors()
        elif entry == "quit":
            break
        elif entry in donors:
            add_donation(entry)
        else:
            add_donor(entry)
    return


def create_report():
    categories = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print("{:<20}| {:>10} | {:>10} | {:>10}".format(*categories))
    for donor in donors:
        i = donors.index(donor)
        total = sum(donations[i])
        num = len(donations[i])
        avg = total / num
        spacing = "{:<20} $ {:>10.2f} {:>10}     $ {:>10.2f}"
        print(spacing.format(donor, total, num, avg))
    print("\n")
    return


if __name__ == "__main__":
    selection = ''
    while selection != '3':
        print("Please enter a Selection")
        print("1. Send a Thank You")
        print("2. Create a Report")
        print("3. Exit")
        selection = input("Enter your selection: ")
        if selection == '1':
            print("Send Thank You")
            t_menu()
        elif selection == '2':
            print("Create Report")
            create_report()
        elif selection == '3':
            print("Exiting Mailroom")
        else:
            print("Invalid Selection")
