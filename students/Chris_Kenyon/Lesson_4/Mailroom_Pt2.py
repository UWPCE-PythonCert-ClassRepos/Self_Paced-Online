#!/usr/bin/env python3

# Lesson_4 Activity 1 Mailroom Part 2

import os


def page_break():
    """ Print a separator to distinguish new 'pages'"""
    print("_"*75+"\n")


def get_amount():
    """Get valid donation amount from user"""
    while True:
        try:
            amount = input("How much did they donate: ")
            if str(amount).lower() == 'exit':
                return amount
            else:
                return float(amount)
        except ValueError:
            print("you have made an invalid choice, try again.")
            continue


def getKey(donor_chart):
    """ Return key for sorted function """
    return(sum(donor_chart[1]))


def menu_page():
    """ Return valid menu option from user """
    while True:
        try:
            print("Please choose one of the following options(1,2,3):"
                  "\n1. Send a Thank you. \n2. Create a report"
                  "\n3. Send Letters to Everyone \n4. Quit")
            option = int(input('--->'))
        except ValueError:
            print("You have made an invalid choice, try again.")
            page_break()
            continue
        if option < 1 or option > 4:
            print("You have made an invalid choice, try again.")
            page_break()
            continue
        return option


def send_thanks():
    """ Send Thanks """
    page_break()
    while True:
        list_names = [item[0] for item in donor_chart.items()]
        try:
            print("To whom would you like to say thank you?\n"
                  "(type \"list\" for a full list of names or"
                  "\"exit\" to return to the menu)")
            name = input("--->")
        except ValueError:
            print("you have made an invalid choice, try again.")
            page_break()
            continue
        if name == 'list':
            print(("{}\n"*len(list_names)).format(*list_names))
            continue
        elif name in list_names:
            amount = get_amount()
            new_donor = False
        elif name.lower() == 'exit':
            break
        else:
            addname = input("The name you selected is not in the list,"
                            " would you like to add it(y/n)? ")
            if addname[0].lower() == 'y':
                amount = get_amount()
                new_donor = True
            elif addname.lower() == 'exit':
                break
            else:
                print("\nName was not added, try again\n")
                continue
        if amount == "exit":
            break
        add_donation(name, amount, new_donor)
        print("\nDear {} \nThank you for your generous donation of ${:.2f}!!\n"
              "Now all of the kittens will get "
              "to eat this year".format(name, amount))
        break


def create_report():
    """ Create Report """
    page_break()
    list_names = [item[0] for item in donor_chart.items()]
    new_list = []
    for donor in donor_chart.items():
        sum_don = sum(donor[1])
        new_list.append(sum_don)
    col_lab = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    max_name = max([len(x) for x in list_names])
    max_don = []
    for don in donor_chart.items():
        max_don.append(max(don[1]))
    max_donl = len(str(max(max_don)))
    max_gift = len(col_lab[2])
    if max_donl < len(col_lab[1]):
        max_donl = len(col_lab[1])
    format_col = "\n{:<" + "{}".format(max_name+5) + "}|{:^"
    format_col += "{}".format(max_donl+5)
    format_col += "}|{:^" + "{}".format(max_gift+5)
    format_col += "}|{:>" + "{}".format(max_donl+5) + "}"
    print(format_col.format(*col_lab))
    print("-"*len(format_col.format(*col_lab)))
    sorted_list = sorted(donor_chart.items(), key=getKey, reverse=True)
    for donor in sorted_list:
        num_gifts = len(donor[1])
        avg_gift = sum(donor[1])/num_gifts
        format_item = "{:<" + "{}".format(max_name+5) + "}${:>"
        format_item += "{}".format(max_donl+5) + ".2f}{:>"
        format_item += "{}".format(max_gift+5) + "d} ${:>"
        format_item += "{}".format(max_donl+5) + ".2f}"
        print(format_item.format(donor[0], sum(donor[1]), num_gifts, avg_gift))


def send_letters():
    """ Write letters to each donor in the donor chart and
        save them in a user specified directory """
    while True:
        try:
            dir_path = input("Please type the desired directory "
                             "to save the letters: ")
            letter_form = ("Dear {},\n\n\tThank you for your very "
                           "kind donation of ${:.2f}!")
            letter_form += ("\n\n\tNow all of the kittens will "
                            "get to eat this year!")
            letter_form += ("\n\n\t\t\t\t Cheers! \n\t\t\t\t "
                            "-The Team")
            if dir_path.lower() == "Exit":
                break
            if os.path.exists(dir_path):
                for name, donation in donor_chart.items():
                    file_name = ("{}.txt".format(name))
                    new_letter = open(dir_path + "/" + file_name, 'w')
                    new_letter.write(letter_form.format(name, sum(donation)))
                    new_letter.close()
                break
            else:
                print("That is not a valid directory, using working directory")
                dir_path = os.getcwd()
                for name, donation in donor_chart.items():
                    file_name = ("{}.txt".format(name))
                    new_letter = open(dir_path + "/" + file_name, 'w')
                    new_letter.write(letter_form.format(name, sum(donation)))
                    new_letter.close()
                break
        except ValueError:
            print("\nsomething went wrong please try again: ")
            continue


def add_donation(name, amount, donor_bool):
    """ add a donation for a new or existing donor """
    if donor_bool is False:
        donor_chart.get(list_names.index(name), [1]).append(amount)
    else:
        donor_chart.update({name: [amount]})
    return


def quit():
    """ return quit for menus """
    return "Quit"

if __name__ == '__main__':
    donor_chart = {"Justin Thyme": [1, 1, 1],
                   "Beau Andarrow": [207.121324, 400.321234, 12345.001234],
                   "Crystal Clearwater": [80082],
                   "Harry Shins": [1.00, 2.00, 3.00],
                   "Bob Zuruncle": [0.53, 7.00],
                   "Al Kaseltzer": [1010101, 666.00],
                   "Joe Somebody": [25]}
    menu_dict = {
                1: send_thanks,
                2: create_report,
                3: send_letters,
                4: quit
                }
    option = 0
    while True:
        page_break()
        option = menu_page()
        if menu_dict[option]() == "Quit":
            break
