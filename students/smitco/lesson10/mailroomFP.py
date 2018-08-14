# lesson 10 mailroom functional programming
# based on mailroom 4 file
# !/usr/bin/env python3


import os
import datetime


# starting list of 5+ donors and 1-3 donations each
donors = {"John Travolta": [5000, 7500],
          "Jane Fonda": [10000, 8000, 6500],
          "Judy Blume": [3000, 3500],
          "Joey Tribbiani": [9000],
          "Jenny Gump": [10300, 13750, 12500]}


def menu():
    ask = input("Please choose an action:\n"
                "1) Send a new thank you\n"
                "2) Create a report\n"
                "3) Send letters to all donors\n"
                "4) Analyze for contribution matching\n"
                "5) Quit\n"
                ">>")
    options = {"1": thank_you, "2": report, "3": letters, "4": match, "5": quit}
    try:
        options[ask]()
    except KeyError:
        print("\nThere was an error. Please try again.\n")


def thank_you():
    """Ask for donor name (add to list if needed) and amount to send email"""
    while True:
        name = input("\nTo whom would you like to send a thank you?\n"
                     "'List' will display current donors.\n"
                     "'Exit' will return to main menu.\n"
                     ">>")
        if name.lower() == "exit":
            print("\nExiting.\n")
            break
        elif name.lower() == "list":
            print(list(donors.keys()))
        else:
            donation = input("\nWhat is the donation amount?\n>>")
            try:
                donation = int(donation)
                if donation >= (10 ** 6):
                    print("\nThe amount entered is too large.")
                else:
                    if name not in donors:
                        donors[name] = []
                    donors[name].append(donation)
                    print("\nThank you, {}, for your generous donation of ${:,.0f} "
                          "to the Brave Heart Foundation.".format(name, donation))
            except ValueError:
                if donation.lower() == "exit":
                    print("\nExiting.")
                else:
                    print("\nInvalid entry.")


def report():
    """Print report of donors and donation details"""
    donor_details = {k:(sum(v), len(v), sum(v)/len(v)) for k,v in donors.items()}
    sorted_details = sorted(donor_details.items(), key=lambda x: x[1], reverse=True)
    print("\n{:<20} {:<12}  {:^10} {:<12}".format("Donor", "Total", "Count", "Average"))
    for i in range(len(sorted_details)):
        info = {"donor_name": sorted_details[i][0],
                "donor_total": sorted_details[i][1][0],
                "donor_count": sorted_details[i][1][1],
                "donor_avg": sorted_details[i][1][2]}
        print("{donor_name:<20} ${donor_total:>12,.2f} "
              "{donor_count:^10} ${donor_avg:>12,.2f}".format(**info))
    print()


def letters():
    """Create txt file in CWD for each donor"""
    current = datetime.datetime.now()
    date = [str(current.month), str(current.day), str(current.year)]
    current_date = "_".join(date)
    for d in donors:
        letter_temp = {"letter_name": d, "letter_amount": sum(donors[d])}
        letter = ("Dear {letter_name},\n\n"
                  "Thank you for supporting The Brave Heart Foundation.\n"
                  "Your donations totaling ${letter_amount:,.0f} have made a positive,\n"
                  "life-changing impact for teens nationwide.\n\n"
                  "Blessings,\n"
                  "BHF".format(**letter_temp))
        letter_name = d + " " + current_date + ".txt"
        with open(letter_name, "w") as donor_letter:
            donor_letter.write(letter)
    print("\nFiles completed.\n")


def match():
    """Analyze donation data for matching contributions"""
    all_donations = list(v for d in donors for v in donors.get(d))
    print("\nThe donation range is ${:,.0f}-{:,.0f}.".format(min(all_donations), max(all_donations)))
    min_match = input("\nWhat is the minimum value to match?\n>>")
    max_match = input("\nWhat is the maximum value to match?\n>>")
    match_range_partial = list(filter(lambda x: int(min_match) <= x, all_donations))
    match_range = list(filter(lambda x: x <= int(max_match), match_range_partial))
    original_sum = sum(match_range)
    print("\nThe total in this range is ${:,.0f}.".format(original_sum))
    factor = input("\nBy what factor would you like to match?\n>>")
    match_sum = sum(map(lambda x: x * int(factor), match_range))
    print("\nThe matching contribution would be ${:,.0f}.\n".format(match_sum))

   
def quit():
    print("\nGoodbye.")
    exit()


if __name__ == '__main__':
    while True:
        menu()
