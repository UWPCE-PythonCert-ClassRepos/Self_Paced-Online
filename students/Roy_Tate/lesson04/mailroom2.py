# author/student: Roy Tate (githubtater)

from collections import defaultdict, Counter

import sys
import os
import os.path


# Create the donor_dict
donor_dict = {}
donor_dict['Bill'] = [1100, 2100, 3100]
donor_dict['Mark'] = [1000, 300000.23, 2000]
donor_dict['Jeff'] = [50, 450.355]
donor_dict['Roy'] = [4500, 7500, 11221, 30232, 323]

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


# Prints the list of keys from donor_dict (in this case, the donor names)
def print_list():
    print('{:*^50}'.format('DONOR LIST'))
    for donor in donor_dict.keys():
        print(donor)


# Helper function to add donations to appropriate user account
def add_donation(name, new_donation):
    if name in donor_dict.keys():
        donor_dict[name].append(new_donation)
    else:
        donor_dict[name] = new_donation


# Send formatted email to donor
def print_email(email_str, donor_name, donation_amount):
    print(email_str.format(donor_name.title(), float(donation_amount)))
    print('Email sent to: ' + donor_name)


def email_all():
    print('Generating emails for all donors...')
    for donor, donations in donor_dict.items():
        filename = donor + '.txt'
        with open(filename, 'w') as f:
            f.write(email_str.format(donor.title(), sum(donations)))
            print('[SUCCESS] Output file -->  ' + str(os.path.abspath(filename)))

def send_thank_you():
    # Obtain the name of the donor, the contribution amount, add the donation to the list, and generate
    # a thank you email.

    name = input("Enter the full name of the recipient (Type 'list' to view donors. Type '1' for Main Menu):\n")
    if name == 'list':
        print_list()

    elif name == '1':
        main()

    elif name in donor_dict.keys():
        donation_amount = float(input('EXISTING: Enter the donation amount: '))
        add_donation(name, donation_amount)
        print_email(email_str, name, donation_amount)
    else:  # name not found in list
        donation_amount = (input('NEW: Enter the donation amount: '))
        add_donation(name, donation_amount)
        print_email(email_str, name, donation_amount)

    # print(email_str.format(name.title(), donation_amount))


def create_report():
    # generate a report of the current donor list, the total donation amounts, avg donation amt, and # of donations
    header = '{:<20}|{:^15}|{:^10}|{:>15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    header_len = len(header)
    dotted_line = '\n{:<20}'.format('-' * header_len)
    print(header + dotted_line)
    donor_str_fmt = '{:<20} ${:>13.2f}{:>11}    ${:>11.2f}'

    c = Counter()
    for name, donations in donor_dict.items():
        num_gifts = len(Counter(donations))
        total_given = sum(donations)
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
    # print(donor_dict)
    # print(donor_dict.items())
    # print(donor_dict.values())
    email_all()
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