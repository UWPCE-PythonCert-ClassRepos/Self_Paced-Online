#!/usr/bin/env python3

# new file for lesson 9 work to incorporate classes.
""" 
    need a donor class
    includes info about donor
    stuff to provide access too donot specific information
"""

""" 
    class that handles the donor collection. subclass of ^?
    methods to add donor
    search for donor
    sum stuff
    generate report
"""

class Donor:
    def __init__(self, name, *donation):
        self.name = name
        self.donations = donation[0]
        #Need to add code for creating without existing donation?

    @property
    def sum_donations(self):
        return sum(self.donations)


    @property
    def avg_donations(self):
        return sum(self.donations)/len(self.donations)

    
    def new_donation(self,new):
        return self.donations.append(new)




class Donors:
    def __init__(self):
        self.data = {}

    

    def new_donor(self,donor):
        #currently allows to add one individual donor with list of donations
        self.data[donor.name] = donor.donations
        print(self.data)





ddonors = {"Manny Machado": [12.2,2.51,3.20],
            "Adam Jones": [1024.14,22.21,323.45],
            "Chris Davis": [3.2,5.55,4.20]}

a = Donor('Adam', [1])
b = Donor("Yasiel", [3])
a.new_donation(8)
print(a.donations)

don = Donors()
don.new_donor(a)
don.new_donor(b)
