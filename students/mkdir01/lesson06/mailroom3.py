#!/usr/bin/env python3
import sys

data = {'John Doe': [120.00, 353.33, 400.00], 'Jane Doe': [3500.04, 2624.44], 'John Smith': [33.33, 400.00, 29.20], 'Jane Smith': [2.00], 'Billy Jo Jones': [100.00, 100.00, 100.00]}

# mode 1 - "send a thank you"
def input_name():
    name = input("Please enter a full name (or type \'list\', or hit \'return\' to go back)> ")
    if name == "list":
            print('\n')
            print('\n'.join(data))
            print('\n')
    elif name == "":
        return None
    else:
        return name


def input_dollars(name):
    dollars = input("Please enter a donation amount (ex: 500.05)> ")
    if float(dollars) > 0:
        for k in data:
            if k == name:
                try:
                    data[k].append(round(float(dollars), 2))
                    return 1
                except ValueError:
                    print("Donation amounts must be numbers")
                    if not data[name]:
                        data.pop(name)  # undo: data[name] = []
        else:  # if no name match, make new entry
            data[name] = [(round(float(dollars), 2))]
            return 1
    else:
        return None


def thank_you():
    while True:
        name = input_name()
        if not name:
            break
        pr = input_dollars(name)
        if pr:
            print(f"Dear {name},\n\nThank you for your donation of {data[name][-1]:.2f}.\n\nLove,\nThe Charity Org\n")


# mode 2 - "create a report"
def sort_by_dollars(donor_lists):
    try:
        donor_lists.sort(key=lambda k: k[1], reverse=True)
    except IndexError:
        print('This list can not be sorted.')
        print(donor_lists)


def create_donor_list():
    # create [[donor 1 name, donor 1 total donations], [donor 2 name, donor 2 total donations], etc]
    temp_donor_lists = [[k, round(float(sum(data[k])), 2)] for k in data]
    sort_by_dollars(temp_donor_lists)
    return temp_donor_lists


def create_gift_list(temp_donor_lists):
    # create [[donor name, total donations, # gifts, avg gift], [donor 2 info]]
    for l in temp_donor_lists:
        l.append(len(data[l[0]]))  # append number of gifts
        try:
            l.append(round(l[1] / (len(data[l[0]])), 2))  # append avg gift)
        except ZeroDivisionError:
            temp_donor_lists.pop(l)  # gets rid of any rows that have 0 donations
    return temp_donor_lists


def print_donor_report(temp_donor_lists):
    print('\n')
    print("Donor Name                | Total Given |   Num Gifts |  Average Gift")
    print("---------------------------------------------------------------------")
    for row in temp_donor_lists:
        print("{:<27}{:>14.2f}{:>14}{:>14.2f}".format(*row))
    print('\n')


def create_report():
    temp_donor_lists = create_donor_list()
    temp_donor_lists = create_gift_list(temp_donor_lists)
    print_donor_report(temp_donor_lists)


# mode 3 - "send letters"
def plural_donate(n):
    if n > 1:
        return 'donations totaling'
    else:
        return 'donation of'


def total_donate(n):
    total = 0
    for d in n:
        total += d
    return round(float(total), 2)


def send_letters():
    for k in data:
        with open(k + '.txt', 'w') as outfile:
            outfile.write(f"Dear {k},\n\tThank you for your {plural_donate(len(data[k]))} {total_donate(data[k]):.2f}.\n\tIt will be put to good use.\n\n\tSincerely,\n\t- The Team")


# mode 4 - "quit"
def end_program():  # exit() and quit() look like they're reserved
    print("Thanks for playing along.")
    sys.exit()


# main loop
def main():
    menu_dict = {"1": thank_you, "2": create_report, "3": send_letters, "4": end_program}
    while True:
        print("Choose a number:")
        print("(1) Send a Thank You")
        print("(2) Create a Report")
        print("(3) Send letter to everyone")
        print("(4) quit")
        mode = input("> ")
        if mode in menu_dict:
            menu_dict.get(mode)()
        else:
            print("Please enter 1, 2, or 3")
            continue


if __name__ == '__main__':
    main()
