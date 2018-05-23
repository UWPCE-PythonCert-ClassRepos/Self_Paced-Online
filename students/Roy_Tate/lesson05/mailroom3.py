#!/usr/bin/python3

## author/student: Roy Tate (githubtater)

from collections import Counter

import sys
import os
import os.path

# Create the donor_dict and manually add a few entries
donor_dict = {}
donor_dict['Bill'] = [1100, 2100, 3100]
donor_dict['Mark'] = [1000, 300000.23, 2000]
donor_dict['Jeff'] = [50, 450.355]
donor_dict['Roy'] = [4500, 7500, 11221, 30232, 323]

# This is the standard template to be used when sending thank you emails. Ideally this would be saved
# externally as a template file.
email_str_ty = '''\n
        From:     A Worthwhile Cause
        To:       {0}
        Subject:  Thank you

        Dear {0},

        We want to thank you for your recent donation of ${1:.2f}. This was
        very generous.

        Sincerely,

        The Boss
        '''

# Email template used for generating thank you emails to all donors.
email_str_annual = '''\n
        From:    A Charity Thankful For Your Kindness
        To:      {0}
        Subject:  This Year's Challenge!

        Dear {0},

        First, we would like to thank you for your continued generosity throughout the 
        years. Without contributions like yours, the good things that we are able to do 
        simply would not be possible. 

        Your contributions to date have totaled ${1:.2f}. 

        This years challenge is to see if you can donate more than your current total
        in one year. This would effectively double your current donations to the 
        organization!  Remember, it is for a good cause!

        Sincerely,

        The good guys at the best organization'''


# Prints the list of keys from donor_dict (in this case, the donor names)
def print_list():
    print('{:*^50}'.format('DONOR LIST'))
    for donor in sorted(donor_dict.keys()):  # sort keys == names print alphabetically
        print(donor)


# Helper function to add donations to appropriate donor's account
def add_donation(name, new_donation):
    if name in donor_dict.keys():
        donor_dict[name].append(new_donation)
    else:
        donor_dict[name] = [new_donation]


# Generate formatted email for specific donor
def print_email(email_str_ty, donor_name, donation_amount):
    print(email_str_ty.format(donor_name.title(), float(donation_amount)))
    print('\n[DONE] Email sent to: ' + donor_name)


# Generate an email to all donors listing the sum of their donations.
def email_all():
    count = 0
    while True:
        try:
            save_path = input('Enter the full path to the directory to save the files.\n'
                              'Press Enter to save to the current directory: ')
            print('Generating emails for all donors...')
            # attempt to make the directory entered by the user.
            # Output is not printed to terminal (/dev/null). This prevents a mkdir --help message from appearing
            # when the user generates output to the current directory
            os.system('mkdir -p ' + save_path + '> /dev/null 2>&1')
            for donor, donations in donor_dict.items():
                filename = os.path.join(save_path, donor + '.txt')
                with open(filename, 'w') as f:
                    f.write(email_str_annual.format(donor.title(), sum(donations)))
                    print('Output file -->  ' + str(os.path.abspath(filename)))
                    count += 1
            print('[DONE] Successfully generated {} files/emails.'.format(str(count)))
            break
        except PermissionError as e:
            print("You can\'t write to that directory: " + str(e))
            print('Try again.\n')
        except FileNotFoundError as e:
            print('Invalid directory: ' + str(e) + '\nTry again.\n')

def send_thank_you():
    # Obtain the name of the donor, the contribution amount, add the donation to the list, and generate
    # a thank you email.
    thank_you_args = {
                   '1': get_donation_amount,
                   '2': main,
                   'list':print_list,
    }
    thank_you_prompt = "\n***Thank You Menu***\n" \
                       "Enter your selection.\n"\
                       "[1] ----- Enter a New Donation (for new or existing donors)\n" \
                       "[2] ----- Return to Main Menu\n"\
                       "[list] -- Print Donor List\n" \
                       "---> "
    menu_selection(thank_you_prompt, thank_you_args)


# Determines if the donor is in the list or not. A different prompt is presented if the donor
# exists or not.
def get_donation_amount():
    name = input('Enter the donor name: ')
    donation_amount = float(input('Enter the donation amount: '))
    add_donation(name, donation_amount)
    print_email(email_str_ty, name, donation_amount)


def sum_donations(donor_dict):
    return donor_dict[1]


def create_report():
    # generate a report of the current donor list, the total donation amounts, avg donation amt, and # of donations
    header = '{:<20}|{:^15}|{:^13}|{:>14}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    header_len = len(header)
    dotted_line = '\n{:<20}'.format('-' * header_len)
    print(header + dotted_line)
    donor_str_fmt = '{:<20} ${:>13.2f}{:>11}    ${:>11.2f}'  # I don't like the way this is spaced out, but it works
    sort_list = []
    for name, donations in donor_dict.items():
        num_gifts = len(Counter(donations))
        total_given = sum(donations)
        avg_gift = total_given / num_gifts
        sort_list.append([name, total_given, num_gifts, avg_gift])
    sort_list.sort(key=sum_donations, reverse=True)
    all_str = ''  # string to hold each line of the list generated
    for donor in sort_list:
        all_str += donor_str_fmt.format(donor[0], donor[1], donor[2], donor[3]) + '\n'
    print(all_str)


# take a prompt as a string and a list of options/arguments as a dict
def menu_selection(prompt, arg_dict):
    while True:
        try:
            response = input(prompt)
            arg_dict[response]() == ''
        except KeyError as e:
            print('Invalid response: ' + str(e) + '\nTry again.')


# All good things come to an end.
def die():
    print('Exiting the mailroom3.')
    sys.exit(0)


# The user is presented with the initial menu when ran.
def main():
    arg_dict = {
        '1': send_thank_you,
        '2': create_report,
        '3': email_all,
        '4': die,
    }
    prompt = '\n***** Main Menu *****\n'\
             'Select an option:\n' \
             '[1] Send a Thank You\n' \
             '[2] Create a Report\n' \
             '[3] Send letters to everyone\n' \
             '[4] Quit\n' \
             '--> '
    menu_selection(prompt, arg_dict)


if __name__ == "__main__":
    print('\n{:+^50}'.format(''))
    print('{:+^50}'.format(' Welcome to the Mailroom '))
    print('{:+^50}'.format(''))
    main()


