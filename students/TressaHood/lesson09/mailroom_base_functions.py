#!/usr/bin/env python3

"""lesson 09, Mail room 5 Assignment, the base functions file
"""

# import modules
import pathlib
import mailroom_donors


def email(name, donation):
    """
    Print the email with the donor name and amount included
    :return: Return the formated email
    """
    return("\nCreating the email: \n\nDear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMail room Assistant\n".format(name, donation))


def report(donor_data):
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
    sorted_donors = donor_data.sorted_database()

    # print the sorted donors list, using the shortcut "*"
    for entry in sorted_donors:
        n = entry.get_name_as_key()
        info = [
            entry.get_total_donations(),
            entry.get_num_donations(),
            entry.get_avg_donations()]

        print(
            "{:<20} ${:<20.2f} {:<20d} ${:<20.2f}\n".format(
                n, *info))


def send_all_letters(donor_data):
    """
    This function sends letters to all donors by creating files with the thank you letters
    """
    # print message and then call the file creator
    print("\nThe following files created: ")
    # sort it by highest donation
    sorted_donors = donor_data.sorted_database()
    create_files(sorted_donors)


def create_files(donors_letters):
    """
    This function creates the files with the thank you letters and saves them to the current directory
    """
    for entry in donors_letters:
        n = entry.get_name_as_key()
        with open(n + ".txt", "w") as donor_file:
            print(n + ".txt")
            donor_file.write(
                "Dear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMail room Assistant\n".format(
                    n, entry.get_recent_donations()))


def quit(donor_data):
    """
    This function quits the program and prints a message, added exit() to the end because
    now I have encapsulated the menu selections into a function, and it will continue to go on
    forever if I don't break out of it.
    """
    print("\nQuitting program ...")
    print("Goodbye!")
    exit()
