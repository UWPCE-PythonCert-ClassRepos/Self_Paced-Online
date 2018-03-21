# author/student: Roy Tate (githubtater)

from collections import defaultdict

import sys

donor_dict = [
    {'name':'Bill', 'donations': [400.254, 100, 200.232, 300]},
    {'name':'Jeff', 'donations': [250, 450.355]},
    {'name':'Bud', 'donations': [1000, 300000.23, 2000]},
    {'name':'Female CEO 1', 'donations': [1030, 20030.171, 30, 30]},
    {'name':'Female CEO 2', 'donations': [1030, 20030.355, 30, 30]},
]



# Extract the names of donors from the list
def donor_names():
    names = []
    for donor in donor_dict:
        names.append(donor['name'])
    return names


# Prints the list of donor names preceded with a formatted line
def print_list():
    print('{:*^50}'.format('DONOR LIST'))
    for donor in donor_names():
        print(donor)


#
def add_donation(donor_name, new_donation):
    for donor in donor_names():
        if donor['name'] == donor_name:
            donor['donations'].append(new_donation)


def print_email(email_str, donor_name, donation_amount):
    print(email_str.format(donor_name.title(), float(donation_amount)))
    print('done')

def send_thank_you():
    # Obtain the name of the donor, the contribution amount, add the donation to the list, and generate
    # a thank you email.
    email_str = '''\n
        From:     A Worthwhile Cause
        To:       {0}
        Subject:  Thank you

        Dear {0},

        We want to thank you for your recent donation of ${1:.2f}. This was
        very generous.

        Sincerely,

        The Boss
        '''
    name = input("Enter the full name of the recipient (Type 'list' to view donors. Type '1' for Main Menu):\n")
    if name == 'list':
        print_list()

    elif name == '1':
        main()

    elif name in donor_names():
        donation_amount = float(input('EXISTING: Enter the donation amount: '))
        add_donation(name, donation_amount)
        print_email(email_str, name, donation_amount)
    else:  # name not found in list
        donation_amount = input('NEW: Enter the donation amount: ')
        print('NEED TO ADD CODE TO APPEND NEW USERS TO DONOR_DICT')
        print_email(email_str, name, donation_amount)

    # print(email_str.format(name.title(), donation_amount))


def create_report():
    # generate a report of the current donor list, the total donation amounts, avg donation amt, and # of donations
    header = '{:<20}|{:^15}|{:^10}|{:>15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    header_len = len(header)
    dotted_line = '\n{:<20}'.format('-' * header_len)
    print(header + dotted_line)
    donor_str_fmt = '{:<20} ${:>13.2f}{:>11}    ${:>11.2f}'

    for donor in donor_dict:
        name = donor['name']
        num_gifts = len(donor['donations'])
        total_given = sum(donor['donations'])
        avg_gift = total_given / num_gifts
        print(donor_str_fmt.format(name, total_given, num_gifts, avg_gift))


def menu_selection(prompt, arg_dict):
    while True:
        response = input(prompt)
        if arg_dict[response]() == 'exit menu':
            print('Invalid reponse. Try again.')


def die():
    print('Exiting the mailroom 2.')
    return sys.exit(0)

def main():
    # main function contains the original donor list and calls other functions.

        arg_dict = {
            '1':send_thank_you,
            '2':create_report,
            '3':die,
        }

        prompt = '\nSelect an option:\n'\
                     '[1] Send a Thank You\n'\
                     '[2] Create a Report\n'\
                     '[3] Quit\n'\
                     '--> '

        menu_selection(prompt, arg_dict)

if __name__ == "__main__":
    main()