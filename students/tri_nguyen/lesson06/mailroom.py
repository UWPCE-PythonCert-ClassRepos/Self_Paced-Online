#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  16-Mar-2018
# ------------------------------------------- #

# Import stuff
from operator import itemgetter
import time

# Get local time
local_time = time.localtime()

# Declare variables and data structure

donor_dict = {

    'William Gates, III': {'total': 653784.49, 'num_gifts': 2, 'avg': 326892.24},
    'Mark Zuckerberg': {'total': 16396.10, 'num_gifts': 3, 'avg': 5465.37},
    'Jeff Bezos': {'total': 877.33, 'num_gifts': 1, 'avg': 877.33},
    'Paul Allen':{'total': 708.42, 'num_gifts': 3, 'avg': 236.14},
    'Tri Nguyen': {'total': 100.00, 'num_gifts': 1, 'avg': 100.00}
    }


# Declare functions


def display_menu():
    ''' display a menu of 3 actions '''

    menu = ''' Select one of the actions below:

    1. Send a Thank You
    2. Create a Report
    3. Send letters to everyone
    4. Quit

    '''
    return menu


def display_donor_list():
    ''' display list of donors
        from donor_dict '''

    # enumerate the list to get the index number
    donor_name = enumerate([donor for donor in donor_dict])
    for idx, name in donor_name:
        print(idx + 1, '-', name)


def convert_to_float(num):
    ''' convert numeric values from string to float '''

    try:
        num = float(num)
    except ValueError:
        print('value entered is not a number!!')
    else:
        return num


def generate_email_template():
    ''' send an email to one donor that has just donated
        this function works with send_thanks() function '''

    email_template = '''
                Dear {0},

                Thank you for giving us ${1:,.2f}. Your money will be put to good use.
                Please come back and donate more.

                Best Regards,

                John Doe
            '''

    return email_template


def send_thanks():
    ''' send thanks to a donor for their generous donation '''

    while True:

        full_name = input('Enter a Full Name (or type "list" to get the list of donors): ').title()

        if full_name.lower() == 'list':
            display_donor_list()
            continue

        elif donor_dict.get(full_name):
            donation_amount = convert_to_float(input('Enter donation amount: '))
            # Update values in list
            donor_dict[full_name]['total'] += donation_amount
            donor_dict[full_name]['num_gifts'] += 1
            donor_dict[full_name]['avg'] = donor_dict[full_name]['total'] / donor_dict[full_name]['num_gifts']

        else:
            donation_amount = convert_to_float(input('Enter donation amount: '))
            donor_dict[full_name] = dict(total=donation_amount, num_gifts=1, avg=donation_amount)

        choice = input('Do you want to quit and send email?(y/n) ')

        if choice == 'y':
            email_template = generate_email_template()
            print(email_template.format(full_name, donation_amount))

            break
        else:
            continue


def print_header():
    ''' print the header of donor report '''

    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    template = '{0:<26}|{1:^13}|{2:^11}|{3:^14}'

    formatted_columns = template.format(*header)
    border = '{}'.format('-' * len(formatted_columns))

    return (formatted_columns, border)


def generate_donor_list():
    ''' generate a list of donors from donor_dict 
        and sort the list from high total to low '''

    donor_list = [(name, donor_dict[name]['total'], donor_dict[name]['num_gifts'], donor_dict[name]['avg'])
        for name in donor_dict]

    donor_list.sort(key=itemgetter(1), reverse=True)

    return donor_list

def create_report():
    ''' generate a report of donors '''

    value_template = '{0:<26} ${1:12.2f} {2:11} ${3:13.2f}'
    columns, border = print_header()
    donor_list = generate_donor_list()

    print('Report of Donors is below:\n')

    print(columns)
    print(border)

    for item in donor_list:
        print(value_template.format(item[0], item[1], item[2], item[3]))
    print()


def format_filename(name):
    ''' format name to create a filename that looks like
        William_Gates_III.txt '''

    if isinstance(name, (int, float)):
        raise TypeError('name must be a string.')
    if ',' in name:
        name = name.replace(',', '').replace(' ', '_') + '.txt'
        return name
    else:
        name = name.replace(' ', '_') + '.txt'
        return name


def send_all_letters():
    ''' send letters to everyone '''

    # email template
    email_temp = ['Thank you for your kind donation of',
        'It will be put to very good use.',
        'Sincerely',
        '-The Team']

    for name in donor_dict:
        with open(format_filename(name), 'w') as f:
            f.write('Dear {},\n\n'.format(name))

            f.write('\t{0} ${1:,.2f}\n\n'.format(email_temp[0], donor_dict[name]['total']))

            f.write('\t{}\n\n'.format(email_temp[1]))

            f.write('\t\t{}.\n'.format(email_temp[2]))

            f.write('\t\t    {}\n'.format(email_temp[3]))
            
            f.write('\t\t    {0}/{1}/{2}'.format(local_time.tm_mon, local_time.tm_mday, local_time.tm_year))

    print('ALL LETTERS HAVE BEEN SENT!!!\n')


def default():
    print('BAD CHOICE\n')


def main():
    ''' prompt user to see the menu of 3 actions '''

    while True:
        print(display_menu())

        action = input('Enter the corresponding number for action [1 to 4]:  ')
        print()
        if action == '4':
            break

        options = {
            '1': send_thanks,
            '2': create_report,
            '3': send_all_letters}

        options.get(action, default)()

# End of function definition


# Presentation

if __name__ == '__main__':
    main()
