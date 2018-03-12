#!/usr/bin/env python3


# initial list of donors
lst_donors = [{"donor name": "Lionel Messi", "total donations": 1000000.00, "number donations": 5, "avg donation": 20000.00},
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
        for x in lst_donors:
            print(x["donor name"])
        print('----------------------------')

    while True:

        # validates to make sure the user inputs a first and last name
        try:
            # input donor name to print an email
            donor_first_name = input("Please input the first name of the donor. ")
            donor_last_name = input("Please input the last name of the donor. ")
            if donor_first_name == "" or donor_last_name == "":
                raise Exception
        except Exception:
            print("\nPlease input a first and last name")
            print()
        else:
            break

    donor_full_name = donor_first_name.capitalize() + " " + donor_last_name.capitalize()
    print('-----------------------------------------------------')
    print()

    # prints an email if the donors name is currently in the list
    for x in lst_donors:
        if x["donor name"] == donor_full_name:

            while True:

                # raise exception if the user inputs anything other than 'yes' or 'no'
                try:
                    str_donation_choice = input("Would you like to add another donation? (yes or no) ")
                    if str_donation_choice not in ("yes","no"):
                        raise Exception
                except Exception:
                    print("Please input 'yes' or 'no'")
                else:
                    break

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
                print('-----------------------------------------------------\n')
            email = "Dear {donor_name},\n\nThank you for your generous donations of ${donations:.2f} " \
                    "to our charity.\n".format(donor_name=x["donor name"],donations=x["total donations"])
            print(email)
            break

    # if the donor's name is not in the list it adds the name to the list and ask for a donation amount
    # then prints an email to the new donor
    else:

        print("Donor not found")
        new_donation_amount = None

        while True:

            # raises an exception if the user doesnt input a valid number
            try:
                new_donation_amount = float(input("Please input a donation "
                                                  "amount in order to add the donor to the list. "))
            except ValueError as e:
                print(e)
                print("Please input a valid number")
            else:
                break
        new_donor.append({"donor name": donor_full_name, "total donations": new_donation_amount, "number donations": 1,
                          "avg donation": new_donation_amount})
        lst_donors.extend(new_donor)
        print('-----------------------------------------------------')
        for x in lst_donors:
            if x["donor name"] == donor_full_name:
                email = "Dear {donor_name},\n\nThank you for your generous donations of ${donations:.2f} " \
                        "to our charity.\n".format(donor_name=x["donor name"],donations=x["total donations"])
                print(email)
    print('-----------------------------------------------------')


def sort_list(lst_donors):
    # used to sort the donor list by the total donations column

    return lst_donors["total donations"]


def create_report():
    # creates a report of the the donors
    # headers used in table
    print()
    lst_headers = [["Donor Name", "| Total Donation(s)", "| # of Donations", "| Avg Donation"]]

    for x in lst_headers:
        print('{:<25}{:<20}{:<17}{:<15}'.format(*x))
    print("----------------------------------------------------------------------------")
    for x in sorted(lst_donors,key=sort_list, reverse= True):
        print('{:<25} $ {:<20}{:^14} $ {:<15}'.format(*x.values()))


def send_letter_all():
    print('\n----------------------------------------------')
    # creates a letter to every donor by writing them to separate text files
    for x in lst_donors:

        # opens or creates a new text file for writing based on the donor name
        with open('{file_name}.txt'.format(file_name=x['donor name']), 'w') as f1:

            # writes a thank you letter to the text file
            f1.write('Dear {donor_name},\n\nThank you for your generous donation(s) of ${donations:.2f} to our charity.'.format(
                donor_name=x['donor name'], donations=x['total donations']))
            print('Letter sent to  {a}'.format(a=x['donor name']))

    print('----------------------------------------------\n')


def main():
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
        user_selection = {1: send_thank_you, 2: create_report, 3: send_letter_all}

        # try/except block to make sure the user inputs a valid option
        try:
            str_choice = int(input("Which option would you like to perform? Input a number [1 to 4] "))
            if str_choice in user_selection:
                # runs a function selection from the dictionary
                user_selection[str_choice]()
            elif str_choice == 4:
                print("\nExiting Program")
            else:
                raise Exception
        except Exception:
            print("Please input a valid option: 1, 2, 3, or 4")


if __name__ == "__main__":
    main()
