#!/usr/bin/env python3

# donor data structure, a list of donors, each donor sublist constains the name, followed by the total donations
# (for easy sorting), followed by the history of donations
donors = [
["Bill Ted", 726.63, 353.53, 348.1, 25.00],
["Frank Fred", 178.76, 120.50, 56.76, 1.50],
["Laura Todd", 5.75, 5.75],
["Steve Lincoln", 165.28, 75.38, 89.9],
["Lisa Grant", 209.7, 175.50, 34.20]
]

def list_donors():
    """ Prints a list of the donors by name """
    print("\n" + ("-"*10) + " Donors " + ("-"*10))
    for donor in donors:
        print(donor[0])

def print_thank_you(name, amount):
    """
    Prints a thank for you the given donor and amount

    :param name: name of the donor to thank
    :param amount: amount of donation from the donor in dollars
    """
    print(f"\nDear {name},")
    print(f"Thank you for your very generous donation of ${amount:.2f}.  It \nwill go very far in supporting the Human Fund, \"Money for \nPeople.\"\n")
    print("{:>40}".format("Sincerely,"))
    print("{:>50}".format("Art Vandelay"))

def get_donor_index(name):
    """
    Gets the index of the donor that matches the given name

    :param name: the name of the donor to search for
    :returns: the index of the donor or -1 if no match is found
    """
    donor_names = []
    for i, donor in enumerate(donors):
        if(donor[0] == name):
            return i
    return -1

def send_thank_you():
    """ Handles the send thank you menu selection """
    name = input("\nEnter donor full name to send thank you to that donor, list to see a list of a available donors, a new name to add to the list of donors, or 'q' to return to the main menu: ")
    if(name.lower() == "list"):
        list_donors()
        send_thank_you()
    elif(name == "q"):
        display_prompt()
    elif(get_donor_index(name) == -1):
        donors.append([name, 0])
    i = get_donor_index(name)
    amount = input("Enter donation amount or 'q' to return to the main menu: ")
    if (amount == "q"):
        display_prompt()
    amount = float(amount)
    donors[i].append(amount)
    donors[i][1] += amount
    print_thank_you(name, amount)

def total_donations(donor):
    """ Key sort method to retrieve total contribution amount for donors data structure """
    return donor[1]

def create_report():
    """ Handles the create report menu selection """
    header = "\n{:<20}| Total Given | Num Gifts | Average Gift".format("Donor Name")
    print(header)
    print("-" * (len(header) - 1))
    donors.sort(key=total_donations, reverse=True)
    for donor in donors:
        print("{:<20}| ${:>10.2f} | {:>9} | ${:>11.2f}".format(donor[0], donor[1], len(donor) - 2, donor[1]/(len(donor)-2)))

def display_prompt():
    """ Handles the main user input loop by displaying the main menu and receiving user input """
    while(True):
        print("\nChoose from the following menu of options:")
        print("1. Send a Thank You")
        print("2. Create a Report")
        print("3. Quit")

        selection = input("\nPlease enter your choice: ")

        if (selection == "1"):
            send_thank_you()
        elif (selection == "2"):
            create_report()
        elif (selection == "3"):
            exit()

if __name__ == '__main__':
    display_prompt()