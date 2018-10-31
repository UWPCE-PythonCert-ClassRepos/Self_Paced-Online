#!/usr/bin/env python3

from functools import reduce

class Donor:

    def __init__(self, name, list_donations):
        self._name = name
        self._list_donations = list_donations
        self._donation_count = len(list_donations)
        self._amount = sum(list_donations)

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def add(self, donation_amount):
        self._amount += donation_amount
        self._donation_count += 1
        self._list_donations.append(donation_amount)

    @property
    def donation_count(self):
        return self._donation_count

    @property
    def average(self):
        return self._amount / self._donation_count

    def get_letter_text(self, name, amount):
        msg = []
        msg.append('Dear {},'.format(name))
        msg.append('\n\n\tThank you for your very kind donation of ${:.2f}.'.format(amount))
        msg.append('\n\n\tIt will be put to very good use.')
        msg.append('\n\n\t\t\t\tSincerely,')
        msg.append('\n\t\t\t\t-The Team\n')
        return "".join(msg)

    def challenge(self, factor, min_donation=None, max_donation=None):
        """Get the sum of projection donation from a donor"""
        new_list = []
        if min_donation is not None and max_donation is not None:
            #filter minimum & maximum
            new_list = list(filter(lambda donation: donation >= min_donation, self._list_donations))
            new_list = list(filter(lambda donation_amount: donation_amount <= max_donation, new_list))
            new_list = list(map(lambda x: x*factor, new_list))
        elif min_donation is None and max_donation is not None:
            #filter maximum
            new_list = list(filter(lambda donation: donation <= max_donation, self._list_donations))
            new_list = list(map(lambda x: x*factor, new_list))
        elif min_donation is not None and max_donation is None:
            # filter minimum
            new_list = list(filter(lambda donation: donation >= min_donation, self._list_donations))
            new_list = list(map(lambda x: x*factor, new_list))
        else:
            # no minimum and maximum
            new_list = list(map(lambda x: x*factor, self._list_donations))

        return sum(new_list)

    def __lt__(self, other):
        return self._amount < other._amount

    def __gt__(self, other):
        return self._amount > other._amount

    def __eq__(self, other):
        return self._amount == other._amount

class Donations:

    def __init__(self):
        """collection of donors"""
        self._donors = {'William Gates, III': Donor('William Gates, III', [100.00, 200.00]),
                    'Mark ZuckerBerg': Donor('Mark ZuckerBerg', [300.00, 400.00])}

    def add(self, donor):
        """ add donor"""
        # existing donor
        if donor.name in self._donors.keys():
            d =self._donors[donor.name]
            # update donation amount
            d.add(donor.amount)
        else:
            # new donor
            self._donors[donor.name] = donor
    @property
    def donors(self):
        return self._donors

    def generate_report(self):
        """Generate report"""
        report = []
        report.append("--------------------------------------------------------------")
        msg = "{:20} | {:10} | {:5} | {:10}".format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        report.append(msg)
        report.append("--------------------------------------------------------------")
        for k, v in sorted(self._donors.items(), key=lambda value: value[1], reverse=True):
            a_row = '{:20}  $ {:>10.2f}  {:>10d}  $ {:>11.2f}'.format(k, v.amount,v.donation_count,v.average)
            report.append(a_row)
        return "\n".join(report)

    def challenge(self, factor, min_donation=None, max_donation=None):
        """ Get a list of projection donation sum from  all donors"""
        new_list = list(map(lambda item: item.challenge(factor, min_donation, max_donation), self._donors.values()))
        return new_list

    def projections(self,factor, min_donation=None, max_donation=None):
        """ Total projections from all donors"""
        return sum(self.challenge(factor, min_donation, max_donation))