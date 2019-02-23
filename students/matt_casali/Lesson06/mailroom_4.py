#!/usr/bin/env python3

import os, datetime, sys
now = datetime.datetime.now()

donors = {"William Gates, III": [326892.23, 326892.25], "Mark Zuckerberg": [500.00, 800.00, 2.00], "Jeff Bezos": [877.33],
          "Paul Allen": [750.23, 23.53, 999.99], "Dakota Dakota": [10.00, 100.00,1000.00]}

def list_donors(database):
    return ", ".join(x for x in database)


def thank_you(database):
    # Get person's name or provide list.
    person = input("Who would you like to thank? If you would like a list of donors, enter 'list'. ")
    if person == "list":
        print(list_donors(database))
        person = input("Who would you like to thank? ")

    # Convert the amount to a float and add to donor dictionary
    try:
        amount = float(input(f"How much did {person} donate? "))
    except ValueError:
        print("You did not enter a numeric value. Please try again.")
        sys.exit()
    else:
        if person not in database:
            database[person] = [amount]
        else:
            database[person] += [amount]

    # Print thank you message
    directory = input("Please input a directory to save your thank you message. ")
    try:
        ty_name = person.replace(" ", "_") + f"_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt"
        ty_text = os.path.join(directory, ty_name)
        f = open(ty_text, "w")
        f.write(f"Dear {person},\nThank you very much for your donation of ${amount:,.2f}.\nSincerely,\nMatt Casali")
        f.close()
        print("A thank you message has been created.")
    except FileNotFoundError:
        print("You have entered an invalid directory. Please try again.")
        thank_you()


def make_report(database):
    # Get headers prepared
    report = "          Donor Name        | Total Given | Num Gifts | Average Gift\n"

    # Append data from dictionary to list in order of presentation
    summary = [(d, sum(v), len(v), sum(v)/(len(v))) for d, v in database.items()]

    # Sort list based on total amount given descending
    def sum_sort(summary):
        return summary[1]

    summary.sort(key=sum_sort, reverse=True)

    # Iterate over summary list and print report
    for x in summary:
        report += f"{x[0]:^28} {x[1]:^12,.2f} {x[2]:^13} {x[3]:,.2f}\n"
    return report


# Function to print returned result from make_report function
def print_report(database):
    print(make_report(database))


def send_all_letters(database):
    # Get directory from user and create check to determine output message
    directory = input("Please input a directory to save your thank you message. ")
    for person, amount in database.items():
        try:
            ty_name = person.replace(" ", "_") + f"_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt"
            ty_text = os.path.join(directory, ty_name)
            f = open(ty_text, "w")
            f.write(f"Dear {person},\nThank you very much for your donation of ${sum(amount):,.2f}.\nSincerely,\nMatt Casali")
            f.close()
        except FileNotFoundError:
            print("You have entered an invalid directory.")
            break
        else:
            print(f"A thank you letters have been written for {person}.")


def main():
    # Create switch dictionary
    choices_dic = {"1": thank_you, "2": print_report, "3": send_all_letters}
    while True:
        print("Please choose: \n1: Send Thank You\n2: Create Report\n3: Send Letters to Everyone\n4: Quit")
        choice = input("Choice: ")
        try:
            if choice == "4":
                break
            choices_dic.get(choice)(donors)
        except TypeError:
            print("You have made an invalid choice. Goodbye.")
            break


if __name__ =='__main__':
    main()