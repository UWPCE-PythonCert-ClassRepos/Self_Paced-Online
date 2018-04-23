#!/usr/bin/env python3
import os
import sys
import datetime

"""
Lesson4 - Mailroom, Part 2
"""

now = datetime.datetime.now()

_donors = [
    [
        {
            'first_name': 'Jim',
            'last_name': 'Halpert'
        },
        {
            'donations': [
                1.00
            ]
        }
    ],
    [
        {
            'first_name': 'Pam',
            'last_name': 'Beesley'
        },
        {
            'donations': [
                1000.00,
                2000.00,
                3000.00
            ]
        }
    ],
    [
        {
            'first_name': 'Dwight',
            'last_name': 'Shrute'
        },
        {
            'donations': [
                2.00,
                3.00
            ]
        }
    ],
    [
        {
            'first_name': 'Michael',
            'last_name': 'Scott'
        },
        {
            'donations': [
                10.00,
                20.00,
                30.00
            ]
        }
    ],
    [
        {
            'first_name': 'Andy',
            'last_name': 'Bernard'
        },
        {
            'donations': [
                500.00
            ]
        }
    ]
]


def submit_donor():
    donor_name = input("Please enter donor name: ")

    # request donation
    donation = request_donation()

    # donor lookup
    donor_found = donor_lookup(donor_name)

    if donor_found:
        # append existing donor
        append_donation(donor_name, donation)
    else:
        # add new donor
        add_donor(donor_name, donation)

    donor_email(donor_name, donation)
    exit_menu()
    return


def letters():
    cwd = os.getcwd()
    date = now.strftime('%Y-%m-%d')
    path = cwd + '/letters/'
    ext = '.txt'
    for d in _donors:
        fn = d[0]['first_name']
        ln = d[0]['last_name']
        file_path = "{}{}_{}_{}{}".format(path, date, fn, ln, ext)
        donations = format_donation(sum(d[1]['donations']))
        with open(file_path, 'w') as file:
            text = ('Dear {} {},\n\n'
                    '        Thank you for your very kind donation of ${}.\n\n'
                    '        It will be put to very good use.\n\n'
                    '               Sincerely,\n'
                    '                  -The Team')
            body = text.format(fn, ln, donations)
            file.write(body)
    return


def donor_name_split(donor_name):
    donor_name = donor_name.split(' ')
    return [donor_name[0], donor_name[1]]


def donor_lookup(donor_name):
    name = donor_name_split(donor_name)
    for d in _donors:
        if d[0]['first_name'] == name[0] and d[0]['last_name'] == name[1]:
            return True
        else:
            return False


def request_donation():
    donation = input('Donation amount: ')
    return donation


def format_donation(donation):
    donation = float(donation)
    donation = "${0:.2f}".format(donation)
    return donation


def append_donation(donor_name, donation):
    name = donor_name_split(donor_name)
    for i in range(len(_donors) - 1):
        fn = _donors[i][0]['first_name']
        ln = _donors[i][0]['last_name']
        if fn == name[0] and ln == name[1]:
            _donors[i][1]['donations'].append(float(donation))
            return


def add_donor(donor_name, donation):
    name = donor_name_split(donor_name)
    new_donor = [
        {
            'first_name': name[0],
            'last_name': name[1]
        },
        {
            'donations': [
                float(donation)
            ]
        }
    ]
    _donors.append(new_donor)


def donor_email(donor_name, donation):
    email_str = 'Dear {a},\nThank you for your generous ' \
        + 'donation of ${b}.\nRegards\nUW Student'
    print(email_str.format(a=donor_name, b=donation))
    return


def create_report():
    sorted_donors = sort_donors()
    rows = get_donor_summary(sorted_donors)
    print_report(rows)
    return 'break'


def sort_donors():
    sorted_donors = list(_donors)
    sorted_donors.sort(key=lambda x: sum(x[1]['donations']), reverse=True)
    return sorted_donors


def get_donor_summary(donors):
    """ pass summary list of strings that is ready for parsing"""
    summary = []
    for d in donors:
        donations = d[1]['donations']
        total = float(sum(donations))
        number = len(donations)
        str_total = format_donation(sum(donations))
        str_number = str(len(donations))
        str_average = format_donation(total / max(number, 1))
        summary.append([d[0], str_total, str_number, str_average])
    return summary


def print_report(rows):
    # table heading
    h = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    hs = ' | '
    hf = '{0:<25}{1}{2}{3}{4}{5}{6}'
    print(hf.format(h[0], hs, h[1], hs, h[2], hs, h[3]))
    # table rows
    for r in rows:
        name = "{first_name} {last_name}".format(**r[0])
        f0 = '{0:<' + str(max(len(name), 25)) + '}'
        f2 = '{2:>' + str(max(len(r[1]), len(h[1]))) + '}'
        f4 = '{4:>' + str(max(len(r[2]), len(h[2]))) + '}'
        f6 = '{6:>' + str(max(len(r[3]), len(h[3]))) + '}'
        rf = f0 + '{1}' + f2 + '{3}' + f4 + '{5}' + f6
        args = [name, '  $', r[1], ' | ', r[2], '  $', r[3]]
        print(rf.format(*args))
    menu_selection(main_prompt, main_dispatch)


def quit_script():
    sys.exit()


def exit_menu():
    menu_selection(main_prompt, main_dispatch)
    return "break"


def menu_selection(prompt, dispatch_dict):
    while True:
        r = input(prompt)
        if dispatch_dict[r]() == "break":
            break


# main menu
main_prompt = ("\n--- MAIN MENU ---\n"
               "What do you want to do?\n"
               "Type '1' - Send a Thank You\n"
               "Type '2' - Print a Report\n"
               "Type '3' - Send letters to everyone\n"
               "Type 'q' - Quit script >> "
               )
main_dispatch = {"1": submit_donor,
                 "2": create_report,
                 "3": letters,
                 "q": quit_script,
                 }


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
