#!/usr/bin/env python3

# lesson 04, Mailroom2 Assignment

# import modules
import pathlib


def thank_you():
    """
    Prompt the user for more information to create the thank you, then call the email function to write it
    """
    print("\nYou have chosen to create a Thank You Note")
    response = input(
        "\nPlease give me the full name of the donor or type 'list' to see all current donors: ")

    # create the selection
    while True:
        if response == "list":
            # print the list of donors
            for item in donors:
                print(item)
            response = input("\nPlease give me the full name of the donor: ")
        elif response in donors:
            # find their donation amount
            amount = float(input("\nHow much did they donate? "))
            email(response, amount)

            # add the new donation to the total and average
            donors[response][0] += amount
            donors[response][1] += 1
            donors[response][2] = donors[response][0] / donors[response][1]
            break

        else:
            # there is a new donor
            print(
                "\nGreat! A new donor! Adding to {} database now...".format(response))
            amount = float(input("How much did they donate? "))
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

    # go through the sorted list
    sorted_donors = dict(
        sorted(
            donors.items(),
            key=lambda x: x[1],
            reverse=True))

    # print the sorted donors list, using the shortcut "*"
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
    This function quits the program and prints a message
    """
    print("\nQuitting program ...")
    print("Goodbye!")


def main():
    """
    This is the main function that calls the program, gives the user the menu selection (in a dictionary) and sets up the donor starting list
    Depending on their selection either exits, or calls the appropriate function
    :global donors: global variable for the donor database
    :global menu_items: global variable for the menu selection items
    :response: the user's response used
    """

    # Set global variables
    global donors
    global menu_items

    # database of donors
    donors = {
        "Sarah Sanderson": [
            3000, 3, 1000], "Amy Anderson": [
            300, 2, 150], "Erin Eckoff": [
                12536.26, 1, 12536.26], "Cassandra Cooper": [
                    234.34, 2, 117.17], "Debbie Danger": [
                        9809.56, 3, 3269.85]}

    # menu selection
    menu_items = {
        '1': (
            "- Send a Thank You", thank_you), "2": (
            "- Create a Report", report), "3": (
                "- Send letters to everyone", send_all_letters), "4": (
                    "- Quit", quit)}

    # set up menu selection prompts
    response = ""
    while response != "4":
        print("\nWelcome to the mail room, please choose an action: ")
        # get the user info by prompting with a menu selection
        for item in menu_items:
            print(item, menu_items[item][0])

        response = input("\nWhat action would you like to choose?").strip()

        # now pull that function
        menu_items[response][1]()


# call the main function
if __name__ == '__main__':
    main()
