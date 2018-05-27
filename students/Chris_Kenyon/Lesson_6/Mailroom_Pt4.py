#!/usr/bin/env python3

# Lesson_6 Activity 1 Mailroom Part 4

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


def get_key(donor_chart):
    """ Return key for sorted function """
    return(sum(donor_chart[1]))


def menu_page(option=None):
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
        return option


def send_thanks():
    """ Send Thanks """
    page_break()
    list_names = [item[0] for item in donor_chart.items()]
    while True:
        print("To whom would you like to say thank you?\n"
              "(type \"list\" for a full list of names or"
              "\"exit\" to return to the menu)")
        name = input("--->")
        if name == 'list':
            print(("{}\n"*len(list_names)).format(*list_names))
            continue
        elif name in list_names:
            amount = get_amount()
        elif name.lower() == 'exit':
            break
        else:
            addname = input("The name you selected is not in the list,"
                            " would you like to add it(y/n)? ")
            if addname[0].lower() == 'y':
                amount = get_amount()
            elif addname.lower() == 'exit':
                break
            else:
                print("\nName was not added, try again\n")
                continue
        add_donation(name, amount)
        break


def create_report():
    """ Create Report """
    report = []
    page_break()
    list_names = [item[0] for item in donor_chart.items()]
    new_list = [sum(donor[1]) for donor in donor_chart.items()]
    col_lab = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    max_name = max([len(x) for x in list_names])
    max_don = [max(don[1]) for don in donor_chart.items()]
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
    sorted_list = sorted(donor_chart.items(), key=get_key, reverse=True)
    for donor in sorted_list:
        num_gifts = len(donor[1])
        avg_gift = sum(donor[1])/num_gifts
        format_item = "{:<" + "{}".format(max_name+5) + "}${:>"
        format_item += "{}".format(max_donl+5) + ".2f}{:>"
        format_item += "{}".format(max_gift+5) + "d} ${:>"
        format_item += "{}".format(max_donl+5) + ".2f}"
        report.append(format_item.format(donor[0], sum(donor[1]),
                                         num_gifts, avg_gift))
    return '\n'.join(report)


def print_report():
    print(create_report())


def send_letters(dir_path=None):
    """ Write letters to each donor in the donor chart and
        save them in a user specified directory """
    if not dir_path:
        dir_path = input("Please type the desired directory "
                         "to save the letters: ")
    letter_form = ("Dear {},\n\n\tThank you for your very "
                   "kind donation of ${:.2f}!")
    letter_form += ("\n\n\tNow all of the kittens will "
                    "get to eat this year!")
    letter_form += ("\n\n\t\t\t\t Cheers! \n\t\t\t\t "
                    "-The Team")
    if dir_path.lower() == "exit":
        return
    if not os.path.exists(dir_path):
        print("That is not a valid directory, using working directory")
        dir_path = os.getcwd()
    for name, donation in donor_chart.items():
        file_name = ("{}.txt".format(name))
        path_name = os.path.join(dir_path, file_name)
        with open(path_name, 'w') as cur_file:
            cur_file.write(letter_form.format(name, sum(donation)))
    print(f"Letters saved in {dir_path}")


def add_donation(name, amount):
    """ add a donation for a new or existing donor """
    list_names = [item[0] for item in donor_chart.items()]
    if amount == "exit":
        return
    if name in list_names:
        donor_chart.get(list_names.index(name), [1]).append(amount)
    else:
        donor_chart.update({name: [amount]})
    print("\nDear {} \nThank you for your generous donation of ${:.2f}!!\n"
          "Now all of the kittens will get "
          "to eat this year".format(name, amount))


def menu_quit():
    """ return quit for menus """
    return "Quit"

donor_chart = {"Justin Thyme": [1, 1, 1],
               "Beau Andarrow": [207.121324, 400.321234, 12345.001234],
               "Crystal Clearwater": [80082],
               "Harry Shins": [1.00, 2.00, 3.00],
               "Bob Zuruncle": [0.53, 7.00],
               "Al Kaseltzer": [1010101, 666.00],
               "Joe Somebody": [25]}

options = range(1, 5)
test_dump = "C:/Users/chris.kenyon/Documents/Kenyon/UWPython/Testing_File_dump"
menus = (send_thanks, print_report, send_letters, menu_quit)
menu_dict = dict(zip(options, menus))

if __name__ == '__main__':
    option = 0
    while True:
        page_break()
        try:
            option = menu_page()
            if option == 3:
                menu_dict[option](test_dump)
            elif menu_dict[option]() == "Quit":
                break
        except KeyError:
            print("You have made an invalid choice, try again.")
            page_break()
