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
            self._donors = {}

    @property
    def donors(self):
        return self._donors

    def find_donors(self):
        """List all donors by name. Called by thank_you() menu."""
        donor_list = [k for k in self.donors]
        return donor_list

    def add_new_donor(self, name, amt):
        self.donors[name] = [amt]

    def create_report(self):
        report = ""
        for k, v in self.donors:
            num_gifts = Donor(k, v).number_donations()
            total_given = Donor(k, v).sum_donations()
            average_gifts = Donor(k, v).avg_donations()
            report = report + f'{k: <26}| ${total_given:>10.2f} |{num_gifts:^11}| ${average_gifts:>11.2f}\n'
        return report

donor_names = ["John Smith", "Jane Doe", "Alan Smithee", "Tom D.A. Harry", "Joe Shmoe"]
donation_amounts = [[18774.48, 8264.47, 7558.71], [281918.99, 8242.13], [181.97, 955.16], [67.10, 500.98], [200.01]]

donor_db = {name: donation for name, donation in zip(donor_names, donation_amounts)}


def thank_you():
    """Module with three functions:
    1) Append donation to record (if existing donor) or create a new record in database (if not an existing donor.
    2) Print thank you letter after updating database record.
    3) List all current donors in database."""
    user_input = input('Enter a donor\'s full name, or type \'list\' for a full list. ' +
                       'Type \'e\' to exit and return to the main menu.\n> ').title()
    if user_input.lower() == 'list':
        d = DonorDatabase(donor_db)
        print(d.find_donors())
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
        donor_list = DonorDatabase(donor_db).find_donors()
        for k in donor_db:
            if user_input in donor_list and k == user_input:
                DonorDatabase(donor_db).append_donations(user_input, donation)
                print("Existing donor found.")
                print("Appending the amount of {0} to {1}'s file...".format(donation, user_input))
                print("Printing thank you email...")
                print("---------------------------")
                print(create_letter(0, user_input, donation))
                print("---------------------------")
                print("Returning to thank you letter menu...")
                thank_you()
            else:
                DonorDatabase(donor_db).add_new_donor(user_input, donation)
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
        print(DonorDatabase(donor_db).create_report())
        print('Returning to main menu...\n')
        return


def report_generation():
    """Generate and return report based on donor_db."""
    report = ""
    for k, v in donor_db:
        num_gifts = len(donor_db[k])
        total_given = sum(donor_db[k])
        average_gifts = total_given / num_gifts
        report = report + f'{k: <26}| ${total_given:>10.2f} |{num_gifts:^11}| ${average_gifts:>11.2f}\n'
    return report


def create_letter(donor_status, donor_name, donation_amt):
    """Return formatted letters, depending on options selected. Not intended to be used by itself."""
    if donor_status == 0:
        letter_text = '''
        Dear {0},

            Thank you for your very kind donation of ${1}, and for your continuing support.

            Your generous contribution will be put to very good use.

                           Sincerely,
                              -The Team
                              '''.format(donor_name, donation_amt)
        return letter_text
    elif donor_status == 1:
        letter_text = '''
        Dear {0},

            Thank you for your very kind donation of ${1}.

            Your generous contribution will be put to very good use.

                           Sincerely,
                              -The Team
                              '''.format(donor_name, donation_amt)
        return letter_text
    elif donor_status == 2:
        return('''
        Dear {0},

            Thank you for your very kind contribution(s) totaling ${1}.

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

    for k, v in donor_db.items():
        letter = create_letter(2, k, sum(v))
        with open('{:s}.txt'.format(k), 'w') as f:
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
