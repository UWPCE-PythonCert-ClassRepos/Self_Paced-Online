#!/usr/bin/env python3
"""
Victor Medina
Date: 1/12/2019
Assignment 4: Mailroom Part 2
"""
import sys


def send_thank_you(donors):
    """

    :param donors: dictionary
        Dictionary of donor names with a value of a list of donation amoounts
    :return: donors: dictionary
        updated dictionary with new donation amount and/or new donor
    """
    print(donors)
    name = input("What's the name? ")

    if name == 'list':
        for donor in donors.keys():
            print(donor)
        name = input("What's the name? ")
    if any(name in donor_info for donor_info in donors):
        donor = name
    else:
        donors[name] = []
        donor = name

    try:
        donation_amount = int(input('Donation Amount? '))
    except ValueError:
        print('Please insert an integer')
    else:
        donors.get(donor).append(donation_amount)
        print(donors)
        print('Thank you {} for your generous donation of {} dollars!'.format(donor, donation_amount))
    return donors


def create_report(donors):
    """
    function that prints out a nicely formatted report summarizing donor list, total donations, average donation and
    number of donations
    :param donors: dictionary
        Dictionary of donor names with a value of a list of donation amoounts
    :return: None
        function prints out report. No return is needed
    """
    donor_report = {}
    for donor in donors:
        donor_report[donor] = dict(total_donation=sum(donors[donor]), num_donations=len(donors[donor]),
                                   avg_donation=sum(donors[donor]) / len(donors[donor]))

    print(donor_report)
    print('Donor Name      | Total Given |   Num Gifts  | Average Gift')
    print('------------------------------------------------------------')
    for donor in donor_report:
        print('{:<15} ${:>13} {:>14} ${:>13,.2f}'.format(donor, donor_report[donor]['total_donation'],
                                                         donor_report[donor]['num_donations'],
                                                         donor_report[donor]['avg_donation']))



def send_letters(donors):
    """
    function that creates a text file thanking the donor with the last donation amount listed.
    :param donors: dictionary
        Dictionary of donor names with a value of a list of donation amoounts
    :return: None
        function writes out text files. No return is needed
    """
    for donor in donors:
        with open(str(donor) + '.txt', 'w') as file:
            file.write('Dear {},\n\nThank you for your very kind donation of ${}!\n\nSincerely,\n -The Team'.
                       format(donor, donors[donor][-1]))



if __name__ == "__main__":
    donors = {
        'Victor': [100, 20, 30],
        'John': [12],
        'Kevin': [91, 32],
        'Kelly': [5, 21],
        'Matt': [75, 20],
        'Josh': [31, 3],
        'Micah': [120]}
    # initial request
    response = input('Do you want to: "Send a Thank you", "Create a Report", "Send letters to everyone" or "quit"? ')

    response_func_dict = {'send a thank you': send_thank_you,
                          'create a report': create_report,
                          'send letters to everyone': send_letters,
                          'quit': sys.exit}
    while response != 'quit':
        try:
            response_func_dict[response](donors)
        except KeyError:
            print('please input a valid response')
        response = input('Do you want to: "Send a Thank you",'
                         ' "Create a Report", "Send letters to everyone" or "quit"? ')
    else:
        response_func_dict.get(response)()
