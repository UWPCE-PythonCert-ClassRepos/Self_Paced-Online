#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  18-May-2018
# ------------------------------------------- #

# Import stuff
from operator import itemgetter
import time
from pprint import pprint

# Get local time
local_time = time.localtime()

# Declare variables and data structure

# donors dict stores each donation from each donor
donors = {

    'William Gates, III': [326892.24, 396892.24, 600],
    'Mark Zuckerberg': [546.37, 5485.37, 6465.37, 450],
    'Jeff Bezos': [877.33, 898],
    'Paul Allen': [235.14, 216.14, 296.14],
    'Tri Nguyen': [100]
    }

# Declare functions

def total(donations):
    ''' return the total amount of money a donor has donated '''
    return sum(donations)


def num_gifts(donations):
    ''' return how many times a donor has donated '''
    return len(donations)


def average(donations):
    ''' return the average of all the amount 
        of money that a donor has donated '''
    return sum(donations) / len(donations)


def donor_db(a_dict):
    ''' return donors and their donations in more readable dict '''
    return {name: {'total': total(a_dict[name]),
                   'num_gifts': num_gifts(a_dict[name]),
                   'avg': average(a_dict[name])} for name in a_dict if len(a_dict[name]) > 0}


def display_menu():
    ''' display a menu of 3 actions '''

    menu = ''' Select one of the actions below:

    1. Send a Thank You
    2. Create a Report
    3. Send letters to everyone
    4. Challenge
    5. Run projections
    6. Quit

    '''
    return menu
    

def display_donor_list():
    ''' display list of donors
        from donor_dict '''
    for idx, name in enumerate(donors.keys()):
        print(idx + 1, '-', name, '\n')


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

        elif donors.get(full_name):
            donation_amount = convert_to_float(input('Enter donation amount: '))
            donors[full_name].append(donation_amount)

        else:
            donation_amount = convert_to_float(input('Enter donation amount: '))
            donors[full_name] = [donation_amount]

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

    return formatted_columns, border


def generate_donor_list():
    ''' generate a list of donors from donor_dict 
        and sort the list from high total to low '''

    donor_list = [(name, donor_db(donors)[name]['total'],
                   donor_db(donors)[name]['num_gifts'], 
                   donor_db(donors)[name]['avg'])
        for name in donor_db(donors)]

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
        raise TypeError('name must be a string not an int or float')
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

    for name in donors:
        with open(format_filename(name), 'w') as f:
            f.write('Dear {},\n\n'.format(name))

            f.write('\t{0} ${1:,.2f}\n\n'.format(email_temp[0], total(donors[name])))

            f.write('\t{}\n\n'.format(email_temp[1]))

            f.write('\t\t{}.\n'.format(email_temp[2]))

            f.write('\t\t    {}\n'.format(email_temp[3]))
            
            f.write('\t\t    {0}/{1}/{2}'.format(local_time.tm_mon, local_time.tm_mday, local_time.tm_year))

    print('ALL LETTERS HAVE BEEN SENT!!!\n')


def challenge(factor=1, min_donation=0, max_donation=0):
    ''' each donation on record can be multiplied by an arbitray factor '''
    
    factor = convert_to_float(input('Enter a factor to multiply: '))
    
    new_data = dict(list((name, list(map(lambda x: x * factor, donations))) for name, donations in donors.items()))
    
    min_donation = convert_to_float(input('Enter the min donation: '))
    max_donation = convert_to_float(input('Enter the max donation: '))
    
    new_db = dict(list((name, list(filter(lambda x: x >= min_donation and x <= max_donation, donations))) for name, donations in new_data.items()))
    
    print('\nNew donor database after the challenge factor of "{}"\n'.format(factor))
    pprint(donor_db(new_db))
    print()
    

def refactor_challenge(amount, factor):
    ''' refactor challenge function using dict comprehension for readability '''
    
    updated_db = {name: [item * factor for item in donors[name] if item < amount] for name in donors}
    current_db = {name: [item for item in donors[name] if item >= amount] for name in donors}
    
    for name in current_db:
        current_db[name].extend(updated_db[name])
        
    return current_db


def output_resutls(template, a_dict):
    ''' display projections results on screen '''

    for name in a_dict:
        print(template.format(name, sum(a_dict[name])))
    print()
        

def run_projections():
    
    double_100 = refactor_challenge(100, 2)
    triple_50 = refactor_challenge(50, 3)
    template_100 = '{} - Total contribution to be doubled for amounts under $100 = ${:.2f}'
    template_50 = '{} - Total contribution to be tripled for amounts over $50 = ${:.2f}'
    output_resutls(template_100, double_100)
    output_resutls(template_50, triple_50)
    

def default():
    print('BAD CHOICE\n')


def main():
    ''' prompt user to see the menu of 3 actions '''

    while True:
        print(display_menu())

        action = input('Enter the corresponding number for action [1 to 6]:  ')
        print()
        if action == '6':
            break

        options = {
            '1': send_thanks,
            '2': create_report,
            '3': send_all_letters,
            '4': challenge,
            '5': run_projections}

        options.get(action, default)()

# End of function definition


# Presentation

if __name__ == '__main__':
    main()
