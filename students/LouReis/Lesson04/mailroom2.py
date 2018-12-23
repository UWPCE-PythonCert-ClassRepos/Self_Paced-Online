#!/usr/bin/env python3
# mailroom2.py
# Coded by LouReis

"""
Write a small command-line script called mailroom.py.
It should have a data structure that holds a list of your donors and a history
of the amounts they have donated. This structure should be populated at first
with at least five donors, with between 1 and 3 donations each.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”)

Report should look like the following:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Joe Donor                  $  653784.49           2  $   326892.24
John Rich                  $   16396.10           3  $     5465.37
Sally Neighbor             $     877.33           1  $      877.33
Mack Jack                  $     708.42           3  $      236.14

"""

# donations = ['Robin Hood', 1500000, 3, 500000, 'Tycoon Reis', 75000000, 3, 25000000, 'Howie Long', 100000, 1, 100000, 'Joe Neighbor', 50, 2, 25, 'Rick Retiree', 1.00, 2, 0.50]
# Data structure in global namespace to store all donations & donors.
donations = ['Robin Hood', 50000, 'Tycoon Reis', 25000000, 'Howie Long', 100000, 'Joe Neighbor', 25, 'Rick Retiree', 0.50, 'Robin Hood', 50000, 'Tycoon Reis', 25000000, 'Joe Neighbor', 25, 'Rick Retiree', 0.50, 'Robin Hood', 50000, 'Tycoon Reis', 25000000]
donor_list = ['Robin Hood', 'Tycoon Reis', 'Howie Long', 'Joe Neighbor', 'Rick Retiree']

# The following function takes lists as input then returns and sorts the output by max amount donated.
def sort_max(donor_name, donor_amount, donor_count, donor_average):
    # temp_donors is a temporary data structure used & destroyed for sorting purposes.
    temp_donors = []
    for n, item in enumerate(donor_name):
        temp_donors.append(donor_name[n])
    print('{:25} | {:^13} | {:^13} |   {:>13}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('---------------------------------------------------------------------------')
    print()
    while len(donor_amount) != 0:
        max = 0
        max_index = 0
        for z, item_c in enumerate(donor_amount):
            if item_c > max:
                max = item_c
                max_index = z
        print('{:25} ${:>15,.2f} {:>15} ${:>15,.2f}'.format(temp_donors[max_index], donor_amount[max_index], donor_count[max_index], donor_average[max_index]))
        del temp_donors[max_index]
        del donor_amount[max_index]
        del donor_count[max_index]
        del donor_average[max_index]

# The following function takes the donation list and calculates & stores totals & averages
def total(list, donors):
    donor_amount = []
    donor_count = []
    donor_average = []
    for x, item_a in enumerate(donors):
        count = 0
        amount = 0
        for y, item_b in enumerate(list):
            if item_b == donors[x]:
                name = item_a
                count = count + 1
                amount = amount + list[y+1]
        # The below print statement was for testing unsorted output.
        # print('{:25} ${:>15} {:>15} ${:>15}'.format(name, amount, count, amount/count))
        donor_amount.append(amount)
        donor_count.append(count)
        donor_average.append(amount/count)
    print()
    sort_max(donors, donor_amount, donor_count, donor_average)

# Below is the main menu function that continues prompting until quit.
def main_menu(main_prompt,menu_options_dict):
    while True:
        response = input(main_prompt)
        if menu_options_dict[response]() == "Quit":
            break

# Below are the 4 menu options that are declared in the dict.
def option_one():
    print('\nYou Chose Option 1\n\n')
    print('DONATION SUMMARY REPORT\n\n')
    total(donations,donor_list)

def option_two():
    print('\nYou Chose Option 2\n\n')
    print('Create a Thank You Letter\n\n')
    donor = 'L'
    while donor == 'L':
        donor=input("Enter the full name of the Donor (Type 'L' for a donor list):")
        if donor == 'L':
            print(donor_list)
    if donor not in donor_list:
        print("You have entered a new donor:", donor)
        amount = input("Please enter a donation amount '0.00':")
        amount = float(amount)
        donor_list.append(donor)
        donations.append(donor)
        donations.append(amount)
    elif donor in donor_list:
        print("You have entered an existing donor:", donor)
        amount = input("Please enter the donation amount:")
        amount = float(amount)
        donations.append(donor)
        donations.append(amount)
    print_letter(donor,amount)

def option_three():
    print('\nYou Chose Option 3\n\n')
    print('Send a Thank You Letter to Everyone.\n')
    for item in (donor_list):
        filename = item.replace(" ","") + '.txt'
        outfile = open(filename, 'w')
        outfile.write(f"\n\nSubject: Donation\n\nDear {item},\n\nThank you for your donation, it will be used to help meet our goals.")
        outfile.write("\nWe will welcome any future donations and appreciate your support.")
        outfile.write("\n\n\nSincerely,\n\nMDTS Staff\n\n\n")
        outfile.close()
    print("\n\nA Letter has been created for each donor and stored in a text file.\n\n")
    return "Menu"

def option_four():
    print('\nYou Chose Option 4\n\n')
    print('Thanks for using MDTS, Goodbye!\n')
    return "Quit"

# Below is the dict defining the menu options.
menu_options_dict = {
    "1": option_one,
    "2": option_two,
    "3": option_three,
    "4": option_four,
}

# The following function prints out an email when the user enters a donation.
def print_letter(donor, amount):
    message = "We will welcome any future donations and appreciate your support."
    letter_dict = {'donor_name': donor, 'amount_donated': amount}
    print('\n\nSubject: Donation\n\nDear {donor_name},\n\nThank you for your ${amount_donated:,.2f} donation, it will be used to help meet our goals.'.format(**letter_dict))
    print(message,'\n\nSincerely,\n\nMDTS Staff\n\n\n')

main_prompt = ("\nMailroom Donation Tracking System - MDTS\n\nMAIN MENU\n\n""Please choose from the following Menu Options:\n\n"
"1 - Generate A Donation Report\n\n""2 - Create a Thank You Note\n\n""3 - Send a Thank You Letter to Everyone\n\n""4 - Quit Program\n\n""Enter Menu Option: ")

# The following function & dict could be used if it was desired to have an additonal sub menu off of the main menu.
# The main program does not implement a sub menu.
#
# def sub_menu():
#     main_menu(sub_menu_prompt, sub_menu_dispatch)sub_menu_prompt = ("\nSub-menu Options\n")
# sub_menu_dispatch = {"L": print_donors}

main_menu(main_prompt,menu_options_dict)

# Put your main interaction into an if __name__ == '__main__' block.
if __name__ == '__main__':
    main_menu(main_prompt,menu_options_dict)
