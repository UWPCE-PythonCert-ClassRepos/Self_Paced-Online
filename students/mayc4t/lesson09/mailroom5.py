#!/usr/bin/env
# #############################################################################
# Written By: Mayc4t
# June 3, 2018
# Self-paced Python
# lesson 9 -
# fileID: mailroom5.py
# #############################################################################


import collections
from collections import *


class Donor():
    # You’ll want a Donor class –
    # this will hold all the information about the donor
    # , and have attributes,
    #            properties,
    #            and methods to provide access to the donor specific information that is needed.
    def __init__(self, first, last, donations=None):
        self._last = last
        self._first = first
        self._donations = donations
        self._num_gift = len(donations)
        self._avg = sum(donations)/len(donations)

    @property
    def donations(self):
        return(self._donations)

    @property
    def name(self):
        self._name = "{} {}".format(self._first, self._last)
        return self._name

    @property
    def total_donation(self):
        return sum(self._donations)

    @property
    def avg(self):
        if len(self.donations) == 0:
            print("Error: This person has no donations")
        else:
            return(sum(self.donations)/len(self.donations))

    @property
    def num_gift(self):
        return len(self.donations)

    @staticmethod
    def sort_by_name(self):
        return (self._lname, self._fname)

    @staticmethod
    def sort_by_total(self):
        return(self.total_donation)

    def __str__(self):
        str_ret = "\t{:<30}|{:>14} | {:>12} | {:>14}".format(
            self.name, self.total_donation, self.num_gift, self.avg)
        return (str_ret)

    def __repr__(self):
        return "'({} {} {})'".format(self.name, self._num_gift, self._avg)

    def print_thank(self, amt):
        print("\n\n\t\tDear {},\n\t\tThank you for your recent generous donation of {}.\n\t\tThanks,".format(
            self.name, amt))

    def add_donation(self, amount):
        self._donations.append(amount)


class Donor_DB():
    # You’ll then want a class that handles the collection of donors.
    # This will hold all the donor objects,
    #       but also methods to add a new donor,
    #       search for a given donor, etc.
    #       If you want a way to save and re-load your data, this class would have that too.
    # Your class for the collection of donors will also hold the code
    # that generates reports about multiple donors.
    def __init__(self, donors=None):
        if donors is None:
            self.donors_db = []
        else:
            self._donors_db = donors

    def print_donors_name_list(self):
        print ("\n\tList of Donor Name")
        print ("\t------------------")
        for dn_idx in self._donors_db:
            print("\t\t{}".format(dn_idx.name))

    @property
    def names(self):
        name_list = []
        for dn_idx in self._donors_db:
            name_list.append(dn_idx.name)
        self._names = name_list
        return self._names

    def create_report(self):
        sorted_list = sorted(
            self._donors_db, key=Donor.sort_by_total, reverse=True)
        print ("\n\n\tDonor.DB.create_report")
        print("\t{:<30}|{:>14} | {:>12} | {:>14}".format(
            "Donor Name", "Total Gift", "Num Gifts", "Avg Gift"))
        print("\t" + "_"*30 + " " + "_"*14 + "   " + "_"*12 + "   " + "_"*14)
        for dn_idx in sorted_list:
            print(dn_idx.__str__())

    def send_letters(self):
        for dn in self._donors_db:
            name = dn.name.split()
            fname = name[0]+name[1] + ".txt"
            print (fname)
            try:
                with open(fname, 'w') as outfile:
                    outfile.write(
                        "Dear {},\n\nThank you for your total generous donations: ${}.\n"
                        "This will be put to good use. \n\nThanks".format(dn.name, dn.total_donation))
            except PermissionError:
                print ("Permission denied, can't open file {}".format(fname))

    def add_donation(self, donor):
        # check if donor is in self._donors_db
        if any(donor.name in x for x in self.names):
            idx = self.names.index(donor.name)
            #print ("Exist")
            #print (idx)
            gift = donor.total_donation
            self._donors_db[idx].add_donation(gift)
            #print (self._donors_db[idx].__str__())
        else:
            self._donors_db.append(donor)

    def get_info_from_name(self, name):
        if any(name in x for x in self.names):
            idx = self.names.index(donor.name)
            db_ret = self._donors_db[idx]
            print (db_ret.donations)
            return self._donors_db[idx]


# Remember that the user interaction code (anything with an input function)
# should be outside of these “logic” or “model” classes.

# In general, you will have a method for each of the functions in your non-OO version.
# Which class they go it will depend on whether the method only needs the information
#       from one donor, or from the whole collection.


# Rules of thumb for where to put methods:
# 1.	Hopefully, once you made your code testable,
#       -all the user-interaction code (with input()) is self contained in functions
#           that don’t have any logic (data manipulation) in them.
#           If not, then this is a good time to refactor.
# 2.	If a function does something with a single donor – it should be a method in the Donor class.
# 3.	If a function works with multiple donors – it should be in the class that handles a collection of donors.
# 4.	If a function contains a call to input() – it belongs outside of the logic classes – either stand alone in the module (like they are already) or perhaps all in a CLI class.


d1 = Donor("Kate", "Spade", [100])
d2 = Donor("Michael", "Kors", [100, 100])
d3 = Donor("Tory", "Burch", [100, 100, 100])
d4 = Donor("Stuart", "Weitzman", [100, 100, 100, 100])
d5 = Donor("Kate", "Summerville", [100, 100, 100, 100, 100])
donors_db = Donor_DB([d1, d2, d3, d4, d5])


def send_thank():
    """ Get donor name or option of action (list, quit)
        if "donor name" is quit --> come back to orignial menu
        if "donor name" is list --> list all the donors in the data
        if "donor name" is not anything above, update the donation list
    """
    done = False
    time = 0

    print("\n\tSelect Option 1:")
    print("\tGet Donor Name, Gift --> Send thank note to the gift")
    while not done:
        (first, last, done, show_dns) = enter_dn_name()
        if done:
            break
        elif show_dns:
            print("\tList of Available Donors")
            print("\t{}".format(donors_db.names))
        else:
            amt = int(input("\tEnter Gift Amt :$"))
            dn = Donor(first, last, [amt])
            dn.print_thank(amt)
            donors_db.add_donation(dn)
        print ("\n\n\t--Another donor--")
        print ("\t-----------------")


def enter_dn_name():
    first = input("\n\tEnter first name :")
    if first.capitalize() == 'Quit':
        return (None, None, True, None)
    elif first.capitalize() == 'List':
        return (None, None, False, True)
    else:
        last = input("\n\tEnter last name :")
        if last.capitalize() == 'Quit':
            return (None, None, True, None)
        elif last.capitalize() == 'List':
            return (None, None, False, True)
        else:
            return (first.capitalize(), last.capitalize(), False, False)


if __name__ == "__main__":

    main_prompt = ("\nSelect Options!!!\n"
                   "1. Send a Thank You \n"
                   "2. Create The ReportType\n"
                   "3. Send letters to everyone\n"
                   "4. Quit >> "
                   )

    main_dispatch = {"1": send_thank,
                     "2": donors_db.create_report,
                     "3": donors_db.send_letters,
                     "4": quit,
                     }
    print("Dispatch :", main_dispatch)

    while True:
        try:
            ans = input(main_prompt)
            if main_dispatch[ans]() == "Quit":
                break

        except KeyError:
            print ("Wrong Choice Retry")
