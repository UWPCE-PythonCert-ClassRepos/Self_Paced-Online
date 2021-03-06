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
    if donor_l == "list":
        print(list_donors())
    else:
        donation_amt = float(input("Amount of the donation? "))
        if donor_l in donor_db:
            donor_db[donor_l][1].append(donation_amt)
        else:
            donor_db[donor_l] = (donor, [donation_amt])
        letter = write_letter(donor_db[donor_l])
        print(letter)


def list_donors():
    return "\n".join(sorted([d[0] for d in donor_db.values()]))

def create_report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift" )
    print("-" * 66)
    for donor in sorted(donor_db.keys(), key=sort_key, reverse=True):
         print("{:<26} $ {:>10,.2f} {:>11}  ${:>12,.2f}".format(
             donor_db[donor][0], 
             sum(donor_db[donor][1]), 
             len(donor_db[donor][1]), 
             sum(donor_db[donor][1]) / len(donor_db[donor][1]))
            )


def write_letter(donor):
    letter = "Thank you, {}, for your kind donation of ${:,.2f}"
    return letter.format(donor[0],donor[1][-1])


def send_letters():
    for donor in  donor_db.values():
        letter = write_letter(donor)
        filename = donor[0].replace(' ','_') + '.txt'
        with open(filename, 'w') as f:
            f.write(letter)
    return


def quit():
    return "exit menu"


def sort_key(donor_l):
    return sum(donor_db[donor_l][1])


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if response in dispatch_dict.keys():
            if dispatch_dict[response]() == "exit menu":
                break


if __name__ == "__main__":
    donor_db = get_donor_db()
    prompt = "\n".join(("Welcome to the mailroom!",
                        "Please choose from below options:",
                        "1 - Send a thank you",
                        "2 - Create a report",
                        "3 - Send a letter to all donors",
                        "4 - Exit",
                        ">>> "))
    main_dispatch = {
        "1": thank_you,
        "2": create_report,
        "3": send_letters,
        "4": quit
    }
    menu_selection(prompt, main_dispatch)
