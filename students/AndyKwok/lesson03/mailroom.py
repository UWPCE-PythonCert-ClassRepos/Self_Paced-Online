# Description: Mailroom Program (Database Organizer)
# Author: Andy Kwok
# Last Updated: 07/14/2018
# ChangeLog: 
# v1.0 - Initialization


"""#!/usr/bin/env python3"""

def database_print(database):
    print('Donor Name' + ' '*10 + '| Total Given' + ' '*5 + '| Num Gifts' + ' '*5 + '| Average Gift')
    print('-'*75)    
    for donor in database:
        print('{:20} $ {:>10.2f} {:7}'.format(*donor) + ' '*14 + '$ {:>10.2f}'.format(donor[1]/donor[2]))    

def sort_databse(database):
    """
    """
    database = sorted(database, key=lambda x: x[1], reverse=True)
    return database

def add_donation(name, database, location):
    """
    """
    donation = float(input('How much does {} want to donate? '.format(name)))
    add_list = database[location]
    add_list[1] += donation
    add_list[2] += 1
    database[location] = add_list
    return database
    
if __name__ == '__main__':
    database = [['Donor A', 2300.30, 3],
                ['Donor B', 1394.12, 2],
                ['Donor C', 14349.00, 1],
                ['Donor D', 42800.11, 3],
                ['Donor E', 12312.23, 2]]
    

option = None
while option.lower() != 'quit':
    print(
        """    
        > Sent a Thank you
        > Create a Report
        > quit
        """
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
                database += [[entry, 0.0, 0]]
                database = add_donation(entry, database, name_id)
            else:
                # Edit existing donor donation to database
                database = add_donation(entry, database, name_id)
    elif option.lower() == 'create a report':
        # Sort and display database
        database = sort_databse(database)
        database_print(database)
                              
                    


