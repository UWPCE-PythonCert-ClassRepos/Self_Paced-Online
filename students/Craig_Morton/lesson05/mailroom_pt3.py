# ------------------------------------------------- #
# Title: Lesson 5, pt 2/2, Mail room 3
# Dev:   Craig Morton
# Date:  8/29/2018
# Change Log: CraigM, 8/29/2018, Mail room 3
# ------------------------------------------------- #

# !/usr/bin/env python3


def user_input(user_prompt, user_menu):
    """While loop for user input"""
    while True:
        response = input(user_prompt)
        try:
            if user_menu[response]() == "quit":
                break
        except KeyError:
            print('Please enter a valid option!')


def thank_you_letter():
    """Thank you letter prompt"""
    user_input(donor_prompt, thank_you_menu)


def add_donation():
    """Add donation prompt"""
    try:
        name_of_donor = input("\nPlease enter a donor name: ")
        create_donation = float(input(f"Please enter a donation amount for {name_of_donor}: "))
    except ValueError:
        print("Please enter a numeric value!")
        add_donation()
    else:
        if name_of_donor not in donations_list:
            donations_list[name_of_donor] = [create_donation]
        else:
            donations_list[name_of_donor].append(create_donation)
        donor_email(name_of_donor, create_donation)


def write_letters_to_all():
    """Write letter to all donors"""
    for donor in donations_list:
        file_name = '_'.join(donor.split()) + ".txt"
        with open(file_name, 'w') as f:
            f.write(f"""Dear {donor},

Thank you so much for your generous donation of ${(donations_list[donor][-1])}! 
You've donated a total of ${sum(donations_list[donor])}!  Please consider us for future donations.

Highest regards,
The Charity""")
            print(f"\nLetter generated for {donor}")


def donor_email(donor, amount):
    """Thank you letter to donor"""
    letter_details = {'name': donor, 'donation_amount': amount}
    letter = """\nDear {name},\n
Thank you so much for your generous donation of ${donation_amount}!  We will make sure it is put to good use.\n
Highest regards,
The Charity""".format(**letter_details)
    print(letter)


def report_generation():
    """Create report"""
    header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print()
    print(header)
    print("-" * len(header))

    for donor, donor_data in donations_list.items():
        total_given = sum(donor_data)
        num_gifts = len(donor_data)
        avg_gift = total_given / num_gifts
        print('{:21}{:>15.2f}{:>16}{:>16.2f}'.format(donor, total_given, num_gifts, avg_gift))
    print()


def donors_list():
    """List of donors"""
    print("\nList of donors:")
    for donor in donations_list:
        print(donor)
    print()


def menu_quit():
    """Escape menu option"""
    return "quit"


donations_list = {"Bill Gates": [988.0], "Jeff Bezos": [120.50, 50.0, 270.50], "Paul Allen": [12.9, 122.0, 310.0],
                  "Sergey Brin": [55.50, 342.50], "Elon Musk": [3.0, 85.0, 100.0]}

main_menu_selection = {"1": thank_you_letter, "2": report_generation, "3": write_letters_to_all, "q": menu_quit}

thank_you_menu = {"1": add_donation, "2": donors_list, "q": menu_quit}

main_menu_prompt = ("""\nPlease choose one of the following options:\n
1> Send a thank you
2> Create a report
3> Send letters to everyone
q> Quit the program
: """)

donor_prompt = ("""\nPlease choose an option:\n
1> Add a donation and send thanks
2> List of donors
q> Return to main menu
: """)


if __name__ == "__main__":
    user_input(main_menu_prompt, main_menu_selection)
