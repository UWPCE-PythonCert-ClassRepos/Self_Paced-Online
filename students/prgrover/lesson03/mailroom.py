#!/usr/bin/env python3

# Global tuple containing donor list and donation amounts
donor_list = [["Harry Potter", [10000, 5000, 500.55]], ["Ronald Weasley", [2499.99, 7500.01]], ["Hermione Granger", [100, 2000, 30000]], ["Draco Malfoy", [10, 888.88]], ["Neville Longbottom", [10]]]

# Email template for Thank You message
email = """Dear {},\n\nThank you for your generous donation of ${}.\n\nSincerely,\nHogwarts School of Witchcraft and Wizardry"""


def send_thankyou():
    """
    * If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    * If the user types ‘list’, show them a list of the donor names and re-prompt
    * If the user types a name not in the list, add that name to the data structure and use it.
    * If the user types a name in the list, use it.
    * Once a name has been selected, prompt for a donation amount.
    * Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    * Once an amount has been given, add that amount to the donation history of the selected user.
    * Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

    Args: None
    """
    donor_name = input("Please enter the full name of a donor. You can also enter list to see all current donors or e to exit: ")
    if donor_name == "e":
        return

    while donor_name == "list":
        for donor in donor_list:
            print (donor[0])
        donor_name = input("Please enter the full name of a donor. You can also enter list to see all current donors or e to exit: ")

    for donor in donor_list:
        if donor_name == donor[0]:
            donor_found = 0
            break
        elif donor_name == "e":
            return
        else:
            donor_found = 1

    if donor_found == 0:
        donation_amount = input("Please enter the donation amount or e to exit: ")
        if donation_amount == "e":
            return
        donor[1].append(float(donation_amount))
        print(email.format(donor_name, donation_amount))
    else:
        donation_amount = input("Please enter the donation amount or e to exit: ")
        if donation_amount == "e":
            return
        donor_list.append([donor_name, [float(donation_amount)]])
        print(email.format(donor_name, donation_amount))


def create_report():
    """
    * If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
    * Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
    * Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
    * After printing this report, return to the original prompt.

    Args: None
    """
    print ("{:30s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print ("-" * 71)

    donor_list.sort(key=lambda i: sum(i[1]), reverse=True)
    
    for donor in donor_list:
        donor_name = donor[0]
        total_given = sum(donor[1])
        num_gifts = len(donor[1])
        average_gift = (total_given / num_gifts)
        print ("{:30s}  ${:11.2f}   {:9d}  ${:12.2f}".format(donor_name, total_given, num_gifts, average_gift))


def user_option():
    """
    Prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)

    Args: None
    """
    quit = 1
    while quit:
        option = input("Please select an option:\nc: Create a Report\ns: Send a Thank You Letter\nq: Quit\n: ")
        if option == "c":
            create_report()
        elif option == "s":
            send_thankyou()
        elif option == "q":
            print ("Bye!")
            quit = 0
        else:
            print ("Try again")

if __name__ == '__main__': 
    user_option()