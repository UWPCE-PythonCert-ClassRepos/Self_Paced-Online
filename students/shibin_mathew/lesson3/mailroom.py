#!/usr/bin/env python3
import sys


def optionOne():
    # Function to Send a Thank You Email
    quit = False
    while not quit:
        print("Please input your full name")
        name = input()
        if name == "list":
            print("list of names")
            for names in donors:
                print(names['name'])
            print("Please select from the list or add a new name")
            name = input()
            if name != 'quit':
                print("Please enter a donation amount")
                donation = input()
                if donation != 'quit':
                    for names in donors:
                        if names['name'] == name:
                            names['donation'].append(float(donation))
                    print(donors)  # Debug
                    quit = True
                else:
                    quit = True
            else:
                quit = True
        elif name == 'quit':
            quit = True
        else:
            print("Please enter a donation amount")
            donation = float(input())
            if donation != 'quit':
                donors.append({'name': name, 'donation': [donation]})
                print(donors)  # Debug
                quit = True
            else:
                quit = True


def optionTwo():
    #  Function to create a report
    print("hello")
    print("{: <20s}{: ^4s}{: <10s}{: ^4s}{: <10s}{: ^4s}{: <10s}"
            .format('Donor Name', '|', 'Total Given', '|',
            'Num Gifts', '|', 'Average Gift'))
    print('-'*70)
    print(' ')
    for names in donors:
        print("{: <24s}{: <2s}{: >10}{: >13}{: >6s}{: >11}"
            .format(names['name'], '$', round(sum(names['donation']), 2),
                len(names['donation']), '$',
                round(sum(names['donation'])/len(names['donation']), 2)))
    questionModule()


def questionModule():
    #  Function that acts as the main gate into the app
    quit = False
    while not quit:
        print("Please choose from the following choics: Send a Thank You, Create a Report or quit")
        userResponse = input()
        if userResponse == "Send a Thank You":
            optionOne()
        elif userResponse == "Create a Report":
            optionTwo()
        elif userResponse == 'quit':
            print('Thanks for using this application!')
            quit = True
            sys.exit()
        else:
            print("Please pick from one of the choices")


if __name__ == "__main__":
    donors = [{'name': 'Shibin', 'donation': [25.25, 456.21]},
        {'name': 'Kimberly', 'donation': [125.50, 5.55, 14.5]},
        {'name': 'Andreck',
        'donation': [1250, 50, 1555]}, {'name': 'Jordy', 'donation':
        [55, 25, 4.50]}, {'name': 'Nelly', 'donation': [254.2, 500, 125]}]
    questionModule()
