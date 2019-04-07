import os
import sys



class Donor(object):
    def __init__(self, name, donation_list):
        self.name = name
        self.donations = donation_list
        self._donation_total = sum(donation_list)
        self._donation_average = self._donation_total / len(self.donations)

    @property
    def donation_total(self):
        self._donation_total = sum(self.donations)
        return self._donation_total

    @property
    def donation_average(self):
        self._donation_total = self.donation_total
        self._donation_average = self._donation_total/len(self.donations)
        return self._donation_average

    def add_donation(self, donation):
        self.donations.append(donation)

    def create_letter(self):
        """Return form letter string."""
        return ('Dear {},'
                '\n\n\tThank you for your generous gift of ${}.'
                '\n\tYour contribution will keep {} Fleebs floobing for an entire year.'
                '\n\tWe truly could not do this important work without you.'
                '\n\nSincerely,'
                '\nFleeb Freedom Now'.format(self.name, self.donations[-1], self.donations[-1]/20))


class DonorCollection(object):
    def __init__(self, donor_dict):
        self.donors = []
        for key in donor_dict.keys():
            self.donors.append(Donor(key, donor_dict[key]))

    def add_donor(self, donor, donation):
        self.donors.append(Donor(donor, donation))

    def create_report_table(self):
        """Take input dictionary and create a sorted list of tuples based on key and values."""
        report_table_header = [("Donor Name", "Total Given", "Num Gifts", "Average Gift")]
        report_table = []

        for d in self.donors:  # read dict values into 2D list to be displayed.
            report_table += self.generate_table_row(d.name, d.donations)

        report_table = report_table_header + sorted(report_table, key=lambda k: float(k[1][1:]), reverse=True)
        return report_table

    @staticmethod
    def generate_table_row(name, donation_list):
        """Take input name and donation list and return a list of a single tuple of strings."""
        total_given = sum(donation_list)
        num_gifts = len(donation_list)
        try:
            average_gift = total_given / num_gifts
        except ZeroDivisionError:
            average_gift = '0'
        return [(name, '$' + str(total_given), str(num_gifts), '$' + str(average_gift))]

    @staticmethod
    def max_column_width(table):
        """Take an input table  and return a list with each value representing the most characters in each column."""
        column_width_list = []  # list for the longest characters in each column
        for i in range(len(table[0])):
            column_length = 0
            for row in table:
                if len(str(row[i])) > column_length:
                    column_length = len(str(row[i]))
            column_width_list.append(column_length)
        return column_width_list

    @staticmethod
    def add_column_spaces(cwl, spaces=3):
        """Return list of column spaces with additional spaces, default = 3"""
        for i in range(len(cwl)):
            cwl[i] += spaces
        return cwl

    @staticmethod
    def create_report_formstring(mtl):
        """Return a form string based on the column widths from mtl list."""
        form_string = []
        for i in mtl:
            form_string.append('{:' + str(i) + '}')
        form_string = ''.join(form_string)
        return form_string

    def display_report(self):
        """Generate report based on existing donors and donations. Display in variable column widths."""
        report_table = self.create_report_table()
        mcw = self.max_column_width(report_table)  # list of max width of each column in report table
        mcw = self.add_column_spaces(mcw)
        form_string = self.create_report_formstring(mcw)

        print('\n\n')  # Begin printing out table
        print(form_string.format(*report_table.pop(0)))
        print('{}'.format('-' * sum(mcw)))  # spacer line between header and body of table
        for row in report_table:
            print(form_string.format(*row))

    def write_letters(self):
        """Take input dictionary and write form letter to txt file based on key and last item in value."""
        for d in self.donors:
            name = d.name.replace(' ', '_')
            with open('{}.txt'.format(name), 'w') as f:
                f.write(d.create_letter())

    @staticmethod
    def is_name_list(donor_name):
        if donor_name == 'list':
            for d in ddb:  # display all donor names on user input 'list'
                print(d + ': ', ddb[d])
            return True
        else:
            return False

    def is_name_existing(self, donor_name):
        """Check if 'donor_name' value exists in global dict ddb, case insensitive."""
        for i in self.donors:
            if i.name.lower() == donor_name.lower():
                return True
        else:
            return False

def goodbye():
    print("goodbye!")
    sys.exit()


def new_thank_you():
    while True:
        donor = input("\nEnter donor name, or type 'list' for current donor list:")
        if not d.is_name_list(donor):
            break
    if d.is_name_existing(donor):
        print(f"Donor name {donor} found in database.")
        while True:
            try:
                donation = float(input('\nEnter new donation amount:'))
                break
            except ValueError:
                print("Input was not a number.")
        for i in d.donors:
            if i.name == donor:
                i.add_donation(donation)
                print('\n\n', i.create_letter())
    else:
        print(f"Donor name not found. Will add {donor} to database.")
        while True:
            try:
                donation = float(input('\nEnter donation amount:'))
                break
            except ValueError:
                print("Input was not a number.")
        d.add_donor(donor, [donation])
        print('\n\n', d.donors[-1].create_letter())


def letters_to_all():
    user_input = input("Would you like save to current directory,{}? >(y,n)".format(os.getcwd()))
    if user_input == 'n':
        path = input("Enter full path to desired directory: ")
        os.chdir(path)
    d.write_letters()


def main():
    # Initiate top user menu.
    while True:
        user_input = input('\n\nMENU:\n'
                           '1 - Send a Thank You for a New Donation\n'
                           '2 - Create a Report\n'
                           '3 - Send letters to everyone\n'
                           '4 - Quit\n'
                           'Please enter 1-4>')
        user_menu = {'1': new_thank_you,
                     '2': d.display_report,
                     '3': letters_to_all,
                     '4': goodbye}
        try:
            user_menu[user_input]()
        except KeyError:
            print('\nOption not found. Please enter the numeral 1,2,3 or 4')


ddb = {'Archie Bunker': [20, 100, 75, 98],
       'Beyonce Knowles': [2000000, 50000000],
       'Charlie Kauffman': [12345],
       'David Sedaris': [23000, 1200, 2000],
       'Edvard Munch': [1, 2, 3]}

d = DonorCollection(ddb)

if __name__ == '__main__':
    main()
