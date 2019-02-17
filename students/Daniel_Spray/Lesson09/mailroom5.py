import sys

class Donor:
    """Create a class that sets up one donor"""

    def __init__(self,full_name,donation_history = None):
        self.name = full_name
        self.donations = donation_history if donation_history else []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,key):
        self.name = key
		
    @property
    def donations(self):
        return self.donations

    def num_gifts(self):
        return self.donations.len()

    def total_given(self):
        return round(sum(donations),2)

    def average(self):
        return round(float(sum(donations))/float(self.donations.len()),2)

    def add_donation(self, new_donation):
        self.donations.append(new_donation)
 
class Collection:
    """Create a class that manages a collection of donors"""

    def __init__(self, names = None)
        self.names = names if names else []

    @property
    def names(self):
        return self.names

    def add_new(self,new_donor):
        self.names.append(new_donor)

    def list_all(self):
        return " ,".join(self.names)
   

        












"""Establish donor data dictionary"""
donation_data = {
'William Gates, III': [100000.00,553784.49],
'Mark Zuckerberg': [5000.00,5000.00,6396.10],
'Jeff Bezos': [877.33],
'Paul Allen': [100.00,100.00,508.42]
}

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
        '2': create_report,
        '3': send_all,
        '4': quit
    }
    
    try:
        switch_menu[selection]()
    except KeyError:
        print("Sorry, I didn't recognize that command")
        return

def quit():
    """Quit the program"""
    sys.exit()

def send_thank_you():
    """Prompt inputs for new donation data"""
    name = input("Please enter a full name > ")
	
    while name == "list":
        list_of_donors = "{}, "*(len(donation_data)-1)+"{}"
        print(list_of_donors.format(*donation_data))
        name = input("Please enter a full name > ")

    if name.lower() == "quit":
        return
    
    while True:
        donation = input("Donation Amount? > ")
        if donation.lower() == "quit":
            return
        try:
            donation_data.setdefault(name,[]).append(float(donation))
            break
        except ValueError:
            print("That's not a valid donation")
		
    print("Data added!")
    letter_dictionary = {'donor':name,'amount':round(float(donation),2)}
    letter(letter_dictionary)

    return donation_data
	
def letter(letter_dictionary):
    """Format a letter for one donor and donation"""	
    content = """
Dear {donor},

Thank you for your generous donation of ${amount:.2f}

Sincerely,
The Charity
""".format(**letter_dictionary)
    print(content)
    return(content)

def create_report():
    """Build a report"""
    result = calculation()
    table(result)
    return

def table(result):
    """Make a formatted table from the sorted calculation data output"""
    table_output = ["{:<24}{:<1}{:^13}{:<1}{:^13}{:<1}{:^17}".format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')+"\n"+"-"*67]
    for row in result:
        table_output.append("{:<25}{:<1}{:>12.2f}{:>14}{:>2}{:>13.2f}".format(*row))
    table_string = "\n"+"\n".join(table_output)+"\n"
    print(table_string)
    return table_string

def use_total(amounts):
    return amounts[2]

def calculation():
    """Calculate averages and return sorted data for each donor"""
    data = []

    for donor, donations in donation_data.items():
        total_given = round(sum(donations),2)
        num_gifts = len(donations)
        average = round(float(total_given)/float(num_gifts),2)
        data.append([donor, "$", total_given, num_gifts, "$", average])

    sorted_data = sorted(data,key=use_total,reverse=True)
    return sorted_data

def send_all():
    """Write letters to all donors in text documents"""
    for person in donation_data:
        with open(person.replace(' ','_')+'.txt','w') as f:
            f.write(letter({'donor':person,'amount':donation_data[person][-1]}))
    print("Done!")

if __name__ == '__main__':
    while True:
        menu()