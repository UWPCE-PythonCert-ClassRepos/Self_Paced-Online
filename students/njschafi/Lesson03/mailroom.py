#!/usr/bin/env python3

# NEIMA SCHAFI, LESSON 3 Assignment - mailroom part1

#Using lists as the data structure since they are mutable (can change the contents).
donors = [
    ['Leon Dechino',200.43,30.23,1.50], ['Rupert Everton',23.99],
    ['Zordon Lagasse',400.00, 500.00, 600.00],
    ['Kavinsky Mega', 23.23,100.45], ['Corey Camelot', 1.00, 2.00]
    ]
donor_names = [x[0] for x in donors] ## puts all names into a sequence

def menu():
    """Main menu function which user can select one of the options shown"""
    while True:
        selection = input('\nPlease select one of the following actions (select number):\n 1. Send a Thank You\n'
                        ' 2. Create a Report\n 3. Quit\n Your selection: ')
        try:
            int(selection)
        except: #throws error if not a numeric option
            print('Not a valid option.')
        else:
            if int(selection) == 1:
                thank_you()
            elif int(selection) == 2:
                report()
            elif int(selection) == 3:
                SystemExit(0)


def thank_you():
    """Function which tests if name inputted is in a list or not,adds the name if not on the list then calls donation function"""
    name = input('Please enter a full name or enter "list" for'
                'list of names or enter "Menu" to return to main prompt: ')
    while name.isdigit() or name == "":
        name = input('\nNot a valid name. Please enter a full name or enter "list"'
                    'for list of names or enter "Menu" to return to main prompt: ')
    if name.title() == "Menu": menu()
    elif name.lower() == "list":
        name_list()
    elif name.title() not in donor_names:
        #If the user types a name not in the list, add that name to the data structure and use it.
        donors.append([name.title()])
        donor_names.append(name.title()) ##Name needs to show up in both lists
        donate(name.title(), 0)
    elif name.title() in donorNames:
        donate(name.title(), 1) #If the user types a name in the list, use it.


def name_list():
    """Prints the names in the donors list"""
    for names in donor_names:
        print(names)
    thank_you()


def donate(n, t):
    """Adds donated amount to donors running amount then calls email function to print thank you"""
#Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    donation = input('Enter donation amount or enter "Menu" to return to main prompt: ')
    while donation == "":
        donation = input('\nNo amount entered. Please enter donation amount'
                        'or enter "Menu" to return to main prompt: ')
    if donation.title() == "Menu": menu()
    elif t == 1: #Case that the name exists already in donors list
        donation = float(donation)
        for n2 in donors:
            if n2[0] == n:
                n2.append(donation)
                email(n,donation)
    else: #Case that the name DOESNT exist so need to add user with donation
        donation = float(donation)
        donors.append([n,donation])
        email(n,donation)


def email(name, donation):
    """Writes thank you email to donor for given amount"""
    print('\nDear {}, \n\tThank you for your generous ${:.2f} donation.'
            '\n\tYou are an amazing person. Good job!'.format(name.title(), donation))
    menu()


def report():
    """Prints table of donors"""
    d2=[]
    for i in donors:
        if len(i) == 1: #for donor with 0 donations
            d2.append([i[0], 0, 0, 0])
        else:
            d2.append([i[0], sum(i[1:]), len(i[1:]), (sum(i[1:])/len(i[1:]))])
    d2.sort(key=lambda x:x[1], reverse = True)
    print('{:25} | {:>15} | {:9} | {:>14}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*73)
    for names in d2:
            print('{:25} | ${:>14.2f} | {:9} | ${:14.2f}'.format(names[0],
                    names[1], names[2], names[3]))
    menu()


if __name__ == '__main__':
    menu()
