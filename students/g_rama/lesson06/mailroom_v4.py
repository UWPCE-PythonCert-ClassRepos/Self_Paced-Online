#!/usr/bin/env python3
donors_data = {"John": [200, 20, 35.5],
               "Jeff": [500, 20],
               "Susan": [1000, 20, 70],
               "Rob": [250, 20],
               "Ross": [200]}


def display_donors():
    """Display donors if user enters list"""
    for name in donors_data.keys():
        print('{}'.format(name))


def amount_input():
    amount = float(input("Enter the amount of donation:\n"))
    return amount


def fullname_input():
    fullname = input("Enter the Donor name:\n")
    return fullname


def amount_validate(amount):
    if amount < 0:
        print("Enter the correct amount with out negitives")
    else:
        return True


def update_data_print_thanks(amount, fullname):
    if amount_validate(amount):
        donors_data[fullname].append(amount)
        thank_you_letter(fullname, amount)


def add_data_print_thanks(amount, fullname):
    if amount_validate(amount):
        donors_data.update({fullname: [amount]})
        thank_you_letter(fullname, amount)


def thank_you():
    """Send a thank you letter"""
    fullname = fullname_input()
    if fullname.isalpha():
        if fullname == str("list"):
            display_donors()
        elif fullname in donors_data.keys():
            amount = amount_input()
            update_data_print_thanks(amount, fullname)
        else:
            try:
                amount = amount_input()
                add_data_print_thanks(amount, fullname)
            except ValueError:
                print("Enter the correct amount in integer")
    else:
        print("Enter the donor name correctly")


def thank_you_letter(donor_name,amount):
    """Send a thank you letter"""
    print(f"Thank you {donor_name} for donating {amount} dollars generously.")
    return f"Thank you {donor_name} for donating {amount} dollars generously."


def donor_details(**data):
    """Print the Donor table"""
    print(f'{"Donor Name":<20} |{"Total Given":>20} |{"Num Gifts":<20} |{"Average Gift":>20.4}')
    print('-'*90)
    print(data.items())
    sorted_d = sorted(data.items(), key=lambda x: sum(x[1]), reverse=True)
    print(sorted_d)
    for row in sorted_d:
        print(f'{row[0]:<20} ${sum(row[1]):>20} {len(row[1]):>20} ${(sum(row[1])/len(row[1])):>10.4}')
        # return f'{row:<20} ${sum(data[row]):>20} {len(data[row]):>20} ${(sum(data[row])/len(data[row])):>10.4}\n'


def create_report():
    """Call the function to create the donor details"""
    data = donors_data
    donor_details(**data)


def send_letters():
    """Call the function to create the donor details"""
    data = donors_data
    send_letters_all(**data)


def send_letters_all(**data):
    for name in data:
        with open('{}'".txt".format(name), 'w') as outfile:
            outfile.write("Dear {},\n"
                          "Thank you for your very kind donation of ${}\n"
                          "It will be put to very good use.\n"
                          "                     Sincerely\n"
                          "                      -The team".format(name,sum(data[_])))


def menu_selection(prompt, dispatch_dict):

    while True:
        try:
            response = input(prompt)
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print("Please enter key as 1 2 3 or 4")


def exit_menu():
    print("Quitting this menu")
    return "exit menu"


main_prompt = ("1 - Send a Thank You\n"
               "2 - Create a Report\n"
               "3 - Send letters to everyone\n"
               "4 - Quit\n")
main_dispatch = {"1": thank_you,
                 "2": create_report,
                 "3": send_letters,
                 "4": exit_menu,
                 }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
