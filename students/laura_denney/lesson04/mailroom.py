#-------------------------------------------------#
# Title: Mail Room Part 2
# Dev:   LDenney
# Date:  October 11, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/11/18, Created File
#   Laura Denney, 10/12/18, Modified File
#   Laura Denney, 10/12/18, Starte Part 2
#-------------------------------------------------#

donor_list = {"john doe":[100, 200],
        "laura denney":[5],
        "bill gates":[4000],
        "samuel jackson":[1, 2, 3],
        "mr. bean": [500, 100]}


main_prompt = '''
What would you like to do today?
1) Send a Thank You
2) Create a Report
3) Send letterss to everyone
4) Quit
Please choose the number of your choice >> '''

thank_you_prompt = '''
\nYou have chosen to Send a Thank You.
1) See List of Current Donors
2) I'm Ready to Thank a Donor
3) Quit this submenu
Please choose the number of your choice >> '''


def quit():
    return 'quit'

def send_letters():
    pass


def send_thank_you():
    while True:
        response = input(thank_you_prompt).lower()
        if response not in sub_choice_dict:
            print("\nThat is not a valid selection. Please choose 1, 2, or 3.")
        elif sub_choice_dict[response]() == 'quit':
            print("\nYou have chosen to leave this submenu.")
            break

    # print("\nYou have chosen to Send a Thank You.")
    # name = "list"
    # while name.lower() == 'list':
    #     print("Please enter the full name of the donor you would like to thank.")
    #     name = input("OR type 'list' to see current donors. >> ")
    #     if name.lower() == "list":
    #         print_list()
    #     else:
    #         donor, amount = check_list(name.lower())
    #         send_email(donor, amount)
    #print("You have successfully sent a Thank You.")

def print_list():
    names = []
    for name in donor_list.keys():
        names += [name.title()]
    strformat = "\nWe have {} current donors: " + ", ".join(["{}"] * len(names))
    print(strformat.format(len(names), *names))

def check_list():
    #Taking in lower case donor name
    name = input("\nPlease enter the full name of the donor you would like to thank: ").lower()
    donation = input("How much money did they donate? (type 100 for $100) >> ")
    #validate donation amount
    try:
        num = float(donation)
    except:
        print("Invalid amount entered, marking donation as $0.")
        num = 0.0
    if name in donor_list:
        print("\n{} is a current donor, we will update their donations.".format(name.title()))
        donor_list[name].append(num)
    else:
        print("\n{} is not a current donor, we will add them to our system.".format(name.title()))
        donor_list[name] = [num]
    send_email(name.title(), num)

    # for donor in donor_list:
    #     if name == donor["name"]:
    #         print("\n{} is a current donor.".format(name.title()))
    #         num = input("How much money did they donate? (type 100 for $100) >> ")
    #         try: #validate donation amount entered is a number
    #             num = float(num)
    #             x.append(num)
    #             return name.title(), num
    #         except:
    #             print("Invalid amount entered, marking donation as $0.")
    #             x.append(0)
    #             return name.title(), 0
    # else: #not a current donor
    #     print("\n{} is not a current donor, we will add them to our list.".format(name.title()))
    #     num = input("How much did they donate? (type 100 for $100) >> ")
    #     try: #validate donation is number
    #         num = float(num)
    #         tabl.append([name, num])
    #         return name.title(), num
    #     except:
    #         print("\nInvalid amount entered, marking donation as $0.")
    #         tabl.append([name, 0])
    #         return name.title(), 0

def send_email(donor, amount):
    print("\nThe email you are sending is as follows:")
    fstring =f'''
    Dear {donor},

    We would like to thank you for your generous donation
    of ${amount}. It will be put to great use!

    Thank you!
    <3 The MailRoom
    '''
    print(fstring)
    print("You have successfully sent a Thank You to {}.".format(donor))

def create_report():
    print("\nYou have chosen to Create a Report.")
    header = '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------'''
    print(header)
    strformat = '{:<26}${:>13}{:^12}${:>13}'
    for row in tabl:
        sumamount = sum(row[1:])
        numberdonations = len(row[1:])
        average = sumamount/numberdonations
        print(strformat.format(row[0].title(),round(sumamount,2), numberdonations, round(average,2 )))


#Main Menu options for user
main_choice_dict = {
    "1": send_thank_you,
    "2": create_report,
    "3": send_letters,
    "4": quit
}

#Sub Menu options for user
sub_choice_dict = {
    "1": print_list,
    "2": check_list,
    "3": quit
}

#Main menu to prompt user
def prompt_user():
    while True:
        response = input(main_prompt)
        if response not in main_choice_dict:
            print("\nThat is not a valid selection. Please choose 1, 2, 3 or 4.")
        elif main_choice_dict[response]() == 'quit':
            print("\nYou have chosen to quit. Have a good day!")
            break

#if __name__ == "__main__":
#    prompt_user()