#!/usr/bin/env python3

## NEIMA SCHAFI, LESSON 3 Assignment - mailroom part1

##Using lists as the data structure since they are mutable (can change the contents).
donors = [['Leon Dechino',200.43,30.23,1.50],['Rupert Everton',23.99],['Zordon Lagasse',400.00, 500.00, 600.00],['Kavinsky Mega', 23.23,100.45],['Corey Camelot', 1.00, 2.00]]
donorNames = [x[0] for x in donors] ## puts all names into a sequence
def menu():
    """Main menu function which user can select one of the options shown"""
    selection = input('\nPlease select one of the following actions (select number):\n 1. Send a Thank You\n 2. Create a Report\n 3. Quit\n Your selection: ')
    while selection.isdigit() == False or int(selection) <= 0 or int(selection) > 3:
        selection = input('\nNot a valid option.\n\nPlease select one of the following actions (select number):\n 1. Send a Thank You\n 2. Create a Report\n 3. Quit\n Your selection: ')
##Based on selection, now will call up correct function
    if int(selection) == 1:
        thankYou()
    elif int(selection) == 2:
        report()
    else:
        SystemExit(0)

def thankYou():
    """Function which tests if name inputted is in a list or not, adds the name if not on the list then calls donation function"""
    name = input('Please enter a full name or enter "list" for list of names or enter "Menu" to return to main prompt: ')
    while name.isdigit() or name == "":
        name = input('\nNot a valid name. Please enter a full name or enter "list" for list of names or enter "Menu" to return to main prompt: ')
    if name.title() == "Menu": menu()
    elif name.lower() == "list": namelist()
    elif name.title() not in donorNames:
        #If the user types a name not in the list, add that name to the data structure and use it.
        donors.append([name.title()])
        donorNames.append(name.title()) ##Name needs to show up in both lists
        donate(name.title(),0)
    elif name.title() in donorNames: donate(name.title(),1) #If the user types a name in the list, use it.

def namelist():
    """Prints the names in the donors list"""
    for names in donorNames:
        print(names)
    thankYou()

def donate(n,t):
    """Adds donated amount to donors running amount then calls email function to print thank you"""
# Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    donation = input('Enter donation amount or enter "Menu" to return to main prompt: ')
    while donation == "":
        donation = input('\nNo amount entered. Please enter donation amount or enter "Menu" to return to main prompt: ')
    if donation.title() == "Menu": menu()
    elif t == 1: ##Case that the name exists already in donors list
        donation = float(donation)
        print(donors)
        for n2 in donors:
            if n2[0] == n:
                n2.append(donation)
                email(n,donation)
    else: ##Case that the name DOESNT exist so need to add user with donation
        donation = float(donation)
        donors.append([n,donation])
        email(n,donation)

def email(name,donation):
    """Writes thank you email to donor for given amount"""
    print('\nDear {}, \n\tThank you for your generous ${:.2f} donation.\n\tYou are an amazing person. Good job!'.format(name.title(),donation))
    menu()

def report():
    """Prints table of donors"""
    print('{:25} | {:>15} | {:9} | {:>14}'.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print('-'*73)
    for names in donors:
        if len(names) == 1: ####IN CASE DONOR HAS GIVEN 0 DONATIONS - this can happen if user inputs name not on list then returns to orignal menu without supplying a donation amount
            print('{:25} | ${:>14.2f} | {:9} | ${:14.2f}'.format(names[0],0,0,0))
        else:
            print('{:25} | ${:>14.2f} | {:9} | ${:14.2f}'.format(names[0],sum(names[1:]),len(names[1:]),(sum(names[1:])/len(names[1:]))))
    menu()

if __name__ == '__main__':
    menu()
