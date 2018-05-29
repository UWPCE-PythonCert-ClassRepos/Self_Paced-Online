#!/usr/bin/env python3

import os
from mailroom import Donor, Donor_list

my_donors = Donor_list(Donor('Ryan Moore', [500, 250]),
                       Donor('Ted Laws', [1000, 100]),
                       Donor('Ben Snell', [150]),
                       Donor('Andrew Crawford', [2000, 2000, 4000]),
                       Donor('Beth Ross', [400]))


prompt = ("\nWhat would you like to do?\n"
          "Choose an action from this list:\n"
          "1 - Add a New Donation to the Records\n"
          "2 - Send a Thank You\n"
          "3 - Thank Everyone\n"
          "4 - Create a Report\n"
          "5 - Manage a Philanthropist donation\n"
          "6 - Build projections for a philanthropist\n"
          "7 - Quit\n")

directory_prompt = ("\nWhere would you like to save the thank you note?"
                    "\n(Leave blank for this directory): ")


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "Exit Menu":
                break
        except KeyError:
            print("\nThat was not one of the options.")


def exit():
    return "Exit Menu"


def report():
    my_donors.donor_report()


def generate_file(letter, destination):
    with open(destination, 'w') as f:
        f.write(letter)


def generate_destination(donor, need_dir='y', directory=""):
    if need_dir == "y":
        directory = input(directory_prompt)
    destination = os.path.join(directory,
                               "{}.txt".format(donor.name.replace(' ', '_')))
    return destination


def get_donation_amt(name):
    while True:
        try:
            amount = int(input("\nHow much did {} donate: ".format(name)))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    return amount


def thank_everyone():
    directory = input(directory_prompt)
    for donor in my_donors.donor_dictionary:
        generate_file(donor.write_note(), generate_destination(donor, 'n', directory))
    print("\nFinished")


def add_donation(name, amount, donor_list_obj):
    new_donor = True
    for donor in donor_list_obj.donor_dictionary:
        if name == donor.name:
            donor.new_donation(amount)
            temp = donor
            new_donor = False
    if new_donor:
        temp = Donor(name, [amount])
        donor_list_obj.add_donor(temp)
    return temp


def add_new_full(name="", thank_you=""):
    if name == "":
        name = input("\nA new donation! Who donated? (First and Last Name): ")
    amount = get_donation_amt(name)
    donor = add_donation(name, amount, my_donors)
    if thank_you == "":
        thank_you = input("\nWould you like a thank you note for {} (y/n): ".format(name))        
    if thank_you.lower() == 'y':
        generate_file(donor.write_note(amount), generate_destination(donor))


def send_to():
    recipient = input("\nWho is the thank you note for?\n"
                      "Enter a full name or 'list' to see a list: ")
    if recipient.lower() == 'list':
        print("\nHere are all the donors:")
        print(my_donors)
        recipient = input("\nWho is the thank you note for? ")
        return recipient
    else:
        return recipient


def thank_you():
    name = send_to()
    donor_exists = my_donors.check_donor(name)
    if donor_exists:
        donor = my_donors.get_donor(name)
        new_donation = input("\nDid {} make a new donation (y/n)? ".format(name))
        if new_donation.lower() == 'y':
            amount = get_donation_amt(name)
            donor.new_donation(amount)
        else:
            amount = 0
        generate_file(donor.write_note(amount), generate_destination(donor))
    else:
        add_new_full(name, 'y')


def donation_multiplier(donation, multiplier, min = 0, max = 9999999):
    if donation > min and donation < max:
        return donation * multiplier
    else:
        return donation


def donor_multiplier(donor, multiplier, min, max):
    return Donor(donor.name, [donation_multiplier(x, multiplier, min, max) for x in donor.donations])


def donor_list_multiplier(donor_reference, multiplier, min, max):
    return [donor_multiplier(x, multiplier, min, max) for x in donor_reference.donor_dictionary]


def philanthropist():
    global my_donors
    while True:
        try:
            multiplier = int(input("\nWhat factor would the philanthropist "
                                   "like to multiply donations by? "))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    while True:
        try:
            min_donation = int(input("\nWhat is the min donation to match? "))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    while True:
        try:
            max_donation = int(input("\nWhat is the max donation to match? "))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    new_list = donor_list_multiplier(my_donors, multiplier, min_donation, max_donation)
    new_donor_list = Donor_list()
    for new_donor in new_list:
        new_donor_list.add_donor(new_donor)
    my_donors = new_donor_list


def hypothetical_philanthropist():
    global my_donors
    while True:
        try:
            multiplier = int(input("\nWhat factor would the philanthropist "
                                   "like to multiply donations by? "))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    while True:
        try:
            min_donation = int(input("\nWhat is the min donation to match? "))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    while True:
        try:
            max_donation = int(input("\nWhat is the max donation to match? "))
            break
        except ValueError:
            print("\nThat wasn't a number value.")
    new_list = donor_list_multiplier(my_donors, multiplier, min_donation, max_donation)
    new_donor_list = Donor_list()
    for new_donor in new_list:
        new_donor_list.add_donor(new_donor)
    original_total_donations = 0
    for donor in my_donors.donor_dictionary:
        original_total_donations += sum(donor.donations)
    total_donations = 0
    for donor in new_donor_list.donor_dictionary:
        total_donations += sum(donor.donations)
    print('\nThe total donations after your gift will be {}. Your share is {}'.format(total_donations, total_donations-original_total_donations))


menu_dict = {"1": add_new_full, "2": thank_you, "3": thank_everyone,
             "4": report, "5": philanthropist, "6": hypothetical_philanthropist, "7": exit}

if __name__ == '__main__':
    menu_selection(prompt, menu_dict)
