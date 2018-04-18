import sys
import os
from collections import defaultdict
donor_data = defaultdict(list,{'Andy':[960,256,123.5,40],'Bryce':[30,45,27],
                            'Charile': [25,50], 'David':[10], 'Elaine' :[75,26]})

class Donor():


    """this is Donor class to save donor's information"""
    def __init__(self, name, donation):
        self.name = name
        self.donation = donation


    def add_donor_in_data(self):
        return donor_data[self.name].append(self.donation)


d1 = Donor('xxxx',54664)
d1.add_donor_in_data()

print(donor_data)
