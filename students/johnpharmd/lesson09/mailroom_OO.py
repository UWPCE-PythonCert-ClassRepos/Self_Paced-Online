#!/usr/bin/env python3


class Donor:
    """creates donor objects"""
    def __init__(self, title, last_name, donation_amt):
        self.title = title
        self.last_name = last_name
        self.donations = []
        self.donation_amt = self.donations.append(donation_amt)

    @property
    def donor(self):
        return {self.last_name: {'title': self.title, 'donations':
                sum(self.donations), 'num_donations': len(self.donations)}}
