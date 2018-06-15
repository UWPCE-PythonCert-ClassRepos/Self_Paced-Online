import sys
import os
import datetime


def menu():
        print("\n------------------ Main Menu ------------------\n")
        print("Choose an action:\n")
        print("Press 1 to send a Thank You\n")
        print("Press 2 to print letters\n")
        print("Press 3 to create a report\n")
        print("Press 4 to quit\n")
        choice = input("Enter your choice-> ")
        user_options.get(choice, menu)()

def thankyou():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("- If the user types ‘list’, show them a list of the donor names and re-prompt -")
    print("- type 'menu' at any time to return to the menu -\n")

    name_check = input("Enter first and last name of a donor\n\n-> ").lower()

    if name_check not in user_options:
        donation = float(input("What is the donation amount? -> "))
        name_check = name_check.title()
        if name_check in donors:
            donors[name_check].append(donation)
        else:
            donors.setdefault((name_check), []).append(donation)
        letter_dict = {"name": name_check, "don": donation}

        print("""\n------------------ On Screen Letter ------------------\n
Dear {name},

Thank you for your contribution of ${don:,.2f}
It will be put to very good use.

Sincerely,
Vinodh""".format(**letter_dict))

    user_options.get(name_check, menu)()

def letters():
    print("""\n--------- Exporting Letters to Everyone ---------\n
Thank you letters have been exported to {}""".format(os.getcwd()))

    for name in donors:
        letter_dict = {"donor": name, "donation": donors[name][-1]}
        letter = """Dear {donor},

Thank you for your contribution of ${donation:,.2f} .It will be put to very good use.

Sincerely,
Scrooge McDuck""".format(**letter_dict)
        with open(str(name) + "_" + str(datetime.date.today()) +
                  '.txt', 'w') as out_file:
            out_file.write(letter)

    menu()

def report():
    print("\n-------------------- REPORT --------------------\n")

    column = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    donors_report = []

    for name in donors:
        sum_don = sum(donors[name])
        num_don = len(donors[name])
        ave_don = sum_don / num_don
        donors_report.append([name, sum_don, num_don, ave_don])

    print("{:<15}{:>17}{:>15}{:>10}".format(*column))
    print("---------------------------------------------------------------")


    for name in donors_report:
        print('{:<20} ${:>13.2f}{:>12}  ${:>10.2f}'.format(*name))

    menu()

def donor_list():
    # lists all the donors
    # calls the 'thankyou' function at the end to ask for user input
    print("\n------------------ DONOR LIST ------------------\n")

    for name in donors:
        print(name)

    thankyou()


def quit_program():
    print("quit program")

donors = {
        'William Gates, III': [653784.49, 2, 326892.24],
        'Mark Zuckerberg': [16396.10, 3, 5465.37],
        'Jeff Bezos': [877.33, 1, 877.33],
        'Paul Allen': [708.42, 3, 236.14],
        }

user_options = {
                '1':thankyou,
                '2':letters,
                '3':report,
                '4':quit_program,
                'list': donor_list,
                'menu': menu
                }


if __name__ == '__main__':
    menu()