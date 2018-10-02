# ------------------------------------------------- #
# Title: Lesson 9, mail room 5.2 main
# Dev:   Craig Morton
# Date:  9/29/2018
# Change Log: CraigM, 9/29/2018, mail room 5.2 main
# ------------------------------------------------- #

from datetime import datetime
import os
import mailroom_data
import mailroom_behavior


def send_thank_you(db):
    """Generate thank you letter"""
    name_queries = ("First name", "Last name")
    full_name = list()
    q = 0
    while q < len(name_queries):
        print("Please enter {}, 'list' for names, or '*' for main menu".format(name_queries[q]))
        name = input(": ")
        if name == '*':
            return ""
        elif name.lower() == 'list':
            for donor in db.get_donors():
                print(donor.get_name())
        else:
            full_name.append(name)
            q += 1
    amount = ""
    while not amount.isnumeric():
        print("Please enter a donation amount, or '*' for main menu:")
        amount = input("$ ")
        if amount == '*':
            return
    amount = float(amount)
    return mailroom_behavior.send_thank_you(db, full_name[0], full_name[1], amount)


def send_letters(db):
    """Generates letters for all donors"""
    subdir = str(datetime.now())
    subdir = subdir.replace(':', '_')
    try:
        os.mkdir(subdir)
    except OSError as oserr:
        print(oserr)
        print("\nThe directory was unable to be created!\n")
        return "Error!"
    try:
        with open("template.txt", 'r') as infile:
            template_in = infile.read()
    except FileNotFoundError as fnferr:
        print(fnferr)
        print("\nThe template letter file was not found!")
        return "Error!"
    letters = mailroom_behavior.send_letters(db, template_in)
    for letter in letters:
        filename = "./{dir}/{name}.txt".format(name=letter[0], dir=subdir)
        with open(filename, 'w') as outfile:
            outfile.write(letter[1])
    return "\n{num} letters created!".format(num=len(letters))


def challenge_multiplier(db):
    """Donation multiplier"""
    multiplier = input("Amount to multiply donations by: ")
    if not multiplier.isnumeric():
        return "A user input error has occurred!\n"
    multiplier = float(multiplier)
    print("Please apply a multiplier only to existing donations: ")
    print("1: Above an amount")
    print("2: Below an amount")
    print("3: All donations")
    threshold = input(": ")
    above_amount = 0
    below_amount = 0
    if threshold == '1':
        above_amount = input("Above which amount: ")
        if not above_amount.isnumeric():
            return "A user input error has occurred!\n"
        above_amount = float(above_amount)
    elif threshold == '2':
        below_amount = input("Below which amount: ")
        if not below_amount.isnumeric():
            return "A user input error has occurred!\n"
        below_amount = float(below_amount)
    elif threshold != '3':
        return "A user input error has occurred!\n"
    return mailroom_behavior.challenge_project(db=db, above=above_amount, below=below_amount, multiplier=multiplier)


main_menu_list = [
    "\nPlease choose a number: \n",
    "1: Send 'Thank You' note",
    "2: Create Report",
    "3: Send letters to everyone",
    "4: Challenge Multiplier",
    "q: Quit"]

main_menu_actions = {'1': send_thank_you, '2': mailroom_behavior.create_report,
                     '3': send_letters, '4': challenge_multiplier}


def draw_main_menu():
    """Main menu presentation"""
    print("\n".join(main_menu_list))


def get_main_menu_input():
    """Main menu user input"""
    user_input = input(":")
    user_input = user_input.lower().strip()
    return user_input


if __name__ == "__main__":
    db = mailroom_data.DonorCapture()
    d1 = mailroom_data.Donor("Bill", "Gates")
    d1.add_donation(150)
    d2 = mailroom_data.Donor("Paul", "Allen")
    d2.add_donation(90)
    d2.add_donation(1000)
    d3 = mailroom_data.Donor("Jeff", "Bezos")
    d3.add_donation(47)
    d3.add_donation(340)
    d3.add_donation(2001)
    db.add_donor(d1)
    db.add_donor(d2)
    db.add_donor(d3)
    running = True
    while running:
        draw_main_menu()
        user_input = get_main_menu_input()
        if user_input in main_menu_actions.keys():
            print(main_menu_actions[user_input](db))
        running = user_input != 'q'
