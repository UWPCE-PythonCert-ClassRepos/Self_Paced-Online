#!/usr/bin/env python

# This script maintains a databse of donors including name and donation amounts

# Create a data structure that contains the donors an a history of the amounts
# they have donated
donors = (\
('Han Solo', [3468.34, 457, 34.2]),\
('Luke Skywalker', [5286286.3, 567, 23.5678]),\
('Chewbacca', [432, 679.4553]),\
('Princess Leia', [5.3434]))

# Define functions
def print_names():
    """Print the list of donor names."""
    for donor in donors:
        print(donor[0])

def find_donor(name):
    """Find donor by name in donors and return corresponding row index."""
    for index,donor in enumerate(donors):
        if donor[0].lower() == name.lower():
            return index

def add_donation(name, amount):
    """This function adds a donation amount to the donors data structure under
    the donor name specified."""
    donors[find_donor(name)][1].append(amount)

def compose_email(name, amount):
    """This function prints an email to the command line thanking donor name
    for a donation of amount."""
    form_str = 'Dear {:s},\n Thank you so much for your generous donation of ${:.2f}.\n Sincerely, The Wookie Foundation'
    print(form_str.format(name.title(), amount))


# User interaction
if __name__ == '__main__':
    while True:
        print('Select an action to perform...')
        action = input('1: Send a Thank You | 2: Create a Report | 3: Quit\n')

        if action == '3':
            # If the user selects 3, quit the program
            break
        elif action == '1':
            # If the user selects 1, prompt for the name of a donor and a
            # donation amount.
            while True:
                name = input("Enter the donor's Full Name, or 'list': ")

                if name == 'list':
                    # If the user enters list, display a list of donor names
                    print_names()
                else:
                    # If the user enters a name, add it to the donors data
                    # structure if not already there.
                    if name.lower() not in (donor[0].lower() for donor in donors):
                        donors.append((name, []))
                    break

            while True:
                amount = input('Enter the donation amount: ')

                try:
                    # Try to add donation amount to donors data structure
                    amount = float(amount)
                    add_donation(name, amount)
                    break
                except ValueError:
                    # If value is not a number, ask the user to enter a number
                    amount = input('Please enter a number value for donation amount: ')

            # Compose a thank you email and print to command line
            compose_email(name, amount)

        elif action == '2':
            print('Still working on it!')
