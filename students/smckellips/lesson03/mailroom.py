#! /usr/bin/env python
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Exit",
          ">>> "))

def thank_you():
    global donor_db
    #I'm getting an error accessing the global variable donor_db, so passing in as argument to get around the error.
    donor = input("Name of the donor? ").title()
    # donor = "Paul Allen"
    if donor == "List":
        print("\n".join(x[0] for x in donor_db))
        thank_you()
    else:
        if donor in [x[0] for x in donor_db]:

            # donor_name = [x[0] for x in donor_db if x[0] == donor]
            # donor_donations = [x[1] for x in donor_db if x[0] == donor]

            donor_e = [(x[0],x[1]) for x in donor_db if x[0] == donor]
            donor_name = donor_e[0][0]
            donor_donations = donor_e[0][1]
        else:
            donor_name = donor
            donor_donations = []
        donation_amt = float(input("Amount of the donation? "))
        donor_donations.append(donation_amt)

        donor_db = [d for d in donor_db if d[0] != donor]
        donor_db.append((donor_name,donor_donations))

        letter = "Thank you, {}, for your kind donation of ${:,.2f}"
        print(letter.format(donor_name,donation_amt))


def create_report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift" )
    print("-" * 66)
    for donor in sorted(donor_db, key=sort_key, reverse=True):
        print("{:<26} $ {:>10,.2f} {:>11}  ${:>12,.2f}".format(donor[0], sum(donor[1]), len(donor[1]), sum(donor[1]) / len(donor[1])))

def sort_key(donor):
    return sum(donor[1])


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()