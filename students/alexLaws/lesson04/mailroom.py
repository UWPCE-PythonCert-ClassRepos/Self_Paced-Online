#!/usr/bin/env python3

donor_dict = {
    'Ryan Moore': [500, 250], 'Ted Laws': [1000, 100], 'Ben Snell': [150],
    'Andrew Crawford': [2000, 2000, 4000], 'Beth Ross': [400]}


def user_action():
    print("Choose an action from this list:")
    print("Send a Thank You")
    print("Create a Report")
    print("Quit")
    while True:
        option = input("What is your choice: ")
        if option.lower() in ["send a thank you", "create a report", "quit"]:
            return option
            break
        else:
            print("That is not an option. Choose again.")


def send_to(donor_list):
    recipient = input("Who is the thank you note for? Enter a full name or 'list' to see a list: ")
    if recipient.lower() == 'list':
        print("Here are all the donors:")
        for i in donor_list:
            print(i)
        recipient = input("Who is the thank you note for? ")
        return recipient
    else:
        return recipient


def thank_you(recip, donor_dictionary):
    print("OK, here is a thank you note for {}".format(recip))
    total = sum(donor_dictionary[recip])
    note = "Dear {},\nThank you for your recent donation. You have now donated ${}.\nThank you so much!\n- Alex Laws"
    print(note.format(recip, total))


def report(donor_dictionary):
    print("Donor Name       |  Total Given  |  Num Gifts  |  Average Gift")
    to_sort = {}
    for donor in donor_dictionary:
        total = sum(donor_dictionary[donor])
        to_sort[donor] = total
    in_order = sorted(to_sort, key=to_sort.__getitem__, reverse=True)
    for donor in in_order:
        total = to_sort[donor]
        number = len(donor_dictionary[donor])
        average = total / number
        print("{:17} ${:14,.2f} {:13} ${:13,.2f}".format(donor, total, number, average))


if __name__ == '__main__':
    while True:
        act = user_action().lower()
        if act == "send a thank you":
            name = send_to(donor_dict)
            if name in donor_dict:
                thank_you(name, donor_dict)
            else:
                amt = int(input("Wait, A new donation! How much: "))
                donor_dict[name] = [amt]
                thank_you(name, donor_dict)
        if act == "create a report":
            report(donor_dict)
        if act == "quit":
            break
        print("Would you like to do something else...")
