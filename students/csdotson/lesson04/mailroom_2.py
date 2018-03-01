#!/usr/bin/env python3
# Lesson 3 - Mailroom... part 1

# Initial list of donors/donations
donations = [["Bill Gates", 10.50, 123.45, 1111.11],
             ["Jeff Bezos", 7.65, 1000],
             ["Paul Allen", 145.90],
             ["John Nordstrom", 45.67, 6519.65],
             ["Mark Zuck", 789.12]]  # Convert this to a dict


### Function Definitions ###
def prompt():
    # Original prompt for main menu selections
    while True:
        response = input("What would you like to do?\n1 - Send a Thank You\n2 - Create a Report\n3 - Quit\n--> ")

        if response == "1":
            print()
            send_thank_you()
            break
        elif response == "2":
            print()
            print_report()
            break
        elif response == "3":
            break
        else:
            print("Invalid response, please try again...")
            print()
            prompt()

def send_thank_you():
    # Add donor/donations and trigger thank you email
    response = input("Please enter full name of person you'd like to thank, you can also do the following:\n1 - Display list of current donors\n2 - Return to the main menu\n--> ")

    if response == "1":
        print()
        list_donors()
        send_thank_you()
    elif response == "2":
        print()
        prompt()
    elif response not in donor_names():
        new_donor = response
        new_donation = input(f"Please enter a donation amount for {new_donor}: ")
        donations.append([new_donor, float(new_donation)])
        print_email(new_donor, new_donation)
    else:
        donor = response
        donation = input(f"Please enter a donation amount for {donor}: ")
        add_donation(donor, float(donation))
        print_email(donor, donation)

def add_donation(search_donor, new_donation):
    # Add donation to existing donor
    for index, donor in enumerate(donations):
        if donor[0] == search_donor:
            donations[index].append(new_donation)

def print_email(donor, amount):
    # Print formatted email thanking donor
    letter_details = {'name': donor, 'donation_amount': amount}
    letter = "\nDear {name},\nThank you so very much for you kind donation of ${donation_amount}. We can assure you that it will be put to great use.\n\nBest,\nChris\n".format(**letter_details)
    print(letter)
    prompt()

def list_donors():
    # Formatted print of donor names
    print("List of donors:")
    for i in donor_names():
        print(i)
    print()

def donor_names():
    # Create array of donor names
    name_list = []
    for donor in donations:
        name_list.append(donor[0])
    return name_list

def print_report():
    # Print formatted report showing donors and donation stats
    header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * len(header))

    for donor in donations:
        name = donor[0]
        total_given = sum(donor[1:])
        num_gifts = len(donor[1:])
        avg_gift = total_given / num_gifts
        print('{:21}{:>15.2f}{:>16}{:>16.2f}'.format(name, total_given, num_gifts, avg_gift))

    print()
    prompt()


if __name__ == "__main__":
    # Will only execute if mailroom.py is run as a script
    prompt()
