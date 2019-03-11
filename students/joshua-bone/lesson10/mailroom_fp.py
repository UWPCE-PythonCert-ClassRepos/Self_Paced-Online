# Joshua Bone - UW Python 210 - Lesson 10
# 03/08/2019
# Assignment: Functional Mailroom

from donors import Donors
from formatter import Formatter

MAIN_MENU = ("Welcome to the Mailroom!",
             "",
             "Please select from the following options:",
             "(S)end a Thank You",
             "(C)reate a Report",
             "(M)ail Letters to Everyone",
             "(P)rojection Explorer",
             "(Q)uit")

TY_MENU = ("Send a Thank You",
           "",
           "At the prompt you can either:",
           "\tEnter a donor name,",
           "\tType 'list' to display all existing donors,",
           "\tType 'q' to go back to main menu.")

NOT_UNDERSTOOD = "Input not understood. Please try again."

PROMPT = "Your selection: "

MIN_AMT_PR = "Enter a minimum amount, or press Enter to skip: "
MAX_AMT_PR = "Enter a maximum amount, or press Enter to skip: "

donors = Donors()
formatter = Formatter(donors)


def display(lines):
    print('-' * 80)
    if isinstance(lines, str):
        print(lines)
    else:
        for line in lines:
            print(line)
    print("\n")


def display_donors():
    display(["Existing Donors:", ""] + donors.names)


def display_report(f=formatter):
    display(f.report_header())
    display(f.sorted_report_body())


def mail_all_donors():
    donor_list = donors.get_all()
    for d in donor_list:
        with open(d.name + ".txt", "w") as f:
            f.write("\n".join(formatter.format_ty(d.name, d.donations)))
    display(f"Mailed {len(donor_list)} letters.")


def send_ty(name):
    display("Sending a thank you to " + name)
    amt = get_float("Enter amount: ")
    donors.add_donation(name, amt)
    display(formatter.format_ty(name, [amt]))


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


def get_menu_input(menu, prompt=PROMPT):
    display(menu)
    return input(prompt)


def do_projection():
    factor = get_float("Enter factor to scale by: ")
    min_amt = get_float(MIN_AMT_PR, required=False)
    max_amt = get_float(MAX_AMT_PR, required=False)
    new_donors = donors.challenge(factor, min_amt=min_amt, max_amt=max_amt)
    new_fmt = Formatter(new_donors)
    display("<<<BEGIN CUSTOM PROJECTION>>>")
    display_report(new_fmt)
    display("<<< END CUSTOM PROJECTION >>>")


def get_float(msg, *, required=True):
    _input = None
    while _input is None:
        try:
            _input = input(msg)
            if _input == '' and not required:
                return None
            _input = float(_input)
        except ValueError:
            display("Error: Could not parse float. Please try again.")
    return _input


ty_dict = {'list': [display_donors, do_ty_menu],
           'q': [lambda: display("Returning to Main Menu."), do_main_menu]}


main_dict = {'s': [do_ty_menu],
             'c': [display_report, do_main_menu],
             'm': [mail_all_donors, do_main_menu],
             'p': [do_projection, do_main_menu],
             'q': [lambda: display("Exiting...")]}


if __name__ == "__main__":
    donors.add_donation("William Gates, III", 456456.22)
    donors.add_donation("William Gates, III", 197328.27)
    donors.add_donation("Mark Zuckerberg", 4567.97)
    donors.add_donation("Mark Zuckerberg", 7521.42)
    donors.add_donation("Mark Zuckerberg", 4306.71)
    donors.add_donation("Jeff Bezos", 877.33)
    donors.add_donation("Paul Allen", 150.00)
    donors.add_donation("Paul Allen", 450.00)
    donors.add_donation("Paul Allen", 108.42)
    donors.add_donation("Sergey Brin", 956755.89)
    donors.add_donation("Sergey Brin", 123.89)
    donors.add_donation("Sergey Brin", 34732.22)
    do_main_menu()
