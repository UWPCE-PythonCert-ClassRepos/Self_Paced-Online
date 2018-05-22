"""
Thomas Horn

Object Oriented refactor of mailroom_oo.py
"""

import os


class Donor:
    """
    Information about single donors.
    """
    def __init__(self, name, donations=None):
        self.name = name
        self.donations = donations

    @property
    def donor_totals(self):
        # Takes in a list --> use sum this time
        return sum(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def average_donations(self):
        return self.donor_totals / self.num_donations

    def add_donation(self, donation):
        self.donations.append(donation)

    def print_thanks(self, new_donation):
        message = f"""Dear {self.name},
        Thank you for you generous donation of ${new_donation:.2f}.
        It will truly help the children.

        Sincerely,
        Donation Recievers"""
        print(message)

    """
    OO Sorting.
    """
    def __lt__(self, other):
        return self.donor_totals < other.donor_totals

    def __gt__(self, other):
        return self.donor_totals > other.donor_totals

    # def __eq__(self, other):
    #     return self.donor_totals == other.donor_totals and other.donor_totals == self.donor_totals
        

class DonorList:
    """
    Holds a list of donor objects.

    Performs following after user inputs a donor:
        'list' input --> shows a list of donor names and reprompts
        adds donor if they do not exist or uses existing user
        prompts for a donation amd adds to donor
        prints thank you note
    """
    def __init__(self, donors=None):
        # Accepts only a list of donors now
        self.donors = donors

    def list_donor_names(self):
        donor_names = [donor.name for donor in self.donors]
        return '\n'.join(donor_names)

    def add_donation(self, target_donor, new_donation):
        target_donor.add_donation(new_donation)
    
    def add_donor_and_donation(self, target_donor, new_donation):
        """ Called for a brand new donor only.  Creates new donor object """
        new_donor = Donor(target_donor, [new_donation])
        self.donors.append(new_donor)

        # Thank the donor
        new_donor.print_thanks(new_donation)

    def determine_donor_status(self, target_donor, new_donation):
        if target_donor in self.donors:
            self.add_donation(target_donor, new_donation)
        else:
            self.add_donor_and_donation(target_donor, new_donation)     
    
    def send_thanks(self, target_donor, new_donation):
        """ Determines if the donor exists and gets the donation amount. """
        # Find donor or create and add new donor object.
        self.determine_donor_status(target_donor, new_donation)
        # self.print_thanks(target_donor, new_donation)

    def order_donors(self):
        """ 
        Orders the donors based on the sum of their total donations. 
        """
        ordered_donors = []
        for donor in self.donors:
            ordered_donors.append([donor])
        
        # Sorts on class default donor totals
        ordered_donors.sort(reverse=True)
        return ordered_donors
        
    def create_report(self):
        """ Prints a report based ordered by total donations. """
        # Base setup
        line_out = ''
        line_out += "Donor:                    | $    Total     |   Donations   | $   Average   |\n"
        line_out += ("-"*76) + '\n'
        
        # Setup line format to recieve ordered donor info 
        line_in = "{:<26}| ${:>14,.2f}|{:>15}| ${:>13,.2f}\n"
        ordered_donors = self.order_donors()

        # Donor object itself is contained in a list. [[donor1], [donor2]].  Peel that away to access properties.
        for info in ordered_donors:
            for donor in info: 
                line_out += line_in.format(donor.name, donor.donor_totals, donor.num_donations, donor.average_donations)

        print(line_out)

    def create_letters(self):
        """ Creates text files for each donor in the list. """
        for donor in self.donors:
            outletter = os.path.join(os.getcwd(), f'{donor.name}_ty_letter.txt')
            with open(outletter, 'w+') as f:
                message = f"""Dear {donor.name[0]},
                Thank you for you generous donation of ${donor.donor_totals:.2f}.
            It will truly help the children.


            Sincerely,
            Donation Receivers
        """
                f.write(message)

    def quitter(self):
        print("Quitting.")
        quit()
    

def main():
    """ Controls the menu. """
    donor1 = Donor("Tom Horn", [599.23, 1000.00])
    donor2 = Donor("Theo Hartwell", [0.01, 0.01, 0.1])
    donor3 = Donor("Bailey Kimmitt", [8723.22, 27167.22, 91817.66])
    donor4 = Donor("Paul Hubbell", [90012.32, 2312.24])
    donor5 = Donor("David Beckham", [1817266.11, 123123.66, 111335.112])
    donors = DonorList([donor1, donor2, donor3, donor4, donor5])

    while True:
        choice = input(
        "Please select an option:\n\
        1 - Send Thanks\n\
        2 - Create Donor Report\n\
        3 - Send Letters\n\
        4 - Quit\n")
        print()
        if choice == '1':
             # Get donor
            target_donor = input("Please enter the donor's full name.  ")
            # Get donation
            try:
                new_donation = float(input("Please enter the donation amount for {}.  ".format(target_donor)))
            except ValueError:
                print("Please enter a number.  ")
            donors.send_thanks(target_donor, new_donation)
        if choice == '2':
            donors.create_report()
        if choice == '3':
            donors.create_letters()
        if choice == '4':
            donors.quitter()

if __name__ == "__main__":
    main()
