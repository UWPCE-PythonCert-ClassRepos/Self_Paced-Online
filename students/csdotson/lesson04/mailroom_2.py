#!/usr/bin/env python3
# Lesson 4 - Mailroom... part 2

### Function Definitions ###
def prompt(prompt, menu):
    # Original prompt for main menu selections
    while True:
        response = input(prompt)
        if menu[response]() == "quit":
            break


def send_thank_you():
    # Add donor/donations and trigger thank you email
    prompt(thank_you_prompt, thank_you_menu)


def add_donation():
    response = input("\nPlease enter a donor name: ")
    if response not in donations.keys():
        new_donor = response
        new_donation = input(f"Please enter a donation amount for {new_donor}: ")
        donations[new_donor] = [float(new_donation)]
        print_email(new_donor, new_donation)
    else:
         current_donor = response
         new_donation = input(f"Please enter a donation amount for {current_donor}: ")
         donations[current_donor].append(float(new_donation))
         print_email(current_donor, new_donation)


def print_email(donor, amount):
    # Print formatted email thanking donor
    letter_details = {'name': donor, 'donation_amount': amount}
    letter = "\nDear {name},\n\nThank you so very much for your kind donation of ${donation_amount}. We can assure you that it will be put to great use.\n\nBest,\nChris".format(**letter_details)
    print(letter)


def print_report():
    # Print formatted report showing donors and donation stats
    header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print()
    print(header)
    print("-" * len(header))

    for donor in donations:
        name = donor
        total_given = sum(donations[donor])
        num_gifts = len(donations[donor])
        avg_gift = total_given / num_gifts
        print('{:21}{:>15.2f}{:>16}{:>16.2f}'.format(name, total_given, num_gifts, avg_gift))
    print()


def list_donors():
    # Formatted print of donor names
    print("\nList of donors:")
    for donor in donations:
        print(donor)
    print()


def quit():
    return("quit")


donations = {"Bill Gates": [10.50, 123.45, 1111.11],
             "Jeff Bezos": [7.65, 1000],
             "Paul Allen": [145.90],
             "John Nordstrom": [45.67, 6519.65],
             "Mark Zuck": [789.12]}

main_menu = {
    "1": send_thank_you,
    "2": print_report,
    "q": quit,
}

thank_you_menu = {
    "1": add_donation,
    "2": list_donors,
    "q": quit,
}

main_prompt = ("\nWelcome to the Main Menu! What would you like to do?\n1 - Send a Thank You\n2 - Create a Report\nq - Quit\n--> ")

thank_you_prompt = ("\nPlease choose one of the following:\n1 - Add a donation and send thank you message\n2 - Display list of current donors\nq - quit\n--> ")


if __name__ == "__main__":
    # Will only execute if mailroom.py is run as a script
    prompt(main_prompt, main_menu)
