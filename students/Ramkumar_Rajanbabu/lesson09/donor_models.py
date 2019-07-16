#Main Script

import sys

class Donor():
    """Single donor information"""
    
    def __init__(self, name, donations = None):
        self._name = name
        if donations is not None:
            self._donations = donations
        else: 
            self._donations = []
    
    def __repr__(self):
        return f"Donor: {self.name}, Donations: {self.donations}"
    
    def add_donations(self, amount):
        self.donations.append(amount)
    
    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations
    
    @property
    def total_donations(self):
        return sum(self._donations)
    
    @property
    def number_donations(self):
        return len(self._donations)
    
    @property
    def average_donations(self):
        return int(self.total_donations/self.number_donations)

class DonorCollection():
    """All donor information"""
    
    def __init__(self, donors=None):
        if donors is not None:
            self.donors = donors
        else:
            self.donors = []
    
    def add_new_donor(self, donor):
        self.donors.append(donor)
    
    def list_donor(self):
        return [donor.name for donor in self.donors]
    
    def list_donations(self):
        return [donor.donations for donor in self.donors]
    
    def send_thanks(self):
        name = None
        while not name:
            name = input_name()
            if name == "list":
                print(self.list_donor())
                name = None
        
        donation_amount = None
        while not donation_amount:
            #Exception handling
            try:
                donation_amount = input_donation()
            except ValueError: #ValueError if not integer/float
                print("Please enter an integer.")
    
        if name not in self.list_donor():
            self.add_new_donor(Donor(name, [donation_amount]))
        else:
            for donor in self.donors:
                if donor.name == name:
                    donor.add_donations(donation_amount)
        print(f"\n\tDear {name}, \n\n\tThank you for choosing to donate to this group. A special thank you for your generous donation of ${donation_amount:0.2f}. \n\n\tSincerely, \n\tDonation Society")
    
    def display_report(self):
        table = self.create_title()
        for donor_report in self.get_donor_report():
            row = "\n{:<25s}  ${:>11.2f}  {:>10d}  ${:>12.2f}".format(*donor_report) #f_string
            table += row
        print(table)
    
    def create_title(self):
        title = "\n{:<25s} | {:s} | {:s} | {:s}\n".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        title += ((len(title) - 1) * "-")
        return title
    
    def get_donor_report(self):
        reports = []
        for donor in self.donors:
            reports.append([donor.name, donor.total_donations, donor.number_donations, donor.average_donations])
        reports = sorted(reports, key=self.sort_key, reverse=True)
        return reports
    
    def sort_key(self, reports):
        return reports[1]
    
    def send_letters_all(self):
        for donor in self.donors:
            file_name = donor.name + ".txt"
            with open(file_name, 'w') as f:
                f.write(f"\n\tDear {donor.name}, \n\n\tThank you for choosing to donate to this group. A special thank you for your generous donation of ${donor.total_donations:0.2f}. \n\n\tSincerely, \n\tDonation Society")
        print("\nA thank you letter to each donor is saved as a text file.")

def input_name():
    return input("Type in the full donor name (or 'list' to view a list of donor names): ")
    
def input_donation():
    return float(input("Please enter the donation amount: "))
        
def exit_program():
    """Exit program."""
    
    print("\nYou chose to quit the program, good-bye!")
    sys.exit() #Exit script

def main():
    """Display menu with options to user."""
    
    prompt = "\n".join(("Menu: ",
                        "Please choose from below options:",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Send Letters to all donors",
                        "4 - Quit",
                        ">>> "))
    
    while True:
        #Exception Handling
        try:
            user_response = int(input(prompt))
        except ValueError: #ValueError if not integer/float
            print("Please enter a number (not a string)!")
        else:
            if user_response == 1:
                donors_db.send_thanks()
            elif user_response == 2:
                donors_db.display_report()
            elif user_response == 3:
                donors_db.send_letters_all()
            elif user_response == 4:
                exit_program()
            elif user_response not in range(1,4):
                print("Please enter a valid number within 1-4!\n")

if __name__ == "__main__":
    d1 = Donor("William Gates, III", [653772.32, 12.17])
    d2 = Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
    d3 = Donor("Jeff Bezos", [877.33])
    d4 = Donor("Paul Allen", [663.23, 43.87, 1.32])
    d5 = Donor("Ramkumar Rajanbabu", [200.30, 50.10, 5.25])
    donors_db = DonorCollection([d1, d2, d3, d4, d5])
    main()