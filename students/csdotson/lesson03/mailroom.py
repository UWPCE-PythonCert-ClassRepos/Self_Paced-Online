#!/usr/bin/env python3
# Lesson 3 - Mailroom... part 1

# Initial list of donors/donations
donations = [ ["Bill Gates", 10.50], ["Bill Gates", 123.45], ["Bill Gates",    1111.11], ["Jeff Bezos", 7.65], ["Jeff Bezos", 1000], ["Paul Allen", 145.90], ["John Nordstrom", 45.67], ["John Nordstrom", 6519.65], ["Mark Zuck", 789.12] ]


### Function Definitions ###
def prompt(which = 0):
    # Original prompt for main menu selections
    if which == 0:
        response = input("Welcome Chris! What would you like to do?\n(S)end a Thank You / (C)reate a Report / (Q)uit\n--> ")
    else:
        response = input("What would you like to do next?\n(S)end a Thank You / (C)reate a Report / (Q)uit\n--> ")

    while True:
        if response == "S":
            send_thank_you()
            break
        elif response == "C":
            print_report()
            break
        else:
            print("Goodbye Sir!")
            break

def send_thank_you():
    # Add donor/donations and trigger thank you email
    response = input("Please enter full name of person you'd like to thank:\nBy the way, you can also type 'list' to get a list of donors or 'P' to return to the main prompt\n--> ")

    if response == "list":
        print()
        list_donors()
        send_thank_you()
    elif response == "P":
        prompt(1)
    elif response not in donor_names():
        new_donor = response
        donation_response = input(f"Please enter a donation amount for {new_donor}: ")
        donations.append([new_donor, float(donation_response)])
        print_email(new_donor, donation_response)
    else:
        donor = response
        donation_response = input(f"Please enter a donation amount for {donor}: ")
        donations.append([donor, float(donation_response)])
        print_email(donor, donation_response)

def print_email(donor, amount):
    # Print formatted email thanking donor
    print()
    print(f"Dear {donor},\nThank you so very much for you kind donation of ${amount}. We can assure you that it will be put to great use.\nBest,\nChris")
    print()
    prompt(1)

def list_donors():
    # Formatted print of unique list of donor names
    donor_list = donor_names()
    print("List of donors:")
    for i in donor_list:
        print(i)
    print()

def donor_names():
    # Create unique list of donor names
    name_list = []
    for i, j in donations:
        if i not in name_list:
            name_list.append(i)
    return name_list

def print_report():
    # Print formatted report showing donors and donation stats
    header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * len(header))

    for name in donor_names():
        print('{:21}{:>15.2f}{:>16}{:>16.2f}'.format(name, total_given(name), num_gifts(name), avg_gift(name)))

    print()
    prompt(1)

def total_given(donor):
    # Compute/return total amount donated for a given donor
    sum = 0
    for i, j in donations:
        if i == donor:
            sum += j
    return sum

def num_gifts(donor):
    # Compute/return number of donations for a given donor
    count = 0
    for i, j in donations:
        if i == donor:
            count += 1
    return count

def avg_gift(donor):
    # Compute/return average gifr for a given donor
    return (total_given(donor)/num_gifts(donor))


if __name__ == "__main__":
    # Will only execute if mailroom.py is run as a script
    prompt()
