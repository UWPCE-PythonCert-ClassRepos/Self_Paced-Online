#!/usr/bin/env python3


class Donor:
    """creates objects for individual donors"""
    def __init__(self, title, last_name, donation):
        self.title = title
        self.last_name = last_name
        self.donations = [donation]
        super().__init__()

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
        return self.donations[-1]

    @donation.setter
    def donation(self, donation):
        """enables addition of new donation"""
        self.donations.append(donation)


class DonorGroup(Donor):
    """creates donor group objects for multiple donors"""
    def __init__(self, *donors):
        self.donors = [*donors]
        super().__init__(*donors)

    @property
    def donor_group(self):
        return [donor.donor for donor in self.donors]
