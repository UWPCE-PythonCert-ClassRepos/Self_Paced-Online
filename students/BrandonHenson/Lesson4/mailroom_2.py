# Brandon Henson
# 4/12/18
# Lesson 04 mailroom_2.py
donor_history = {'Brandon Henson': [1005.49, 3116.72, 5200],
                    'Alicia Henson': [21.47, 1500],
                    'Michael Green': [2400.54],
                    'Brandon Henson Jr': [355.42, 579.31],
                    'Kaiya Henson': [636.9, 850.13, 125.23]}


def email_all():
    for key, values in donor_history.items():
        filename = str(key)+'.txt'
        fileobj = open(filename, 'w')
        total = sum(values)
        numgifts = len(values)
        fileobj.write("Dear {}\nThank you for your {} generous donations \
totaling ${}\nThe money will be put to good use.\n\n\
        Sincerely, \n                -The Team".format(key, numgifts, total))
        fileobj.close()

    main_menu()


def main_menu():
    arg_dict = {
        '1': menu_1,
        '2': menu_2,
        '3': email_all,
        '4': exit
    }

    prompt = '\nSelect an option:\n' \
             '[1] Send a Thank You\n' \
             '[2] Create a Report\n' \
             '[3] Send letters to everyone\n' \
             '[4] Exit\n' \

    menu_selection(prompt, arg_dict)


def menu_selection(prompt, arg_dict):
    try:
        while True:
            response = input(prompt)
            arg_dict[response]() == ''
    except KeyError as e:
        print("Enter 1,2,3, or 4")
# If the user (you) selects Send a Thank You, prompt for a Full Name


def menu_1():
    fullname = input("Enter a full name or 'list' to view all\n")
    if fullname.lower() == 'list':
        print(name_list)
        menu_1()
    elif str(fullname) in donor_history:
        amount = float(input("Donation amount? \n"))
        newvalue = donor_history.get(fullname) + [amount]
        donor_history[fullname] = newvalue
        print("Dear {}\nThank you for your generous donation of ${}\nIt will \
 be put to good use.\n\n Sincerely,\n\
        -The Team".format(fullname, amount))
    elif str(fullname) not in donor_history:
        amount = float(input("Donation amount? \n"))
        donor_history[fullname] = amount
        print("Dear {}\nThank you for your generous donation\
 of ${}\nIt will be put to good use.\n\n Sincerely,\n\
        -The Team".format(fullname, amount))
    main_menu()


def menu_2():
    print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
    print("---------------------------------------------------------------\n")
    for key, values in donor_history.items():
        total = sum(values)
        numgifts = len(values)
        avgifts = total/numgifts
        print(f'{str(key):20s}     ${total:8n} {numgifts:10n}     ${avgifts:8n}')
    main_menu()

if __name__ == '__main__':
    main_menu()
