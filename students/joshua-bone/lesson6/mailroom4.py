#!/usr/bin/env python3.6

# Joshua Bone - UW Python 210 - Lesson 6
# 01/09/2019
# Assignment: Mailroom, Part 4

import sys
from collections import defaultdict

MAIN_MENU = ("Welcome to the Mailroom!",
             "",
             "Please select from the following options:",
             "(S)end a Thank You",
             "(C)reate a Report",
             "(M)ail Letters to Everyone",
             "(Q)uit")

TY_MENU = ("Send a Thank You",
           "",
           "At the prompt you can either:",
           "\tEnter a donor name,",
           "\tType 'list' to display all existing donors,",
           "\tType 'q' to go back to main menu.")

PROMPT = "Your selection: "

BAD_INPUT_NOTIF = "Input not understood. Try again"

TY_LETTER = ("Dear {full_name},",
             "",
             "\tThank you for your very kind donation{s} of {amounts}.",
             "",
             "\t{it_they} will be put to very good use.",
             "",
             "\t\tSincerely,",
             "\t\t\t-The Team")

NUM_FORMAT_WIDTH = 13

NOT_UNDERSTOOD = "Input not understood. Please try again."

DONORS = defaultdict(list)


def display(lines):
    print('-' * 80)
    if isinstance(lines, str):
        print(lines)
    else:
        for line in lines:
            print(line)


def add_gift(name, amt, *, donors=DONORS):
    donors[name].append(amt)


def report_header(*, donors=DONORS, width=NUM_FORMAT_WIDTH):
    max_len = 5 + max((len(d) for d in donors.keys()))
    return (f"{'Donor Name': <{max_len}}|" +
            f"{'Total Given': >{width}} |" +
            f"{'Num Gifts': >{width}} |" +
            f"{'Average Gift': >{width}}")


def dollar_string(amt):
    return f"${amt:.2f}"


def sorted_report_body(*, width=NUM_FORMAT_WIDTH, donors=DONORS):
    max_len = 5 + max((len(d) for d in donors))
    unsorted_list = []
    for name in donors:
        amt = sum(donors[name])
        num = len(donors[name])
        avg = amt / num
        output = (f"{name:<{max_len}}|" +
                  f"{dollar_string(amt):>{width}} |" +
                  f"{str(num):>{width}} |" +
                  f"{dollar_string(avg):>{width}}")
        unsorted_list.append((amt, output))
    # Sort by total amount, descending.
    return list(map(lambda t: t[1],
                    sorted(unsorted_list, key=lambda t: t[0], reverse=True)))


def display_report(*, donors=DONORS, width=NUM_FORMAT_WIDTH):
    display(report_header(donors=donors, width=width))
    display(sorted_report_body(donors=donors, width=width))


def format_amts(amts):
    fmt = "${:.2f}"
    string = ", and ".join([fmt.format(amt) for amt in amts])
    return string.replace("and ", "", len(amts) - 2)


def format_ty(name, amts, *, letter=TY_LETTER):
    d = {
        "full_name": name,
        "amounts": format_amts(amts),
        "it_they": "They" if len(amts) > 1 else "It",
        "s": "s" if len(amts) > 1 else ""
    }
    return [line.format(**d) for line in letter]


def send_ty(name, *, donors=DONORS):
    display("Sending a thank you to " + name)
    try:
        amt = float(input("Enter amount: "))
    except ValueError:
        display("Error: Could not parse input. Please try again.")
        send_ty(name)
    add_gift(name, amt, donors=DONORS)
    display(format_ty(name, [amt]))


def display_donors(*, donors=DONORS):
    display(["Existing Donors:", ""] + list(donors.keys()))


def get_menu_input(menu, prompt=PROMPT):
    display(menu)
    print("\n")
    return input(prompt)


def mail_all_donors(*, donors=DONORS):
    for d in donors:
        with open(d + ".txt", "w") as f:
            f.write("\n".join(format_ty(d, donors[d])))
    display(f"Mailed {len(donors)} letters.")


def do_ty_menu():
    i = get_menu_input(TY_MENU)
    fns = ty_dict.get(i.lower(),
                      [lambda: send_ty(i),
                       do_main_menu])
    for fn in fns:
        fn()


def do_main_menu():
    i = get_menu_input(MAIN_MENU)
    fns = main_dict.get(i.lower(),
                        [lambda: display(NOT_UNDERSTOOD),
                         do_main_menu])
    for fn in fns:
        fn()


ty_dict = {'list': [display_donors, do_ty_menu],
           'q': [lambda: display("Returning to Main Menu."), do_main_menu]}

main_dict = {'s': [do_ty_menu],
             'c': [display_report, do_main_menu],
             'm': [mail_all_donors, do_main_menu],
             'q': [lambda: display("Exiting...")]}


def do_mailroom():
    add_gift("William Gates, III", 456456.22)
    add_gift("William Gates, III", 197328.27)
    add_gift("Mark Zuckerberg", 4567.97)
    add_gift("Mark Zuckerberg", 7521.42)
    add_gift("Mark Zuckerberg", 4306.71)
    add_gift("Jeff Bezos", 877.33)
    add_gift("Paul Allen", 150.00)
    add_gift("Paul Allen", 450.00)
    add_gift("Paul Allen", 108.42)
    add_gift("Sergey Brin", 956755.89)
    add_gift("Sergey Brin", 123.89)
    add_gift("Sergey Brin", 34732.22)
    do_main_menu()


if __name__ == "__main__":
    do_mailroom()
