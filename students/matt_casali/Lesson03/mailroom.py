#!/usr/bin/env python3

donors = {"William Gates, III": [326892.23, 326892.25], "Mark Zuckerberg": [500.00, 800.00, 2.00], "Jeff Bezos": [877.33],
          "Paul Allen" : [750.23, 23.53, 999.99], "Dakota Dakota": [10.00, 100.00,1000.00]}

def thank_you():
    # Get person's name or provide list.
    person = input("Who would you like to thank? If you would like a list of donors, enter 'list'. ")
    if person == "list":
        for x in donors:
            print(x)
        person = input("Who would you like to thank? ")
    else:
        pass

    # Convert the amount to a float and add to donor dictionary
    amount = float(input(f"How much did {person} donate? "))

    if person not in donors:
        donors[person] = [amount]
    elif person in donors:
        donors[person] += [amount]

    # Print thank you message
    print(f"\n\nDear {person},\nThank you very much for your donation of ${amount:,.2f}.\nSincerely,\nMatt Casali\n\n")


def report():
    # Get headers prepared
    print("          Donor Name        | Total Given | Num Gifts | Average Gift")

    # Append data from dictionary to list in order of presentation
    summary = []
    for d, v in donors.items():
        summary.append((d, sum(v), len(v), sum(v)/(len(v))))

    # Iterate over summary list and print report
    for x in summary:
        print(f"{x[0]:^28} {x[1]:^12,.2f} {x[2]:^13} {x[3]:,.2f}")


def main():
    while True:
        print("Please choose: \n1: Send Thank You\n2: Create Report\n3: Quit")
        choice = input("Choice: ")

        # Loop based on choice, break loop for quit or wrong input
        if choice == "1":
            thank_you()
            continue
        elif choice == "2":
            report()
            continue
        elif choice == "3":
            break
        else:
            print("You have made an invalid choice. Goodbye.")
            break


if __name__ =='__main__':
    main()