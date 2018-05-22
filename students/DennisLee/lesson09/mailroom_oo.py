#!/usr/bin/env python3

import os

class Donor():

    def __init__(self, name, amount):
        if not name or not name.strip():
            raise ValueError("A non-blank name must be specified.")
        if not amount:
            raise ValueError("A donation amount must be specified.")
        self.name = name.strip()
        self.donations = []
        self.add(amount)

    def __repr__(self):
        return "Donor(name, amount)"

    @property
    def total(self):  # Cumulative donation amount
        if self.donations:
            return sum(self.donations)
        else:
            return 0.00

    @property
    def gifts(self):  # Number of donations
        return len(self.donations)

    @property
    def average(self):  # Average donation amount
        if self.gifts:
            return 1.0 * self.total / self.gifts
        else:
            return '0.00'

    @property
    def largest(self):  # Largest donation amount
        if self.gifts:
            return max(self.donations)
        else:
            return '0.00'

    @property
    def smallest(self):  # Smallest donation amount
        if self.gifts:
            return min(self.donations)
        else:
            return '0.00'

    def add(self, amount):
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError(
                    "The 'amount' argument must contain a positive number.")
        else:
            self.donations.append(round(amount, 2))

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

    def __init__(self):
        self.donors = {}

    def __repr__(self):
        return "DonorCollection()"

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError(f"Donor item name '{key}' is type "
                    f"'{type(key)}' - it should be a string instead.")
        try:
            return self.donors[key.strip()]
        except IndexError:
            raise IndexError(
                    f"Name '{key}' is not in the donor collection.")

    def add(self, name, amount):
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
        Print out statistics for the entire donor list.

        :return:  None.
        """
        col_headings = (
                'Donor name', 'Number of gifts', 'Total given', 
                'Average gift', 'Largest gift', 'Smallest gift')
        print('\n')
        print(('{:<25s} | {:>15s}' + 4*' |  {:>18s}').format(*col_headings))
        print('-'*25 + '-|-' + '-'*15 + 4*('-|--' + '-'*18))

        for i in self.donors.values():
            stats = (i.name, i.gifts, i.total, i.average, i.largest, i.smallest)
            print(('{:<25s} | {:>15d}' + 4*' | ${:>18,.2f}').format(*stats))
        print('\n')

    def save_letters(self, folder=""):
        """
        Save the donor thank-you letters to disk.

        :folder:  The folder in which to save the files. If an invalid
                  folder is specified or no folder is specified, the
                  current folder is used. If the folder does not exist,
                  the method attempts to create the folder to continue.

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
