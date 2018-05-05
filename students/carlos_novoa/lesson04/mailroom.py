#!/usr/bin/env python3
import os
import datetime

"""
Lesson4 - Mailroom, Part 2
"""

now = datetime.datetime.now()

_donors = {
    'Jim Halpert': [1.00],
    'Pam Beesley': [1000.00, 2000.00, 3000.00],
    'Dwight Shrute': [2.00, 3.00],
    'Michael Scott': [10.00, 20.00, 30.00],
    'Andy Bernard': [500.00]
}


def quit_menu():
    return "break"


def thank_you():
    donor_name = input("Please enter donor's name: ")
    donor_foud = donor_lookup(donor_name)
    if donor_foud:
        donations = get_donations(donor_name)
        donor_email(donor_name, donations)
    else:
        print("Please choose an existing donor: ")
        donor_list()
        thank_you()


def donor_lookup(donor_name):
    if donor_name in _donors:
        return True
    else:
        return False


def donor_list():
    for d in _donors:
        print(d)


def get_donations(donor_name):
    donations = _donors.get(donor_name)
    if donations is not None:
        return sum(donations)
    else:
        return 0


def format_donation(donation):
    donation = float(donation)
    donation = "${0:.2f}".format(donation)
    return donation


def donor_email(donor_name, donations):
    donations = format_donation(donations)
    body = ('Dear {},\n\n'
            '        Thank you for your very kind donation of {}.\n\n'
            '        It will be put to very good use.\n\n'
            '               Sincerely,\n'
            '                  -The Team')
    print(body.format(donor_name, donations))


def letters():
    cwd = os.getcwd()
    date = now.strftime('%Y-%m-%d')
    path = cwd + '/letters/'
    ext = '.txt'
    for key, val in _donors.items():
        total_donations = sum(val)
        name = key.split(' ')
        file_path = "{}{}_{}_{}{}".format(path, date, name[0], name[1], ext)
        donations = format_donation(total_donations)
        with open(file_path, 'w') as letter:
            text = ('Dear {} {},\n\n'
                    '        Thank you for your very kind donation of {}.\n\n'
                    '        It will be put to very good use.\n\n'
                    '               Sincerely,\n'
                    '                  -The Team')
            body = text.format(name[0], name[1], donations)
            letter.write(body)
    print('Letters created.')


def create_report():
    sorted_donors = sort_donors()
    rows = get_donor_summary(sorted_donors)
    print_report(rows)


def sort_donors():
    sorted_donors = sorted(_donors.items(), key=lambda x: x[1], reverse=True)
    return sorted_donors


def get_donor_summary(donors):
    """ pass summary list of strings that is ready for parsing"""
    summary = []
    for name, donations in _donors.items():
        total = float(sum(donations))
        number = len(donations)
        str_total = format_donation(total)
        str_number = str(len(donations))
        str_average = format_donation(total / max(number, 1))
        summary.append([name, str_total, str_number, str_average])
    return summary


def print_report(rows):
    # table heading
    h = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    hs = ' | '
    hf = '{0:<25}{1}{2}{3}{4}{5}{6}'
    print(hf.format(h[0], hs, h[1], hs, h[2], hs, h[3]))
    # table rows
    for r in rows:
        name = "{}".format(r[0])
        f0 = '{0:<' + str(max(len(name), 25)) + '}'
        f2 = '{2:>' + str(max(len(r[1]), len(h[1]))) + '}'
        f4 = '{4:>' + str(max(len(r[2]), len(h[2]))) + '}'
        f6 = '{6:>' + str(max(len(r[3]), len(h[3]))) + '}'
        rf = f0 + '{1}' + f2 + '{3}' + f4 + '{5}' + f6
        args = [name, '  $', r[1], ' | ', r[2], '  $', r[3]]
        print(rf.format(*args))
    menu_selection(main_prompt, main_dispatch)


def menu_selection(prompt, dispatch_dict):
    while True:
        r = input(prompt)
        if r not in main_dispatch:
            print('Please choose a valid menu option.')
            continue
        if dispatch_dict[r]() == "break":
            break


# main menu
main_prompt = ("\n--- MAIN MENU ---\n"
               "What do you want to do?\n"
               "Type '1' - Send a Thank You\n"
               "Type '2' - Print a Report\n"
               "Type '3' - Send letters to everyone\n"
               "Type 'q' - Quit >> "
               )
main_dispatch = {'1': thank_you,
                 '2': create_report,
                 '3': letters,
                 'q': quit_menu,
                 }

if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
