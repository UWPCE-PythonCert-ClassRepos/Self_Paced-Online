#!/usr/bin/env python3

# donor data structure, a dictionary of donors, each donor name is key and the value is a list constaining the total donations
# (for easy sorting), followed by the history of donations
donors = {
"Bill Ted":[726.63, 353.53, 348.1, 25.00],
"Frank Fred":[178.76, 120.50, 56.76, 1.50],
"Laura Todd":[5.75, 5.75],
"Steve Lincoln":[165.28, 75.38, 89.9],
"Lisa Grant":[209.7, 175.50, 34.20]
}

def list_donors():
    """ Creates a list of the donors by name """
    return f"\n{'-'*10} Donors {'-'*10}\n" + '\n'.join(donors)

def print_donors():
    """ Prints the list of donors """
    print(list_donors())

def quit_menu():
    """ Handles the menu quit selection """
    return "Quit"

def create_thank_you(donation):
    """
    Prints a thank for you the given donor and amount
    :param donation: dictionary containing name of the donor to thank and the amount donated
    :returns: formatted thank you string
    """
    return f"Dear {donation['name']},\nThank you for your very generous donation of ${donation['amount']:.2f}.  It \nwill go very far in supporting the Human Fund, \"Money for \nPeople.\"\n{'Sincerely':>40}\n{'Art Vandelay':>50}"

def donation_entry(name):
    """
    Handles the donation entry and prints the thank you to the screen.
    :param name: the name of the donor
    """
    amount = input("Enter donation amount or 'q' to return to the main menu: ")
    if (amount == "q"):
        return
    try:
        add_donation(name, amount)
    except ValueError:
        print("Please enter a valid number.")
        donation_entry(name)

def add_donation(name, amount):
    """
    Add a donation.
    :param name: the name of the donor.
    :param amount: the amount of the donation.the
    :returns: the list of donations for the donor
    """
    if(name not in donors):
        donors[name] = [0]
    amount = float(amount)
    donors[name].append(amount)
    donors[name][0] += amount
    print("\n" + create_thank_you({"name":name, "amount":amount}))
    return donors[name]

def donor_entry():
    """ Handles donor entry menu selection """
    name = input("\nEnter donor's full name or 'q' to return to the previous menu: ")
    if(name == "q"):
        return
    donation_entry(name)

def send_thank_you():
    """ Handles the send thank you menu selection """
    # modify donor entry slightly (no more list) to reuse display prompt funtion
    thank_you_menu_prompt = "1. Enter donation\n2. See a list of donors\n3. Return to previous menu"
    thank_you_menu_dict = {'1':donor_entry, '2':print_donors, '3':quit_menu}
    display_prompt(thank_you_menu_prompt, thank_you_menu_dict)

def total_donations(donor):
    """ Key sort method to retrieve total contribution amount for donors data structure """
    return donor[1]

def mail_everyone():
    """ Handles the mail to everyone menu selection """
    for donor in donors:
        with open(donor.lower().replace(' ', "_") + ".txt", 'w') as f:
            f.write(create_thank_you({"name":donor, "amount":donors[donor][0]}))

def create_report():
    """
    Handles the create report menu selection
    :returns: returns the report string
    """
    header = "\n{:<20}| Total Given | Num Gifts | Average Gift\n".format("Donor Name")
    result = header
    result += f"{'-' * (len(header) - 1)}"
    donors_list = create_flattened_sorted_donors_list()
    for donor in donors_list:
        result += "\n{:<20}| ${:>10.2f} | {:>9} | ${:>11.2f}".format(donor[0], donor[1], len(donor) - 2, donor[1]/(len(donor)-2))
    return result

def create_flattened_sorted_donors_list():
    """
    Converts the donors dict name:value pair into a flattened list and the sorts the results donors list by total donations amount
    :returns: the flattened and sorted donors list
    """
    donors_list = [[name] + donations for name, donations in donors.items()]
    donors_list.sort(key=total_donations, reverse=True)
    return donors_list

def print_report():
    """ Prints the report """
    print(create_report())

def display_prompt(menu_prompt, menu_dict):
    """
    Handles the user input loop for a menu of options by displaying the menu prompt and dispatching
    to the appropriate method based on the user selection

    :param menu_prompt: the menu prompt
    :param menu_dict: the mapping of menu selections to functions
    """
    while True :
        print("\nChoose from the following menu of options:")
        print(menu_prompt)
        selection = input("\nPlease enter your choice: ")
        try:
            if menu_dict[selection]() == "Quit":
                break
        except KeyError:
            print("Invalid selection")

if __name__ == '__main__':
    main_menu_prompt = "1. Send a Thank You\n2. Create a Report\n3. Send letters to everyone\n4. Quit"
    main_menu_dict = {'1': send_thank_you, '2':print_report, '3':mail_everyone, '4':quit_menu}
    display_prompt(main_menu_prompt, main_menu_dict)