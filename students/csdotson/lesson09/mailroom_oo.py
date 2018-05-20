#!/usr/bin/env python3
# Lesson 9 - Object-oriented Mailroom

class Donor:
    """ Create Donor class representing a donor and all donations """
    def __init__(self, name, donations=[]):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be a string value")
        self.donations = donations


    @property
    def total_donation(self):
        return sum(self.donations)


    @property
    def number_of_donations(self):
        return len(self.donations)


    @property
    def average_donation(self):
        return self.total_donation / self.number_of_donations


    def __contains__(self, name):
        if name in self.name:
            return True


    def add_donation(self, donation):
        if donation < 0:
            raise ValueError("Donation can't be negative")
        self.donations.append(donation)


    def create_email(self):
        """ Create formatted email thanking donor """
        letter_details = {
            'name': self.name,
            'donation_amount': self.donations[-1]
            }
        letter = "\nDear {name},\n\nThank you so very much for your kind donation of ${donation_amount}. We can assure you that it will be put to great use.\n\nBest,\nChris".format(**letter_details)
        return letter


    def compose_letter(self):
            return (f"""Dear {self.name},

            Thank you very much for your generosity! Your most recent gift of ${self.donations[-1]} will be put to great use. So far, you've donated a total of ${self.total_donation}!

            Sincerely,
            The Team""")


    def __repr__(self):
        return "Donor({},{})".format(self.name, repr(self.donations))


    def __str__(self):
        return "Donor: {}, Donations: {}".format(self.name, self.donations)


class DonorCollection():
    """ Create container object to hold multiple donors """
    def __init__(self, donors=[]):
        self.donors = donors
        self.index = 0


    def add_new_donor(self, donor):
        self.donors.append(donor)


    def __len__(self):
        return len(self.donors)


    def __getitem__(self, index):
        return self.donors[index]


    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= len(self):
            raise StopIteration
        else:
            self.index += 1
            return self.donors[self.index - 1]


    def __contains__(self, item):
        if item in self.donors:
            return True


    def find_donor(self, name):
        current_donor = None
        for donor in self.donors:
            if name in donor:
                current_donor = donor
        return current_donor


    def list_donors(self):
        """ Create formatted list of donor names """
        donor_names = "\nList of donors:\n"
        for donor in self.donors:
            donor_names += donor.name + '\n'
        return donor_names


    def create_report_header(self):
        """ Generate formatted header for report """
        header = '{:20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift") + '\n'
        header += ("-" * len(header))
        return header


    def generate_report(self):
        """ Create formatted data for report """
        rows = ''
        for donor in self.donors:
            rows += '{:21}{:>15.2f}{:>16}{:>16.2f}'.format(
                donor.name,
                donor.total_donation,
                donor.number_of_donations,
                donor.average_donation) + '\n'
        return rows


    def write_letters(self):
        """ Generate thank you's to all donors and write files to disk """
        for donor in self.donors:
            file_name = '_'.join(donor.name.split()) + ".txt"
            with open(file_name, 'w') as f:
                f.write(donor.compose_letter())
                print(f"\nCreated letter for {donor.name}!")


    def __repr__(self):
        return "DonorCollection({})".format(repr(self.donors))


    def __str__(self):
        return "Donor collection with: {}".format(self.donors)
        # Once collection functionality added, can clean this up


### User Input Module ###
def prompt(prompt, menu):
    """ Create menu based on arguments """
    while True:
        response = input(prompt)
        try:
            if menu[response]() == "quit":
                break
        except KeyError:
            print('Please enter a valid selection!')


def send_thank_you():
    """ Create sub_prompt """
    prompt(thank_you_prompt, thank_you_menu)


def print_report():
    """ Generate donor report """
    print(donors.create_report_header())
    print(donors.generate_report())


def send_letters():
    """ Generate text files in current directory """
    donors.write_letters()


def prompt_for_donation():
    """ Prompt user for new donor/donation """
    try:
        name = input("\nPlease enter a donor name: ")
        donation = float(input(f"Please enter a donation amount for {name}: "))
    except ValueError:
        print("Please enter a numeric value for 'donation'!")
        prompt_for_donation()
    add_donation(name, donation)


def add_donation(name, donation):
    """ Add donation, create donor if necessary """
    if donors.find_donor(name):
        donor = donors.find_donor(name)
        donor.add_donation(donation)
    else:
        donor = Donor(name, [donation])
        donors.add_new_donor(donor)
    print(donor.create_email())


def print_donors():
    """ Show list of current donors """
    print(donors.list_donors())


def quit_menu():
    """ Quit current menu """
    return "quit"


# Dictionaries for menu control flow
main_menu = {
    "1": send_thank_you,
    "2": print_report,
    "3": send_letters,
    "q": quit_menu,
}

thank_you_menu = {
    "1": prompt_for_donation,
    "2": print_donors,
    "q": quit_menu,
}

# Prompts used
main_prompt = ("\nWelcome to the Main Menu! What would you like to do?\n1 - Send a Thank You\n2 - Create a Report\n3 - Send letters to everyone\nq - Quit and exit\n--> ")

thank_you_prompt = ("\nPlease choose one of the following:\n1 - Add a donation and send thank you message\n2 - Display list of current donors\nq - Return to main menu\n--> ")


### Main ###
if __name__ == "__main__":
    d1 = Donor("Bill Gates", [100.00, 20.00, 35.00])
    d2 = Donor("Jeff Bezos", [1.34, 5.67])
    d3 = Donor("Paul Allen", [167.00])
    donors = DonorCollection([d1, d2, d3])
    prompt(main_prompt, main_menu)
