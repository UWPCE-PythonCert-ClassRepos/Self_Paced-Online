#!/usr/bin/env python3

# lesson 05, Mail room 3 Assignment, added exceptions to all the user
# inputs, also added the option to quit at any of the user inputs.
# Comprehensions were added where they seemed to fit.

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

        # tried to do this with comprehension but I couldn't get it to print
        # pretty
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

    response = input(
        "\nFull name of the donor or type 'list': ")

    # create the selection
    while True:

        # if list print the list of donors
        if response.lower().strip() == "list":
            for item in donors:
                print(item)
            response = input(
                "\nPlease give me the full name of the donor: ")

        # if they type 4, go back to the menu
        elif response.lower().strip() == "quit":
            print("Going back to main menu")
            menu()

        # if they give a bunch of white spaces
        elif response.strip() == "":
            print("You did not type anything, going back to main menu")
            menu()

        # if they give a numeric
        elif not isinstance(response, str):
            print("You did not type a string, going back to the main menu")
            menu()

        # if the person is in the donors database, add the donation - adding
        # try/catch block here
        elif response in donors:

            try:
                amount = float(input("\nHow much did they donate? "))

            except ValueError:
                print("Please enter a numeric value!!")

            else:
                # add the new donation to the total and average
                donors[response][0] += amount
                donors[response][1] += 1
                donors[response][2] = donors[response][0] / donors[response][1]

                # call the email
                email(response, amount)
                break

        else:
            # there is a new donor
            print(
                "\nGreat! A new donor! Adding to {} database now...".format(response))
            try:
                amount = float(input("How much did they donate? "))

            except ValueError:
                print("Please enter a numeric value!!")

            else:
                donors.update({response: [amount, 1, amount]})

                # call the email
                email(response, amount)
                break


def email(name, donation):
    """
    Print the email with the donor name and amount included
    """
    print("\nCreating the email: \n")
    print(
        "Dear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMailroom Assitant\n".format(
            name,
            donation))


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

    # go through the sorted list - using comprehension here
    sorted_donors = dict(
        sorted(
            donors.items(),
            key=lambda x: x[1],
            reverse=True))

    # print the sorted donors list, using the shortcut "*", also tried
    # comprehension but printing pretty was a problem
    for entry in sorted_donors:
        print(
            "{:<20} ${:<20.2f} {:<20d} ${:<20.2f}\n".format(
                entry, *sorted_donors[entry]))


def send_all_letters():
    """
    This function sends letters to all donors by creating files with the thank you letters
    """
    # print message
    print("\nThe following files created: ")
    for entry in donors:
        with open(entry + ".txt", "w") as donor_file:
            print(entry + ".txt")
            donor_file.write(
                "Dear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMail room Assistant\n".format(
                    entry,
                    donors[entry][0]))


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
