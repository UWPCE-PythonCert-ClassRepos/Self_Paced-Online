# ------------------------------------------------- #
# Title: Lesson 4, pt 1/2, Mail room 2
# Dev:   Craig Morton
# Date:  8/24/2018
# Change Log: CraigM, 8/24/2018, Mail room 2
# ------------------------------------------------- #

# !/usr/bin/env python

import os
import datetime

donors = [{"firstname": "Bill", "lastname": "Gates", "donations": [988]},
          {"firstname": "Sergey", "lastname": "Brin", "donations": [55, 342]},
          {"firstname": "Jeff", "lastname": "Bezos", "donations": [120, 50, 270]},
          {"firstname": "Paul", "lastname": "Allen", "donations": [12, 122, 310]},
          {"firstname": "Elon", "lastname": "Musk", "donations": [3, 85, 100]}]


def dict_name(name_one):
    user_input = True
    while user_input:
        print("Please enter a name (type 'list' for a list of names and '^' to go back)")
        if name_one == "first":
            user_input2 = input("First name: ")
        elif name_one == "last":
            user_input2 = input("Last name: ")
        if user_input2.lower() == "list":
            for i in donors:
                print("{firstname} {lastname}".format(**i))
        else:
            user_input = False
    return user_input2


def send_thank_you():
    """Requests donor name, amount, and displays a 'thank you' message"""
    firstname = dict_name("first")
    if firstname == "^":
        return
    lastname = dict_name("last")
    if lastname == "^":
        return
    print("Donation amount, or '^' to go to main menu:")
    amount = input(":")
    if amount == "^":
        return
    amount = float(amount)
    for i in donors:
        if i["firstname"] == firstname and i["lastname"] == lastname:
            i["donations"].append(amount)
            break
    else:
        donors.append({"firstname": firstname, "lastname": lastname, "donations": [amount]})
    thank_you_msg = "Thank you {firstname} {lastname} for your generous donation of ${amount:.2f}".format(
        firstname=firstname, lastname=lastname, amount=amount)
    print(thank_you_msg)


def get_total(donation_data):
    """Donation data"""
    return donation_data[1]


def create_a_report():
    """Prints a list of donors and donation amount"""
    reporting = str()
    reporting += "Donor Name    | Total Given   | Num Gifts | Average Gift"
    reporting += "\n"
    reporting += "--------------------------------------------------------"
    reporting += "\n"
    data_list = list()
    for donation_data in donors:
        fullname = "{firstname} {lastname}".format(**donation_data)
        gift_data = [fullname, 0, 0, 0]
        for donation in donation_data["donations"]:
            gift_data[1] += donation
            gift_data[2] += 1
        gift_data[3] = gift_data[1] / gift_data[2]
        data_list.append(gift_data)
    data_list.sort(key=get_total, reverse=True)
    formatting = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    for d in data_list:
        reporting += formatting(name=d[0], total=d[1], num=d[2], avg=d[3])
    print("\n", reporting)


def send_letters_to_everyone():
    """Creates a letter for everyone and writes to file"""
    number = 0
    sub_directory = str(datetime.date.today())
    try:
        os.mkdir(sub_directory)
    except OSError as filerror:
        print("\nCould not create directory.  Does it already exist?\n")
        return
    for d in donors:
        filename = "./{dir}/{firstname}_{lastname}.txt".format(**d, dir=sub_directory)
        with open(filename, 'w') as outfile, open("thank_you.txt", 'r') as infile:
            donations = d["donations"]
            last = donations[len(donations) - 1]
            total = 0
            for gifts in donations:
                total += gifts
            outfile.write(infile.read().format(**d, amount=last, total=total))
        number += 1
    print(number, "letters created")


if __name__ == "__main__":
    usr_choice = {
        "1": send_thank_you,
        "2": create_a_report,
        "3": send_letters_to_everyone}
    out = 0
    while out != "0":
        print("""\n
Please select a number:
1> Send a Thank You
2> Create a Report
3> Send letters to everyone
0> Quit""")
        out = input(":")
        if out in usr_choice:
            usr_choice[out]()
