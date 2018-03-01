#!/usr/bin/env python
from datetime import date

"""This module runs the mailroom script.
"""

data = [['Alpha', 3.65, 54.50],
        ['Beta', 36.54, 1.25, 54.87],
        ['Gamma', 17.38],
        ['Delta', 25.55, 33.33, 78.14],
        ['Epsilon', 65.40]]


def menu_selection(prompt, selection_dict):
    """Return options for user to select from."""
    while True:
        userinput = input(prompt)
        if selection_dict.get(userinput) is None:
            print('\n{} is not a valid selection. '
                  'Please try again!'.format(userinput))
        else:
            if selection_dict.get(userinput)() == 'Exit Menu':
                break


def exit_menu():
    """Return 'Exit Menu'"""
    return 'Exit Menu'


def send_thankyou_email():
    """Return a menu selection to send thank you email to donor."""
    menu_selection(thankyou_prompt, thankyou_dict)


def list_donors():
    """Return all donors name."""
    [print(subdata[0]) for subdata in data]


def donor_and_amount():
    """Return prompt for donor name and donation amount and print to screen."""
    name = input('Enter a donor name > ').title()  # 'Title' checking
    for subdata in data:  # search for existing donor
        if name == subdata[0]:
            amount = float(add_donation())
            subdata.append(amount)
            print(format_letter(name, amount))
            break
    else:  # add new donor
        data.append([name])
        amount = float(add_donation())
        data[-1].append(amount)
        print(format_letter(name, amount))


def add_donation():
    """Return prompt asking for donation amount."""
    return input('Enter donation amount! > ')


def summarize_donation():
    '''Return total given, number of gifts, and average gifts for each donor'''
    summary = []
    for subdata in data:
        total_given = sum(subdata[1:])
        num_gifts = len(subdata[1:])
        summary.append([subdata[0],
                        total_given,
                        num_gifts,
                        total_given/max(num_gifts, 1)
                        ])
    summary.sort(key=lambda x: x[1], reverse=True)
    return summary


def create_report():
    """Return a summary report of donations."""
    summary = summarize_donation()
    header = '\nDonor Name                | Total Given |' \
             ' Num Gifts | Average Gift'
    print(header)
    print('-'*len(header))
    for item in summary:
        print('{:<26} ${:>11,.2f} {:>11d}  ${:>12,.2f}'.format(*item))


def format_letter(name, amount):
    """Return formatted letter with donor name and donated amount"""
    return ('Dear {},\n\n'
            '    Thank you for your very kind donation of $${:,.2f}.\n\n'
            '    It will be put to very good use.\n\n'
            '                   Sincerely,\n'
            '                   -The Team'.format(name, amount))


def send_letters():
    """Create thank you letter for each donor and save as text files"""
    summary = summarize_donation()
    for item in summary:
        filename = ''.join([item[0], ' ', str(date.today()), '.txt'])
        with open(filename, 'w') as outfile:
            outfile.write(format_letter(item[0], item[1]))


main_prompt = ('\nEnter "q" to "Exit Menu" \n'
               'Enter "1" to "Send a Thank You" \n'
               'Enter "2" to "Create a Report" \n'
               'Enter "3" to "Send Letters to Everyone" \n'
               'What do you want to do? > '
               )

main_dict = {'q': exit_menu,
             '1': send_thankyou_email,
             '2': create_report,
             '3': send_letters
             }

thankyou_prompt = ('\nEnter "q" to "Exit Menu" \n'
                   'Enter "1" to "List Donors" \n'
                   'Enter "2" to "Enter a Donor Name" \n'
                   'What do you want to do? > '
                   )

thankyou_dict = {'q': exit_menu,
                 '1': list_donors,
                 '2': donor_and_amount
                 }


if __name__ == '__main__':
    menu_selection(main_prompt, main_dict)
