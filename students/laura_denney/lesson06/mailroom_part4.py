#-------------------------------------------------#
# Title: Mail Room Part 4
# Dev:   LDenney
# Date:  November 7, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 10/11/18, Created File
#   Laura Denney, 10/12/18, Modified File
#   Laura Denney, 10/12/18, Started Part 2
#   Laura Denney, 10/12/18, Finished Part 2
#   Laura Denney, 10/31/18, Started MailRoom Part 3
#   Laura Denney, 11/7/18, Started MailRoom Part 4
#-------------------------------------------------#

donor_list = {"john doe":[100.50, 200.00],
        "laura denney":[5.00],
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
    total_letters_sent = 0
    for each_donor in total_donor:
        amount = each_donor[0]
        donor = each_donor[1].title()
        #Name formatting for one word names like 'Cher' vs normal full names
        first_last = donor.split(" ")
        if len(first_last) == 1:
            first = first_last[0]
            last = ""
        else:
            first = first_last[0]
            last = first_last[1]
        total_letters_sent += send_email(donor, amount, "{}_{}.txt".format(first, last))
    print(f"\nA total of {total_letters_sent} letters have been successfully sent to our donors.")
    print("A copy of those letters are now saved in your current directory.")

#creates a table of donors sorted by total amount donated
def sort_by_amount():
    sorted_tuple = sorted([(sum(value),key) for (key,value) in donor_list.items()], reverse = True)
    return sorted_tuple

def send_thank_you():
    while True:
        try:
            response = input(thank_you_prompt).lower()
            if sub_choice_dict[response]() == 'quit':
                print("\nYou have chosen to leave this submenu.")
                break
        except KeyError:
            print("\nThat is not a valid selection. Please choose 1, 2, or 3.")

#adding list comprehension here
def print_list():
    # names = [name.title() for name in donor_list.keys()]
    # strformat = "\nWe have {} current donors: " + ", ".join(["{}"] * len(names))
    # print(strformat.format(len(names), *names))
    print(get_list())

def get_list():
    names = [name.title() for name in donor_list.keys()]
    strformat = "\nWe have {} current donors: " + ", ".join(["{}"] * len(names))
    return strformat.format(len(names), *names)

def thank_a_donor():
    name = input("\nPlease enter the full name of the donor you would like to thank: ").lower()
    donation = input("How much money did they donate? (type 100 for $100) >> ")
    donation = validate_donation(donation)
    print(check_current_donor(name, donation))
    print("The email you are sending is as follows:")
    print(send_email(name.title(), donation))
    print("You have successfully sent a Thank You to {}.".format(name.title()))

def check_current_donor(name, donation):
    if name in donor_list:
        donor_list[name].append(donation)
        return "\n{} is a current donor, we will update their donations.".format(name.title())

    else:
        donor_list[name] = [donation]
        return "\n{} is not a current donor, we will add them to our system.".format(name.title())


def validate_donation(donation):
    #validate donation amount
    try:
        num = float(donation)
    except ValueError:
        print("\nERROR: Invalid donation amount entered, marking donation as $0.")
        num = 0.0
    return num

#modified to either print to screen or disk
def send_email(donor, amount, dest = 0):
    fstring =f'''
    Dear {donor},

    We would like to thank you for your generous donation
    of ${amount:.2f}. It will be put to great use!

    Thank you!
    <3 The MailRoom
    '''
    if not dest:

        return fstring

    else:
        with open(dest, 'w') as outfile:
            outfile.write(fstring)
        return 1

def create_report():
    report_list = sort_by_amount()
    print("\nYou have chosen to Create a Report.")
    print(create_string_report(report_list))

def create_string_report(report_list = []):
    report = '''
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------'''
    strformat = '\n{:<26}${:>13.2f}{:^12}${:>13.2f}'
    for donor in report_list:
        total_donations = donor[0]
        number_donations = len(donor_list[donor[1]])
        average = total_donations/number_donations
        report +=  strformat.format(donor[1].title(),total_donations, number_donations, average)
    return report

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
    "2": thank_a_donor,
    "3": quit
}

#Main menu to prompt user
def prompt_user():
    while True:
        try:
            response = input(main_prompt)
            if main_choice_dict[response]() == 'quit':
                print("\nYou have chosen to quit. Have a good day!")
                break
        except KeyError:
            print("\nThat is not a valid selection. Please choose 1, 2, 3 or 4.")

if __name__ == "__main__":
    prompt_user()