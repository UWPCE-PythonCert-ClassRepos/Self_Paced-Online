#!/usr/bin/env python

import datetime
import os

donors = [{"name": ("Chase", "Zuma"), "donations": [25 * x for x in range(2)]},
          {"name": ("Marshall", "Rocky"), "donations": [30 * x for x in range(2, 4)]},
          {"name": ("Skye", "Rubble"), "donations": [45 * x for x in range(10, 13)]}]


def get_name(prompt):
    """Anything can be a name, so accept anything as a name."""
    getting_name = True

    while getting_name:

        print("Type 'list' for a list of names in the database, '~' to go back")
        response = input(prompt)
        response = response.strip()

        if response.lower() == "list":
            for d in donors:
                print("{0} {1}".format(*d["name"]))
        else:
            getting_name = False
    return response


def send_thank_you():
    """Prompts for a donor name and donation amount, then prints a 'thank you' message to the screen."""
    firstname = get_name("First name: ")

    if firstname == "~":
        return

    lastname = get_name("Last name: ")

    if lastname == "~":
        return

    amount = "nada"
    while not amount.isnumeric():
        print("Donation amount, or '~' to go to main menu:")
        amount = input("$ ")
        amount = amount.strip()
        if amount == '~':
            return
    amount = float(amount)

    # Add the donation
    name = (firstname, lastname)
    for d in donors:
        if name in d:
            # If it's an existing donor, add it to their donation list.
            d["donations"].append(amount)
            break
    else:
        # If it's a new donor, create a new entry.
        donors.append({"name": name, "donations": [amount]})

    thank_you_msg = "Thank you {firstname} {lastname} for your generous donation of ${amount:.2f}".format(
        firstname=firstname, lastname=lastname, amount=amount)
    print(thank_you_msg)


def get_total(donor_data):
    return donor_data[1]


def create_row(donor_data):
    fullname = "{0} {1}".format(*donor_data["name"])
    total = sum(donor_data["donations"])
    num = len(donor_data["donations"])
    avg = total / num
    return [fullname, total, num, avg]


def create_report():
    """Prints a list of all donors, sorted by total amount given."""
    report = str()
    report += "Donor Name    | Total Given   | Num Gifts | Average Gift"
    report += "\n"
    report += "--------------------------------------------------------"
    report += "\n"

    # Create a list with the data to be printed
    data_list = [create_row(d) for d in donors]

    # Sort the list by total amount given
    data_list.sort(key=get_total, reverse=True)

    # Define the formatter
    line_fmtr = "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}\n".format
    for d in data_list:
        report += line_fmtr(name=d[0], total=d[1], num=d[2], avg=d[3])

    print("\n", report)


def send_letters_everyone():
    """Create letters for everyone in the database, and write them to files."""
    num = 0
    subdir = str(datetime.datetime.now())
    subdir = subdir.replace(':', '_')
    try:
        os.mkdir(subdir)
    except OSError as oserr:
        print(oserr)
        print("\nThere was an error creating the directory.\n")
        return
    for d in donors:
        filename = "./{dir}/{0}_{1}.txt".format(*d["name"], dir=subdir)
        try:
            with open(filename, 'w') as outfile, open("template.txt", 'r') as infile:
                donations = d["donations"]
                last = donations[len(donations) - 1]
                total = 0
                for gift in donations:
                    total += gift
                name = d["name"]
                outfile.write(infile.read().format(firstname=name[0], lastname=name[1], amount=last, total=total))
        except FileNotFoundError as fnferr:
            print(fnferr)
            print("\nThere was an error reading the template file")
            return
        except KeyError as kerr:
            print("Key Error:", kerr, "is a bad key.")
            print("There was an error with the template {keys}. Verify the {keys} are correct.")
            return
        except ValueError as verr:
            print("There was an error while reading the formatting strings.")
            return
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
        response = response.strip()
        if response in choices:
            choices[response]()
