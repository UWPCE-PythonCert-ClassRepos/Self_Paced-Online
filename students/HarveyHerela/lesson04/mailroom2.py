#!/usr/bin/env python

import datetime
import os

donors = [{"firstname": "Chase", "lastname": "Zuma", "donations": [25]},
          {"firstname": "Marshall", "lastname": "Rocky", "donations": [30, 60]},
          {"firstname": "Skye", "lastname": "Rubble", "donations": [100, 100, 100]}]

def get_name(name_type):    
    gettingInput = True

    while gettingInput:
        
        print("Type 'list' for a list of names in the database, '~' to go back")
        if name_type == "first":
            response = input("First name: ")
        elif name_type == "last":
            response = input("Last name: ")

        if response.lower() == "list":
            for d in donors:
                print("{firstname} {lastname}".format(**d))
        else:
            gettingInput = False
    return response

def send_thank_you():
    """Prompts for a donor name and donation amount, then prints a 'thank you' message to the screen."""
    firstname= get_name("first")

    if firstname == "~":
        return

    lastname = get_name("last")

    if lastname == "~":
        return

    print("Donation amount, or '~' to go to main menu:")
    amount = input(":")
    if amount == '~':
        return
    amount = float(amount)
    # If it's an existing donor, add it to their donation list.
    # If it's a new donor, create a new entry.
    for d in donors:
        if d["firstname"] == firstname and d["lastname"] == lastname:
            d["donations"].append(amount)
            break
    else:
        donors.append({"firstname": firstname, "lastname": lastname, "donations": [amount]})
        
    thank_you_msg = "Thank you {firstname} {lastname} for your generous donation of ${amount:.2f}".format(
        firstname=firstname, lastname=lastname, amount=amount)
    print(thank_you_msg)

def get_total(donor_data):
    return donor_data[1]

def create_report():
    """Prints a list of all donors, sorted by total amount given."""
    report = str()
    report += "Donor Name    | Total Given   | Num Gifts | Average Gift"
    report += "\n"
    report += "--------------------------------------------------------" 
    report += "\n"
    # Create a list with the data to be printed
    data_list = list()
    for donor_data in donors:
        fullname = "{firstname} {lastname}".format(**donor_data)
        gift_data = [fullname, 0, 0, 0]
        for donation in donor_data["donations"]:
            gift_data[1] += donation
            gift_data[2] += 1
        gift_data[3] = gift_data[1] / gift_data[2]
        data_list.append(gift_data)
    
    # Sort the list by total amount given
    data_list.sort(key=get_total, reverse=True)
    
    # Define the formatter
    line_fmtr = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    for d in data_list:
        report += line_fmtr(name=d[0], total=d[1], num=d[2], avg=d[3])
    
    print("\n", report)

def send_letters_everyone():
    """Creates a letter for everyone in the database, and writes them to file."""
    num = 0
    subdir = str(datetime.date.today())
    try:
        os.mkdir(subdir)
    except OSError as oserr:
        print("\nThere was an error creating the directory. Perhaps it already exists?\n")
        return
    for d in donors:
        filename = "./{dir}/{firstname}_{lastname}.txt".format(**d, dir=subdir)
        with open(filename, 'w') as outfile, open("template.txt", 'r') as infile:
            donations = d["donations"]
            last = donations[len(donations) - 1]
            total = 0
            for gift in donations:
                total += gift
            outfile.write(infile.read().format(**d, amount=last, total=total))

                          
        num += 1
    print(num, "letters created.")
    
if __name__ == "__main__":
    choices = {
        "1": send_thank_you,
        "2": create_report,
        "3": send_letters_everyone}
    response = 0
    while response != "0":
        print("\n\nPick an action by number:")
        print("1: Send a 'thank you' note")
        print("2: Create a report")
        print("3: Send letters to everyone")
        print("0: Quit")
        response = input(":")
        if response in choices:
            choices[response]()



    
