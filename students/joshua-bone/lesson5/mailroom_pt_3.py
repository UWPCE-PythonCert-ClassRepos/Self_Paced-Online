#!/usr/bin/env python3

# Joshua Bone - UW Python 210 - Lesson 5
# 01/07/2019
# Assignment: Mailroom, Part 3

from enum import Enum


class LoopAction(Enum):
    CONTINUE = 1
    BREAK = 2


MAIN_MENU = ("Welcome to the Mailroom!\n\n\n" +
             "Please select from the following options:\n" +
             "(S)end a Thank You\n" +
             "(C)reate a Report\n" +
             "(M)ail Letters to Everyone\n"
             "(Q)uit\n\n\n")
TY_MENU = ("Enter a name, or type 'list' for existing donors.\n" +
           "Type 'q' or 'quit' to go back to main menu.\n")
PROMPT = "Your selection: "
BAD_INPUT_NOTIF = "Input not understood. Try again\n"
TY_LETTER = ("Dear {full_name},\n\n" +
             "\tThank you for your very kind donation{s} of {amounts}.\n\n" +
             "\t{it_they} will be put to very good use.\n\n" +
             "\t\tSincerely,\n" +
             "\t\t\t-The Team")
NUM_FORMAT_WIDTH = 13

donors = {}


def add_donor_gift(name, amt):
    assert isinstance(amt, (int, float))
    assert amt > 0
    assert isinstance(name, str)
    if name not in donors:
        donors[name] = []
    donors[name].append(amt)


add_donor_gift("William Gates, III", 456456.22)
add_donor_gift("William Gates, III", 197328.27)
add_donor_gift("Mark Zuckerberg", 4567.97)
add_donor_gift("Mark Zuckerberg", 7521.42)
add_donor_gift("Mark Zuckerberg", 4306.71)
add_donor_gift("Jeff Bezos", 877.33)
add_donor_gift("Paul Allen", 150.00)
add_donor_gift("Paul Allen", 450.00)
add_donor_gift("Paul Allen", 108.42)
add_donor_gift("Sergey Brin", 956755.89)
add_donor_gift("Sergey Brin", 123.89)
add_donor_gift("Sergey Brin", 34732.22)


def print_horizontal():
    print('-' * 80)


def create_report():
    max_len = 5 + max((len(d) for d in donors))
    # print header and horizontal lines
    print("-" * (max_len + 2 + 3 * (1 + NUM_FORMAT_WIDTH)))
    print((f"{'Donor Name': <{max_len}}|" +
           f"{'Total Given': >{NUM_FORMAT_WIDTH}} |" +
           f"{'Num Gifts': >{NUM_FORMAT_WIDTH}} |" +
           f"{'Average Gift': >{NUM_FORMAT_WIDTH}}"))
    print("-" * (max_len + 2 + 3 * (1 + NUM_FORMAT_WIDTH)))
    unsorted_list = []
    for name in donors:
        amt = sum(donors[name])
        num = len(donors[name])
        avg = amt / num
        output = (f"{name: <{max_len}}" +
                  f"${amt:{NUM_FORMAT_WIDTH}.2f}  " +
                  f"{num:>{NUM_FORMAT_WIDTH}d} " +
                  f"${avg:{NUM_FORMAT_WIDTH}.2f}")
        unsorted_list.append((amt, output))
    sorted_list = sorted(unsorted_list, key=lambda t: t[0], reverse=True)
    for p in sorted_list:
        print(p[1])
    print("-" * (max_len + 2 + 3 * (1 + NUM_FORMAT_WIDTH)) + "\n\n")


def print_donors():
    print("Existing donors:")
    for d in donors:
        print(d)


def format_amts(amts):
    fmt = "${:.2f}"
    string = ", and ".join([fmt.format(amt) for amt in amts])
    return string.replace("and ", "", len(amts) - 2)


def format_ty(name, amts):
    d = {
        "full_name": name,
        "amounts": format_amts(amts),
        "it_they": "They" if len(amts) > 1 else "It",
        "s": "s" if len(amts) > 1 else ""
    }
    return TY_LETTER.format(**d)


def send_ty(name):
    try:
        amt = float(input("Enter amount: "))
    except ValueError:
        print("Error: Could not parse input. Please try again.")
        return LoopAction.CONTINUE
    add_donor_gift(name, amt)
    print_horizontal()
    print(format_ty(name, [amt]))
    return LoopAction.BREAK


def quit_ty():
    print("Returning to Main Menu...")
    return LoopAction.BREAK


ty_dict = {'list': print_donors, 'q': quit_ty, 'quit': quit_ty}


def do_ty_menu():
    resp = LoopAction.CONTINUE
    while resp != LoopAction.BREAK:
        i = do_menu(TY_MENU)
        resp = ty_dict.get(i.lower(), lambda: send_ty(i))()


def quit_main():
    print("Exiting...")
    return LoopAction.BREAK


def mail_all_donors():
    for d in donors:
        with open(d + ".txt", "w") as f:
            f.write(format_ty(d, donors[d]))
    print(f"Mailed {len(donors)} letters.\n\n")


menu_dict = {'s': do_ty_menu,
             'c': create_report,
             'm': mail_all_donors,
             'q': quit_main}


def do_menu(menu, prompt=PROMPT):
    print_horizontal()
    print(menu)
    return input(prompt)


if __name__ == "__main__":
    resp = LoopAction.CONTINUE
    while resp != LoopAction.BREAK:
        i = do_menu(MAIN_MENU).lower()
        resp = menu_dict.get(i, lambda: print(BAD_INPUT_NOTIF))()
