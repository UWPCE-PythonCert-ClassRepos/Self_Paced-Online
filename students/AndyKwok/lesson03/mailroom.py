# Description: Mailroom Program (Database Organizer)
# Author: Andy Kwok
# Last Updated: 07/14/2018
# ChangeLog: 
# v1.0 - Initialization

#!/usr/bin/env python3

if __name__ == '__main__':
    database = [['Donor A', [2300.30, 1000.01, 2000.00], 5300.31],
                ['Donor B', [1394.12], 1394.12],
                ['Donor C', [14349.00, 175.95], 145324.95],
                ['Donor D', [42800.11, 1500.04, 3534.20], 47834.35],
                ['Donor E', [12312.23, 250.50], 12562.73]]

def database_print(database):
    """ Function to display donor's information in a table format
    donor: individual donor info
    database: donor's name and donation amount and frequency in a list
    """
    print('Donor Name' + ' '*10 + '| Total Given' + ' '*5 + '| Num Gifts' + ' '*5 + '| Average Gift')
    print('-'*75)
    for donor in database:
        donor[2] = sum(donor[1])
        print('{:20} '.format(donor[0]) + '$ {:>10.2f} {:7}'.format(donor[2], len(donor[1])) + ' '*14 + '$ {:>10.2f}'.format(donor[2]/len(donor[1])))
        
def sort_databse(database):
    """ Function to sort the database
    database: donor's name and donation amount in a list
    donor: individual donor info
    """
    for donor in database:
        donor[2] = sum(donor[1])
    database = sorted(database, key=lambda x: x[2], reverse=True)
    return database

def add_donation(name, database, location):
    """ Function to add new donation to the database
    name: new/edit existing donor's name
    database: donor's name and donation amount in a list
    location: donor index location in the database 
    donation: new donation amount
    add_list: donor's name, donation amount to be added to the database
    """
    donation = float(input('How much does {} want to donate? '.format(name)))
    if location == len(database):
        #Add entry
        add_list = [[name, [donation], donation]]
        database += add_list
    else:
        #edit entry
        add_list = database[location]
        add_list[1] += [donation]
        database[location] = add_list
    send_thank_you(name, donation)
    return database

def send_thank_you(name, donation):
    print('To {},'.format(name) + '\n' +
    'Thank you for your donation of ${:.2f}.'.format(donation) + '\n'*2 +
    '\t'*5 + '-System Generated Email')

option = 'start'
while option.lower() != 'quit':
    # Main menu   
    print(
        '''    
        > Sent a Thank you
        > Create a Report
        > quit
        '''
        )
    option = input('Please select an option> ')
    if option.lower() == 'sent a thank you':
        entry = input('Enter donor\'s name to search or \'list\' to show all donors> ')
        if entry == 'list':
            # Display database
            database_print(database)
        else:
            name_id = None
            for counter, donor in enumerate(database):
                # Search for donor match in list
                if entry.lower() == donor[0].lower():
                    name_id = counter
            if name_id == None:
                # Add new donor and donation to database
                name_id = len(database)
                database = add_donation(entry, database, name_id)
            else:
                # Edit existing donor donation to database
                database = add_donation(entry, database, name_id)
    elif option.lower() == 'create a report':
        # Sort and display database
        database = sort_databse(database)
        database_print(database)
                              
                    


