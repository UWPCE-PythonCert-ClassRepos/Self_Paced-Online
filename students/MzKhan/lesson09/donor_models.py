'''
Name: Muhammad Khan
Date: 04/09/2019
Assignment09
'''

import os
import re
import datetime
from operator import itemgetter as igetter

class Donor:
    # The donor class manages the functionality for a single donor.

    def __init__(self, name, donations):
        #Initializer or Constructor
        # Make sure that the data is added to a list.
        self._name = name
        if isinstance(donations, list):
            self._donations = donations
        elif isinstance(donations, tuple):
            self._donations = list(donations)
        else:
            self._donations = [donations]


    def __repr__(self):
        """Reproduce the Donor Object"""
        return "Donor({},{})".format(self._name, self._donations)


    def add_donation(self, amount):
        """Add the the donation amount for a donor"""
        self._donations.append(amount)

    #Properties for attribute-like access.
    @property
    def name(self):
        return self._name


    @property
    def donations(self):
        return self._donations


    @property
    def total_donations(self):
        return len(self._donations)


    @property
    def total_donations_amount(self):
        return sum(self._donations)


    @property
    def avg_donation(self):
        return self.total_donations_amount / self.total_donations


    def thank_you(self, name, amount):
        """
        :parm 1: name - required argument
        :parm 2: amount - requried argument.
        :return: string - a formatted email message for the donor.
        """
        email_msg = """
        \rDear {:},

        \rThank you so much for your generous donation of $ {:.2f}.

        \rBest Regards,

        \r-Team"""
        return email_msg.format(name, amount)



class DonorCollection:
    # This class contains the functionality for all the donors in the donors'
    # database.

    def __init__(self, *args):
        #dict comprehension
        self.donors = {d.name: d for d in args}


    def add_donation(self, name, donation):
        if self.donors.get(name):
            self.donors[name].add_donation(donation)
        else:
            self.donors[name] = Donor(name, donation)


    @property
    def list(self):
        """Return the key values ( donor names ) from the dict."""
        return list(self.donors)


    @staticmethod
    def sort_desc(a_list):
        return sorted(a_list, key=igetter(1), reverse=True)


    def a_list(self):
        """
        Return a list from the donors' database that holds the data in the
        dict
        """
        new_report = []
        for donor in self.donors.values():
            new_report.append([donor.name, donor.total_donations_amount,
                                   donor.total_donations,donor.avg_donation ])
        return new_report


    def create_report(self):
        """Return a sorted list in the desc order"""
        a_list = self.a_list()
        a_sorted_list = self.sort_desc(a_list)
        return a_sorted_list


    def send_letter_everyone(self):
        """Generate the thank you letters for each donor in the list"""
        date_format = '{:%m-%d-%Y}'.format(datetime.datetime.now())
        for donor in self.donors.values():
            letter = self.letter_format(donor.name,donor.donations[-1],
                                        donor.total_donations_amount,
                                               donor.total_donations)
            file_name = donor.name+"_"+date_format+'.txt'
            self.write_a_letter(file_name,letter)


    def write_a_letter(self, filename, content):
        """Create a new file in the Letters folder and write to it"""
        folder = "Letters"
        if not os.path.exists(folder): os.mkdir(folder)
        with open(os.path.join(folder,filename),'w+') as out:
            out.write(content)


    def letter_format(self, *donor_info):
        """Return the letter message"""
        message = """Dear {:},

        Thank you so much for your kind donation of ${:.2f}. With that you have
        generously donated a total amount of ${:.2f} in your last {} donation(s).
        We must ensure you that your donations will be put to a very good use.

                                                            Sincerely,

                                                            -Team """
        return message.format(*donor_info)


