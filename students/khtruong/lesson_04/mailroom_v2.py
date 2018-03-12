#!/usr/bin/env python
from datetime import date

"""This module runs the mailroom script.
"""

data_dict = {'Jeff Bezos': [3.65, 54.50],
             'Mark Zuckerberg': [36.54, 1.25, 54.87],
             'Paul Allen': [17.38],
             'William Gates III': [25.55, 33.33, 78.14]
             }


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
    [print(donor) for donor in data_dict.keys()]


def donor_and_amount():
    """Return prompt for donor name and donation amount and print to screen."""
    fullname = fullname_input()
    amount = float(amount_input())
    data_dict.setdefault(fullname, [])  # add name to key if doesn't exist
    data_dict[fullname].append(amount)
    print(format_letter(fullname, amount))


def amount_input():
    """Return prompt asking for donation amount."""
    return input('Enter donation amount! > ')


def fullname_input():
    """Return prompt asking for full name."""
    return input('Enter a donor first and last name > ').title()


def summarize_donation():
    '''Return total given, number of gifts, and average gifts for each donor'''
    summarized_list = []
    for donor_name in data_dict.keys():
        value = data_dict.get(donor_name)
        total_given = sum(value)
        num_gifts = len(value)
        avg_gifts = total_given/max(num_gifts, 1)
        summarized_list.append({'donor_name': donor_name,
                                'total_given': total_given,
                                'num_gifts': num_gifts,
                                'avg_gifts': avg_gifts,
                                }
                               )
    # sort by total given
    summarized_list = sorted(summarized_list,
                             key=lambda k: k['total_given'],
                             reverse=True
                             )
    return summarized_list


def create_report():
    """Return a summary report of donations."""
    summary = summarize_donation()
    header = '\nDonor Name                | Total Given |' \
             ' Num Gifts | Average Gift'
    print(header)
    print('-'*len(header))
    for donor_dict in summary:
        print('{donor_name:<26} '
              '${total_given:>11,.2f} '
              '{num_gifts:>11d}  '
              '${avg_gifts:>12,.2f}'.format(**donor_dict)
              )


def format_letter(fullname, amount):
    """Return formatted letter with donor name and donated amount"""
    return ('Dear {},\n\n'
            '    Thank you for your very kind donation of $${:,.2f}.\n\n'
            '    It will be put to very good use.\n\n'
            '                   Sincerely,\n'
            '                   -The Team'.format(fullname, amount))


def send_letters():
    """Create thank you letter for each donor and save as text files"""
    for donor_name in data_dict.keys():
        filename = ''.join([donor_name, ' ', str(date.today()), '.txt'])
        with open(filename, 'w') as outfile:
            # use last donated amount
            outfile.write(format_letter(donor_name,
                                        data_dict.get(donor_name)[-1]
                                        )
                          )


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
