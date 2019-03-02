import sys

class Donor:
    """Create a class that sets up one donor"""

    def __init__(self,full_name,donation_history = None):
        """Initialize the donor's name and history"""
        self.full_name = full_name
        if donation_history is None:
            self.donation_history = []
        else:
            self.donation_history = donation_history

    @property
    def name(self):
        """Add a name property"""
        return self.full_name

    @name.setter
    def name(self,new_name):
        """Add a name setter"""
        self.full_name = new_name
		
    @property
    def donations(self):
        """Add a donations property"""
        return self.donation_history

    def num_gifts(self):
        """Add a number of gifts property"""
        return len(self.donation_history)

    def total_given(self):
        """Add a total given property"""
        return round(sum(self.donation_history),2)

    def average(self):
        """Add an average of gifts property"""
        return round(float(sum(self.donation_history))/float(len(self.donation_history)),2)

    def add_donation(self, new_donation):
        """Make a method for adding a donation to the donor's history"""
        self.donations.append(float(new_donation))

    def letter(self):
        """Format a letter for one donor and donation"""	
        content = """Dear {},

Thank you for your generous donation of ${:.2f}.

Sincerely,
The Charity
""".format(str(self.full_name), float(self.donation_history[-1]))
        print(content)
        return(content)
		
    def __lt__(self,other):
        """Add a comparison method"""
        return self.total_given() < other.total_given()
 
    def __str__(self):
        """Add a printable string method"""
        return str(self.full_name)
		
    def __repr__(self):
        """Add a printable string method"""
        return str(self.full_name)
 
class Collection:
    """Create a class that manages a collection of donors"""

    def __init__(self, donors = None):
        if donors == None:
            self.donors = []
        else:
            self.donors = donors

    @property
    def names(self):
        """Add a names property"""
        return self.donors

    def add_new(self,new_donor):
        """Add a method for adding new donors"""
        self.donors.append(new_donor)

    def list_all(self):
        """Add a list of all donors property"""
        str_list = []
        for donor in self.donors:
            str_list.append(repr(donor))
        return", ".join(str_list)

    def create_report(self):
        """Make a formatted table"""
        sorted_donors = sorted(self.donors,reverse=True)
        data = []

        for donor in sorted_donors:
            data.append([donor.name, '$', donor.total_given(), donor.num_gifts(), '$', donor.average()])

        table_output = ["{:<24}{:<1}{:^13}{:<1}{:^13}{:<1}{:^17}".format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')+"\n"+"-"*67]
        for row in data:
            table_output.append("{:<25}{:<1}{:>12.2f}{:>14}{:>2}{:>13.2f}".format(*row))
        table_string = "\n"+"\n".join(table_output)+"\n"
        print(table_string)
        return table_string

    def send_all(self):
        """Write letters to all donors in text documents"""
        for donor in self.donors:
            with open(str(donor).replace(' ','_')+'.txt','w') as f:
                f.write(donor.letter())
        print("Done!")

def menu():
    """Create a selection menu"""
    selection = input("""This program will hopefully help you send some meaningful messages
Type the corresponding number to select from the following list:

1: Send a Thank You
2: Create a Report
3: Send Thank You to Everyone
4: Quit
>""")

    switch_menu = {
        '1': send_thank_you,
        '2': collection.create_report,
        '3': collection.send_all,
        '4': quit
    }
    
    try:
        switch_menu[selection]()
    except KeyError:
        print("Sorry, I didn't recognize that command")

def send_thank_you():
    """Prompt inputs for new donation data"""
    name = input("Please enter a full name > ")
	
    while name == "list":
        print(collection.list_all())
        name = input("Please enter a full name > ")

    if name.lower() == "quit":
        return

    donation = input("Donation Amount? > ")

    string_list = [str(names) for names in collection.names]
    while True:
        try:
            if donation.lower() == "quit":
                return
            for donor in collection.names:
                if str(donor) == name:
                    donor.add_donation(donation)
                    donor.letter()

            if name not in string_list:
                donor = Donor(name,[float(donation)])
                collection.add_new(donor)
                donor.letter()
            break
        except ValueError:
            print("That's not a valid donation")
            donation = input("Donation Amount? > ")
		
    print("Data added!")

def quit():
    """Quit the program"""
    sys.exit()

"""Add the default data to classes"""
collection = Collection([
Donor('William Gates, III', [100000.00,553784.49]),
Donor('Mark Zuckerberg', [5000.00,5000.00,6396.10]),
Donor('Jeff Bezos', [877.33]),
Donor('Paul Allen', [100.00,100.00,508.42])
])

if __name__ == '__main__':
    while True:
        menu()

