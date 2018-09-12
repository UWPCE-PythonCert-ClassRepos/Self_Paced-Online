# ------------------------------------------------- #
# Title: Lesson 6, pt 1/2, Mail room 4
# Dev:   Craig Morton
# Date:  9/8/2018
# Change Log: CraigM, 9/8/2018, Mail room 4
# ------------------------------------------------- #

# !/usr/bin/env python3

from datetime import datetime
import os


def get_name(prompt, donors):
    """Get donor name"""
    getting_name = True
    while getting_name:
        print("Type 'list' for a list of names in the database, '~' to go back")
        usr_input = input(prompt)
        usr_input = usr_input.strip()
        if usr_input.lower() == "list":
            for d in donors:
                print("{0} {1}".format(*d))
        else:
            getting_name = False
    return usr_input


def get_full_name(donors):
    """Full donor name"""
    firstname = get_name("First name: ", donors)
    if firstname == "~":
        return ()
    lastname = get_name("Last name: ", donors)
    if lastname == "~":
        return ()
    return firstname, lastname


def get_donation_amount():
    """Donation amount"""
    amount = "Nothing"
    while not amount.isnumeric():
        print("Donation amount, or '~' to go to main menu:")
        amount = input("$ ")
        amount = amount.replace(",", "")
        if amount == '~':
            return
    return float(amount)


def send_thank_you(donors):
    """Request user name and amount"""
    name = get_full_name(donors)
    if len(name) == 0:
        return
    amount = get_donation_amount()
    if amount == '~':
        return
    if name in donors:
        donors[name]["donations"].append(amount)
    else:
        donors[name] = {"donations": [amount]}
    thank_you_msg = "Thank you {firstname} {lastname} for your generous donation of ${amount:.2f}".format(
        firstname=name[0], lastname=name[1], amount=amount)
    print(thank_you_msg)


def get_total(donor_data):
    """Get total amount"""
    return donor_data[1]


def create_row(donor_name, donor_data):
    """Create new donor row"""
    fullname = "{0} {1}".format(*donor_name)
    total = sum(donor_data["donations"])
    num = len(donor_data["donations"])
    avg = total / num
    return [fullname, total, num, avg]


def create_report(donors):
    """Generates list of all donors and donation data"""
    report = list()
    report.append("Donor Name    | Total Given   | Num Gifts | Average Gift")
    report.append("\n")
    report.append("--------------------------------------------------------")
    report.append("\n")
    data_list = [create_row(name, data) for name, data in donors.items()]
    data_list.sort(key=get_total, reverse=True)
    line_fmtr = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    for d in data_list:
        report.append(line_fmtr(name=d[0], total=d[1], num=d[2], avg=d[3]))
    print("\n", ''.join(report))


def send_letters_everyone(donors):
    """Generates thank you letters for all donors"""
    num = 0
    subdir = str(datetime.now())
    subdir = subdir.replace(':', '_')
    try:
        os.mkdir(subdir)
    except OSError as oserr:
        print(oserr)
        print("\nThere was an error creating the directory.\n")
        return
    try:
        with open("template.txt", 'r') as infile:
            template_in = infile.read()
    except FileNotFoundError as fnferr:
        print(fnferr)
        print("\nThere was an error reading the template file")
        return
    donor_template = template_in
    for donor_name in donors:
        donations = donors[donor_name]["donations"]
        last = donations[-1]
        total = sum(donations)
        donor_template = donor_template.replace('{amount}', '{amount:.2f}')
        donor_template = donor_template.replace('{total}', '{total:.2f}')
        try:
            letter_out = donor_template.format(firstname=donor_name[0], lastname=donor_name[1], amount=last, total=total)
        except KeyError as kerr:
            print("Key Error:", kerr, "is not a valid key.",
                  "The only valid keys are: ",
                  "{firstname}, {lastname}, {amount}, and {total}")
            return
        filename = "./{dir}/{0}_{1}.txt".format(*donor_name, dir=subdir)
        with open(filename, 'w') as outfile:
            outfile.write(letter_out)
        num += 1
    print(num, "letters created.")


if __name__ == "__main__":
    donors = dict()
    donors[("Bill", "Gates")] = {"donations": [25, 8000, 500]}
    donors[("Jeff", "Bezos")] = {"donations": [30, 60]}
    donors[("Sergey", "Brin")] = {"donations": [1907, 1253, 100]}
    donors[("Paul", "Allen")] = {"donations": [2868, 1444, 2000]}
    donors[("Elon", "Musk")] = {"donations": [3, 85, 100]}

    choices = {
        "1": send_thank_you,
        "2": create_report,
        "3": send_letters_everyone}
    response = 0
    while response != "0":
        print("""\nPick an action by number:\n
1: Send a 'thank you' note
2: Create a report
3: Send letters to everyone
0: Quit""")
        response = input(":")
        response = response.strip()
        if response in choices:
            choices[response](donors)
