#!/usr/bin/env python3

# Lesson_3 Activity 4 Mailroom Part 1


def page_break():
    """ Print a separator to distinguish new 'pages'"""
    print("_"*75+"\n")


def menu_page():
    """ Main Menu Page """
    while True:
        try:
            print("Please choose one of the following options(1,2,3):"
                  "\n1. Send a Thank you. \n2. Create a report\n3. Quit")
            option = int(input('--->'))
        except ValueError:
            print("you have made an invalid choice, try again.")
            page_break()
            continue
        if option < 1 or option > 3:
            print("you have made an invalid choice, try again.")
            page_break()
            continue
        return option


def send_thanks():
    """ Send Thanks """
    page_break()
    while True:
        list_names = [item[0] for item in donor_chart]
        amount = []
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
            amount = getAmount()
            print(amount)
            if amount == 'exit':
                break
            else:
                donor_chart[list_names.index(name)][1].append(amount)
        elif name.lower() == 'exit':
            break
        else:
            addname = input("The name you selected is not in the list,"
                            "would you like to add it(y/n)? ")
            if addname[0].lower() == 'y':
                amount = getAmount()
                print(amount)
                if amount == 'exit':
                    break
                else:
                    donor_chart.append([name, [amount]])
            elif addname.lower() == 'exit':
                break
            else:
                print("\nName was not added, try again\n")
                continue
        print("\nDear {} \nThank you for your generous donation of ${:.2f}!!\n"
              "Now all of the kittens will get "
              "to eat this year".format(name, amount))
        break
    return


def getAmount():
    while True:
        try:
            amount = input("How much did they donate: ")
            if str(amount).lower() == 'exit':
                return amount.lower()
            else:
                return float(amount)
        except:
            print("you have made an invalid choice, try again.")
            continue


def getKey(donor_list):
    """Return key for sorted function"""
    return(donor_list[2])


def create_report():
    """ Create Report """
    page_break()
    list_names = [item[0] for item in donor_chart]
    new_list = []
    for donor in donor_chart:
        sum_don = sum(donor[1])
        new_list.append(donor + [sum_don])
    col_lab = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    max_name = max([len(x) for x in list_names])
    max_don = []
    for don in donor_chart:
        max_don.append(max(don[1]))
    max_donl = len(str(max(max_don)))
    max_gift = len(col_lab[2])
    if max_donl < len(col_lab[1]):
        max_donl = len(col_lab[1])
    format_col = "\n{:<" + "{}".format(max_name+5) + "}|{:^"
    format_col += "{}".format(max_donl+5)
    format_col += "}|{:^" + "{}".format(max_gift+5) +
    format_col += "}|{:>" + "{}".format(max_donl+5) + "}"
    print(format_col.format(*col_lab))
    print("-"*len(format_col.format(*col_lab)))
    sorted_list = sorted(new_list, key=getKey, reverse=True)
    for donor in sorted_list:
        num_gifts = len(donor[1])
        avg_gift = sum(donor[1])/num_gifts
        format_item = "{:<" + "{}".format(max_name+5) + "}${:>"
        format_item += "{}".format(max_donl+5) + ".2f}{:>"
        format_item += "{}".format(max_gift+5) + "d} ${:>"
        format_item += "{}".format(max_donl+5) + ".2f}"
        print(format_item.format(donor[0], donor[2], num_gifts, avg_gift))

if __name__ == '__main__':
    donor_chart = [["Justin Thyme", [1, 1, 1]],
                   ["Beau Andarrow", [207.121324, 400.321234, 12345.001234]],
                   ["Crystal Clearwater", [80082]],
                   ["Harry Shins", [1.00, 2.00, 3.00]],
                   ["Bob Zuruncle", [0.53, 7.00]],
                   ["Al Kaseltzer", [1010101, 666.00]],
                   ["Joe Somebody", [25]]]
    option = 0
    while option != 3:
        page_break()
        option = menu_page()
        if option == 1:
            send_thanks()
        elif option == 2:
            create_report()
