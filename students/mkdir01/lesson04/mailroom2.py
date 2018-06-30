#!/usr/bin/env python3
import sys

# changed from list of lists to a dict with values as list
data = {'John Doe': [120.00, 353.33, 400.00], 'Jane Doe': [3500.04, 2624.44], 'John Smith': [33.33, 400.00, 29.20], 'Jane Smith': [2.00], 'Billy Jo Jones': [100.00, 100.00, 100.00]}


# mode 1 - "send a thank you"
def thank_you():
    while True:
        name = input("Please enter a full name (or type \'list\', or hit \'return\' to go back)> ")
        if name == "list":
            for k in data:
                print(k)
        elif name == "":
            return
        else:
            dollars = input("Please enter a donation amount (ex: 500.05)> ")
            for k in data:
                if k == name:
                    data[k].append(round(float(dollars), 2))
                    break
            else:  # if no name match, make new entry
                data[name] = [(round(float(dollars), 2))]
            print(f"Dear {name},\n\nThank you for your donation of {data[name][-1]:.2f}.\n\nLove,\nThe Charity Org\n")
            return


# mode 2 - "create a report"
def sort_by_dollars(donor_lists):  # bubble sort
    counter = 0  # counter will ensure we've taken one full pass of the list where all rows are in order before quitting
    temp_row = []
    while counter < (len(donor_lists) - 1):  # we will get an out of bounds error if we don't stop at len-1
        counter = 0
        for i in range(len(donor_lists) - 1):
            if donor_lists[i][1] < donor_lists[i + 1][1]:
                temp_row = donor_lists.pop(i)
                donor_lists.insert(i + 1, temp_row)
            else:
                counter += 1  # when we get through a whole for loop withought "bubbling" we leave the while loop
    else:
        return donor_lists


def create_report():
    temp_donor_lists = []
    for k in data:  # create [[donor 1 name, donor 1 total donations], [donor 2 name, donor 2 total donations], etc]
        temp_total = 0.00
        for donation in data[k]:
            temp_total += float(donation)  # total gifts, added from cells in value
        temp_donor_lists.append([k, (round(float(temp_total), 2))])

    temp_donor_lists = sort_by_dollars(temp_donor_lists)
    for l in temp_donor_lists:
        l.append(len(data[l[0]]))  # append number of gifts
        l.append(round(l[1] / (len(data[l[0]])), 2))  # append avg gift)

    print("Donor Name                | Total Given |   Num Gifts |  Average Gift")
    print("---------------------------------------------------------------------")
    for row in temp_donor_lists:
        print("{:<27}{:>14.2f}{:>14}{:>14.2f}".format(*row))  # [0], temp_dict[name][1], temp_dict[name][2]))


# mode 3 - "send letters"
def plural_donate(n):
    if n > 1:
        return 'donations totaling'
    else:
        return 'donatation of'


def total_donate(n):
    total = 0
    for d in n:
        total += d
    return round(float(total), 2)


def send_letters():
    for k in data:
        outfile = open(k + '.txt', 'w')
        outfile.write(f"Dear {k},\n\tThank you for your {plural_donate(len(data[k]))} {total_donate(data[k]):.2f}.\n\tIt will be put to good use.\n\n\tSincerely,\n\t- The Team")
        outfile.close()


# mode 4 - "quit"
def end_program():  # exit() and quit() look like they're reserved
    print("Thanks for playing along.")
    sys.exit()


# main loop
def main():
    menu_dict = {1: thank_you, 2: create_report, 3: send_letters, 4: end_program}
    while True:
        print("Choose a number:")
        print("(1) Send a Thank You")
        print("(2) Create a Report")
        print("(3) Send letter to everyone")
        print("(4) quit")
        mode = input("> ")
        if mode == "1" or mode == "2" or mode == "3" or mode == "4":
            menu_dict.get(int(mode))()
        else:
            print("Please enter 1, 2, or 3")
            continue


if __name__ == '__main__':
    main()
