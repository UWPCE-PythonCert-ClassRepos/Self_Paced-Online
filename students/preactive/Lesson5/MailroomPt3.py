#!/usr/bin/env python3
import sys
from pathlib import Path
import pickle

donors_file = "donors.pkl"
donors = list()


def file_init():
    global donors
    donorsHistory = Path(donors_file)
    if donorsHistory.is_file():
        with open(donors_file, 'rb') as donersFile:
            donors = pickle.load(donersFile)

    else:
        donors = [
            {'donor':'Hutch', 'amounts':[10, 15, 75.75] },
            {'donor':'Carlton', 'amounts':[32, 19000.01]},
            {'donor':'William Gates, III', 'amounts':[1000000, 17000000, 3.99]},
            ]
        file_write(donors)
    return

def file_write(donors):
    with open(donors_file, 'wb') as donorsFile:
        pickle.dump(donors, donorsFile)
    print("***File updated!***\n")
    return


def send_thank_you():
    global donors
    donor_name = input(
        "Enter the donor's name or "
        "type 'list' to get list of current doners:\n> "
    )
    if donor_name == "list":
        for donor in donors:
            print(donor['donor'])
        print("")
        return
    existing_donor = "new"
    for index, donor in enumerate(donors):
        if donor_name == donor['donor']:
            existing_donor = index
            break
    donation_amount = input(
        'Please enter a donation amount: ')
    try:
        donation_amount = float(donation_amount)
    except ValueError:
        print("Value entered not a number")
        print("returning to menu")
        return
    if existing_donor == "new":
        donors.append({'donor': donor_name, 'amounts': [donation_amount]})
    else:
        donors[existing_donor]['amounts'].append(donation_amount)
    print('Thank you {} for your generous donation of {}\n'.format(
        donor_name, donation_amount))
    file_write(donors)
    return


def create_report():
    donorNameLen, givenLen, numGiftsLen, avgGiftsLen = [10], [11], [9], [12]
    for row in donors:
        donorNameLen.append(len(row['donor']))
        givenLen.append(len(str(sum(int(x) for x in row['amounts']))))
        numGiftsLen.append(len(str(len(row['amounts']))))
        avgGiftsLen.append(len(str(round(sum(int(x) for x in row['amounts']) / len(row['amounts'])))))
    print("{:<{}} |   {:<{}} | {:<{}} |   {:<{}}".format(
        'Donor Name', max(donorNameLen),
        'Total Given', max(givenLen),
        'Num Gifts', max(numGiftsLen),
        'Average Gift', max(avgGiftsLen)
        ))
    print("-"*(max(donorNameLen) + max(givenLen) + max(numGiftsLen) + max(avgGiftsLen) + 13))
    for donateTotal in donors:
        donateTotal['totalDonated'] = sum(int(x) for x in donateTotal['amounts'])
    sortedList = sorted(donors, key=lambda k: k['totalDonated'], reverse=True)
    for donor in sortedList:
        print("{:<{}} | $ {:<{}} | {:<{}} | $ {:<{}}".format(
        donor['donor'], max(donorNameLen),
        sum(int(x) for x in donor['amounts']), max(givenLen),
        len(donor['amounts']), max(numGiftsLen),
        round(sum(int(x) for x in donor['amounts']) / len(donor['amounts'])), max(avgGiftsLen)
        ))
    print("")
    return


def exit_program():
    print("Exiting")
    sys.exit()


if __name__ == '__main__':
    file_init()

    options = {
        "1": send_thank_you,
        "2": create_report,
        "3": exit_program,
    }

    while True:
        selection = input(
            "Please select \n"
            "1) Send a Thank You\n"
            "2) Create a Report\n"
            "3) Quit\n"
            "> ")
        options[selection]()

