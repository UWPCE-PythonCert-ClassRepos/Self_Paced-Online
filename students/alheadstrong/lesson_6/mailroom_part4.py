import os
import sys


def is_name_list(donor_name):
    """Check if user input is string 'list'."""
    if donor_name == 'list':
        for d in ddb:  # display all donor names on user input 'list'
            print(d + ': ', ddb[d])
        return True
    else:
        return False


def is_name_existing(d):
    """Check if 'donor_name' value exists in global dict ddb, case insensitive."""
    for key in ddb.keys():
        if key.lower() == d['donor_name'].lower():
            return True
    else:
        return False


def add_donation_to_existing(d):
    """Add new value to existing value list in global dict ddb."""
    ddb[d['donor_name']].append(d['donation'])
    print('\nDonation added.')


def add_donation_to_new(d):
    """Add single key input dict to global dict ddb."""
    ddb[d['donor_name']] = [d['donation']]
    print('\nDonation added.')


def new_thank_you():
    """Add donation amount to new or existing donor and generate a thank you text."""
    while True:
        current_dict = {'donor_name': input("\nEnter donor name, or type 'list' for current donor list:")}
        if not is_name_list(current_dict['donor_name']):
            break
    if is_name_existing(current_dict):
        print(f"Donor name {current_dict['donor_name']} found in database.")
        while True:
            try:
                current_dict['donation'] = float(input('\nEnter new donation amount:'))
                break
            except ValueError:
                print("Input was not a number.")
        add_donation_to_existing(current_dict)
    else:
        print(f"Donor name not found. Will add {current_dict['donor_name']} to database.")
        while True:
            try:
                current_dict['donation'] = float(input('\nEnter donation amount:'))
                break
            except ValueError:
                print("Input was not a number.")
        add_donation_to_new(current_dict)

    print('\n\n', create_letter(current_dict))


def create_letter(d):
    """Return form letter string based on input dictionary. Dictionary needs 'donor_name' and 'donation' keys"""
    d['fleebs_floobed'] = round(d['donation']/20)
    return ('Dear {donor_name},'
            '\n\n\tThank you for your generous gift of ${donation:,.2f}.'
            '\n\tYour contribution will keep {fleebs_floobed} Fleebs floobing for an entire year.'
            '\n\tWe truly could not do this important work without you.'
            '\n\nSincerely,'
            '\nFleeb Freedom Now'.format(**d))


def generate_table_row(name, donation_list):
    """Take input name and donation list and returns a list of a single tuple of strings."""
    total_given = sum(donation_list)
    num_gifts = len(donation_list)
    try:
        average_gift = total_given / num_gifts
    except ZeroDivisionError:
        average_gift = '0'
    return [(name, '$' + str(total_given), str(num_gifts), '$' + str(average_gift))]


def create_report_table(d):
    """Take input dictionary and creates a sorted list of tuples based on key and values."""
    report_table_header = [("Donor Name", "Total Given", "Num Gifts", "Average Gift")]
    report_table = []

    for key in d.keys():  # read dict values into 2D list to be displayed.
        report_table += generate_table_row(key, d[key])

    report_table = report_table_header + sorted(report_table, key=lambda k: float(k[1][1:]), reverse=True)
    return report_table


def max_column_width(table):
    """Take an input table  and returns a list with each value representing the most characters in each column."""
    column_width_list = []  # list for the longest characters in each column
    for i in range(len(table[0])):
        column_length = 0
        for row in table:
            if len(str(row[i])) > column_length:
                column_length = len(str(row[i]))
        column_width_list.append(column_length)
    return column_width_list


def add_column_spaces(cwl, spaces=3):
    """Return list of column spaces with additional spaces, default = 3"""
    for i in range(len(cwl)):
        cwl[i] += spaces
    return cwl


def create_report_formstring(mtl):
    """Return a form string based on the column widths from mtl list."""
    form_string = []
    for i in mtl:
        form_string.append('{:' + str(i) + '}')
    form_string = ''.join(form_string)
    return form_string


def display_report():
    """Generate report based on existing donors and donations. Display in variable column widths."""
    report_table = create_report_table(ddb)
    mcw = max_column_width(report_table)  # list of max width of each column in report table
    mcw = add_column_spaces(mcw)
    form_string = create_report_formstring(mcw)

    print('\n\n')  # Begin printing out table
    print(form_string.format(*report_table.pop(0)))
    print('{}'.format('-'*sum(mcw)))  # spacer line between header and body of table
    for row in report_table:
        print(form_string.format(*row))


def letters_to_all():
    """Write form letter to txt files based on input dictionary. Optional directory change."""
    user_input = input("Would you like save to current directory,{}? >(y,n)".format(os.getcwd()))
    if user_input == 'n':
        path = input("Enter full path to desired directory: ")
        os.chdir(path)
    write_letters(ddb)

def write_letters(d):
    """Take input dictionary and write form letter to txt file based on key and last item in value."""
    for key in d.keys():
        current_dict = {'donor_name': key, 'donation': d[key][-1]}
        key = key.replace(' ', '_')
        with open('{}.txt'.format(key), 'w') as f:
            f.write(create_letter(current_dict))


def goodbye():
    print("goodbye!")
    sys.exit()


ddb = {'Archie Bunker': [20, 100, 75, 98],
       'Beyonce Knowles': [2000000, 50000000],
       'Charlie Kauffman': [12345],
       'David Sedaris': [23000, 1200, 2000],
       'Edvard Munch': [1, 2, 3]}


def main():
    """Establish initial donor database and initiate top user menu. """
    while True:
        user_input = input('\n\nMENU:\n'
                           '1 - Send a Thank You for a New Donation\n'
                           '2 - Create a Report\n'
                           '3 - Send letters to everyone\n'
                           '4 - Quit\n'
                           'Please enter 1-4>')
        user_menu = {'1': new_thank_you, '2': display_report, '3': letters_to_all, '4': goodbye}
        try:
            user_menu[user_input]()
        except KeyError:
            print('\nOption not found. Please enter the numeral 1,2,3 or 4')


if __name__ == '__main__':
    main()
