import os
import sys


class Donor:
    """Container for a single donor's data, and methods to access/manipulate that data."""
    def __init__(self, name, donations=None):
        self._name = name
        if donations is None:
            self._donations = []
        else:
            self._donations = donations

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def donations(self):
        return self._donations

    def append_donations(self, amt):
        try:
            self.donations.append(float(amt))
        except ValueError:
            print("Error: donations can only be entered as integers and floats.")

    def sum_donations(self):
        return sum(self.donations)

    def number_donations(self):
        return len(self.donations)

    def avg_donations(self):
        return self.sum_donations() / self.number_donations()


class DonorDatabase:
    """Class and methods for donors in aggregate."""
    def __init__(self, donors=None):
        if donors:
            self._donors = donors
        else:
            self._donors = []

    @property
    def donors(self):
        return self._donors

    def list_donors(self):
        """List all donors by name. Called by thank_you() menu."""
        return [donor.name for donor in self.donors]

    def add_new_donor(self, donor):
        self.donors.append(donor)

    def create_report(self):
        report = ""
        for donor in self.donors:
            k = donor.name
            num_gifts = donor.number_donations()
            total_given = donor.sum_donations()
            average_gifts = donor.avg_donations()
            report = report + f'{k: <26}| ${total_given:>10.2f} |{num_gifts:^11}| ${average_gifts:>11.2f}\n'
        return report


donor1 = Donor("John Smith", [18774.48, 8264.47, 7558.71])
donor2 = Donor("Jane Doe", [281918.99, 8242.13])
donor3 = Donor("Alan Smithee", [181.97, 955.16])
donor4 = Donor("Tom D.A. Harry", [67.10, 500.98])
donor5 = Donor("Joe Shmoe", [200.01])

donor_db = DonorDatabase([donor1, donor2, donor3, donor4, donor5])


def thank_you():
    """Module with three functions:
    1) Append donation to record (if existing donor) or create a new record in database (if not an existing donor.
    2) Print thank you letter after updating database record.
    3) List all current donors in database."""
    user_input = input('Enter a donor\'s full name, or type \'list\' for a full list. ' +
                       'Type \'e\' to exit and return to the main menu.\n> ').title()
    if user_input.lower() == 'list':
        print(donor_db.list_donors())
        thank_you()
    elif user_input.lower() == 'e':
        mailroom()
    else:
        try:
            donation = float(input("Please enter a donation amount: "))
        except ValueError:
            print("Error: donations can only be entered as numbers and decimals.")
            print("Returning to previous menu...")
            thank_you()
        donor_list = donor_db.list_donors()
        for donor in donor_db.donors:
            if user_input in donor_list and donor.name != user_input:
                continue
            elif user_input in donor_list and donor.name == user_input:
                donor.append_donations(donation)
                print("Existing donor found.")
                print("Appending the amount of {0} to {1}'s file...".format(donation, user_input))
                print("Printing thank you email...")
                print("---------------------------")
                print(create_letter(0, user_input, donation))
                print("---------------------------")
                print("Returning to thank you letter menu...")
                thank_you()
            else:
                donor_db.add_new_donor(Donor(user_input, [donation]))
                print("New donor detected. Creating record for {0}...".format(user_input))
                print("Printing thank you email...")
                print("---------------------------")
                print(create_letter(1, user_input, donation))
                print("---------------------------")
                print("Returning to thank you letter menu...")
                thank_you()


def report_printing():
    """Print some user-friendly text and call report_generation() function below."""
    while True:
        print('Donor Name' + ' ' * 16 + '| Total Given | Num Gifts | Average Gift')
        print('-' * 66)
        print(donor_db.create_report())
        print('Returning to main menu...\n')
        return


def create_letter(donor_status, donor_name, donation_amt):
    """Return formatted letters, depending on options selected. Not intended to be used by itself."""
    if donor_status == 0:
        letter_text = '''
        Dear {0},

            Thank you for your very kind donation of ${1:.2f}, and for your continuing support.

            Your generous contribution will be put to very good use.

                           Sincerely,
                              -The Team
                              '''.format(donor_name, donation_amt)
        return letter_text
    elif donor_status == 1:
        letter_text = '''
        Dear {0},

            Thank you for your very kind donation of ${1:.2f}.

            Your generous contribution will be put to very good use.

                           Sincerely,
                              -The Team
                              '''.format(donor_name, donation_amt)
        return letter_text
    elif donor_status == 2:
        return('''
        Dear {0},

            Thank you for your very kind contribution(s) totaling ${1:.2f}.

            We would like you to know that your generous donation(s) will be put to very good use.

                           Sincerely,
                              -The Team
                              '''.format(donor_name, donation_amt))


def thank_all():
    """Print some user-friendly text and calls create_txt_files() function."""
    current_dir = os.getcwd()
    print("Saving letters to {0}...".format(current_dir))
    create_txt_files()
    print("---------------------------")
    print("Letters saved to text files in directory. Returning to main menu...")
    mailroom()


def create_txt_files():
    """Write letters generated by create_letter to text files, saving them to same directory as script."""

    for donor in donor_db.donors:
        name = donor.name
        donation = sum(donor.donations)
        letter = create_letter(2, name, donation)
        with open('{:s}.txt'.format(donor.name), 'w') as f:
            f.write(letter)


def mailroom():
    """Generate main menu options and activate other functions."""
    while True:
        selection = input('MAILROOM v0.5: Object-Oriented Edition\n------------------------' +
                          '\nChoose an option:\n1) Send a thank you' +
                          '\n2) Create a report\n3) Send letters to everyone\n4) Quit\n> ')
        menu_dict = {'1': thank_you, '2': report_printing, '3': thank_all, '4': quit_program}
        try:
            menu_dict.get(selection)()
        except TypeError:
            print("Invalid value. Enter a number from 1-4.")
            pass


def quit_program():
    """Quit Mailroom program."""
    print("Exiting...")
    sys.exit()


if __name__ == "__main__":
    mailroom()
