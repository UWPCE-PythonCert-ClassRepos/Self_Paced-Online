import sys

class Donor:
    """Create a class that sets up one donor"""

    def __init__(self,full_name,donation_history = None):
        self.full_name = full_name
        if donation_history is None:
            self.donation_history = []
        else:
            self.donation_history = donation_history

    @property
    def name(self):
        return self.full_name

    @name.setter
    def name(self,new_name):
        self.full_name = new_name
		
    @property
    def donations(self):
        return self.donation_history

    def num_gifts(self):
        return self.donations.len()

    def total_given(self):
        return round(sum(donations),2)

    def average(self):
        return round(float(sum(donations))/float(self.donations.len()),2)

    def add_donation(self, new_donation):
        self.donations.append(new_donation)

    def letter(self):
        """Format a letter for one donor and donation"""	
        content = """ 
Dear {},

Thank you for your generous donation of ${:.2f}

Sincerely,
The Charity
""".format(str(self.full_name), float(self.donation_history[-1]))
        print(content)
        return(content)
 
class Collection:
    """Create a class that manages a collection of donors"""

    def __init__(self, full_names = None):
        if full_names == None:
            self.full_names = []
        else:
            self.full_names = full_names

    @property
    def names(self):
        return self.full_names

    def add_new(self,new_donor):
        self.names.append(new_donor)

    def list_all(self):
        return" ,".join(self.names)

    def create_report(self):
        """Build a report"""
        result = collection.calculation
        collection.table(result)
        return

    def table(self,result):
        """Make a formatted table from the sorted calculation data output"""
        table_output = ["{:<24}{:<1}{:^13}{:<1}{:^13}{:<1}{:^17}".format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')+"\n"+"-"*67]
        for row in result:
            table_output.append("{:<25}{:<1}{:>12.2f}{:>14}{:>2}{:>13.2f}".format(*row))
        table_string = "\n"+"\n".join(table_output)+"\n"
        print(table_string)
        return table_string

    def use_total(amounts):
        return amounts[2]

    def calculation(self):
        """Calculate averages and return sorted data for each donor"""
        data = []

        for donor in self.full_names:
            data.append(donor.name, donor.total_given, donor.num_gifts, donor.average)

        sorted_data = sorted(data,key=Collection.use_total,reverse=True)
        return sorted_data

    def send_all(self):
        """Write letters to all donors in text documents"""
        for donor in self.full_names:
            with open(donor.replace(' ','_')+'.txt','w') as f:
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
        return

def send_thank_you():
    """Prompt inputs for new donation data"""
    name = input("Please enter a full name > ")
	
    while name == "list":
        print(Collection.list_all)
        name = input("Please enter a full name > ")

    if name.lower() == "quit":
        return
    
    while True:
        donor = Donor(name)
        if donor not in Collection().names:
            Collection().add_new(name)
        donation = input("Donation Amount? > ")
        if donation.lower() == "quit":
            return
        try:
            donor.add_donation(donation)
            break
        except ValueError:
            print("That's not a valid donation")
		
    print("Data added!")
    donor.letter()
    return

def quit():
    """Quit the program"""
    sys.exit()

"""Add the default data to classes"""
Donor('William Gates, III', [100000.00,553784.49])
Donor('Mark Zuckerberg', [5000.00,5000.00,6396.10])
Donor('Jeff Bezos', [877.33])
Donor('Paul Allen', [100.00,100.00,508.42])

collection = Collection(['William Gates, III','Mark Zuckerberg','Jeff Bezos','Paul Allen'])

if __name__ == '__main__':
    while True:
        menu()

