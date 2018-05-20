#!/usr/bin/env python3

import os

class Donor():

    def __init__(self, name, amount):
        if not name or not name.strip():
            raise ValueError("A non-blank name must be specified.")
        if not amount:
            raise ValueError("A donation amount must be specified.")
        self.add(amount)
        self.name = name.strip()
        self.donations = []

    def __getitem__(self, index):
        return self.donations[index]
    
    def add(self, amount):
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError(
                    "The 'amount' argument must contain a positive number.")
        else:
            self.donations.append(round(amount, 2))

    @property
    def total(self):
        if self.donations:
            return sum(self.donations)
        else:
            return 0.00

    @property
    def gifts(self):
        return len(self.donations)

    @property
    def average(self):
        if self.gifts:
            return 1.0 * self.total / self.gifts
        else:
            return '0.00'


class DonorCollection():
    items = {}

    def __init__(self):
        pass

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError(f"Donor item name '{key}' is type "
                    f"'{type(key)}' - it should be a string instead.")
        try:
            return items[key.strip()]
        except IndexError:
            raise IndexError(
                    f"Name '{key}' is not in the donor collection.")

    def add(self, name, amount):
        if not name or not name.strip():
            raise ValueError("A non-blank name must be specified.")
        if not amount:
            raise ValueError("A donation amount must be specified.")
        clean_name = name.strip()
        if clean_name in items:
            items[clean_name].add(amount)
        else:
            items[clean_name] = Donor(clean_name, amount)

class DonorUI():
    def print_list(self, collection):
        """
        Print the full list of donors.

        :collection:  The donor collection (a `DonorCollection` object).

        :return:  None.
        """
        print("\nLIST OF DONORS:")
        for donor in collection.items:
            print(donor)

    def create_report(self, collection):
        """
        Print out statistics for the entire donor list.

        :collection:  The donor collection (a `DonorCollection` object).

        :return:  None.
        """
        col_headings = (
            'Donor name', 'Total given', 'Number of gifts', 'Average gift')
        print('\n')
        print('{:<25s} |  {:>18s} | {:>15s} |  {:>18s}'.format(*col_headings))
        print('-'*25 + '-|--' + '-'*18 + '-|-' + '-'*15 + '-|--' + '-'*18)

        for i in collection.items.values():
            stats = (i.name, i.total, i.gifts, i.average)
            print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                    *stats))
        



if __name__ == '__main__':
    pass