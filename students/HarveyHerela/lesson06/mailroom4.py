#!/usr/bin/env python

from datetime import datetime
import os

def get_name(prompt, donors):
    """Anything can be a name, so accept anything as a name."""
    getting_name = True

    while getting_name:

        print("Type 'list' for a list of names in the database, '~' to go back")
        response = input(prompt)
        response = response.strip()

        if response.lower() == "list":
            for d in donors:
                print("{0} {1}".format(*d))
        else:
            getting_name = False
    return response


def get_full_name(donors):
    """Prompt for first and last name. Returna tuple of the name."""
    firstname = get_name("First name: ", donors)

    if firstname == "~":
        return ()

    lastname = get_name("Last name: ", donors)

    if lastname == "~":
        return ()
    
    return (firstname, lastname)
    

def get_donation_amount():
    amount = "nada"
    while not amount.isnumeric():
        print("Donation amount, or '~' to go to main menu:")
        amount = input("$ ")
        amount = amount.replace(",", "")
        if amount == '~':
            return
    return float(amount)

    
def send_thank_you(donors):
    """Prompts for a donor name and donation amount, then prints a 
    'thank you' message to the screen.
    """
    name = get_full_name(donors)
    if len(name) == 0:
        return
    
    amount = get_donation_amount()
    if amount == '~':
        return

    # Add the donation
    if name in donors:
        # If it's an existing donor, add it to their donation list.
        donors[name]["donations"].append(amount)
    else:
        # If it's a new donor, create a new entry.
        donors[name] = {"donations": [amount]}

    thank_you_msg = "Thank you {firstname} {lastname} for your generous donation of ${amount:.2f}".format(
        firstname=name[0], lastname=name[1], amount=amount)
    print(thank_you_msg)


def get_total(donor_data):
    return donor_data[1]


def create_row(donor_name, donor_data):
    fullname = "{0} {1}".format(*donor_name)
    total = sum(donor_data["donations"])
    num = len(donor_data["donations"])
    avg = total / num
    return [fullname, total, num, avg]


def create_report(donors):
    """Prints a list of all donors, sorted by total amount given."""
    report = list()
    report.append("Donor Name    | Total Given   | Num Gifts | Average Gift")
    report.append("\n")
    report.append("--------------------------------------------------------")
    report.append("\n")

    # Create a list with the data to be printed
    data_list = [create_row(name, data) for name, data in donors.items()]

    # Sort the list by total amount given
    data_list.sort(key=get_total, reverse=True)

    # Define the formatter
    line_fmtr = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    
    # Apply the formatting to all the data
    for d in data_list:
        report.append(line_fmtr(name=d[0], total=d[1], num=d[2], avg=d[3]))

    print("\n", ''.join(report))


def send_letters_everyone(donors):
    """Create letters for everyone in the database, and write them to files."""
    num = 0
    subdir = str(datetime.now())
    subdir = subdir.replace(':', '_')
    try:
        os.mkdir(subdir)
    except OSError as oserr:
        print(oserr)
        print("\nThere was an error creating the directory.\n")
        return
        
    # Read in the template
    try:
        with open("template.txt", 'r') as infile:
            template_in = infile.read()
    except FileNotFoundError as fnferr:
        print(fnferr)
        print("\nThere was an error reading the template file")
        return
            
    donor_template = template_in
    
    for donor_name in donors:
        # Setup up the data to write
        donations = donors[donor_name]["donations"]
        last = donations[-1]
        total = sum(donations)
        
        # Create the personalized letter
        # First, apply the formatting string
        donor_template = donor_template.replace('{amount}', '{amount:.2f}')
        donor_template = donor_template.replace('{total}', '{total:.2f}')
        # Now, replace the keys with the data
        try:
            letter_out = donor_template.format(firstname=donor_name[0], 
                lastname=donor_name[1], amount=last, total=total)
        except KeyError as kerr:
            print("Key Error:", kerr, "is not a valid key.",
                "The only valid keys are: ",
                "{firstname}, {lastname}, {amount}, and {total}")
            return
            
        # Write the letter to file
        filename = "./{dir}/{0}_{1}.txt".format(*donor_name, dir=subdir)
        with open(filename, 'w') as outfile:
            outfile.write(letter_out)
            
        num += 1

    print(num, "letters created.")


if __name__ == "__main__":
    # Default donor list
    donors = dict()
    donors[("Chase", "Zuma")] = {"donations": [25]}
    donors[("Marshall", "Rocky")] = {"donations": [30, 60]}
    donors[("Skye", "Rubble")] = {"donations": [100, 100, 100]}

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
        response = response.strip()
        if response in choices:
            choices[response](donors)
