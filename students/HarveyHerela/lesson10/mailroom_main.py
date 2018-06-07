import mailroom_db
import mailroom_actions
from datetime import datetime
import os

def send_thank_you(db):
    name_queries = ("First name", "Last name")
    full_name = list()
    q = 0
    while q < len(name_queries):
        print("Enter {}, 'list' for names in db, or ~ to go back".format(name_queries[q]))
        name = input(": ")
        if name == '~':
            return ""
        elif name.lower() == 'list':
            for donor in db.get_donors():
                print(donor.get_name())
        else:
            full_name.append(name)
            q += 1
    amount = ""
    while not amount.isnumeric():
        print("Donation amount, or '~' to go to main menu:")
        amount = input("$ ")
        if amount == '~':
            return
    amount = float(amount)
    return mailroom_actions.send_thank_you(db, full_name[0], full_name[1], amount)


def send_letters(db):
    """Create letters for everyone in the database, and write them to files."""
    subdir = str(datetime.now())
    subdir = subdir.replace(':', '_')
    try:
        os.mkdir(subdir)
    except OSError as oserr:
        print(oserr)
        print("\nThere was an error creating the directory.\n")
        return "Failed!"

    # Read in the template
    try:
        with open("template.txt", 'r') as infile:
            template_in = infile.read()
    except FileNotFoundError as fnferr:
        print(fnferr)
        print("\nThere was an error reading the template file")
        return "Failed!"

    letters = mailroom_actions.send_letters(db, template_in)

    # Write the letters to file
    for letter in letters:
        filename = "./{dir}/{name}.txt".format(name=letter[0], dir=subdir)
        with open(filename, 'w') as outfile:
            outfile.write(letter[1])
    return "{num} letters created!".format(num=len(letters))


def challenge_projection(db):
    multiplier = input("Amount to multiply donation by: ")
    if not multiplier.isnumeric():
        return "There was a user input error.\n"
    multiplier = float(multiplier)
    
    print("Only apply multiplier to donations: ")
    print("1: Above a certain amount")
    print("2: Below a certain amount")
    print("3: All donations")
    threshold = input(": ")
    above_amount = 0
    below_amount = 0
    if threshold == '1':
        above_amount = input("Above what amount: ")
        if not above_amount.isnumeric():
            return "There was a user input error.\n"
        above_amount = float(above_amount)
    elif threshold == '2':
        below_amount = input("Below what amount: ")
        if not below_amount.isnumeric():
            return "There was a user input error.\n"
        below_amount = float(below_amount)
    elif threshold != '3':
        return "There was a user input error.\n"
    
    return mailroom_actions.challenge_project(db=db, above=above_amount, below=below_amount, multiplier=multiplier) 
    

main_menu_list = [
    "Pick an action by number",
    "1: Send 'Thank You' note",
    "2: Create Report",
    "3: Send letters to everyone",
    "4: Challenge Projection",
    "q: Quit"
]


main_menu_actions = {
    '1': send_thank_you,
    '2': mailroom_actions.create_report,
    '3': send_letters,
    '4': challenge_projection
}


def draw_main_menu():
    print("\n".join(main_menu_list))


def get_main_menu_input():
    user_input = input(":")
    user_input = user_input.lower().strip()
    return user_input


if __name__ == "__main__":
    db = mailroom_db.DonorCollection()
    # Some default data
    d1 = mailroom_db.Donor("Jimmy", "Stewart")
    d1.add_donation(50)
    d2 = mailroom_db.Donor("Cary", "Grant")
    d2.add_donation(30)
    d2.add_donation(40)
    d3 = mailroom_db.Donor("Audrey", "Hepburn")
    d3.add_donation(80)
    d3.add_donation(90)
    d3.add_donation(100)
    db.add_donor(d1)
    db.add_donor(d2)
    db.add_donor(d3)

    # Now on to the meat and potatos of the mailroom
    running = True
    while running:
        draw_main_menu()
        user_input = get_main_menu_input()
        if user_input in main_menu_actions.keys():
            print(main_menu_actions[user_input](db))
        running = user_input != 'q'
