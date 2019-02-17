#!/usr/bin/env python3

import os, datetime
now = datetime.datetime.now()

donors = {"William Gates, III": [326892.23, 326892.25], "Mark Zuckerberg": [500.00, 800.00, 2.00], "Jeff Bezos": [877.33],
          "Paul Allen" : [750.23, 23.53, 999.99], "Dakota Dakota": [10.00, 100.00,1000.00]}

def thank_you():
    # Get person's name or provide list.
    person = input("Who would you like to thank? If you would like a list of donors, enter 'list'. ")
    if person == "list":
        for x in donors:
            print(x)
        person = input("Who would you like to thank? ")

    # Convert the amount to a float and add to donor dictionary
    amount = float(input(f"How much did {person} donate? "))

    if person not in donors:
        donors[person] = [amount]
    else:
        donors[person] += [amount]

    # Print thank you message
    directory = input("Please input a directory to save your thank you message. ")
    try:
        ty_name = person.replace(" ", "_") + f"_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt"
        ty_text = os.path.join(directory, ty_name)
        f = open(ty_text, "w")
        f.write(f"Dear {person},\nThank you very much for your donation of ${amount:,.2f}.\nSincerely,\nMatt Casali")
        f.close()
        print("A thank you message has been created.")
    except:
        print("You have entered an invalid directory.")


def report():
    # Get headers prepared
    print("          Donor Name        | Total Given | Num Gifts | Average Gift")

    # Append data from dictionary to list in order of presentation
    summary = []
    for d, v in donors.items():
        summary.append((d, sum(v), len(v), sum(v)/(len(v))))

    # Sort list based on total amount given descending
    def sum_sort(summary):
        return summary[1]

    summary.sort(key=sum_sort, reverse=True)

    # Iterate over summary list and print report
    for x in summary:
        print(f"{x[0]:^28} {x[1]:^12,.2f} {x[2]:^13} {x[3]:,.2f}")

def send_all_letters():
    # Get directory from user and create check to determine output message
    directory = input("Please input a directory to save your thank you message. ")
    Success = True
    for person, amount in donors.items():
        try:
            ty_name = person.replace(" ", "_") + f"_{now.year}_{now.month:0>2d}_{now.day:0>2d}" + ".txt"
            ty_text = os.path.join(directory, ty_name)
            f = open(ty_text, "w")
            f.write(f"Dear {person},\nThank you very much for your donation of ${sum(amount):,.2f}.\nSincerely,\nMatt Casali")
            f.close()
        except:
            Success = False

    if Success is True:
        print("Thank you letters have been written for every donor.")
    else:
        print("You have entered an invalid directory.")


def main():
    while True:
        print("Please choose: \n1: Send Thank You\n2: Create Report\n3: Send Letters to Everyone\n4: Quit")
        choice = input("Choice: ")

        # Loop based on choice, break loop for quit or wrong input
        if choice == "1":
            thank_you()
        elif choice == "2":
            report()
        elif choice == "3":
            send_all_letters()
        elif choice == "4":
            break
        else:
            print("You have made an invalid choice. Goodbye.")
            break


if __name__ =='__main__':
    main()