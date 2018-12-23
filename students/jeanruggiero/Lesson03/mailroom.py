#!/usr/bin/env python
import statistics

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
    """Add a donation amount to the donors data structure under the donor name
    specified."""
    donors[find_donor(name)][1].append(amount)

def compose_email(name, amount):
    """Print an email to the command line thanking donor name for a donation
    of amount."""
    form_str = 'Dear {:s},\n Thank you so much for your generous donation of ${:.2f}.\n Sincerely, The Wookie Foundation'
    print(); print(form_str.format(name.title(), amount)); print()

def size_report():
    """Determine column widths for a donor report."""
    # Determine width of columns based on data in donors data structure
    # Convert numbers to strings to determine their length in characters
    # Convert the dollar amounts to an integer to remove decimal places (since
        # there are an unknown number of them), then add 3 to the length to
        # accomodate for a period, dollar sign, space, and 2 decimal places
    # Ensure column size is at least as wide as header text

    name_width = max(len(donor[0]) for donor in donors)
    name_width = max(name_width, len('Donor Name'))

    total_width = max(len(str(int(sum(donor[1])))) for donor in donors)+3
    total_width = max(total_width, len('Total Given'))

    num_width = max(len(str(len(donor[1]))) for donor in donors)
    num_width = max(num_width, len('Num Gifts'))

    avg_width = max(len(str(int(statistics.mean(donor[1])))) for donor in donors)+3
    avg_width = max(avg_width, len('Average Gift'))

    return [name_width, total_width, num_width, avg_width]


def create_report():
    """Print a report of donors with a summary of their donation history."""

    # Determine table size_report
    table_size = size_report()

    # Build format strings for header and table rows
    head_string = '{:{}s} | {:^{}s} | {:^{}s} | {:^{}s}'
    row_string  = '{:{}s} | $ {:>{}.2f} | {:>{}d} | $ {:>{}.2f}'

    # Print table header
    # Add 2 to width of dollar value fields to account for dollar sign and space
    print(head_string.format('Donor Name', table_size[0], 'Total Given', \
    table_size[1]+2, 'Num Gifts', table_size[2], 'Average Gift', table_size[3]+2))
    print('-'*(sum(table_size) + 13))

    # Print table rows
    for donor in donors:
        print(row_string.format(donor[0], table_size[0], sum(donor[1]), \
        table_size[1], len(donor[1]), table_size[2], statistics.mean(donor[1]), \
        table_size[3]))


# User interaction
if __name__ == '__main__':
    while True:
        print(); print('Select an action to perform...')
        print("Type 'quit' at any time to exit.")
        action = input('1: Send a Thank You | 2: Create a Report | 3: Quit\n')

        if action == '3' or action.lower() == 'quit':
            # If the user selects 3, quit the program
            break
        elif action == '1':
            # If the user selects 1, prompt for the name of a donor and a
            # donation amount.
            while True:
                name = input("Enter the donor's Full Name, or 'list': ")

                if name.lower() == 'quit':
                    break
                elif name == 'list':
                    # If the user enters list, display a list of donor names
                    print_names()
                else:
                    # If the user enters a name, add it to the donors data
                    # structure if not already there.
                    if name.lower() not in (donor[0].lower() for donor in donors):
                        donors = (*donors, (name, []))
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
            create_report()
