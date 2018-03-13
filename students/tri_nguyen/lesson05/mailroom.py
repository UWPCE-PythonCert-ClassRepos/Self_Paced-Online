#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  09-Mar-2018
# ------------------------------------------- #

# Import stuff
from operator import itemgetter
import time

# Get local time
local_time = time.localtime()

# Declare variables and data structure

donor_dict = { #  [0] == total donation, [1] == number of gifts, [2] == average

    'William Gates, III': [653784.49, 2, 326892.24],
    'Mark Zuckerberg': [16396.10, 3, 5465.37],
    'Jeff Bezos': [877.33, 1, 877.33],
    'Paul Allen':[708.42, 3, 236.14],
    'Tri Nguyen': [100.00, 1, 100.00]
    }

    
# Declare functions


def display_menu():
    ''' this function displays a menu
        of 3 actions '''

    print(''' Select one of the actions below:

    1. Send a Thank You
    2. Create a Report
    3. Send letters to everyone
    4. Quit

    ''')


def display_donor_list():
    ''' this function displays list of donors
        from donor_dict '''

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
    


def send_thanks():
    ''' this function composes an email thanking
        the donor for their generous donation '''

    while True:

        full_name = input('Enter a Full Name (or type "list" to get the list of donors): ').title()

        if full_name.lower() == 'list':
            display_donor_list()
            continue

        elif donor_dict.get(full_name):
            donation_amount = convert_to_float(input('Enter donation amount: '))
            # Update values in list
            donor_dict[full_name][0] = donor_dict[full_name][0] + donation_amount
            donor_dict[full_name][1] = donor_dict[full_name][1] + 1
            donor_dict[full_name][2] = donor_dict[full_name][0] / donor_dict[full_name][1]

        else:
            donation_amount = convert_to_float(input('Enter donation amount: '))
            donor_dict[full_name] = [donation_amount, 1, donation_amount]

        choice = input('Do you want to quit and send email?(y/n) ')

        if choice == 'y':
            email_template = '''
                Dear {0},

                Thank you for giving us ${1:,.2f}. Your money will be put to good use.
                Please come back and donate more.

                Best Regards,

                John Doe
            '''
            print(email_template.format(full_name, donation_amount))

            break
        else:
            continue


def create_report():
    ''' this function generates a report of donors '''

    template = '{0:<26}|{1:^13}|{2:^11}|{3:^14}'
    value_template = '{0:<26} ${1:12.2f} {2:11} ${3:13.2f}'

    formatted_columns = template.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')

    print(formatted_columns)

    print('{}'.format('-' * len(formatted_columns)))

    print('Report of Donors is below:\n')

    donor_list = list(donor_dict.items())

    donor_list.sort(key=itemgetter(1), reverse=True)

    for item in donor_list:
        print(value_template.format(item[0], item[1][0], item[1][1], item[1][2]))
    print()


def format_filename(name):
    ''' format name to create a filename that looks like
        William_Gates_III.txt '''

    if ',' in name:
        name = name.replace(',', '')
        name = name.replace(' ', '_')
        name = name + '.txt'
        return name
    else:
        name = name.replace(' ', '_')
        name = name + '.txt'
        return name
    
    
def send_all_letters():
    ''' this function sends letters to everyone '''

    # email template
    email_temp = ['Thank you for your kind donation of',
        'It will be put to very good use.',
        'Sincerely',
        '-The Team']

    for name in donor_dict:
        with open(format_filename(name), 'w') as f:
            f.write('Dear {},\n\n'.format(name))

            f.write('\t{0} ${1:,.2f}\n\n'.format(email_temp[0], donor_dict[name][0]))

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
        display_menu()

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
