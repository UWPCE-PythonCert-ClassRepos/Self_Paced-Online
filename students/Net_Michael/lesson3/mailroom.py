#!/usr/bin/env python
# coding: utf-8

import os

# update the list of donors and donation
# donor_name is the list of donors
# donation is the amount of donation of each donor
# donor_name[j] = donation[j]

def add_donor(donor_name, donation):
    new_donor = input("Name of donor?").title()
    if new_donor not in donor_name:
        donor_name.append(new_donor)
        new_donation1 = input("Amount of donation by {}?".format(new_donor))
        idx = len(donor_name)-1
        new_donation1 = float(new_donation1)
        donation[idx].append(new_donation1)
    elif new_donor in donor_name:
        idx = donor_name.index(new_donor)
        new_donation1 = float(input("Amount of donation?".format(new_donor)))
        donation[idx].append(new_donation1)
        print(f"{new_donor} has made a new donation of {new_donation1}")
    return(new_donor, new_donation1)

# sort
def sort_key( donor_db2):
    return( donor_db2[0].split(" ")[1])

# creates request summary donation report for all donors

def create_report(donor_name, donation):
    donor_info = dict(zip(donor_name, donation))
    donors = list( donor_info.keys())
    all_gifts = list( donor_info.values())
    for ll in range( len( donor_info)):
        total_gift = sum( all_gifts[ll])
        num_gifts = len( all_gifts[ll])
        avg_gift = total_gift/num_gifts
        print ('{:23}'.format( donors[ll]),
               '${:^6,.2f}'.format( total_gift),
               '{:20}'.format( num_gifts),
               '{:14}'.format(""),
               '${:^6,.2f}'.format( avg_gift))

# send thank you to all donors

def thank_all_letter(donor_name, donation):
    donor_info = dict(zip(donor_name, donation))
    donors = list( donor_info.keys())
    all_gifts = list( donor_info.values())
    for ll in range( len(donor_info)):
        letter_format( donor = donors[ll], gift = sum(all_gifts[ll]))

# given the full name (firs, last and suffix), it generates the corresponding
# thank you letter to the selected donor

def thank_one_letter(donor_name, donation):
    donor_info = dict(zip(donor_name, donation))
    donors = list( donor_info.keys())
    # input donor info
    first_name = input( "Donor's first name - ").title()
    last_name = input( "Donor's last name - ").title()
    suffix = input( "Donor's suffix (if available) - ")
    if suffix is not "":
       donorname = " ".join( [first_name,last_name, suffix])
    else:
       donorname = " ".join( [first_name,last_name])
    if donorname in donors:
        gifts = donor_info[donorname]
        last_gift = gifts[len(gifts)-1]
        letter_format( donor = donorname, gift = last_gift)
    else:
        print(donorname, " is not in the donor's list")

###############################################
### following modules are supplementary embded on the above functions
###############################################

def letter_format( donor, gift):
    print('''
          Dear {},
          Thank you for your very kind donation of ${:,.2f}.
          It will be put to very good use.
                                Sincerely,
                                  -The Team'''.format(donor,gift))


#The script should prompt the user (you) to choose from a menu of 5 actions:
#“Send a Thank You”, “Create a Report” or “quit"

prompt = "\n".join(("Welcome",
          "Please choose from below options: ",
          "1 - Add new donation ",
          "2 - Create a Report ",
          "3 - Send Thank you to donor ",
          "4 - Send Thank you to all donors ",
          "5 - quit",
          ">>> "))

# list of donors and history of the amounts they have donated.

donor_name = ["William Gates III",
              "Jeff Bezos",
              "Paul Allen",
              "Mark Zuckerberg"]

donation = ( [653772.32, 10020.17, 58796.00],
            [877.33],
            [663.23, 43.87, 100.32],
            [1663.23, 4300.87, 10432.0])


def output_result():
        print("\n Please Select integer from 1 to 5 \n")
        response = input(prompt)
        if response == "1":
            add_donor(donor_name, donation)
        elif response == "2":
            create_report(donor_name, donation)
        elif response == "3":
            thank_one_letter(donor_name, donation)
        elif response == "4":
             thank_all_letter(donor_name, donation)
        else:
             print("Done")

if __name__ == '__main__':
    if donation[len(donation)-1] != []:
        donation += ([],)
    output_result()
