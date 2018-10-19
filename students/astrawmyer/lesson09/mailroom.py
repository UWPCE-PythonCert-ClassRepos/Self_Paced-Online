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
    def __init__(self, name, *donations):
        self.name = name
        self.donations = donations
        if donations is None:
            self.donations = ()
        else:
            self.donations = donations
    
    @property
    def sum_donations(self):
        self.donations
    
    def add_donation(self,new):
        


""" class Donor_Actions(Donor):
    def __init__(self):
        if Donor """





ddonors = {"Manny Machado": [12.2,2.51,3.20],
            "Adam Jones": [1024.14,22.21,323.45],
            "Chris Davis": [3.2,5.55,4.20]}

a = Donor('Adam', 12.2,2.51,3.20)
print(a.name)
print(a.donations)