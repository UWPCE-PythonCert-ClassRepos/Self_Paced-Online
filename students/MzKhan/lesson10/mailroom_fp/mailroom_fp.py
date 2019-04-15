'''
Name: Muhammad Khan
Date: 04/14/2019
Assignment10
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


    @property
    def get_donor_stat(self):
        return [ self.name,self.total_donations_amount,self.total_donations,
                                                           self.avg_donation ]


    def thank_you(self):
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
        return email_msg.format(self.name, self.donations[-1])


    def get_letter_text(self):
        """Return the letter message"""
        message = """Dear {:},

        Thank you so much for your kind donation of ${:.2f}. With that you have
        generously donated a total amount of ${:.2f} in your last {} donation(s).
        We must ensure you that your donations will be put to a very good use.

                                                            Sincerely,

                                                            -Team """
        return message.format( self.name, self.donations[-1],
                             self.total_donations_amount, self.total_donations)



class DonorCollection:
    # This class contains the functionality for all the donors in the donors'
    # database.

    def __init__(self, *args):
        #dict comprehension
        self.donors = {d.name: d for d in args}


    @property
    def total_amount_donated(self):
        return sum([donor.total_donations_amount
                                           for donor in self.donors.values() ])


    def add_donation(self, name, donation):
        """
        Add the donation for the given donor
        :parm 1: name      required positional parameter for the donor's name.
        :parm 2: donation  required positional parameter for the donation amount
        """
        if self.donors.get(name):
            self.donors[name].add_donation(donation)
        else:
            self.donors[name] = Donor(name, donation)


    def get_report_data(self):
        """Return a sorted list in the desc order"""
        un_sorted = [ donor.get_donor_stat for donor in self.donors.values() ]
        return sorted(un_sorted, key=igetter(1), reverse = True)


    def send_letter_everyone(self):
        """Generate the thank you letters for each donor in the list"""
        date_format = '{:%m-%d-%Y}'.format(datetime.datetime.now())
        for donor in self.donors.values():
            file_name = donor.name+"_"+date_format+'.txt'
            self.write_a_letter(file_name, donor.get_letter_text())


    def write_a_letter(self, filename, content):
        """Create a new file in the Letters folder and write to it"""
        folder = "Letters"
        if not os.path.exists(folder): os.mkdir(folder)
        with open(os.path.join(folder,filename),'w+') as out:
            out.write(content)


    def projected_amount(self,name, factor, minn=None, maxx=None):
        """
        This method uses the map to multiply each donation of each donor by
        the multiplying factor.
        :parm1:  factor   required positional argument (int or float)
        :return: float    projected donation amount
        """
        all_donations = [donor.total_donations_amount
                                            for donor in self.donors.values() ]
        if minn is None: minn=0
        if maxx is None: maxx = max(all_donations)
        filter_donation=list(filter(lambda x: minn <= x <= maxx,all_donations))
        match_contribution = list(map(lambda x: factor*x, filter_donation))
        projected_amount = sum(match_contribution)
        self.add_donation(name, projected_amount)
        return projected_amount
