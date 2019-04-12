# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:47:00 2019

@author: acharch
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:14:06 2019

@author: acharch
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:31:49 2019

@author: acharch
"""
import sys
import os
from copy import deepcopy


class Donor:
    def __init__(self, name, donations=None):
        self.name = name
        if donations == None:
            self._donations = []
        else:
            self._donations = list(donations)
  
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def donations(self):
        return self._donations
    @donations.setter
    def donations(self, value):
        self._donations = value
    
    def add_donation(self,amount):
        self.amount = amount
        try:
            self.donations.append(self.amount)
        except ValueError:
            print("Enter a donation amount")
            
    def total_donations(self):
        try:
            return sum(self.donations)
        except TypeError:
            return self.donations
            
    def avg_donation(self):
        try:
            return self.total_donations()/self.num_of_donations()
        except TypeError:
            return self.donations

    def number_donations(self):
        return len(self.donations) 
    
    def Thanks(self, amount):
        note = "{},Thank you for your donation of {}".format(self.name, amount)
        print(note)

    def multiply_donation(self, multiplication_factor):
        self._donations = list(map(lambda x: x*multiplication_factor, self.donations))
        return self._donations

    def donation_greater_than(self, value):
        self._donations = list(filter(lambda x: x > value,self.donations))
        return self._donations

    def donation_lesser_than(self, value):
        self._donations = list(filter(lambda x: x < value,self.donations))
        return self._donations  


class DonorCollection:
    def __init__(self, donors = None):
        if donors is None:
            donors = []
        else:
            self._donors = donors
    @property
    def donors(self):
        return self._donors 
    
           
    def add_donor(self, donor):
        self.donors.append(donor)

    def fit_donor(self, new_name):
        exists = False
        for donor in self.donors:
            if donor.name == new_name:
                exists = True
                break
        if not exists:
            donor = Donor(new_name)
            donors.add_donor(donor)
            return donor
 
    def donor_list(self):
        list_donors = ''
        for donor in self.donors:
            list_donors += donor.name + '\n'
        return list_donors


    def sort_total(self):
        return(sorted(self.donors, key=total_donation_key, reverse=True))


    def Report(self):
        sorted_donors = donors.sort_total()
        for donor in sorted_donors:
            print ("1")
            

    def challenge1(self, multiplication_factor, value):
        donors_copy_less_than = deepcopy(self.donors)
        for donor in donors_copy_less_than:
            donor.donation_lesser_than(value)
            donor.multiply_donation(multiplication_factor)
        return donors_copy_less_than


    def challenge2(self, multiplication_factor, value):
        donors_copy_more_than = deepcopy(self.donors)
        for donor in donors_copy_more_than:
            donor.donation_greater_than(value)
            donor.multiply_donation(multiplication_factor)
        return donors_copy_more_than        
    

donor1 = Donor("Bill Gates", [1000,2000,3000,4000,5000])
donor2 = Donor("Marc Zuckerberg", [1005,2005,3005,4005,5005])
donor3 = Donor("Jeff Bezos", [9000,12000])


donors = DonorCollection([donor1,donor2,donor3])

def total_donation_key(donor):
    return sum(donor.donations)

    
def prompt_new_donor():
    input_name = "list"
    while input_name =="list":
        input_name = input("Please enter a donor name:")
        if input_name == "list":
            print(DonorCollection.donor_list())
        if input_name == 'none':
            return None  
        else:
            prompt_donation(input_name)
            break


      
def prompt_donation(name, donation_amount = None):
    new_donor = donors.fit_donor(name)
    # Promt for donation amount
    if donation_amount == None:
        donation_amount = input('Please enter a donation amount $')
    try:
        new_donor.add_donation(donation_amount)
        print(new_donor.Thanks(donation_amount))
    except ValueError:
        print('Please enter a number')
        prompt_donation(name) 

prompt = "\n".join(('Welcome',
                   'Please select from the following options',
                   '1.Send A Thank You!',
                   '2.Create a report',
                   '3.Send a letter to all participants',
                   '4.Look at Lesser than Projections',
                   '5.Look at Greater than Projections',
                   '6.Quit'))

def Projections_Min():
    input_multiplication_factor1 = 3
    while input_multiplication_factor1 == 3:
        input_multiplication_factor1 = input('Please enter a donation multiplication factor for scenario modeling for lesser than values')
        if input_multiplication_factor1 == 0:
            break
        else:
            input_max_donation = input('Please enter a donation amount for which you would like to see lesser than values')
            donors_copy_less_than = donors.challenge1(int(input_multiplication_factor1),int(input_max_donation))
            for donor in donors_copy_less_than:
                print("{}".format(donor))
                #print("{}".format(donors.challenge1(int(input_multiplication_factor1), int(input_max_donation))))

    
def Projections_Max():
    input_multiplication_factor2 = 2
    while input_multiplication_factor2 == 2:
        input_multiplication_factor2 = input('Please enter a donation multiplication factor for scenario modeling for greater than values')
        if input_multiplication_factor2 == 0:
            break
        else:
            input_min_donation = input('Please enter a donation amount for which you would like to see greater than values')
            donors_copy_more_than = donors.challenge2(int(input_multiplication_factor2),int(input_min_donation))
            for donor in donors_copy_more_than:
                print("{}".format(donor))
                #print ("{}".format(donors.challenge2(int(input_multiplication_factor2), int(input_min_donation))))


def Quit():
    print("Bye!")
    sys.exit()
    
def main():
    while True:
        response = int(input(prompt))
        SwitchFuncDict = {1:prompt_new_donor,2:donors.Report,4:Projections_Min,5:Projections_Max, 6:Quit}
        SwitchFuncDict.get(response)()

if __name__ == "__main__":
    main()
    

