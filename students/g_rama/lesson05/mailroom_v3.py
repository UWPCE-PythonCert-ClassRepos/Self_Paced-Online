#!/usr/bin/env python3
def display_donors():
    """Display donors if user enters list"""
    for _ in donors_data.keys():
        print('{}'.format(_))


def thank_you():
    """Send a thank you letter"""
    fullname = input("Enter the Donor name:\n")
    if fullname.isalpha():
        if fullname == str("list"):
            display_donors()
        elif fullname in donors_data.keys():
            amount = float(input("Enter the amount of donation:\n"))
            if amount < 0:
                print("Enter the correct amount with out negitives")
            else:
                donors_data[fullname].append(amount)
                thank_you_letter(fullname, amount)
        else:
            try:
                amount = float(input("Enter the amount of donation:\n"))
                if amount < 0:
                    print("Enter the correct amount with out negitives")
                else:
                    donors_data.update({fullname: [amount]})
                    thank_you_letter(fullname, amount)
            except ValueError:
                print("Enter the correct amount in integer")
    else:
        print("Enter the donor name correctly")


def thank_you_letter(donor_name,amount):
    """Send a thank you letter"""
    print(f"Thank you {donor_name} for donating {amount} dollars generously.")


def donor_details(**data):
    """Print the Donor table"""
    print(f'{"Donor Name":<20} |{"Total Given":>20} |{"Num Gifts":<20} |{"Average Gift":>20.4}\n')
    print('-'*90)
    for row in data:
        print(f'{row:<20} ${sum(data[row]):>20} {len(data[row]):>20} ${(sum(data[row])/len(data[row])):>10.4}\n')


def create_report():
    """Call the function to create the donor details"""
    data = donors_data
    donor_details(**data)


def send_letters():
    """Call the function to create the donor details"""
    data = donors_data
    send_letters_all(**data)


def send_letters_all(**data):
    for _ in data:
        with open('{}'".txt".format(_), 'w') as outfile:
            outfile.write("Dear {},\n"
                          "Thank you for your very kind donation of ${}\n"
                          "It will be put to very good use.\n"
                          "                     Sincerely\n"
                          "                      -The team".format(_,sum(data[_])))


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
    donors_data = {"John": [200, 20, 35.5],
                   "Jeff": [500, 20],
                   "Susan": [1000, 20, 70],
                   "Rob": [250, 20],
                   "Ross": [200]}
    menu_selection(main_prompt, main_dispatch)
