#!/usr/bin/env python3
# Lesson 6 - Mailroom_4 (Unit testing)

def prompt(prompt, menu):
    """ Create menu based on arguments """
    while True:
        response = input(prompt)
        try:
            if menu[response]() == "quit":
                break
        except KeyError:
            print('Please enter a valid selection!')


def send_thank_you():
    """ Create sub_prompt """
    prompt(thank_you_prompt, thank_you_menu)


def add_donation():
    """ Add donor/donation to existing list of donations """
    try:
        donor_name = input("\nPlease enter a donor name: ")
        new_donation = float(input(f"Please enter a donation amount for {donor_name}: "))
    except ValueError:
        print("Please enter a numeric value for 'donation'!")
        add_donation()
    else:
        if donor_name not in donations:
            donations[donor_name] = [new_donation]
        else:
            donations[donor_name].append(new_donation)
        print_email(donor_name, new_donation)


def write_letters():
    """
    For all donors, generate a thank you letter, and write it to disk as a text file
    """
    for donor in donations:
        file_name = '_'.join(donor.split()) + ".txt"
        with open(file_name, 'w') as f:
            f.write(f"""Dear {donor},

            Thank you very much for your generosity! Your most recent gift of ${(donations[donor][-1])} will be put to great use. So far, you've donated a total of ${sum(donations[donor])}!

            Sincerely,
            The Team""")

            print(f"\nCreated letter for {donor}!")


def compose_letter(donations):
    pass



####  TESTED  ####
def create_report_header():
    """ Generate formatted header for report """
    header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    header += '\n'
    header += ("-" * len(header))
    return header


def create_report_data(donations):
    """ Generate data needed for report """
    data = []
    for donor, donor_data in donations.items():
        total_given = sum(donor_data)
        num_gifts = len(donor_data)
        avg_gift = total_given / num_gifts
        data.append([donor, total_given, num_gifts, avg_gift])
    return data


def create_report_rows(data):
    """ Create formatted data rows for report """
    rows = ''
    for donor, total_given, num_gifts, avg_gift in data:
        rows += '{:21}{:>15.2f}{:>16}{:>16.2f}'.format(donor, total_given, num_gifts, avg_gift) + '\n'
    return rows


def print_report():
    print(create_report_header())
    data = create_report_data(donations)
    print(create_report_rows(data))


def create_email(donor, donation):
    """ Create formatted email thanking donor """
    letter_details = {'name': donor, 'donation_amount': donation}
    letter = "\nDear {name},\n\nThank you so very much for your kind donation of ${donation_amount}. We can assure you that it will be put to great use.\n\nBest,\nChris".format(**letter_details)
    return letter


def print_email(donor, donation):
    print(create_email(donor, donation))


def list_donors(donations):
    """ Create formatted list of donor names """
    donor_names = "\nList of donors:\n"
    for donor in donations:
        donor_names += (donor) + "\n"
    return donor_names


def print_donors():
    print(list_donors(donations))


def quit_menu():
    """ Quit current menu """
    return "quit"


### Parameters ###
donations = {"Bill Gates": [10.50, 123.45, 1111.11],
             "Jeff Bezos": [7.65, 1000.00],
             "Paul Allen": [145.90],
             "John Nordstrom": [45.67, 6519.65],
             "Mark Zuck": [789.12]}

# Dictionaries for menu control flow
main_menu = {
    "1": send_thank_you,
    "2": print_report,
    "3": write_letters,
    "q": quit_menu,
}

thank_you_menu = {
    "1": add_donation,
    "2": print_donors,
    "q": quit_menu,
}

# Prompts used
main_prompt = ("\nWelcome to the Main Menu! What would you like to do?\n1 - Send a Thank You\n2 - Create a Report\n3 - Send letters to everyone\nq - Quit and exit\n--> ")

thank_you_prompt = ("\nPlease choose one of the following:\n1 - Add a donation and send thank you message\n2 - Display list of current donors\nq - Return to main menu\n--> ")


## Execution of file if run as a script ###
if __name__ == "__main__":
    prompt(main_prompt, main_menu)
