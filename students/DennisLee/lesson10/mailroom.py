#!/usr/bin/env python3

import os
from functools import reduce

class Donor():
    """Contains methods and properties for a single donor."""

    def __init__(self, name, amount):
        """Initialize with the donor name & initial donation amount."""
        if not name or not name.strip():
            raise ValueError("A non-blank name must be specified.")
        self.name = name.strip()
        self.donations = []
        self.add(amount)

    def __repr__(self):
        return f"Donor('{self.name}', '{self.donations}')"

    @property
    def total(self):
        """Return the cumulative donation amount from the donor."""
        if self.donations:
            return sum(self.donations)
        else:
            return 0.00

    @property
    def gifts(self):
        """Return the total number of donations from the donor."""
        return len(self.donations)

    @property
    def average(self):
        """Return the average donation amount from the donor."""
        if self.gifts:
            return 1.0 * self.total / self.gifts
        else:
            return 0.00

    @property
    def largest(self):
        """Return the largest donation amount from the donor."""
        if self.gifts:
            return max(self.donations)
        else:
            return 0.00

    @property
    def smallest(self):
        """Return the smallest donation amount from the donor."""
        if self.gifts:
            return min(self.donations)
        else:
            return 0.00

    @property
    def latest(self):
        """Return the most recent donation amount from the donor."""
        if self.gifts:
            return self.donations[-1]
        else:
            return 0.00
        

    def add(self, amount):
        """Add new amount(s) to the donor's gift history."""
        if isinstance(amount, (int, float)):
            amount = [amount]
        amts = list(filter(lambda x: isinstance(x, (int, float)) 
                and x > 0.005, self.donations + list(amount)))
        if amts:
            self.donations = list(map(lambda x: round(x, 2), amts))

    @property
    def form_letter(self, index=-1):
        """
        Create a thank you form letter for a specific donation.

        :index:  An index to a certain gift within the donation history.
                 This value defaults to the most recent gift amount.

        :return:  A string containing the filled-in form letter.
        """
        if index not in range(-self.gifts, self.gifts):
            raise IndexError(f"Donor '{self.name}' has donated '{self.gifts}' "
                    f"times, so gift # '{index}' is out of range.")
        text = """\n\n\n
                From:     Random Worthy Cause Foundation
                To:       {0:s}
                Subject:  Your generous donation

                Dear {0:s},

                We want to express our gratitude for your donation of ${1:,.2f}
                {2:s}to the Random Worthy Cause Foundation.  To show our
                appreciation, we have enclosed a set of address labels
                and a custom tote bag that lets people know that you are a
                generous supporter of our cause.
                
                Thank you again, and please think of us the next time you want
                to give to a worthy cause.

                Sincerely,



                Mister E. Partner
                Random Worthy Cause Foundation

                """
        text = '\n'.join([line.lstrip() for line in text.splitlines()])
        # If a donor has given before, add a parenthetical clause 
        # stating the total donation amount and number of donations
        extra = ''
        if self.gifts > 1:
            extra = '(and total donations of ${0:,.2f} from {1:,d} gifts)' \
                    '\n'.format(self.total, self.gifts)
        
        return text.format(self.name, self.donations[index], extra)
    

class DonorCollection():
    """Contains methods and properties for an entire donor roster."""

    def __init__(self):
        """Create a dict of donor names and associated `Donor` objects."""
        self.donors = {}
        self.factor = 1.0
        self.floor = 0.0
        self.ceiling = 1.0e12

    def __repr__(self):
        return "DonorCollection()"

    def __getitem__(self, key):
        """
        Allows a specific donor to be referenced as an index of this
        donor collection object.

        :key:  The name of the donor.

        :return:  The `Donor` object associated with the donor name.
        """
        if not isinstance(key, str):
            raise TypeError(f"Donor item name '{key}' is type "
                    f"'{type(key)}' - it should be a string instead.")
        try:
            return self.donors[key.strip()]
        except IndexError:
            raise IndexError(
                    f"Name '{key}' is not in the donor collection.")

    def add(self, name, amount):
        """
        Add a new donation with the specified donor name and amount.
        If the donor is not currently in the donation history, a new
        entry is added to the `donors` dict.

        :name:  The name of the donor.

        :amount:  The amount(s) given. Multiple amounts can be specified
                  by using a list or a tuple.

        :return:  None.        
        """
        if not name or not name.strip():
            raise ValueError("A non-blank name must be specified.")
        clean_name = name.strip()
        if clean_name in self.donors:
            self.donors[clean_name].add(amount)
        else:
            self.donors[clean_name] = Donor(clean_name, amount)

    def print_donors(self):
        """
        Print the full list of donors.

        :return:  None.
        """
        print("\nLIST OF DONORS:")
        for donor in self.donors:
            print(donor)
        print("\n")

    def create_report(self):
        """
        Print out statistics for the entire donor roster.

        :return:  None.
        """
        col_headings = (
                'Donor name', 'Number of gifts', 'Total given', 'Latest gift', 
                'Average gift', 'Largest gift', 'Smallest gift')
        print('\n')
        print(('{:<25s} | {:>15s}' + 5*' |  {:>18s}').format(*col_headings))
        print('-'*25 + '-|-' + '-'*15 + 5*('-|--' + '-'*18))

        for i in self.donors.values():
            if i.gifts:
                stats = (i.name, i.gifts, i.total, i.latest, 
                        i.average, i.largest, i.smallest)
                print(('{:<25s} | {:>15d}' + 5*' | ${:>18,.2f}').format(*stats))
        print('\n')

    def save_letters(self, folder=""):
        """
        Save the donor thank-you letters to disk.

        :folder:  The folder in which to save the files. If an invalid
                  folder is specified or no folder is specified, the
                  current folder is used. If the folder does not exist,
                  the method attempts to create the folder and save
                  the letters in the created folder.

        :return:  The folder containing the thank-you letters.
        """
        cur_dir = os.getcwd()
        if not folder:
            folder = cur_dir
        try:
            os.mkdir(folder)
        except FileExistsError:  # Okay if folder already exists
            pass
        finally:  # Save each letter, with donor name in each file name
            os.chdir(folder)
            folder = os.getcwd()  # Set folder name to the full OS path

            # Create dict of letter names+letter texts, then write files
            letters = {
                    f'_{k}.txt': v.form_letter for k, v in self.donors.items()
            }
            for filename, text in letters.items():
                lines = text.splitlines()
                with open(filename, 'w') as f:
                    for line in lines:
                        f.write(line + '\n')
            os.chdir(cur_dir)
            return folder

    def challenge(self, factor, min_donation=0.0, max_donation=1e12):
        """
        Create new donor collection with gifts multiplied by an amount.

        :factor:  The amount to multiply all existing gifts by.

        :return:  A `DonorCollection` object containing the new list of
                  donations.
        """
        new_coll = DonorCollection()
        name_and_donations = self.projector(factor, min_donation, max_donation)
        new_coll.donors = dict(map(self.map_to_collection, name_and_donations))
        return new_coll

    def projector(self, factor, min_donation, max_donation):
        """
        Project a donor list with gifts multiplied by a certain amount.

        :factor:  The amount to multiply all existing gifts by.

        :return:  A list of donor names and projected donation lists.
        """
        self.factor = float(factor)
        if self.factor <= 0.0:
            raise ValueError(f"The 'factor' argument is '{self.factor}' - "
                    "it should be a positive number.")
        self.floor = float(min_donation)
        self.ceiling = float(max_donation)

        # Create temp 2-member tuple containing donor name, and the old
        # donation list
        donor_map = list(map(  
                lambda x: tuple((x, self.donors[x].donations)), 
                list(self.donors)))

        # Filter the donor history for min and max donations
        filtered_donor_map = list(map(self.filter_mapper, list(donor_map)))

        # Do multiplication on the filtered donation list
        transformed_donors = list(map(self.multiply_mapper, filtered_donor_map))
        return transformed_donors
        
    def filter_mapper(self, x):
        """
        Filter out all current donations that are below a minimum value
        or are above a maximum value.

        :x:  A list of 2-member tuples, where the first member is the
             donor name, and the second member is the original donation
             list for this donor.

        :return:  A map of 2-member tuples, where the first member is
                  the donor name, and the second member is the filtered
                  list of original donations.
        """
        return (x[0], 
                list(filter(lambda y: self.floor <= y <= self.ceiling, x[1]))
        )
        
    def multiply_mapper(self, x):
        """
        Multiply all donations in a donation list by a certain number
        (the `factor` class member).

        :x:  A list of 2-member tuples, where the first member is the
             donor name, and the second member is the original donation
             list (filtered or unfiltered) for this donor.

        :return:  A map of 2-member tuples, where the first member is
                  the donor name, and the second member is the
                  multiplied donation list. 
        """
        return (x[0], 
                list(map(lambda y: round(y * self.factor, 2), x[1]))
        )

    def map_to_collection(self, x):
        """
        Map the name/donation list tuple to a name/`Donor` object tuple.

        :x:  A map of 2-member tuples, where the first member is the
             donor name, and the second member is the multiplied
             donation list (filtered or unfiltered).

        :return:  A map of 2-member tuples, where the first member is
                  donor name, and the second member is a `Donor` object
                  containing the name and the multiplied donation list.
        """
        return (x[0], Donor(x[0], x[1]))

    def projection_sum(self, donation_list):
        """
        Get cumulative value of a name/donation list tuple.

        :x:  A map of 2-member tuples, where the first member is the
             donor name, and the second member is the donation list
             (multiplied and filtered, if requested).

        :return:  A single number value, representing all numbers in
                  the donation lists of each donor added up.
        """
        all_gifts = reduce(lambda x, y: x + y, dict(donation_list).values())
        return round(sum(all_gifts), 2)
