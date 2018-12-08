#!/usr/bin/python


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



