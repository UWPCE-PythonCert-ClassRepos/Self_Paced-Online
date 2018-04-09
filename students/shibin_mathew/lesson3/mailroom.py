#!/usr/bin/env python3
import sys


def option_one():
    #  Function to Send a Thank You Email
    program_quit = False
    while not program_quit:
        name = input("Please input your full name\n")
        if name == "list":
            print("list of names")
            for names in donors:
                print(names['name'])
            name = input("Please select from the list or add a new name\n")
            if name != 'quit':
                donation = input("Please enter a donation amount\n")
                if donation != 'quit':
                    for names in donors:
                        if names['name'] == name:
                            names['donation'].append(float(donation))
                    print(donors)  # Debug
                    break  # break out of the while loop
                else:
                    break  # quit has been initialized
            else:
                program_quit = True
        elif name == 'quit':
            break
        else:
            donation = input("Please enter a donation amount\n")
            if donation == 'quit':
                break
            else:
                donation = float(donation)
                if not any(i['name'] == name for i in donors):
                    donors.append({'name': name, 'donation': [donation]})
                else:
                    for names in donors:
                        if names['name'] == name:
                            names['donation'].append(float(donation))
                print(donors)  # Debug
                break  # break out of the while loop


def option_two():
    #  Function to create a report
    print("hello")
    print("{: <20s}{: ^4s}{: <10s}{: ^4s}{: <10s}{: ^4s}{: <10s}"
          .format('Donor Name', '|', 'Total Given', '|',
                  'Num Gifts', '|', 'Average Gift'))
    print('-' * 70)
    print(' ')
    for names in donors:
        print("{: <24s}{: <2s}{: >10}{: >13}{: >6s}{: >11}"
              .format(names['name'], '$', round(sum(names['donation']), 2),
                      len(names['donation']), '$',
                      round(sum(names['donation'])/len(names['donation']), 2)))


def question_module():
    #  Function that acts as the main gate into the app
    program_quit = False
    while not program_quit:
        user_response = input("Please choose from the following choices: "
                              "1. Send a Thank You, 2. Create a Report, 3. quit\n")
        if user_response == "1" or user_response == "Send a Thank You":
            option_one()
        elif user_response == "2" or user_response == "Create a Report":
            option_two()
        elif user_response == "3" or user_response == "quit":
            print('Thanks for using this application!')
            sys.exit()
        else:
            print("Please pick from one of the choices")


if __name__ == "__main__":
    donors = [{'name': 'Shibin', 'donation': [25.25, 456.21]},
              {'name': 'Kimberly', 'donation': [125.50, 5.55, 14.5]},
              {'name': 'Andreck',
               'donation': [1250, 50, 1555]}, {'name': 'Jordy', 'donation':
              [55, 25, 4.50]}, {'name': 'Nelly', 'donation': [254.2, 500, 125]}]
    question_module()
