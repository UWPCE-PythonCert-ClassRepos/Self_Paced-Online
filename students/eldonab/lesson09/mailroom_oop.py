#!/usr/bin/python
import os
import os.path

 #donor_models.py

class Donor():
    """create a class that represents a donor."""
    def __init__(self, name, donations = None):
        self.name = name
        self.donations = donations


    def add_donation(self, amount):
        """add a new donation amount"""
        self.donations.append(amount)
        

    @property
    def total_donations(self):
        """get total donation amount for a donor"""
        return sum(self.donations)


    @property
    def donations_number(self):
        """get number of donations for a donor"""
        return len(self.donations) 


    @property
    def average_donation(self):
        """calculate and get an average donation amount for a donor"""
        return self.total_donations/self.donations_number


    def __repr__(self):
        return f"[{self.name}, {self.donations}]"


    def __lt__(self, other):
        return self.total_donations < other.total_donations


    def __gt__(self, other):
        return self.total_donations > other.total_donations

    
class DonorCollection():
    """create a class that represents a collection of donors"""
    def __init__(self, *args):
        self.collection = []
        for arg in args:
            self.collection.append(arg)


    def __repr__(self):
        return f"{self.collection}"


    def is__in_list(self, name):
        """Check whether donor already exists in the list of donors."""
        for member in self.collection:
            if name == member.name:
                return True

    
    def add_donation_to_list(self, name, amount):
        """Add a new donation amount to an existing donor's name."""
        for member in self.collection:
            if name == member.name:
                member.add_donation(amount)
                print(f"Dear {member.name},\n\n\tThank you for your generous donation in the amount of ${amount}.\n\n\t\t\t\t\t\t\tSincerely, your Charity")
      

    def add_new_donor(self, name, amount):
        """Add a new donor name and donation amount."""
        self.collection.append(Donor(name, [amount]))
        print(f"Dear {name},\n\n\tThank you for your generous donation in the amount of ${amount}.\n\n\t\t\t\t\t\t\tSincerely, your Charity")
    

    def list(self):
        """print a list of donors"""
        for member in self.collection:
            print(f"{member.name}")


    def create_report(self):
        """create a formatted report with donor statistics"""
        print("{0:<20}{1:>12}{2:>12}{3:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        print("--------------------------------------------------------------")
        for member in sorted(self.collection, reverse = True):
            print("{:<20} ${:>12,.2f}{:^12} ${:>12,.2f}".format(member.name, member.total_donations, member.donations_number, member.average_donation))


#cli_main.py
Bill = Donor("Bill Gates", [500, 6000])
Jeff = Donor("Jeff Bezos", [10000, 400])
Hannah = Donor("Hannah Smith", [40000, 60000])
John = Donor("John Clark", [3000, 4000])
Andrew = Donor("Andrew Jones", [8000, 9000, 100])


donors = DonorCollection(Bill, Jeff, Hannah, John, Andrew)


def thank_you_note():
    """Send a thank you note and update the list of donors"""
    name = input("Please, type the full name of a sponsor: ")
    while name == "list":
        donors.list()
        name = input("Please, type the full name of a sponsor: ")
    while name.isnumeric():
        name = input("Please, type the full name of a sponsor. Your input should be a string: ")
    amount = int(input("How much would you like to donate? "))
    if donors.is__in_list(name):
        donors.add_donation_to_list(name, amount)
    else:
        donors.add_new_donor(name, amount)
    

def letter_to_all():
    """Write a thank you note to each donor and save it to a disk"""
    for donor in donors.collection:
        # print(donor)
        directory = str(input("Please specify the directory name for this file: "))
        filepath = os.path.join(os.sep, directory)
        total_don = donor.total_donations
        with open(f"{filepath}\\{donor.name}.txt", "w") as f:
            f.write("Dear {0},\n\n\tThank you for your very kind donation of ${1}.\n\n\t\t It will be put to very good use.\n\n\t\t\t Sincerely,\n\t\t\t -The Team".format(donor.name, total_don)) 
     

def quit():
    """exit the running program"""
    exit()
  

dict_select = {
1: thank_you_note,
2: donors.create_report,
3: letter_to_all,
4: quit
}


if __name__ == '__main__':
    while True:
        action = int(input(("Please tell us what you would like to do: 'send a thank you: type 1', 'create a report: type 2', 'send a letter to all donors: type 3', 'quit: type 4' ")))
        dict_select[action]()
    

       

    

    







