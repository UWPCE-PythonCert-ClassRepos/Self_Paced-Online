#!/usr/bin/env python3

"""lesson 06, Mail room 4 Assignment
This mail room version is now being run through a bunch of unit tests, to see how well it performs,
some refactoring of the code needed to be done to make it more testable and ultimately better.
"""

# import modules
import pathlib


def menu():
    """
    This function lists all the menu items and calls the appropriate
    functions based on the user input to response. It also deals with
    exceptions from user input.
    """

    # set up menu selection prompts
    response = None
    while response != 4:

        # the introduction
        print("\nWelcome to the mail room, please choose an action: ")

        # print menu items
        for item in menu_items:
            print(item, menu_items[item][0])

        # add try/catch block
        try:
            # get the  user's response and convert it to an integer, then call
            # the appropriate function
            response = int(
                input("\nWhat action would you like to choose?").strip())

            if int(response) not in [1, 2, 3, 4]:
                print("\nYou must ONLY choose 1, 2, 3, or 4, please try again")
                continue

        except ValueError:
            print("\nYour entry must be INTEGERS 1,2,3,4, please try again")
            continue

        else:
            menu_items[response][1]()


def thank_you():
    """
    Prompt the user for more information to create the thank you, then
    call the email function to write it. Also deal with exceptions from user input.
    """
    print("\nYou have chosen to create a Thank You Note: ")
    print("\nPlease give the full name of the donor, or type 'list' to see all current donors. Remember you can always type 'quit' to go to the main menu.")

    # create the selection
    while True:

        response = input("\nFull name of the donor or type 'list': ").strip()

        # if list print the list of donors
        if response.lower() == "list":
            print("\n".join(list_donors(donors)))
            continue

        # if they type 4, go back to the menu
        elif response.lower() == "quit":
            print("Going back to main menu")
            menu()

        # if they give a bunch of white spaces
        elif response.strip() == "":
            print("You did not type anything, going back to main menu")
            menu()

        # if they give a numeric
        elif response.replace(".", "").isdigit() == True:
            print("You did not type a string, going back to the main menu")
            menu()

        # if the person is in the donors database, add the donation - adding
        # try/catch block here
        elif response in donors:
            while True:
                try:
                    amount = float(input("\nHow much did they donate? "))

                except ValueError:
                    print("Please enter a numeric value!!")
                    continue

                else:
                    # add the donations and then create the email
                    add_donation(donors, response, amount)
                    print(email(response, amount))
                    menu()

        else:

            while True:
                    # there is a new donor
                print(
                    "\nGreat! A new donor! Adding to {} database now...".format(
                        response.title()))
                try:
                    amount = float(input("How much did they donate? "))

                except ValueError:
                    print("Please enter a numeric value!!")
                    continue

                else:
                    # add them to the database and email
                    add_donation(donors, response.title(), amount)
                    print(email(response, amount))
                    menu()


def list_donors(donor_data):
    """This function lists all the donors in a database
    :return donor_list: Returns a list of all the names in the donor database
    """
    donor_list = [item for item in donor_data]
    return donor_list


def add_donation(donor_data, name, money, num_gifts=1):
    """add the new donation to the total and average
    :return donor_data: The donor database is updated
    """
    # if the donor exists, update it, if not add the new donor
    if name in donor_data:
        donor_data[name][0] += money
        donor_data[name][1] += num_gifts
        donor_data[name][2] = donor_data[name][0] / donor_data[name][1]
    else:
        donor_data[name] = [money, num_gifts, money]

    return donor_data


def email(name, donation):
    """
    Print the email with the donor name and amount included
    :return: Return the formated email
    """
    return("\nCreating the email: \n\nDear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMail room Assistant\n".format(name, donation))


def report():
    """
    Print a formatted report of all donations thus far
    """

    # print the headers
    print(
        "\n{:<20}| {:<20}| {:<20}| {:<20}".format(
            "Donor Name",
            "Total Given",
            "Num Gifts",
            "Average Gifts"))
    print("----------" * 8)

    # sort it by highest donation
    sorted_donors = sort_dictionary(donors)

    # print the sorted donors list, using the shortcut "*"
    for entry in sorted_donors:
        print(
            "{:<20} ${:<20.2f} {:<20d} ${:<20.2f}\n".format(
                entry, *sorted_donors[entry]))


def sort_dictionary(donor_diction):
    """Go through given dictionary and sort it using comprehension
    :return sorted_dict: this is the sorted dictionary
    """
    sorted_dict = dict(
        sorted(
            donor_diction.items(),
            key=lambda x: x[1],
            reverse=True))

    return(sorted_dict)


def send_all_letters():
    """
    This function sends letters to all donors by creating files with the thank you letters
    """
    # print message and then call the file creator
    print("\nThe following files created: ")
    create_files(donors)


def create_files(donors_letters):
    """
    This function creates the files with the thank you letters and saves them to the current directory
    """
    for entry in donors_letters:
        with open(entry + ".txt", "w") as donor_file:
            print(entry + ".txt")
            donor_file.write(
                "Dear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMail room Assistant\n".format(
                    entry, donors_letters[entry][0]))


def quit():
    """
    This function quits the program and prints a message, added exit() to the end because
    now I have encapsulated the menu selections into a function, and it will continue to go on
    forever if I don't break out of it.
    """
    print("\nQuitting program ...")
    print("Goodbye!")
    exit()


def main():
    """
    This is the main function that calls the the main selection program and sets up the donor starting list.
    :global donors: global variable for the donor database
    :global menu_items: global variable for the menu selection items
    """

    # Set global variables
    global donors
    global menu_items

    # donor names and data, easier to update this way using comprehension
    names = [
        "Sarah Sanderson",
        "Amy Anderson",
        "Erin Eckoff",
        "Cassandra Cooper",
        "Debbie Danger"]

    donation_data = [[3000, 3, 1000], [300, 2, 150], [
        12536.26, 1, 12536.26], [234.34, 2, 117.17], [9809.56, 3, 3269.85]]

    # use comprehension to zip it into a dictionary
    donors = {
        names: donation_data for names,
        donation_data in zip(
            names,
            donation_data)}

    # create the menu items
    menu_items = {
        1: (
            "- Send a Thank You", thank_you), 2: (
            "- Create a Report", report), 3: (
                "- Send letters to everyone", send_all_letters), 4: (
                    "- Quit", quit)}

    # call the menu function to get started
    menu()

# call the main function
if __name__ == '__main__':
    main()
