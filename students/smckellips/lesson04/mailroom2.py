#! /usr/bin/env python


def get_donor_db():
    return {
        "william gates, iii": ("William Gates, III", [653772.32, 12.17]),
        "jeff bezos": ("Jeff Bezos", [877.33]),
        "paul allen": ("Paul Allen", [663.23, 43.87, 1.32]),
        "mark zuckerberg": ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
    }


def thank_you():
    donor = input("Name of the donor? ")
    donor_l = donor.lower()
    # donor = "Paul Allen"
    if donor_l == "list":
        print(list_donors())
    else:
        donation_amt = float(input("Amount of the donation? "))
        if donor_l in donor_db:
            donor_db[donor_l][1].append(donation_amt)
            # entry_d = entry[1]
        else:
            donor_db[donor_l] = (donor, [donation_amt])
            # entry_d = []
        # entry_d.append(donation_amt)

        # donor_db[donor_l] = (donor, entry_d)

        letter = "Thank you, {}, for your kind donation of ${:,.2f}"
        print(letter.format(donor,donation_amt))


def list_donors():
    return "\n".join(sorted([d[0] for d in donor_db.values()]))

def create_report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift" )
    print("-" * 66)
    # for donor in sorted(donor_db, key=sort_key, reverse=True):
    #     print("{:<26} $ {:>10,.2f} {:>11}  ${:>12,.2f}".format(donor[0], sum(donor[1]), len(donor[1]), sum(donor[1]) / len(donor[1])))
    for donor in sorted(donor_db.keys(), key=sort_key, reverse=True):
         print("{:<26} $ {:>10,.2f} {:>11}  ${:>12,.2f}".format(
             donor_db[donor][0], 
             sum(donor_db[donor][1]), 
             len(donor_db[donor][1]), 
             sum(donor_db[donor][1]) / len(donor_db[donor][1]))
            )


def quit():
    return "exit menu"


def sort_key(donor_l):
    return sum(donor_db[donor_l][1])


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if response in ['1', '2', '3']:
            if dispatch_dict[response]() == "exit menu":
                break


if __name__ == "__main__":
    donor_db = get_donor_db()
    prompt = "\n".join(("Welcome to the mailroom!",
                        "Please choose from below options:",
                        "1 - Send a thank you",
                        "2 - Create a report",
                        "3 - Exit",
                        ">>> "))
    main_dispatch = {
        "1": thank_you,
        "2": create_report,
        "3": quit
    }
    menu_selection(prompt, main_dispatch)
