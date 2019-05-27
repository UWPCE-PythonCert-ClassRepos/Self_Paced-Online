#! /usr/bin/env python

def get_donor_db():
    return {
        "william gates, iii": ("William Gates, III", [653772.32, 12.17]),
        "jeff bezos": ("Jeff Bezos", [877.33]),
        "paul allen": ("Paul Allen", [663.23, 43.87, 1.32]),
        "mark zuckerberg": ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
    }


def get_donor(name):
    if name.lower() in donor_db.keys():
        donor = donor_db[name.lower()]
        return donor
    else:
        return None


def add_donor(name):
    if name.lower() not in donor_db.keys():
        donor = (name, [])
        donor_db[name.lower()] = donor
        return donor
    else:
        return None


def thank_you():
    try:
        donor_name = input("Name of the donor? ( 'q' to quit, 'list' to list ) ")
    except Exception as e:
        print(f"There is an error with your input, {e}.")
        thank_you()
    donor_l = donor_name.lower()
    if donor_l == 'q':
        return
    elif donor_l == "list":
        print(list_donors())
    else:
        try:
            donation_amt = float(input("Amount of the donation? "))
        except ValueError:
            print("Not a float")
        except Exception as e:
            print("There is an error with your amount")
        donor = get_donor(donor_name)
        if donor == None:
            donor = add_donor(donor_name)
        donor[1].append(donation_amt)

        letter = write_letter(donor)
        print(letter)


def list_donors():
    return "\n".join(sorted([d[0] for d in donor_db.values()]))


def create_report():
    print(write_report())

def write_report():
    report = "Donor Name                | Total Given | Num Gifts | Average Gift" + '\n'
    report += "-" * 66 + '\n'

    for donor in sorted(donor_db.keys(), key=sort_key, reverse=True):
        report += "{:<26} $ {:>10,.2f} {:>11}  ${:>12,.2f}".format(
             donor_db[donor][0], 
             sum(donor_db[donor][1]), 
             len(donor_db[donor][1]), 
             sum(donor_db[donor][1]) / len(donor_db[donor][1])) + '\n'
    return report


def write_letter(donor):
    letter = "Thank you, {}, for your kind donation of ${:,.2f}"
    return letter.format(donor[0],donor[1][-1])


def send_letters():
    for donor in  donor_db.values():
        letter = write_letter(donor)
        filename = donor[0].replace(' ','_') + '.txt'
        try:
            with open(filename, 'w') as f:
                f.write(letter)
        except:
            print(f"Error writing file for {donor[0]}")
    return


def quit():
    return "exit menu"


def sort_key(donor_l):
    return sum(donor_db[donor_l][1])


def menu_selection(prompt, dispatch_dict):
    while True:
        try:
            response = input(prompt)
        except KeyboardInterrupt:
            break
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
    try:
        menu_selection(prompt, main_dispatch)
    except KeyboardInterrupt:
        print("Exiting")
