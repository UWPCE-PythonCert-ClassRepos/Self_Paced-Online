#!/usr/bin/env python3


# initial list of donors
lst_Donors = [{"donor name": "Lionel Messi", "total donations": 1000000.00, "number donations": 5, "avg donation": 20000.00},
              {"donor name": "Thierry Henry", "total donations": 500, "number donations":1, "avg donation": 500},
              {"donor name": "Michael Jordan", "total donations": 45000, "number donations": 3, "avg donation": 15000},
              {"donor name": "Kobe Bryant", "total donations": 8000, "number donations": 2, "avg donation": 4000}]


def send_thank_you():
    # used to add new donors
    new_donor = []

    # function creates a thank you email to current and new donors added to the list
    # add new donors and donations
    # print the names of the current donor if 'list' is input by the user
    print('\n-----------------------------------------------------')
    view_donors = input("If you would like to see a list of donors please type 'list' or any key to continue. ")
    if view_donors == 'list':
        print()
        print("Below are the list of donors:")
        for x in lst_Donors:
            print(x["donor name"])
        print('----------------------------')

    # input donor name to print an email
    donor_first_name = input("Please input the first name of the donor. ")
    donor_last_name = input("Please input the last name of the donor. ")
    donor_full_name = donor_first_name.capitalize() + " " + donor_last_name.capitalize()
    print('-----------------------------------------------------')
    print()

    # prints an email if the donors name is currently in the list
    for x in lst_Donors:
        if x["donor name"] == donor_full_name:
            str_donation_choice = input("Would you like to add another donation? (yes or no) ")
            print('-----------------------------------------------------')
            print()
            if str_donation_choice == 'yes':
                donate_more = float(input("How much would you like to donate? "))
                total_donations = x["total donations"] + donate_more
                count_donations = x["number donations"] + 1
                avg_donation = total_donations/count_donations
                x["total donations"] = total_donations
                x["number donations"] = count_donations
                x["avg donation"] = '{:.2f}'.format(avg_donation)

            email = "Dear {a},\n\nThank you for your generous donations of ${b:.2f} to our charity.\n".format(
                a=x["donor name"],b=x["total donations"])
            print(email)
            break

    # if the donor's name is not in the list it adds the name to the list and ask for a donation amount
    # then prints an email to the new donor
    else:

        print("Donor not found")
        new_donation_amount = None
        boolValid = False
        while boolValid != True:
            try:
                new_donation_amount = float(input("Please input a donation "
                                                  "amount in order to add the donor to the list. "))
            except ValueError as e:
                print(e)
                print("Please input a valid number")
            else:
                boolValid = True
        new_donor.append({"donor name": donor_full_name, "total donations": new_donation_amount, "number donations": 1,
                          "avg donation": new_donation_amount})
        lst_Donors.extend(new_donor)
        print('-----------------------------------------------------')
        for x in lst_Donors:
            if x["donor name"] == donor_full_name:
                email = "Dear {a},\n\nThank you for your generous donations of ${b:.2f} to our charity.\n".format(
                    a=x["donor name"],b=x["total donations"])
                print(email)
    print('-----------------------------------------------------')


def sort_list(lst_Donors):
    # used to sort the donor list by the total donations column

    return lst_Donors["total donations"]


def create_report():
    # creates a report of the the donors
    # headers used in table
    print()
    lst_Header = [["Donor Name", "| Total Donation(s)", "| # of Donations", "| Avg Donation"]]

    for x in lst_Header:
        print('{:<25}{:<20}{:<17}{:<15}'.format(*x))
    print("----------------------------------------------------------------------------")
    for x in sorted(lst_Donors,key=sort_list, reverse= True):
        print('{:<25} $ {:<20}{:^14} $ {:<15}'.format(*x.values()))


def send_letter_all():
    print('\n----------------------------------------------')
    file = ()
    # creates a letter to every donor by writing them to separate text files
    for x in lst_Donors:
        # opens or creates a new text file for writing based on the donor name
        file = open('{a}.txt'.format(a = x['donor name']), 'w')

        # writes a thank you letter to the text file
        file.write('Dear {a},\n\nThank you for your generous donation(s) of ${b:.2f} to our charity.'.format(
            a=x['donor name'], b=x['total donations']))
        print('Letter sent to  {a}'.format(a=x['donor name']))

    #closes and saves the file
    file.close()
    print('----------------------------------------------\n')


print("Welcome to the Charity Mail Room")
print("------------------------------------------------------------------------")

str_choice = 0
# ****Input/Output****
while str_choice != 4:
    # Option menu

    print("""
    Menu of Options
    1) Send Thank You Note
    2) Create Report
    3) Send Letter to Everyone
    4) Exit Program
    """)

    # dictionary used to run different functions of the program
    User_Selection = {1: send_thank_you, 2: create_report, 3: send_letter_all}

    # try/except block to make sure the user inputs a valid option
    try:
        str_choice = int(input("Which option would you like to perform? Input a number [1 to 4] "))
        if str_choice in (1,2,3):
            # runs a function selection from the dictionary
            User_Selection[str_choice]()
        elif str_choice == 4:
            print("\nExiting Program")
        else:
            raise Exception
    except Exception:
        print("Please input a valid option: 1, 2, 3, or 4")


if __name__ == "__main__":
    print()
