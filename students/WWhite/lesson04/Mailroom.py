#!/usr/bin/env python3

# -------------------------------------#
# Desc: Mailroom Part 1
# Dev: Will White
# Date: 5/8/2018
# ChangeLog: (When,Who,What)
# -------------------------------------#


list_donations = [["bill gates", 25000.00, 3], ["monet holt", 50000.00, 2], ["jeff bezos", 123500.09, 3],
                  ["john wick", 120000.00, 2], ["john snow", 10.56, 1]]  # List of donors


def menu_options():  # Function to run the menu options
    user_input = input('''
Please enter a number from the following options:

[1] Send a Thank You
[2] Create a Report
[3] Send Letters to Everyone
[4] Quit the Program

''')
    return user_input  # Function returns user_input


def prompt_for_name():  # Function to prompt the user for a name
    donor_name = input("Please input the donor's name, or type 'list' to see a list of donor names: \n")
    while donor_name == 'list':  # If user inputs "list", program will print a list of current donors
        for i in list_donations:
            print(i[0].title())
        donor_name = input("\nPlease input the donor's name: \n").lower()
    return donor_name  # Function returns the donor's name


def print_letter(donor_name, donation_amount):
    dict_donor_info = {'name': donor_name.title(), 'donation': donation_amount}
    print('''
Dear {name},

Thank you for your donation of {donation}, it is very much appreciated.

Kind Regards,
Your Favorite Local Charity
'''.format(**dict_donor_info))  # Thank you email with formatting to include donor name and amount


def add_donation(donor_name):  # Function for the user to add a donation
    index_val = -1
    for new_index_val, name_of_donor in enumerate(list_donations[0]):  # Determine whether the donor exists in the current list
        if name_of_donor == donor_name:
            index_val = new_index_val

    donation_amount = float(input("Please input the donation amount: "))
    if index_val > -1:  # If donor exists, add the donation amount to total donations and add one to the number of donations
        list_donations[index_val][1] += donation_amount
        list_donations[index_val][2] += 1
    else:  # If donor does not exist, create a new list for them and add it to the broader list
        new_donor_list = [donor_name, donation_amount, 1]
        list_donations.append(new_donor_list)

    print_letter(donor_name, donation_amount)


def create_a_report():  # Function to create a report of all the current donor info
    title_header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print('{:<10}{:>20}{:>20}{:>20}'.format(*title_header))
    print('----------------------------------------------------------------------')
    sorted_list = sorted(list_donations, key=lambda x: x[1], reverse=True)

    for i in sorted_list:
        i[0] = i[0].title()
        print('{:<10}{:>20.2f}{:>20}{:>20.2f}'.format(i[0], i[1], i[2], (i[1] / i[2])))


def send_letters():
    for i in list_donations:
        txt_file = open("{}.txt".format(i[0]), 'w')
        txt_file.write(print_letter(i[0],i[1]))
        txt_file.close()


switch_func_dict = {
    0: menu_options,
    1: prompt_for_name,
    2: add_donation,
    3: create_a_report,
    4: send_letters()
}


if __name__ == "__main__":  # If this is the main file, run the below

    while True:
        str_input = menu_options()  # Run the menu options function and save the input
        if str_input == '1':  # If user entered 1, get the name and run the add_donation function
            name = switch_func_dict.get(1)()
            switch_func_dict.get(2)(name)
            break

        elif str_input == '2':  # If the user enters 2, create a report and then return to the original report
            switch_func_dict.get(3)()

        elif str_input == '3':  # If the user enters 3, create letters for everyone, saved in individual text files
            switch_func_dict.get(4)()

        else:  # If the user enters anything else, quit the program
            break

    print("Thank you, the program will now exit")
    raise SystemExit  # Exit the program