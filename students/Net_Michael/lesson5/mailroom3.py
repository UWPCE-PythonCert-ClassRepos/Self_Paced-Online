#!/usr/bin/env python
# coding: utf-8

import os
import io
import pathlib
import shutil
import re
import string
from collections import defaultdict

def quit_sel():
    raise SystemExit(1)

#new_donor_folder is a folder containing the text files of all donors.

new_donor_folder = "donor_list"

"""
If the cwd is in the pah of the donors folder
the code will search this folder in the path.
For this machine - directory/donor_list/Paul_Allen.txt
"""
# list all the folders and their associated paths
def list_dir_path():
    root = os.path.dirname( os.getcwd())
    for path, subdir, file in os.walk(root):
        for dirname in subdir:
            dir_info = str(os.path.join(dirname))
            yield dir_info, path

# outputs the path  *\*\donor_list
def donor_list_dir(donor_folder = new_donor_folder):
    dir_info = list(list_dir_path())
    for j in range(len(dir_info)):
        if dir_info[j][0] in donor_folder:
            sel_dirct = dir_info[j][1]
    donation_directory = os.path.join(sel_dirct, donor_folder)
    return(donation_directory)

# given filename and directory open the text file with donation information

def open_donor_file( donation_directory ):
    donor_lists = open(donation_directory)
    donations = donor_lists.read()
    donor_lists.close()
    return(donations)

# extract the donation information of one donor
def one_donor_info(file_name, donor_folder = new_donor_folder):
    #file_name: the file name of the donor ("firstname_lastname_suffix.txt")
    donor_filepath = donor_list_dir(donor_folder = new_donor_folder)
    donation_directory = os.path.join( donor_filepath, file_name)
    donation_filename = os.path.basename(file_name)
    donor_name = os.path.splitext( donation_filename)[0].split("_")
    donor_collect = open_donor_file( donation_directory)
    donations = donor_collect.split(", ")
    donation_out = [eval(item) for item in donations]
    donor_info = {'donor': donor_name, 'gifts': donation_out}
    return(donor_info)

# extracts donation information of all donors in the directory
def all_donors_info(donor_folder = new_donor_folder):
    donor_filepath = donor_list_dir(donor_folder = new_donor_folder)
    donor_files = os.listdir( donor_filepath)
    donors_gifts = defaultdict( list)
    for file_name in donor_files:
        donor_gift = one_donor_info(file_name, donor_folder = new_donor_folder)
        donor_name = " ".join( donor_gift["donor"])
        donation = donor_gift["gifts"]
        donors_gifts[donor_name] = donation
    return(donors_gifts)


# send thank you letter to all donors
def thank_all_letter(donor_folder = new_donor_folder):
    donor_info = all_donors_info(donor_folder = new_donor_folder)
    donors = list( donor_info.keys())
    all_gifts = list( donor_info.values())
    for ll in range( len(donor_info)):
        letter_format( donor = donors[ll], gift = sum(all_gifts[ll]))

# creates summry table to report total (and average) donation from each donor
def create_report( ):
    donor_filepath = donor_list_dir(donor_folder = new_donor_folder)
    print("Name\t\t\tTotal Donation\t\tNum Gifts\tAverage Gift")
    donor_info = all_donors_info(donor_folder = new_donor_folder)
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

# given first, last names and suffix, writes thank you letter for the last donation
def thank_one_letter():
    first_name = input( "Donor's first name - ").title()
    last_name = input( "Donor's last name - ").title()
    suffix = input( "Donor's suffix (if available) - ")
    if suffix is not "":
        full_name = "_".join( [first_name,last_name, suffix])
    else:
        full_name = "_".join( [first_name,last_name])
    file_name = ".".join( [full_name, "txt"])
    donor_filepath = donor_list_dir(donor_folder = new_donor_folder)
    if file_name in os.listdir( donor_filepath):
        donor_info = one_donor_info(file_name, donor_folder = new_donor_folder)
        donor = " ".join( donor_info["donor"])
        all_gifts = donor_info["gifts"]
        last_gift = all_gifts[len(all_gifts)-1]
        letter_format( donor = donor, gift = last_gift)
    else:
        print(full_name, " is not in the donor's list")

# format letter
def letter_format( donor, gift):
    print('''
          Dear {},
          Thank you for your very kind donation of ${:,.2f}.
          It will be put to very good use.
                                Sincerely,
                                  -The Team'''.format(donor,gift))
# update the list of donors and donation
# donor_name is the list of donors
# donation is the amount of donation of each donor
# donor_name[j] = donation[j]

def enter_donation(donor_folder = new_donor_folder):
    donor_filepath = donor_list_dir(donor_folder = new_donor_folder)
    donor_info = all_donors_info(donor_folder = new_donor_folder)
    donors = list( donor_info.keys())
    print("The current donors in the database are \n ", donors)
    new_donor = input("Enter full name of the donor?").title()
    if new_donor not in donors:
        if list(new_donor)[0] in list(string.ascii_uppercase):
            new_donor_filename = re.sub(" ", "_", new_donor) + ".txt"
            new_donor_filepath = donor_list_dir(donor_folder = new_donor_folder)
            donation_directory = os.path.join( donor_filepath, new_donor_filename)
            # enter donation information
            new_donation1 = input("Amount of donation by {} ?".format(new_donor))
            #write the donation information
            new_file = open(donation_directory, 'w')
            new_file.write(new_donation1)
            new_file.close()
            print(new_donor, "is a new donor and his first donation is $", new_donation1)
        else:
            print("donor entry not correct.")
    elif new_donor in donors:
        new_donor_filename = re.sub(" ", "_", new_donor) + ".txt"
        donation_directory = os.path.join( donor_filepath, new_donor_filename)
        new_donation1 = input("Amount of donation by {} ?  ".format(new_donor))
        new_donation1 = ', ' + str(new_donation1)
        append_file = open(donation_directory, 'a')
        append_file.write(new_donation1)
        append_file.close()

# enter the correct folder name containing all the text files
# for this computer, the folder name is donor_list

def folder_name_entry():
    print(" \n Folder name is not correct \n")
    donor_folder_name = input(" \n Please enter the folder name in your directory \n"
                                  " containing the list of the donor's names. This \n"
                                  " folder contains a list of donations in text file \n"
                                   " named by full name of the donor (firsname_lastname_suffix) \n"
                                   "\n"
                                   " Folder name is        ")
    Donor_folder = donor_list_dir(donor_folder = donor_folder_name)
    return(Donor_folder)

# switch function to select desired output
main_sel = {
        1: enter_donation,
        2: create_report,
        3: thank_one_letter,
        4: thank_all_letter,
        5: quit_sel,
        }

prompt = "\n".join(("Welcome",
          "Please choose from below options: ",
          "1 - Enter new donation ",
          "2 - Create a Report ",
          "3 - Send Thank you to donor ",
          "4 - Send Thank you to all donors ",
          "5 - Quit",
          ">>> "))

# provide the folder name in the machine that contains
# the donor namelist (example donor_list/Paul_Allen.txt)
# provide donor_list and it will search accross to find
# the directorypath */donor_list and will pull the files
# to execute the desired outputs (report and thank you letters)

if __name__ == "__main__":
    try:
        donor_file_trial = donor_list_dir()
        list_files = os.listdir(donor_file_trial)
        if(len(list_files) > 0):
            while True:
                new_donor_folder = new_donor_folder
                sel_choice = eval(input(prompt))
                if sel_choice < 6:
                    main_sel.get(sel_choice)()
                else:
                    print("\n choose less than 4 or press 4 to exit\n")
    except FileNotFoundError:
        donor_folder_new = folder_name_entry()
        list_files = os.listdir(donor_folder_new)
        folder_new = os.path.basename(donor_folder_new)
        if(len(list_files) > 0):
            while True:
                new_donor_folder = folder_new
                sel_choice = eval(input(prompt))
                if sel_choice < 6:
                    main_sel.get(sel_choice)()
                else:
                    print("\n choose less than 4 or press 4 to exit \n")
