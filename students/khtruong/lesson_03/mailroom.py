#!/usr/bin/env python

"""This module runs the mailroom script.
"""

data = [['Alpha', 3.65, 54.50],
        ['Beta', 36.54, 1.25, 54.87],
        ['Gamma', 17.38],
        ['Delta', 25.55, 33.33, 78.14],
        ['Epsilon', 65.40]]


def main():
    """Return 3 options for user to select to run mailroom script."""
    while True:
        userinput = input('\nEnter "0" to "quit" \n'
                          'Enter "1" to "Send a Thank You" \n'
                          'Enter "2" to "Create a Report" \n'
                          'What do you want to do? > ')
        if userinput == '0':
            break
        elif userinput == '1':
            thankyou()
        elif userinput == '2':
            report()
        else:
            print('\n{} is not a valid option. '
                  'Please try again!'.format(userinput))


def thankyou():
    """Return a thank you email to donor."""
    while True:
        userinput = input('\nEnter "list" to see donors or a '
                          'Full Name > ')
        if userinput == 'list':  # print all names in current list
            [print(subdata[0]) for subdata in data]
        else:
            name = userinput.title()  # 'Title' checking
            for subdata in data:  # search for existing name
                if name == subdata[0]:
                    amount = float(add_donation())
                    subdata.append(amount)
                    email(name, amount)
                    break
            else:  # add new name
                data.append([name])
                amount = float(add_donation())
                data[-1].append(amount)
                email(name, amount)
            break


def report():
    """Return a summary report of donations."""
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
    header = '\nDonor Name                | Total Given |' \
             ' Num Gifts | Average Gift'
    print(header)
    print('-'*len(header))
    for item in summary:
        print('{:<26} ${:>11,.2f} {:>11d}  ${:>12,.2f}'.format(*item))


def add_donation():
    """Return prompt asking for donation amount."""
    return input('Enter donation amount! > ')


def email(name, amount):
    """Return a thankyou email to donor."""
    print('Email: Thank you, {}, for your generous '
          'donation of ${:,.2f}!'.format(name, amount))


if __name__ == '__main__':
    main()
