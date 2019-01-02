#!/usr/bin/env python
# coding: utf-8

import os
import io
import pathlib
import shutil
import re
from collections import defaultdict

#####################################################
# creates modules that output options in switch_fun_dict
#####################################################


def quit_sel():
    raise SystemExit(1)

# send thank you all
def thank_all_letter( donor_folder = "donor_list"):
    # donor_folder: name of the folder in the directory holding donor files
    # the donor_list folder contains donor's gifts in a text file
    # formatted as "firstname_lastname_suffix.txt/firstname_lastname.txt"
    # and each file contans donations (sorted from early donation to the latest).
    # Example - Paul_Allen.txt contains 663.23, 434.87, 122.32
    donor_info = all_donors_info( donor_folder)
    donors = list( donor_info.keys())
    all_gifts = list( donor_info.values())
    for ll in range( len(donor_info)):
        letter_format( donor = donors[ll], gift = sum(all_gifts[ll]))

# creates summry table to report total (and average) donation from each donor

def create_report( donor_folder = "donor_list"):
    print("Name\t\t\tTotal Donation\t\tNum Gifts\tAverage Gift")
    donor_info = all_donors_info( donor_folder)
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

# given the full name (firs, last and suffix), it generates the corresponding
# thank you letter
def thank_one_letter( donor_folder = "donor_list"):
    first_name = input( "Donor's first name - ").title()
    last_name = input( "Donor's last name - ").title()
    suffix = input( "Donor's suffix (if available) - ")
    if suffix is not "":
        full_name = "_".join( [first_name,last_name, suffix])
    else:
        full_name = "_".join( [first_name,last_name])
    file_name = ".".join( [full_name, "txt"])
    if file_name in os.listdir( donor_folder):
        donor_info = one_donor_info( donor_folder = donor_folder,
                                     file_name = file_name)
        donor = " ".join( donor_info["donor"])
        all_gifts = donor_info["gifts"]
        last_gift = all_gifts[len(all_gifts)-1]
        letter_format( donor = donor, gift = last_gift)
    else:
        print(full_name, " is not in the donor's list")

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

# reads text file from the file path
def read_donor_info( donation_directory):
    donor_lists = open(donation_directory)
    donations = donor_lists.read()
    donor_lists.close()
    return(donations)

# extract the donation information of one donor
def one_donor_info( donor_folder, file_name):
    # donor_folder: name of the folder in the directory holding donor files
    #file_name: the file name of the donor (full name of the donor,
    #              "firstname_last_name.txt")
    donation_directory = os.path.join( os.getcwd(), donor_folder, file_name)
    donation_filename = os.path.basename( file_name)
    donor_name = os.path.splitext( donation_filename)[0].split("_")
    donor_collect = read_donor_info( donation_directory)
    donations = donor_collect.split(", ")
    donation_out = [eval(item) for item in donations]
    donor_info = {'donor': donor_name, 'gifts': donation_out}
    return(donor_info)

# creates a loop to get the donation ifnormation of
# all donors in the directory

def all_donors_info( donor_folder):
    # donor_folder: name of the folder in the directory holding donor files
    donation_dir = os.path.join( os.getcwd(), donor_folder)
    donor_files = os.listdir( donation_dir)
    donors_gifts = defaultdict( list)
    for file_name in donor_files:
        donor_gift = one_donor_info( donor_folder, file_name)
        donor_name = " ".join( donor_gift["donor"])
        donation = donor_gift["gifts"]
        donors_gifts[donor_name] = donation
    return(donors_gifts)

def enter_donation(donor_folder = "donor_list" ):
    donor_info = all_donors_info( donor_folder)
    donors = list( donor_info.keys())
    all_gifts = list( donor_info.values())
    print("The current donors in the database are \n ", donors)
    new_donor = input("Enter full name of the donor?").title()
    if new_donor not in donors:
        # file directory information to create one
        new_donor_filename = re.sub(" ", "_", new_donor) + ".txt"
        donation_directory = os.path.join( os.getcwd(), donor_folder, new_donor_filename)
        # enter donation information
        new_donation1 = input("Amount of donation by {} ?".format(new_donor))
        #write the donation information
        new_file = open(donation_directory, 'w')
        new_file.write(new_donation1)
        new_file.close()
    elif new_donor in donors:
        new_donor_filename = re.sub(" ", "_", new_donor) + ".txt"
        donation_directory = os.path.join( os.getcwd(), donor_folder, new_donor_filename)
        new_donation1 = input("Amount of donation by {} ?  ".format(new_donor))
        new_donation1 = ', ' + str(new_donation1)
        append_file = open(donation_directory, 'a')
        append_file.write(new_donation1)
        append_file.close()


# switch function will select the fumctions above
# depending on the selection of user

switch_func_dict = {
        1: create_report,
        2: thank_all_letter,
        3: thank_one_letter,
        4: enter_donation,
        5: quit_sel,
    }

def output_entry_value():
    print('''Please choose one of the following numbers:
             For report select - 1,
             Send thank you letter to all donors - 2,
             Send thank you letter to selected donor - 3,
             Enter new donation - 4,
             Quit - 5

             ''')
    sel_num = input("Enter one of the four numbers: ")
    sel_num = eval(sel_num)
    return(sel_num)


# any of the follwing for choices can be executed for desired output

if __name__ == "__main__":
    sel_choice = output_entry_value()
    if sel_choice <= 5:
        switch_func_dict.get(sel_choice)()
    else:
        print("Select an integer between 1 and 4")
