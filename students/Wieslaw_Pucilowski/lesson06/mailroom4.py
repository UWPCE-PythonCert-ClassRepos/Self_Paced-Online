#!/usr/bin/env python3
# lesson06 mailroom4
from operator import itemgetter
from collections import defaultdict

__author__ = "Wieslaw Pucilowski"


dict_all = {
            ('Richard', 'Lionheart'): [100.5, 36.30, 230],
            ('Andreas', 'Bolen'): [220, 1000],
            ('Ivan', 'Smirnoff'): [1200],
            ('Karl', 'Marx'): [345.2, 140.20],
            ('Alvaro', 'Speedy'): [330, 850, 100.50],
            ('Ilunga', 'Mulungma'): [350, 550],
            ('Denis', 'Donuts'): [68],
            ('Haruto', 'Asai'): [45, 997.50],
            ('Great', 'Gatsby'): [0.5],
           }


def donor_greeting(first, last):
    greetings = """
    Ex Programmers Charity
    1999 Heartbeat Avenue
    11111 Fresh Spring, Alaska

    Dear {first_name} {last_name},

    Thank you so much for your generous donation of ${total}

    It will be put to very good use.

                       Sincerely,
                          -The Team

    """.format(**select_user(first, last))
    return greetings


def write_letter(first, last):
    message = donor_greeting(first, last)
    if message:
        try:
            with open(first+'_'+last+'.txt', 'w') as f:
                f.write(message)
        except IOErrors as e:
            print("""
                Cannot write a file, cought
                {}
            """.format(e))


def send_letter_all():
    print("Sending letters to all donors...")
    for donor in dict_all.keys():
        write_letter(donor[0], donor[1])


def print_greetings(first, last):
    message = donor_greeting(first, last)
    if message:
        print(message)


def select_user(first, last):
    try:
        return {'first_name': first, 'last_name': last,
                'donations': len(dict_all[(first, last)]),
                'total': sum(dict_all[(first, last)])}
    except KeyError:
        return None


def list_donors():
    for donor in sorted(dict_all):
        print("{} {},".format(donor[0], donor[1]))


def add_donor():
    name = input("Type donor first and last name: ")
    if len(name.split()) >= 2:
        first, last = name.split()[0], name.split()[1]
    else:
        print("Only First name added")
        first = name.split()[0]
        last = ""
    donation_in = input("Donation in USD: ")
    try:
        donation = float(donation_in)
    except ValueError as e:
        print("""
                ValueError exception cought: {}
                Please add donor with the right donation in USD.
               """.format(e))
        print()
    else:
        add_donor_dict(first, last, float(donation))
        print_greetings(first, last)


def add_donor_dict(first, last, donation):
    try:
        dict_all[(first, last)].append(donation)
    except KeyError:
        dict_all[(first, last)] = [donation]


def custom_key(a):
    return sum(a[1])


def create_report():
    report = ""
    report += "{:<30}| {:<18}| {:<8}| {:<18}\n".format('Donor Name',
                                                       'Total Given',
                                                       'Num Gifts',
                                                       'Average Gift')
    report += "{:-<80}\n".format('')
    for k, v in sorted(dict_all.items(), key=custom_key, reverse=True):
        report += "{:<30}{}{:>18.2f}{:>11}{}{:>17.2f}\n".format(k[0]+' '
                                                                + k[1],
                                                                ' $',
                                                                sum(v),
                                                                len(v),
                                                                ' $',
                                                                sum(v) /
                                                                len(v))
    return(report)


def print_report():
    print(create_report())


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print(response, wrong_option)


wrong_option = "{:<20}".format(" - Wrong option !!!")


def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)


def quit_menu():
    print("Goodbye...\n")
    return "exit menu"


main_prompt = """
    {:-^30}

    1 - Send a Thank You
    2 - Create a Report
    3 - Send letters to everyone
    q - Quit
""".format(' Main Menu ')


main_dispatch = {'1': sub_menu,
                 '2': print_report,
                 '3': send_letter_all,
                 'q': quit_menu, }


sub_prompt = """
    {:-^30}

    1 - Add new donor, donation
    2 - List donors
    q - Go to Main Menu

""".format(' Add/List donors ')


sub_dispatch = {'1': add_donor,
                '2': list_donors,
                'q': quit_menu, }


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
