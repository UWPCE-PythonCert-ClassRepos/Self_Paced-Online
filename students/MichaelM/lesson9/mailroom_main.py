# !/usr/bin/env python3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson9
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson9
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson9

# git add mailroom_main.py
# git add mailroom_main.py
# git add test_mailroom.py

# git add mailroom_classes.py
# git commit mailroom_classes.py
# git commit test_mailroom.py

# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson9/
# click Pull request > new pull request

from lesson9 import mailroom_classes as mr
import importlib
importlib.reload(mr)
import os

usr_directory = "{}/tmp/".format(os.getcwd())

# >> Menu Selection
def main(prompt, menu):
    while True:
        response = input(prompt)
        if response.lower() not in menu:
            print(f"'{response}' not available. Please make a valid choice.\n")
        elif response.lower() in menu:
            if response.lower() == "ty":
                distinct_donor_list = list(mr.Mailroom.esteemed_donors_dict.keys())
                user_response_ty = input(
                    "- type 'list' to view a list of donors\n- type 'new' to "
                    "add a donor to the list\n- type in an existing donor to add a new donation >> ")
                if user_response_ty == "list":
                    print(mr.Mailroom.esteemed_donors_dict)
                    for item in distinct_donor_list:
                        print(item.title())
                elif user_response_ty == "new":
                    d = mr.Donor()
                    d.donor_name = input("name? >> ").lower()
                    d.donation_amt = float(input("Donation amount? >> "))
                    d.esteemed_donors_dict[d.donor_name] = [d.donation_amt]
                    letter = mr.Mailroom.donor_letters("new", d.donor_name, d.donation_amt, 0.0)
                    print(letter)
                elif user_response_ty.lower() in distinct_donor_list:
                    print("{} found.".format(user_response_ty.title()))
                    d = mr.Donor()
                    d.donor_name = user_response_ty
                    d.donation_amt = float(input("Donation amount? >> "))
                    d.add_donation(d.donor_name, d.donation_amt)
                    sum_amt = float(d.donor_total(d.donor_name))
                    print("{0:,.2f} added to {1}'s total. "
                          "{1}'s total contribution is {2:,.2f}".format(d.donation_amt,
                                                                        d.donor_name.title(),
                                                                        sum_amt))
                    letter = mr.Mailroom.donor_letters("existing_donor", d.donor_name, d.donation_amt, sum_amt)
                    print()
                    print(letter)
            elif response.lower() == "cr":
                donors = mr.Donors()
                summed_donor_list = donors.sum_donors()
                print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(
                    name=mr.Mailroom.esteemed_donors_headers[0],
                    total_donation=mr.Mailroom.esteemed_donors_headers[1],
                    donation_cnt=mr.Mailroom.esteemed_donors_headers[2],
                    ave_donation=mr.Mailroom.esteemed_donors_headers[3]))
                tmp_donor_list = sorted(summed_donor_list, key=lambda x: x[1], reverse=True)
                [print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(name=row[0],
                                                                                                total_donation=row[1],
                                                                                                donation_cnt=row[2],
                                                                                                ave_donation=row[3])
                       ) for row in tmp_donor_list]
            elif response.lower() == "s":
                d = mr.Donors()
                d.tmp_directory = usr_directory
                d.print_letters(d.tmp_directory)
            elif response.lower() == "q":
                break


# >> Main Prompt
main_prompt = ("-Main Menu-\n"
               "Do you want to:\n"
               "Send a Thank You -ty\n"
               "Create a Report -cr\n"
               "Send Thank You Letters - s\n"
               "Quit -q\n"
               " >> ")

# >> Main Menu
main_menu = {"cr", "q", "s", "ty"}
if __name__ == "__main__":
    main(main_prompt, main_menu)
