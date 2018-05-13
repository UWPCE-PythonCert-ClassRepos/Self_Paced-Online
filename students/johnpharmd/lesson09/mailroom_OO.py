#!/usr/bin/env python3


class Donor:
    """creates objects for individual donors"""
    def __init__(self, title, last_name, donation):
        # fixme: self.ID = 0
        self.title = title
        self.last_name = last_name
        self.donations = [donation]
        super().__init__()

    @property
    def donor(self):
        """getter for individual donor"""
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
        """getter for most recent donation amount"""
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
    def donorgroup(self):
        """getter for self.donors"""
        return [donor.donor for donor in self.donors]

    @donorgroup.setter
    def donorgroup_new_donor(self, new_donor):
        """enables addition of new donor"""
        self.donors.append(new_donor)

    def withdraw(self, title, last_name):
        """given donor last name as string, removes donor from self.donors"""
        for d in self.donors[:]:
            if last_name in d.donor and d.donor[last_name]['title'] == title:
                self.donors.remove(d)

    def get_list(self):
        self.donor_list = []
        for d in self.donors:
            for last_name in d.donor:
                self.donor_list.append([d.donor[last_name]['donations'], last_name,
                                        d.donor[last_name]['num_donations']])
        return sorted(self.donor_list, reverse=True)

    def get_report(self):
        print()
        psv = ['Donor Name', '| Total Given', '| Num Gifts',
               '| Average Gift']
        print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
              psv[2], psv[3]))
        for i in range(55):
            print('-', end='')
        print()
        new_list = self.get_list()
        for donor_list in new_list:
            formatted_donor = ('{:<15}'.format(donor_list[1])
                               + '{}{:>10}'.format(' $', donor_list[0])
                               + '{:>13}'.format(donor_list[2])
                               + '{}{:>11}'.format(' $',
                               donor_list[0] // donor_list[2]))
            if __name__ != '__main__':
                print(formatted_donor)
            # return formatted_donor

    def save_data(self):
        with open('test.txt', 'w') as outfile:
            outfile.write('This is current DonorGroup data:\n' +
                          str(self.donorgroup))
