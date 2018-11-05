#-------------------------------------------------#
# Title: Mail Room Part 3
# Dev:   LDenney
# Date:  October 11, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/11/18, Created File
#   Laura Denney, 10/12/18, Modified File
#   Laura Denney, 10/12/18, Started Part 2
#   Laura Denney, 10/12/18, Finished Part 2
#   Laura Denney, 10/12/18, Started MailRoom Part 3
#-------------------------------------------------#

donor_list = {"john doe":[100, 200],
        "laura denney":[5],
        "bill gates":[4000],
        "samuel jackson":[x for x in range(1,4)],
        "mr. bean": [500, 100]}

main_prompt = '''
What would you like to do today?
1) Send a Thank You
2) Create a Report
3) Send letters to everyone
4) Quit
Please choose the number of your choice >> '''

thank_you_prompt = '''
You have chosen to Send a Thank You.
1) See List of Current Donors
2) I'm Ready to Thank a Donor
3) Quit this submenu
Please choose the number of your choice >> '''


def quit():
    return 'quit'

def send_letters():
    print("\nYou have chosen to send letters to everyone.")
    total_donor = sort_by_amount()
    for each_donor in total_donor:
        amount = each_donor[0]
        donor = each_donor[1].title()
        #Name formatting for one word names like 'Cher' vs normal full names
        if " " in donor:
            first_last = donor.split(" ")
        else: first_last = [donor]
        if len(first_last) == 1:
            first = first_last[0]
            last = ""
        else:
            first = first_last[0]
            last = first_last[1]
        send_email(donor, amount, "{}_{}.txt".format(first, last))
    print("\nLetters have been successfully sent to every donor.")
    print("A copy of that letter is now saved in your current directory.")

#creates a table of donors sorted by total amount donated
def sort_by_amount():
    sorted_tuple = sorted([(sum(value),key) for (key,value) in donor_list.items()], reverse = True)
    return sorted_tuple

def send_thank_you():
    while True:
        response = input(thank_you_prompt).lower()
        if response not in sub_choice_dict:
            print("\nThat is not a valid selection. Please choose 1, 2, or 3.")
        elif sub_choice_dict[response]() == 'quit':
            print("\nYou have chosen to leave this submenu.")
            break

#adding list comprehension here
def print_list():
    names = [name.title() for name in donor_list.keys()]
    strformat = "\nWe have {} current donors: " + ", ".join(["{}"] * len(names))
    print(strformat.format(len(names), *names))

def check_list():
    name = input("\nPlease enter the full name of the donor you would like to thank: ").lower()
    donation = input("How much money did they donate? (type 100 for $100) >> ")
    #validate donation amount
    try:
        num = float(donation)
    except ValueError:
        print("\nERROR: Invalid donation amount entered, marking donation as $0.")
        num = 0.0
    if name in donor_list:
        print("\n{} is a current donor, we will update their donations.".format(name.title()))
        donor_list[name].append(num)
    else:
        print("\n{} is not a current donor, we will add them to our system.".format(name.title()))
        donor_list[name] = [num]
    send_email(name.title(), num)

#modified to either print to screen or disk
def send_email(donor, amount, dest = 0):
    fstring =f'''
    Dear {donor},

    We would like to thank you for your generous donation
    of ${amount}. It will be put to great use!

    Thank you!
    <3 The MailRoom
    '''
    if dest == 0:
        print("The email you are sending is as follows:")
        print(fstring)
        print("You have successfully sent a Thank You to {}.".format(donor))
    else:
        with open(dest, 'w') as outfile:
            outfile.write(fstring)

def create_report():
    report_list = sort_by_amount()
    print("\nYou have chosen to Create a Report.")
    header = '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------'''
    print(header)
    strformat = '{:<26}${:>13}{:^12}${:>13}'
    for donor in report_list:
        total_donations = float(donor[0])
        number_donations = len(donor_list[donor[1]])
        average = total_donations/number_donations
        print(strformat.format(donor[1].title(),round(total_donations,2), number_donations, round(average,2 )))


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

if __name__ == "__main__":
    prompt_user()