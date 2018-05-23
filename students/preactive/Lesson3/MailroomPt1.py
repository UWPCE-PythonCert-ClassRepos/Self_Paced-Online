#!/usr/bin/env python3
import sys


donors = [
    {'donor':'Hutch', 'amounts':[10, 15, 75.75] },
    {'donor':'Carlton', 'amounts':[32, 19000.01]},
    {'donor':'William Gates, III', 'amounts':[1000000, 17000000, 3.99]},
    ]



def userPrompt():
    choice = input(
        'Pick one:\n1) Send a thank you\n2) Create a Report\n3) Quit\n>')
    while choice not in ['1', '2', '3']:
        choice = input(
            'Pick one:\n1) Send a thank you\n2) Create a Report\n 3) Quit\n>')
    return main(choice)


def thankYou():
    donor_name = input("Enter the donor's name or type 'list' to get list of current doners:\n>")
    if donor_name == "list":
        for donor in donors:
            print(donor[0])
        print("")
        return userPrompt()
    existingDonor = "new"
    for index, donor in enumerate(donors):
        if donor_name == donor['donor']:
            existingDonor = index
    donation_amount = input(
        'Please enter a donation amount: ')
    if existingDonor == "new":
        print(1)
        donors.append({'donor':donor_name, 'amounts':[donation_amount]})
    if not existingDonor == "new":
        print(2)
        donors[existingDonor]['amounts'].append(donation_amount)
    print('Thank you {} for yout generous donation of {}\n'.format(
        donor_name, donation_amount))
    userPrompt()


def createReport():
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
    userPrompt()

def main(users_choice):
    if users_choice == False:
        users_choice = userPrompt()
    if users_choice == '1':
        thankYou()
    elif users_choice == '2':
        createReport()
    else:
        sys.exit()


if __name__ == '__main__':
    main(False)
