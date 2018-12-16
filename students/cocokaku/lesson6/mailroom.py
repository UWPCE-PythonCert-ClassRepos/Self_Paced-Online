#!/usr/bin/python3
"""
mailroom part 4: adding unit testing
(1) refactor: pass donor_db as input parameter rather than as global
(2) refactor: print donor list in send_thank_you instead of list_donors,
                list_donors now returns string to calling module
(3) refactor: moved user interaction for add_donation out of function,
                into send_thank_you (consolidate user input into one module)
"""
import os

DONOR_DB = {
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Colleen Kaku": [50000, 1000000, 1000000]
    }


def send_thank_you(db):
    """Add a donor/donation and print out a thank you letter"""
    # loop for user input: donor name, or list, or quit
    while True:
        name = input("\nDonor Full Name (type 'list' for donor list or 'q' to quit): ")
        if name in ('q', 'quit'):
            return
        if name == 'list':
            print(list_donors(db))
            continue
        # if name == donor name:
        #   loop for user to input valid donation amount
        while True:
            amount = input("Donation amount (type 'q' to quit): ")
            if amount in ('q', 'quit'):
                return
            try:
                add_donation(db, name, float(amount))
            except ValueError:
                print('Invalid input, try again')
            else:
                break
        print('\n' + thank_you_letter(db, name))


def list_donors(db):
    """Return new-line delimited list of donor names"""
    return '\n'.join(['   '+name for name in db])


def add_donation(db, name, amount):
    """Add donor name and donation to db"""
    if name not in db.keys():
        db[name] = []
    db[name].append(amount)


def thank_you_letter(db, name):
    """Return text of thank you letter"""
    return f"Dear {name},\n" \
           f"Thank you very much for your generous donation of ${db[name][-1]:,.2f}.\n" \
           f"Sincerely,\n" \
           f"PYTHON210 Class of 2018"


def create_a_report(db):
    """Print a summary of donors and amounts donated to screen"""
    print("\n"+summary_report(db))


def summary_report(db):
    """Return a summary report of donors and amounts donated"""
    summary_list = [(name, sum(amounts), len(amounts), sum(amounts)/len(amounts))
                    for (name, amounts) in db.items()]
    summary_list.sort(key=get_second, reverse=True)
    report = "DONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION\n"
    for (name, total, num, avg) in summary_list:
        report += f"{name:20s}   ${total:12,.2f} {num:3d}               ${avg:11,.2f}\n"
    return report


def get_second(elem):
    """Return second item in list, sort key for summary_list"""
    try:
        return elem[1]
    except IndexError:
        return None


def send_all_letters(db):
    """Write thank you letters to all donors to text files, filename = <donor_name>.txt"""
    dir_name = input("Output directory ('.' for current dir): ")
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    for name in db:
        file_name = dir_name + '/' + name.replace(',', '').replace(' ', '_') + '.txt'
        with open(file_name, 'w') as f:
            f.write(thank_you_letter(db, name))


def main_menu_error(_):
    print("Invalid choice, try again")


def quit_program(_):
    quit()


def main():
    """Main menu for mailroom program"""
    switch_menu_dict = {
        "1": send_thank_you,
        "2": create_a_report,
        "3": send_all_letters,
        "q": quit_program,
        "quit": quit_program
        }
    while True:
        print("\nMAIN MENU")
        print("   1 = Send a Thank You")
        print("   2 = Create a Report")
        print("   3 = Send Letters to Everyone")
        print("   q = Quit")
        choice = input("   ? ")
        switch_menu_dict.get(choice, main_menu_error)(DONOR_DB)


if __name__ == '__main__':
    main()
