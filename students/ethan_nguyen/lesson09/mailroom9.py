
import sys, os
import pytest

'''
Class to store Donor object and its attributes
'''
class Donor:
    def __init__(self, donor_name, amount=0):
        self._name = donor_name
        self._amount_gift = amount
        self.count_donation = 1
    
    def __str__(self):
        return str(f"Donor: {self.name}")

    def __repr__(self):
        return repr(f'Donor({self.name})')

    '''function to return historical amount'''
    @property
    def amount(self):
        return self._amount_gift
    @amount.setter
    def amount(self, value):
        self._amount_gift = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    def sort_key(self):
        return self.amount

    '''function to calculate average donation'''
    def cal_average(self):
        return (self.amount/self.count_donation)

    def __eq__(self, other):
        return (self._amount_gift == other._amount_gift)
    
    def __lt__(self, other):
        return (self._amount_gift < other._amount_gift)

    def __gt__(self, other):
        return (self._amount_gift > other._amount_gift)

    def create_thank_you_note(self):
        return f'Dear {self.name}, \n Thank you for your very kind donation of ${self.amount:,.2f} \n \
            It will be put to very good use. \n Sincerely, \n -UW'

class DonorCollection(dict):
    def __init__(self):
        super().__init__(self)
    
    def is_donor_exist(self, Donor):
        if Donor.name in self:
            return True

    def add_donor(self, Donor):
        if self.is_donor_exist(Donor):
            self.add_amount(Donor.name, Donor.amount)
            self.update_num_donnation(Donor.name)
        else:
            self[Donor.name] = Donor

    '''function to return number of donations'''
    #def num_donnation(self, name):
    #    return self[name].count_donation

    def update_num_donnation(self, name):
        self[name].count_donation += 1

    '''function to add new donation amount to historical'''
    def add_amount(self, name, addition):
        self[name].amount += addition

    def sort_key(self, donor):
         return donor[1].amount

    def prepare_report(self):
        sort_Donor_list = sorted(self.items(), key=self.sort_key, reverse = True)
        rows = list()
        for d in sort_Donor_list:
            rows.append("{:<25} ${:>12,.2f}{:>22}{:<10}${:>12,.2f}".format(d[1].name, d[1].amount, d[1].count_donation, '', d[1].cal_average()))
        return rows

    def create_letter(self, path, letter_name, letter):
        """Create letter"""
        with open(f'{path}/{letter_name}.txt', 'w') as f:
            f.write(letter) 

    def send_letters(self, path):
        for k,v in self.items():
            self.create_letter(path, k, v.create_thank_you_note())
        




