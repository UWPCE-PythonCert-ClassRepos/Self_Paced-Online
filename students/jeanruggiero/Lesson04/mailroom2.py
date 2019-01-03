#!/usr/bin/env python
# This script maintains a databse of donors including name and donation amounts
import statistics

# Define exceptions to exit script and return to main menu
class ExitScript(Exception): pass
class MainMenu(Exception): pass

# Create a dict that contains the donors and a history of the amounts they have
# donated
donors = {
'han solo': {'name': 'Han Solo', 'donations': [3468.34, 457, 34.2]},
'luke skywalker': {'name': 'Luke Skywalker', 'donations': [5286286.3, 567, 23.5678]},
'chewbacca': {'name': 'Chewbacca', 'donations': [432, 679.4553]},
'princess leia': {'name': 'Princess Leia', 'donations':[5.3434]},
'bobba fett, bounty hunter': {'name': 'bobba fett, bounty hunter', 'donations': [67]},
}

# Define main menu functions
def add_donation():
    """Add a donation to donors dict and compose a thank you email."""
    # If the user selects 1, prompt for the name of a donor and a
    # donation amount.
    try:
        while True:
            name = input("Enter the donor's Full Name, or 'list': ")

            if name.lower() == 'return':
                raise MainMenu
            elif name.lower() == 'list':
                # If the user enters list, display a list of donor names
                print_names()
            else:
                # If the user enters a name, add it to the donors dict structure if
                # not already there.
                donations = donors.setdefault(name.lower(),{'name': name, 'donations': []})
                break

        while True:
            amount = input('Enter the donation amount: ')

            if amount.lower() == 'return':
                raise MainMenu

            try:
                # Try to add donation amount to donors data structure
                amount = float(amount)
                donors[name][donations].append(amount)
                break
            except ValueError:
                # If value is not a number, ask the user to enter a number
                print('Please enter a number value for donation amount.')

        # Compose a thank you email and print to command line
        compose_email(name, amount)

    except MainMenu:
        pass

def create_report():
    """Print a report of donors with a summary of their donation history."""

    # Determine table size_report
    table_size = size_report()
    sort_donors()

    # Build format strings for header and table rows
    head_string = '{:{}s} | {:^{}s} | {:^{}s} | {:^{}s}'
    row_string  = '{:{}s} | $ {:>{}.2f} | {:>{}d} | $ {:>{}.2f}'

    # Print table header
    # Add 2 to width of dollar value fields to account for dollar sign and space
    print(head_string.format('Donor Name', table_size[0], 'Total Given', \
    table_size[1]+2, 'Num Gifts', table_size[2], 'Average Gift', table_size[3]+2))
    print('-'*(sum(table_size) + 13))

    # Print table rows
    for name, donations in donors.items():
        print(row_string.format(name, table_size[0], sum(donations),\
        table_size[1], len(donor[1]), table_size[2], statistics.mean(donor[1]),\
        table_size[3]))

def send_letters():
    pass

def quit():
    raise ExitScript

# Define sub-functions
def print_names():
    """Print the list of donor names."""
    for donor in donors:
        print(donor.title())

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
        # accomodate for a period and 2 decimal places
    # Ensure column size is at least as wide as header text

    name_width = max(len(name) for name in donors)
    name_width = max(name_width, len('Donor Name'))

    total_width = max(len(str(int(sum(value)))) for value in donors.values())+3
    total_width = max(total_width, len('Total Given'))

    num_width = max(len(str(len(value))) for value in donors.values())
    num_width = max(num_width, len('Num Gifts'))

    avg_width = max(len(str(int(statistics.mean(value)))) for value in donors.values())+3
    avg_width = max(avg_width, len('Average Gift'))

    return [name_width, total_width, num_width, avg_width]

def sort_donors():
    """Sort donors dict in order of total amount donated."""
    totals = []
    for name, donations in donors.items():
        totals.append(sum(donations))
    zip(totals,donors).sort()
    print(totals)


# Dict of possible main menu actions the user can select
actions = {
'1': add_donation,
'2': create_report,
'3': send_letters,
'4': quit
}


# User interaction
if __name__ == '__main__':
    while True:
        try:
            # Main menu - prompt user for an action
            print(); print('Select an action to perform...')
            print('Type "return" at any time to return to main menu.')
            action = input('1: Send a Thank You\n2: Create a Report\n' +\
            '3: Send Letters to Everyone\n4: Quit\n')

            actions.get(action)()
        except ExitScript:
            break
