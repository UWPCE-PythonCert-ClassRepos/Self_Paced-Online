#!/usr/bin/env python3


class Donor:
    """creates objects for individual donors"""
    def __init__(self, title, last_name, donation):
        self.title = title
        self.last_name = last_name
        self.donations = [donation]

    @property
    def donor(self):
        return {self.last_name: {'title': self.title, 'donations':
        sum(self.donations), 'num_donations': len(self.donations)}}
    
    @property
    def title(self):
        return self.new_title

    @title.setter
    def title(self, new_title):
        """enables title change for donor"""
        self.new_title = new_title

    @property
    def donation(self):
        return self.donation

    @donation.setter
    def donation(self, donation):
        """enables addition of new donations"""
        self.donations.append(donation)
