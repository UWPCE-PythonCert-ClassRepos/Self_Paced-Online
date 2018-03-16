#!/usr/bin/env python3
import sys

"""
Lesson3 - Mailroom, Part 1
"""

_donors = [
    [
        'Jim Halpert',
        [
            1.00
        ]
    ],
    [
        'Pam Beesly',
        [
            1000.00, 2000.00, 3000.00
        ]
    ],
    [
        'Dwight Schrute',
        [
            2.00, 3.00
        ]
    ],
    [
        'Michael Scott',
        [
            10.0, 20.00, 30.00
        ]
    ],
    [
        'Andy Bernard',
        [
            500.00
        ]
    ]
]


def check_for_quit(action):
    if action.lower() == 'quit':
        donor_app()
        return
    else:
        return


def format_donation(donation):
    donation = float(donation)
    donation = "{0:.2f}".format(donation)
    return donation


def get_donation():
    donation = input('Donation amount: ')
    check_for_quit(donation)
    return donation


def add_donor(donor, donation):
    _donors.append([donor, [float(donation)]])
    return True


def append_donor(donor, donation):
    for d in _donors:
        if donor.lower() == d[0].lower():
            d[1].append(donation)
            return True


def thank_donor(donor_name, donation):
    email_str = 'Dear {a},\nThank you for your generous ' \
        + 'donation of ${b}.\nRegards\nUW Student'
    print(email_str.format(a=donor_name, b=donation))
    return


def sort_donors(donors):
    sorted_donors = list(donors)
    sorted_donors.sort(key=lambda x: sum(x[1]))
    sorted_donors.reverse()
    return sorted_donors


def get_donor_summary(donors):
    summary = []
    for i, donor in enumerate(donors):
        d = donor[1]  # all donations
        s = sum(d)  # total donations
        g = len(d)
        m = float(s) / max(len(d), 1)  # mean
        n = []  # new donor item
        n.append(donor[0])
        n.append('${0:.2f}'.format(s))
        n.append(str(g))
        n.append('${0:.2f}'.format(m))
        summary.append(n)
    return summary


def print_report(rows):
    # table heading
    h = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    hs = ' | '
    hf = '{0:<25}{1}{2}{3}{4}{5}{6}'
    print(hf.format(h[0], hs, h[1], hs, h[2], hs, h[3]))

    # table rows
    for r in rows:
        f0 = '{0:<' + str(max(len(r[0]), 25)) + '}'
        f2 = '{2:>' + str(max(len(r[1]), len(h[1]))) + '}'
        f4 = '{4:>' + str(max(len(r[2]), len(h[2]))) + '}'
        f6 = '{6:>' + str(max(len(r[3]), len(h[3]))) + '}'
        rf = f0 + '{1}' + f2 + '{3}' + f4 + '{5}' + f6
        args = [r[0], '  $', r[1], ' | ', r[2], '  $', r[3]]
        print(rf.format(*args))


if __name__ == "__main__":

    menu = {}
    menu['1'] = 'Send a Thank You'
    menu['2'] = 'Create a Report'
    menu['3'] = 'quit'

    def donor_app():
        while True:
            # menu options
            options = menu.keys()
            for entry in options:
                print(entry, menu[entry])
            selection = input('Please select an action: ')

            # menu selection:  'Send a Thank You'
            if selection == '1':
                complete = False
                action = ''
                donation = None
                while not complete:
                    action = input("Type a name or 'list': ")
                    check_for_quit(action)
                    # donor IS found
                    a = action.lower()  # line too long without this
                    if any(x for x in _donors if x[0].lower() == a):
                        donation = get_donation()
                        donation = format_donation(donation)
                        complete = append_donor(action, donation)
                        break
                    # list requested
                    elif action == 'list':
                        print(', '.join(d[0] for d in _donors))
                        continue
                    # donor NOT found
                    else:
                        donation = get_donation()
                        donation = format_donation(donation)
                        complete = add_donor(action, donation)
                        break
                # generate email
                thank_donor(action, donation)
                donor_app()
                break

            # menu selection:  'Create a Report'
            elif selection == '2':
                sorted_donors = sort_donors(_donors)
                rows = get_donor_summary(sorted_donors)
                print_report(rows)
                donor_app()
                break

            # menu selection:  'quit'
            elif selection == '3':
                sys.exit()

            # menu selection:  invalid
            else:
                print('Choose a valid option from the list below:')
                donor_app()

    donor_app()
