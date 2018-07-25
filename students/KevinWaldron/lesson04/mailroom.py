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
    """ Prints a list of the donors by name """
    print("\n" + ("-"*10) + " Donors " + ("-"*10))
    for donor in donors:
        print(donor)

def quit_menu():
    """ Handles the menu quit selection """
    return "Quit"

def create_thank_you(donation):
    """
    Prints a thank for you the given donor and amount
    :param donation: dictionary containing name of the donor to thank and the amount donated
    :returns: formatted thank you string
    """
    return f"""Dear {donation["name"]},\nThank you for your very generous donation of ${donation["amount"]:.2f}.  It \nwill go very far in supporting the Human Fund, \"Money for \nPeople.\"\n{"Sincerely":>40}\n{"Art Vandelay":>50}"""

def donor_entry():
    """ Handles donor entry menu selection """
    name = input("\nEnter donor's full name or 'q' to return to the previous menu: ")
    if(name == "q"):
        return
    amount = input("Enter donation amount or 'q' to return to the main menu: ")
    if (amount == "q"):
        return
    if(not name in donors):
        donors[name] = [0]
    amount = float(amount)
    donors[name].append(amount)
    donors[name][0] += amount
    print(donors[name])
    print("\n" + create_thank_you({"name":name, "amount":amount}))

# modify donor entry slightly (no more list) to reuse display prompt funtion
thank_you_menu_prompt = "1. Enter donation\n2. See a list of donors\n3. Return to previous menu"
thank_you_menu_dict = {'1':donor_entry, '2':list_donors, '3':quit_menu}

def send_thank_you():
    # modify donor entry slightly (no more list) to reuse display prompt funtion
    thank_you_menu_prompt = "1. Enter donation\n2. See a list of donors\n3. Return to previous menu"
    thank_you_menu_dict = {'1':donor_entry, '2':list_donors, '3':quit_menu}
    """ Handles the send thank you menu selection """
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
    """ Handles the create report menu selection """
    header = "\n{:<20}| Total Given | Num Gifts | Average Gift".format("Donor Name")
    print(header)
    print("-" * (len(header) - 1))
    # pack the donors into a list of lists for soting
    donors_list = []
    for name in donors:
        donor_copy = [name]
        donor_copy.extend(donors[name])
        donors_list.append(donor_copy)
    donors_list.sort(key=total_donations, reverse=True)
    for donor in donors_list:
        print("{:<20}| ${:>10.2f} | {:>9} | ${:>11.2f}".format(donor[0], donor[1], len(donor) - 2, donor[1]/(len(donor)-2)))

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
        if selection in menu_dict:
            if menu_dict[selection]() == "Quit":
                break
        else:
            print("Invalid selection")

if __name__ == '__main__':
    main_menu_prompt = "1. Send a Thank You\n2. Create a Report\n3. Send letters to everyone\n4. Quit"
    main_menu_dict = {'1': send_thank_you, '2':create_report, '3':mail_everyone, '4':quit_menu}
    display_prompt(main_menu_prompt, main_menu_dict)