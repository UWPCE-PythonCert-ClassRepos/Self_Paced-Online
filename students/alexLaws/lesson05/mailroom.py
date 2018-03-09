#!/usr/bin/env python3

import os

donor_dictionary = {
    'Ryan Moore': [500, 250], 'Ted Laws': [1000, 100], 'Ben Snell': [150],
    'Andrew Crawford': [2000, 2000, 4000], 'Beth Ross': [400]}


prompt = ("\nWhat would you like to do?\n"
          "Choose an action from this list:\n"
          "1 - Add a New Donation to the Records\n"
          "2 - Send a Thank You\n"
          "3 - Thank Everyone\n"
          "4 - Create a Report\n"
          "5 - Quit\n")


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
    print("\nDonor Name       |  Total Given  |  Num Gifts  |  Average Gift")
    to_sort = {}
    for donor in donor_dictionary:
        total = sum(donor_dictionary[donor])
        to_sort[donor] = total
    in_order = sorted(to_sort, key=to_sort.__getitem__, reverse=True)
    for donor in in_order:
        total = to_sort[donor]
        number = len(donor_dictionary[donor])
        average = total / number
        print("{:17} ${:14,.2f} {:13} ${:13,.2f}".format(donor,
                                                         total,
                                                         number,
                                                         average))


def generate_note(name, all_time_total, curr_donate=0):
    note = ["Dear {},\n".format(name),
            "\nThank you for your generosity to our cause.\n",
            "You have now donated a total of ${:,}.\n".format(all_time_total),
            "We greatly appreciate your contributions!"
            "\n\nThank you!\nAlex Laws"]
    if curr_donate > 0:
        curr = ("Your recent gift of ${:,} "
                "is very helpful. ".format(curr_donate))
        note.insert(2, curr)
    return "".join(note)


def generate_file(letter, destination):
    with open(destination, 'w') as f:
        f.write(letter)


def generate_destination(name, need_dir='y', directory=""):
    if need_dir == "y":
        directory = input("\nWhere would you like to save the thank you note?"
                          "\n(Leave blank for this directory): ")
    destination = os.path.join(directory,
                               "{}.txt".format(name.replace(' ', '_')))
    return destination


def thank_everyone():
    directory = input("\nWhere would you like to save the thank you notes?\n"
                      "(Leave blank for this directory): ")
    for i in donor_dictionary:
        destination = generate_destination(i, 'n', directory)
        generate_file(generate_note(i, sum(donor_dictionary[i])), destination)
    print("\nFinished")


def add_new(name="", thank_you=""):
    if name == "":
        name = input("\nA new donation! Who donated? (First and Last Name): ")
    while True:
        try:
            amount = int(input("\nHow much did {} donate: ".format(name)))
            break
        except ValueError:
            print("\nThat wasn't a dollar value.")
    if thank_you == "":
        thank_you = input("\nWould you like a thank you note (y/n): ")
    if name in donor_dictionary:
        donor_dictionary[name].append(amount)
    else:
        donor_dictionary[name] = [amount]
    if thank_you == 'y':
        letter = generate_note(name, sum(donor_dictionary[name]), amount)
        destination = generate_destination(name)
        generate_file(letter, destination)


def send_to():
    recipient = input("\nWho is the thank you note for?\n"
                      "Enter a full name or 'list' to see a list: ")
    if recipient.lower() == 'list':
        print("\nHere are all the donors:")
        for i in donor_dictionary:
            print(i)
        recipient = input("\nWho is the thank you note for? ")
        return recipient
    else:
        return recipient


def thank_you():
    name = send_to()
    new_donation = input("\nDid {} make a new donation (y/n)?".format(name))
    if new_donation == 'y':
        add_new(name, 'y')
    else:
        try:
            letter = generate_note(name, sum(donor_dictionary[name]))
        except KeyError:
            print("\nWe have no donations on record for {}".format(name))
        else:
            destination = generate_destination(name)
            generate_file(letter, destination)


menu_dict = {"1": add_new, "2": thank_you, "3": thank_everyone,
             "4": report, "5": exit}

if __name__ == '__main__':
    menu_selection(prompt, menu_dict)
