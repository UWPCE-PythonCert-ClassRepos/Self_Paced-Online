#!/usr/bin/env python3
import datetime

members = {
    1: {'name': 'Zach Galifianakis', "total": 23757, "donations": 3},
    2: {'name': "Conan O'Brien", "total": 45000, "donations": 3},
    3: {'name': 'Kristen Wiig', "total": 111222, "donations": 2},
    4: {'name': 'Sarah Silverman', "total": 100, "donations": 1},
    5: {'name': 'Bill Burr', "total": 12, "donations": 1},
    6: {'name': 'Will Ferrell', "total": 100000, "donations": 2},
}


def print_member_names():
    """ Return a printed list of member/donor names """
    for member in members.values():
        print(member['name'])


def create_a_report():
    """ Print a donor report with a formatted header and muliple
    lines thereafter for each donor"""
    member_list = []
    counter = 1
    while counter < len(members):
        """ Creates a list of all members/donors info from the existing
        dictionary within a dictionary """
        member_list += members[counter].values()
        counter += 1

    member_total_list = member_list[1::3]
    # Stores just the totals of each member within a variable

    counter = 0
    insert_index = 3
    while counter < len(member_total_list):
        """ Inserting the average donation amount for each member/donor
        in the member_total_list """
        member_list.insert(insert_index, member_list[insert_index - 2] / member_list[insert_index - 1])
        counter += 1
        insert_index += 4

    counter = 0
    member_total_list = sorted(member_total_list, reverse=True)
    # Sorting the totals each member contributes from high to low
    print("Donor Name" + (' ' * 15) + " | " + "Total Given" " | " "Num Gifts" + " | " + "Average Gift\n" + ('- ' * 30))
    while counter < len(member_total_list):
        """Prints each member/donor's name, their total contributions, number of
        times each donor contributed, and their average contribution amount """
        index_num = member_list.index(member_total_list[counter])
        print("{:25} ${:>11.2f} {:^13} ${:>11.2f}\n".format(member_list[index_num - 1], member_list[index_num], member_list[index_num + 1], member_list[index_num + 2]))
        counter += 1


def send_letters_to_everyone():
    """ Creates a file for each donor in the current working directory.
    Each file has a thank you message with the member/donor's name, total
    donations and the number of donations he/she contributed. """
    counter = 1
    while counter <= len(members):
        content = "Thank you {name} for your total donations of ${total} and this is donation number {donations}!".format(**members[counter])
        the_filename = members[counter]['name'] + ' '
        the_filename += str(datetime.datetime.now()) + '.txt'
        the_filename = the_filename.replace(' ', '_')
        with open(the_filename, 'w') as outfile:
            outfile.write(content)
        counter += 1


def send_individual_thank_you_message(single_member):
    """ Prints a thank you message to a new or existing member/donor along with
    their name, total donations, and the number of times they donated. """
    print("Thank you {name} for your total donations of ${total} and this is donation number {donations}!".format(**single_member))


def get_donation_amount():
    while True:
        try:
            donation_amount = 0
            donation_amount = input("Please enter an amount that was donated: $")
            donation_amount = float(donation_amount)
        except ValueError:
            print("\nPlease enter a number only.  No letters.\n")
            continue
        else:
            return donation_amount
            break


def update_existing_donor_info(donor_response):
    """Adds the new donation contributed from a donor to the existing grand
    total, increases by one the amount of times the existing donor has
    contributed, and sends a thank you message to the donor/member. """
    donation_amount = get_donation_amount()
    for member in members.values():
        if member['name'] == donor_response:
            total_donations = float(member['total'])
            total_donations += donation_amount
            member['total'] = total_donations
            num_of_donations = int(member['donations'])
            num_of_donations += 1
            member['donations'] = num_of_donations
            break
    send_individual_thank_you_message(member)


def add_a_new_donor(donor_response):
    """ Adds a new donor to the existing member/donor list, adds her
    contribution amount, mentions it's donation #1 for her, and prints a
    thank you message to the new donor """
    new_member_key = len(members) + 1
    members[new_member_key] = {}
    members[new_member_key]['name'] = donor_response
    contribution = 0
    contribution = get_donation_amount()
    members[new_member_key]["total"] = contribution
    members[new_member_key]["donations"] = 1
    send_individual_thank_you_message(members[new_member_key])


def send_a_thank_you():
    """Prompts user for a name of a donor/member and provides the option of
    listing the names of existing donors.  If the user enters an existing
    donor/member name, the program will proceed with the existing donor/member
    but if the user a new/unfamiliar name, the program will assume the
    user wants to create and proceed with a new donor name. """
    donor_response = ''
    donor_response = input("Please enter a full name of a donor.  Enter 'list' to show a full listing of all donors. \n> ")
    while donor_response == 'list':
        print_member_names()
        donor_response = input("Please enter a full name of a donor. Enter 'list' to show a full listing of all donors.\n> ")
    exists = 0
    for member in members.values():
        if member['name'] in donor_response:
            exists = 1
            break
    if exists == 1:
        update_existing_donor_info(donor_response)
    else:
        add_a_new_donor(donor_response)


if __name__ == '__main__':
    while True:
        """ Prompts user to send a thank you message, create a report,
        send letters, or quit.  This block will repeat until the user enters
        4 to indicate he/she wishes to quit. """
        response = ''
        response = input("Please pick 1, 2, 3, or 4.  Would you like to (1)'Send a Thank You', (2)'Create a Report', (3)'Send letters to everyone', or (4)'Quit'? \n > ")
        while response != "1" and response != '2' and response != '3' and response != '4':
            response = input("Sorry, I didn't catch that.  Please pick 1, 2, 3, or 4.  Would you like to (1)'Send a Thank You', (2)'Create a Report', (3)'Send letters to everyone', or (4)'Quit'? \n > ")
        if response == '1':
            send_a_thank_you()
        elif response == '2':
            create_a_report()
        elif response == '3':
            send_letters_to_everyone()
        elif response == '4':
            quit()
