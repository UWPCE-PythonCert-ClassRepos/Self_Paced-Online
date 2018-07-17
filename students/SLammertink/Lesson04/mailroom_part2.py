#! /usr/bin/env python3
# Author: SLammertink
# Lesson 4 mailroom part 2 exercise

'''
Update your mailroom program to:

Use dicts where appropriate
See if you can use a dict to switch between the users selections. See Using a Dictionary to switch for what this means.
Try to use a dict and the .format() method to do the letter as one big template rather than building up a big string in parts.
'''

import collections
import pathlib

donors = collections.defaultdict(list)

# Create the switch dictionary:
switch_dict = { "1" : "Sending a Thank You" , "2" : "Creating a Report", "3" : "Send letters to everyone", "4" : "Quit"}
donors = {'Sukhmani Travers': [250 ,125, 1000], 'Sebastien Mayo': [500, 35], 'Aryan Davila' : [25, 45, 55, 120], 'Zayan Langley' : [ 1000, 10, 250], 'Charlotte Bates' : [25, 10, 5, 35, 75, 100] }

def pretty():
    ''' a function that adds lines and spaces, just for the looks '''
    print('')
    print('{:-<43}'.format(''))
    print('')

def switch():
    ''' a function that ask the user to input a number that
    corresponds to an action that will be executed '''
    pretty()
    while True:
        print("Please choose from the following menu: \n")
        for k, v in switch_dict.items():
            print(k, v)
        pretty()
        choice = input("Please enter the choice you want to make: ")
        pretty()
        if choice == "list":
            print("List of current donors:\n-----------------------\n")
            for k in donors.keys():
                print(k)
        else:
            switches[choice]()
        pretty()


def sending_a_thank_you():
    '''Checks whether is name is in the name dictionary if not
    it adds it, then will ask the user for a donation and adds it to that users dictionary '''
    input_name = input("Please enter the donor's name: ")
    if input_name not in donors:
        print('')
        print("That name is not in the donor list, will add it now.") # notify the user that the name will be added to the list
        print('')
        donors[input_name] = [] # Creates a new list for that user name where the donation will be stored
        print('')
        print("Adding {} now to the donor list".format(input_name))
        print('')
        input_don = int(input("How much would you like to donate? \n"))
        donors[input_name].append(input_don) # adds the donation to the users list

    elif input_name in donors:
        print('')
        input_don = int(input("How much is the donation: "))
        donors[input_name].append(input_don)
        print('')
        print("Sending email ----->") # pretending to send the email
        print("Thank you {} for your generous donation!".format(input_name)) # format the email message
        print('')


def creating_a_report():
    ''' a function that will create a simple report '''
    print("{:^30}{:5}{:^25}{:5}{:^30}{:5}{:^20}{:5}".format('Name', '|', 'Donation','|', 'Number of gifts','|', 'Average gift', '|'))
    print("{:-<116}".format(''))
    print(' ')
    for k, v in donors.items():
        print("{:35}${:^25.2f}{:^35}${:^20.2f}".format(k, sum(donors[k]), len(donors[k]), (sum(donors[k]) / len(donors[k]))))

def sending_letters_to_everyone():
    ''' a function that will save a .txt file for every donor in the list in the current directory '''
    for k, v in donors.items():
        with open('{}.txt'.format(k), 'w') as f:
            f.write("\n\n\tDear {},\n\n\tThank you for your very nice donation of ${}.\n\n\tIt wil be put to a good use.\n\n\t\tSincerely,\n\t\t---------\n\t\t-The team\n".format(k, sum(donors[k]) ))


def quit():
    ''' a function to exit the program '''
    print("Exiting the program now, bye bye! ")
    pretty()
    exit()


switches = { "1" : sending_a_thank_you, "2" : creating_a_report, "3" : sending_letters_to_everyone, "4" : quit }

# main program

if __name__ == '__main__':
    switch()

