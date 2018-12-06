#!/usr/bin/python3
"""
mailroom part 3: adding exceptions and comprehensions
1. change list_donors print to comprehension
2. exception handling for non-numeric donation amount
(3) was already using exception handling for invalid choice on main menu
(4) was already using comprehension to create summary list for report
"""
import os

donor_db = {
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Colleen Kaku": [50000, 1000000, 1000000]
    }


def send_thank_you():
    """Add a donor/donation and print out a thank you letter"""
    while True:
        name = input("\nDonor Full Name (type 'list' for donor list or 'q' to quit): ")
        if name in ('q', 'quit'):
            return
        if name == 'list':
            list_donors()
            continue
        add_donation(name.title())


def list_donors():
    """List donor names, sub-function for send_thank_you()"""
    print('\n'.join(['   '+name for name in donor_db]))


def add_donation(name):
    """Add donor name and donation to donor_db, sub-function for send_thank_you()"""
    while True:
        amount = input("Donation amount (type 'q' to quit): ")
        if amount in ('q', 'quit'):
            return
        try:
            if name not in donor_db.keys():
                donor_db[name] = [float(amount)]
            else:
                donor_db[name].append(float(amount))
        except ValueError:
            print('Invalid input, try again')
        else:
            break
    print('\n' + thank_you_letter(name))


def thank_you_letter(name):
    """Return text of thank you letter"""
    return f"Dear {name},\n" \
           f"Thank you very much for your generous donation of ${donor_db[name][-1]:,.2f}.\n" \
           f"Sincerely,\n" \
           f"PYTHON210 Class of 2018"


def create_a_report():
    """Print a summary of donors and amounts donated to screen"""
    summary_list = [(name, sum(amounts), len(amounts), sum(amounts)/len(amounts))
                    for (name, amounts) in donor_db.items()]
    summary_list.sort(key=get_second, reverse=True)
    print("\nDONOR NAME             TOTAL DONATED   NUM DONATIONS   AVG DONATION AMT")
    for (name, total, num, avg) in summary_list:
        print(f"{name:20s}   ${total:12,.2f} {num:3d}               ${avg:12,.2f}")


def get_second(elem):
    """Return second item in list, sort key for summary_list"""
    return elem[1]


def send_all_letters():
    """Write thank you letters to all donors to text files, filename = <donor_name>.txt"""
    dir_name = input("Output directory ('.' for current dir): ")
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    for name in donor_db:
        file_name = dir_name + '/' + name.replace(',', '').replace(' ', '_') + '.txt'
        with open(file_name, 'w') as f:
            f.write(thank_you_letter(name))


def main():
    """Main menu for mailroom program"""
    switch_menu_dict = {
        "1": send_thank_you,
        "2": create_a_report,
        "3": send_all_letters,
        "q": exit,
        "quit": exit
        }
    while True:
        print("\nMAIN MENU")
        print("   1 = Send a Thank You")
        print("   2 = Create a Report")
        print("   3 = Send Letters to Everyone")
        print("   q = Quit")
        choice = input("   ? ")
        try:
            switch_menu_dict[choice]()
        except KeyError:
            print("Invalid choice, try again")


if __name__ == '__main__':
    main()
