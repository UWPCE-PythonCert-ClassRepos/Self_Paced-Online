#!/usr/bin/env python3
# #############################################################################
# Written by: Mayc4t
# Date: 4/27/2018
# FileID: mailroom4.py
#
# Purpose: use unittest
#Add a full suite of unit tests.

#“Full suite” means all the code is tested. In practice, it’s very hard to test the user interaction, but you can test everything else. Make sure that there is as little untested code in the user interaction portion of the program as possible – hardly any logic.

#This is a big step – you may find that your code is hard to test. If that’s the case, it’s a good sign that you should refactor your code.
#
# #############################################################################


import collections
from collections import *

names = ["Lily Maycat", "Lulu Lemon", "Marc Jacobs", "Bobbi Brown", "Kate Spade"]
gifts   = [i*[5000] for i in range(1,6)]

def init_db():
    global donors_db
    donors_db = dict(zip(names, gifts))

def quit():
    """Quit the top menu."""
    print ("Quitting this main menu now")
    return "quit"

# def list_all_donor():
#     for each_dn in donors_db:
#         print ("\t\t", each_dn)


def is_donor_in_list ( dn_name):
    """ Check if the dn name is in the dn or not """
    lc_name = dn_name.strip().lower()
    #print (dn_name, "  ", lc_name)
    
    isIn = False
    ret_name = None

    for each_dn_name in donors_db.keys():
        lc_each_dn_name = each_dn_name.strip().lower()
        if lc_name == lc_each_dn_name:
            isIn = True
            #print ("TRUE")
            ret_name = each_dn_name
            break
        else:
            ret_name = dn_name
    return isIn, ret_name


def enter_dn_name():
    dn_name = None

    while not dn_name :
        ans = input_func( "\n\tEnter Donor Name to add"\
                 "\n\t - list (all donors) "\
                 "\n\t - quit (to main mn --- >> ")
        if ans.lower() == "quit": break
        if ans.lower() == "list":
            for each_dn in donors_db: print ("\t\t", each_dn)
        else:
            dn_name = ans

    return dn_name

def enter_dn_gift():
    gift = None

    while not gift : #or gift <0
        ans = input_func("\t\tEnter Donation Amount : ")
        ans = str(ans)
        if ans.lower() == "quit": break
        else:
            try:
                gift = float(ans)
            except ValueError:
                print("\t\tWRONG INPUT\n\t\tAmount of Money should be a valid number:")
    
        #        if  gift < 0:
        #            myError = ValueError( "Amout of Donation should be a positive number")
        #            raise OutofRange
   
    return gift 




def add_donation(name, gift):
    """Add donor, donation information to the system."""
    
    #print ("\t\tAdd Donation:")
    inlist, db_name = is_donor_in_list (name)

    if inlist: donors_db[db_name].append(gift)
    else: donors_db[db_name] = [gift]









def send_thank():
    """Print out the thank you note for the recent donation.
        Get donor name
        Get amount
        Update donor_db
        Send thank you Note
    """
    dn_name = enter_dn_name()
    #print('dn_name = %s' % dn_name)

    #print ("\tSend Thank You")
    if not dn_name: return 

    gift    = enter_dn_gift()
    if not gift: return

    add_donation( dn_name, gift)

    ret_str = "\n\n\t\tDear {},\n\t\tThanks a lot for your generous donation of ${}."\
          "\n\t\tThanks".format(dn_name, gift)
    print (ret_str)
    return ret_str



def get_dn_info_by_name(name):
    """
    Get Donor information.
    -Donor name, total gift, num_gift, avg_gift
    """
    total = sum(donors_db[name])
    num_gift = len(donors_db[name])
    avg  = total/num_gift
    return  [name, total, num_gift, avg]


    #report.append([dn, sum(dnt), len(dnt), sum(dnt)/len(dnt)])


def create_report():
    """Create the report and print out to terminal. """

    # create report
    report = list()
    for dn, dnt in donors_db.items():
        report.append([dn, sum(dnt), len(dnt), sum(dnt)/len(dnt)])
    # sort list
    sorted_report = sorted(report, key=lambda x: -x[1])

    #print the first line
    report_str = "\t{:<40}|{:>14} | {:>12} | {:>14}".format(
        "Donor Name", "Total Give", "Num Gifts", "Average Gift")
    report_str = "%s\n%s" % (report_str,
            "\t" + "_"*40 + " " + "_"*14 + "   " + "_"*12 + "   " + "_"*14)

    #print the table
    for each_dn in sorted_report:
        report_str = "%s\n%s" % (report_str, "\t{:<37}   ${:>16} {:>12}   ${:>14}".format(
            each_dn[0], each_dn[1], each_dn[2], each_dn[3]))

    #print(report_str)
    return report_str
    

def send_letters():
    """Creat and sent out thank letter to everyone on the list for their current donation. """
    #print("\n\n\tSend Letters")
    for k, v in donors_db.items():
        fname = k.replace(' ', "_") + ".txt"
        try: 
            with open(fname, 'w') as outfile:
                outfile.write(
                    "Dear {},\n\nThank you for your current generous donations: ${}.\n"\
                    "This will be put to good use. \n\nThanks".format(k, v[-1]))
        except PermissionError:
            print ("Permission denied, can't open file {}".format(fname))



main_prompt = ("\nSelect Options!!!\n"
               "1. Send a Thank You \n"
               "2. Create The ReportType\n"
               "3. Send letters to everyone\n"
               "4. Quit >> "
               )

main_dispatch = {"1": send_thank,
                 "2": create_report,
                 "3": send_letters,
                 "4": quit,
                 }

def get_menu_selection ( prompt, dispatch_dict):
    while True:
        
        try: 
            ans = input(main_prompt)
            if main_dispatch[ans]() == "quit": break
        except KeyError:
            print ( "Wrong Choice, Retry")



if __name__ == "__main__":
    global input_func
    init_db()
    input_func = input
    get_menu_selection( main_prompt, main_dispatch )


