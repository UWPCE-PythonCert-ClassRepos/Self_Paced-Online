#!/usr/bin/env python3

donor_dict = {
    'Ryan Moore': [500, 250], 'Ted Laws': [1000, 100], 'Ben Snell': [150],
    'Andrew Crawford': [2000, 2000, 4000], 'Beth Ross': [400]}


prompt = ("\nWhat would you like to do\n"
          "Choose an action from this list:\n"
          "1 - Send a Thank You\n"
          "2 - Create a Report\n"
          "3 - Quit\n")


def menu_selection(prompt, dispatch_dict, donor_dictionary):
    while True:
        response = input(prompt)
        if dispatch_dict[response](donor_dictionary) == "Exit Menu":
            break


def exit(a):
    return "Exit Menu"


def send_to(donor_dictionary):
    recipient = input("Who is the thank you note for? Enter a full name or 'list' to see a list: ")
    if recipient.lower() == 'list':
        print("Here are all the donors:")
        for i in donor_dictionary:
            print(i)
        recipient = input("Who is the thank you note for? ")
        return recipient
    else:
        return recipient


def thank_you(donor_dictionary):
    name = send_to(donor_dictionary)
    if name in donor_dictionary:
        amt = sum(donor_dictionary[name])
    else:
        amt = int(input("Wait, A new donation! How much: "))
        donor_dict[name] = [amt]
    print("OK, here is a thank you note for {}".format(name))
    note = "Dear {},\nThank you for your recent donation. You have now donated ${}.\nThank you so much!\n- Alex Laws"
    print(note.format(name, amt))


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


menu_dict = {"1": thank_you, "2": report, "3": exit}

if __name__ == '__main__':
    menu_selection(prompt, menu_dict, donor_dict)
