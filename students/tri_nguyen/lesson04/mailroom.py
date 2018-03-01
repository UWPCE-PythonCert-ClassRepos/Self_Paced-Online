#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  25-Feb-2018
# ------------------------------------------- #

# Import stuff
from operator import itemgetter

# Declare variables and data structure

donor_dict = [
    {'name': 'William Gates, III', 'donation': 653784.49, 'count': 2, 'average': 326892.24},
    {'name': 'Mark Zuckerberg', 'donation': 16396.10, 'count': 3, 'average': 5465.37},
    {'name': 'Jeff Bezos', 'donation': 877.33, 'count': 1, 'average': 877.33},
    {'name': 'Paul Allen', 'donation': 708.42, 'count': 3, 'average': 236.14},
    {'name': 'Tri Nguyen', 'donation': 100.00, 'count': 1, 'average': 100.00}
]
    
# Declare functions


def display_menu():
    ''' this function display a menu
        of 3 actions '''
    ACTIONS = ('Send a Thank You', 'Create a Report', 'Send letters to everyone', 'Quit')

    print(''' Select one of the actions below:

    1. {}
    2. {}
    3. {}
    4. {}
    '''.format(*ACTIONS))


def display_donor_list():
    ''' this function displays list of donors
        from donor_dict '''

    for idx, item in enumerate(donor_dict):
        print(idx + 1, '-', donor_dict[idx]['name'])


def send_thanks():
    ''' this function composes an email thanking
        the donor for their generous donation '''

    name_list = [item['name'] for item in donor_dict]

    while True:

        full_name = input('Enter a Full Name (or type "list" to get the list of donors): ').title()

        if full_name.lower() == 'list':
            display_donor_list()
            continue

        elif full_name not in name_list:
            donation_amount = float(input('Enter donation amount: '))
            donor_dict.append(dict(name=full_name.title(), donation=donation_amount, count=1, average=donation_amount))

        elif full_name in name_list:
            donation_amount = float(input('Enter donation amount: '))
            for item in donor_dict:
                if item['name'] == full_name:
                    item['donation'] = item['donation'] + donation_amount
                    item['count'] = item['count'] + 1
                    item['average'] = item['donation'] / item['count']

        choice = input('Do you want to quit and send email?(y/n) ')

        if choice == 'y':
            email_template = '''
                Dear {0},

                Thank you for giving us ${1:,.2f}. Your money will be put to good use.
                Please come back and donate more.

                Best Regards,

                John Doe
            '''
            print(email_template.format(full_name, float(donation_amount)))

            break
        else:
            continue


def create_report():
    ''' this function generate a report of donors '''

    template = '{0:<26}|{1:^13}|{2:^11}|{3:^14}'
    value_template = '{0:<26} ${1:12.2f} {2:11} ${3:13.2f}'

    formatted_columns = template.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')

    print(formatted_columns)

    print('{}'.format('-' * len(formatted_columns)))

    print('Report of Donors is below:\n')

    donor_list = [list(item.values()) for item in donor_dict]

    donor_list.sort(key=itemgetter(1), reverse=True)

    for item in donor_list:
        print(value_template.format(item[0], item[1], item[2], item[3]))
    print()


def send_all_letters():
    ''' this function send letters to everyone '''

    email_dict = {
        'greetings': 'Dear',
        'body_one': 'Thank you for your kind donation of ',
        'body_two': 'It will be put to very good use.',
        'end': 'Sincerely',
        'signature': '-The Team'}

    value_list = [list(item.values()) for item in donor_dict]

    for each_list in value_list:

        each_list[0] = each_list[0].split()

        template = '{}_' * (len(each_list[0]) - 1) + '{}.txt'

        first_name = each_list[0][0]
        last_name = each_list[0][1]

        with open(template.format(*each_list[0]), 'w') as f:
            f.write('{0} {1} {2},\n\n'.format(email_dict['greetings'], first_name, last_name))
            f.write('\t{0}${1:,.2f}\n\n'.format(email_dict['body_one'], each_list[1]))
            f.write('\t{}\n\n'.format(email_dict['body_two']))
            f.write('\t\t{}\n'.format(email_dict['end']))
            f.write('\t\t    {}'.format(email_dict['signature']))

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
