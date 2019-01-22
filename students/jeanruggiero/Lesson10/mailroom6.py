#!/usr/bin/env python
# This script maintains a databse of donors including name and donation amounts
import statistics
import datetime

# Define exceptions to exit script and return to main menu
class ExitScript(Exception): pass
class MainMenu(Exception): pass

# Create a dict that contains the donors and a history of the amounts they have
# donated
donors = {
    'han solo': {'name': 'Han Solo',
        'donations': [3468.34, 457, 34.2]},
    'luke skywalker': {'name': 'Luke Skywalker',
        'donations': [5286286.3, 567, 23.5678]},
    'chewbacca': {'name': 'Chewbacca',
        'donations': [432, 679.4553]},
    'princess leia': {'name': 'Princess Leia',
        'donations':[5.3434]},
    'bobba fett, bounty hunter': {'name': 'Bobba Fett, Bounty Hunter',
        'donations': [67]},
    }

# Define main menu functions
def add_donation(name='',amount='0'):
    """Add a donation to donors dict and compose a thank you email."""
    # If the user selects 1, prompt for the name of a donor and a
    # donation amount.
    try:
        while True:
            # Ask for user input for name if file run as executable
            if __name__ == '__main__':
                name = input("Enter the donor's Full Name, or 'list': ")
            # Break out of the loop once a donor name has been added to the
            # donors dict
            if donor_name(name):
                break

        while True:
            # Ask for user input for amount if file run as executable
            if __name__ == '__main__':
                amount = input('Enter the donation amount: ')
            # Break out of the loop once an appropriate donation amount has
            # been provided and added to donors dict
            if donor_amount(amount,name):
                break

        # Compose a thank you email and print to command line
        print(); print(compose_email(name.lower())); print()
        return True

    except MainMenu:
        pass

def create_report():
    """Print a report of donors with a summary of their donation history."""

    # Determine table size_report
    table_size = size_report(donors)
    sorted_keys = sort_donors()

    # Build format strings for header and table rows
    head_string = '{:{}s} | {:^{}s} | {:^{}s} | {:^{}s}'
    row_string  = '{:{}s} | $ {:>{}.2f} | {:>{}d} | $ {:>{}.2f}'

    # Print table header
    # Add 2 to width of dollar value fields to account for dollar sign, space
    print(head_string.format('Donor Name', table_size[0], 'Total Given',
        table_size[1]+2, 'Num Gifts', table_size[2], 'Average Gift',
        table_size[3]+2))
    print('-'*(sum(table_size) + 13))

    # Print table rows
    for key in sorted_keys:
        name = donors[key]['name']
        donations = donors[key]['donations']

        print(row_string.format(name, table_size[0], sum(donations),
        table_size[1], len(donations), table_size[2],
        statistics.mean(donations), table_size[3]))

def send_letters():
    """Send letters to all donors thanking them for most recent donation."""
    for donor,info in donors.items():
        filename = build_filename(info)
        # Create one thank you letter file per donor
        with open(filename, 'w') as f:
            f.write(compose_email(donor))
        f.closed

def quit():
    raise ExitScript

# Define sub-functions
def build_filename(info):
    """Build up a filename for a thankyou letter to a donor."""
    d = datetime.date.today()
    # Build file name using donor name and today's date separated by _
    filename = '_'.join([info['name'].replace(' ','_'), str(d.month),
        str(d.day), str(d.year)])+'.txt'
    return filename

def donor_name(name):
    """Add a donor name to the donors dict or display list of donors."""
    if name.lower() == 'return':
        raise MainMenu
    elif name.lower() == 'list':
        # If the user enters list, display a list of donor names
        print_names()
    else:
        # If the user enters a name, add it to the donors dict
        # structure if not already there.
        donors.setdefault(name.lower(),{'name': name, 'donations': []})
        return True

def donor_amount(amount,name):
    """Add a donation amount to the donors dict for donor name."""
    if amount.lower() == 'return':
        raise MainMenu

    try:
        # Try to add donation amount to donors data structure
        amount = float(amount)
        donors[name.lower()]['donations'].append(amount)
        return True
    except ValueError:
        # If value is not a number, ask the user to enter a number
        print('Please enter a number value for donation amount.')

def print_names():
    """Print the list of donor names in alphabetical order."""
    for donor in sorted(donors):
        print(donors[donor]['name'])

def compose_email(donor):
    """Print an email to the command line thanking donor name for a donation
    of amount."""
    name=donors[donor.lower()]['name']
    amount=donors[donor.lower()]['donations'][-1]
    total = sum(donors[donor]['donations'])
    balance = 1000000000-total
    return f"""
        Dear {name},\n
        Thank you so much for your generous donation of ${amount:.2f}.\n
        We really appreciate your donations totalling ${total:.2f}. You are
        ${balance:.2f} away from a gift of Spaceballs: The Flamethrower!\n
        Sincerely, The Wookie Foundation
        """

def size_report(in_dict):
    """Determine column widths for a donor report."""
    # Determine width of columns based on data in donors data structure
    # Convert numbers to strings to determine their length in characters
    # Convert the dollar amounts to an integer to remove decimal places (since
        # there are an unknown number of them), then add 3 to the length to
        # accomodate for a period and 2 decimal places
    # Ensure column size is at least as wide as header text

    name_width = max(len(name) for name in in_dict)
    name_width = max(name_width, len('Donor Name'))

    total_width = max(len(str(int(sum(value['donations'])))) for value in
        in_dict.values())+3
    total_width = max(total_width, len('Total Given'))

    num_width = max(len(str(len(value['donations']))) for value in
        in_dict.values())
    num_width = max(num_width, len('Num Gifts'))

    avg_width = max(len(str(int(statistics.mean(value['donations'])))) for
        value in in_dict.values())+3
    avg_width = max(avg_width, len('Average Gift'))

    return [name_width, total_width, num_width, avg_width]

def sort_donors():
    """Sort donors dict in order of total amount donated."""
    return sorted(donors,key=sort_fun, reverse=True)

def sort_fun(x):
    """"Sort function for use in sort_donors. x is a value in donors
    (type dict)"""
    return sum(donors[x]['donations'])

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
        except TypeError:
            continue
