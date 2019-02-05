"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    February 2nd 2019
"""
'''
Mailroom 10 with adding challenge function (Donors Class) which uses a Map
and a Filter per the instructions in lesson 10
'''
class Donor():

    def __init__(self, name, donation=0):
        self._name = name
        if donation != 0:
            self._donations = [donation]
        else:
            self._donations = []

    #String dunder allowing for human readable string output
    def __str__(self):
        return str(self._name)

    """Adds a donation to a donor"""
    def add_donation(self, donation):
        self._donations.append(donation)

    """Adds a list of donations to the donor"""
    def add_multiple_donations(self, donations):
        for amount in donations:
            self._donations.append(amount)

    #Property for the donor name
    @property
    def name(self):
        return self._name

    #Setter for the donor name
    @name.setter
    def name(self, name):
        self._name = name

    #Property for the donor donations
    @property
    def donations(self):
        return self._donations

    #Propety to return the total of all donations inside this donor
    @property
    def total(self):
        return sum(self._donations)


class Donors():

    def __init__(self):
        self._donors = []

    #String dunder allowing for human readable string output
    def __str__(self):
        return ', '.join(donor.name for donor in self._donors)

    """Add a new donor"""
    def append(self, donor):
        self._donors.append(donor)

    #Return a donor if found using a passed in name
    def get_donor(self, name):
        for donor in self._donors:
            if donor.name == name:
                return donor

    #Print function for the donor and donations in a collection of donors
    def print_all(self):
        return ', '.join(donor.name + str(donor.donations) for donor in self._donors)

    #Donor dictionary return for use with the mailroom program
    def donor_dict(self):
        donor_send = {}
        for donor in self._donors:
            donor_send[donor.name] = donor.donations
        return donor_send

    #Challenge function takes a required 'factor' and optional min/max
    def challenge(self, factor, min_donation=0, max_donation=0):
        new_donors = Donors()
        for donor in self._donors:
            new_donor = Donor(donor.name)
            donations = donor.donations
            if min_donation and max_donation != 0:
                donations = filter(lambda n: n < max_donation and n > min_donation, donor.donations)
            elif min_donation != 0:
                donations = filter(lambda n: n > min_donation, donor.donations)
            elif max_donation != 0:
                donations = filter(lambda n: n < max_donation, donor.donations)
            new_donor.add_multiple_donations(list(map(lambda n: n * factor, donations)))
            new_donors.append(new_donor)
        return new_donors

###############################################################################
donor1 = Donor('Adam Alvarez')
donor1.add_donation(1.25)
donor2 = Donor('Beth Bonnor', 2.73)
the_donors = Donors()
the_donors.append(donor1)
the_donors.append(donor2)

#Letters to everyone
def letters():
    all_donors = the_donors.donor_dict()
    for donor in all_donors:
        name = donor
        donations = the_donors.get_donor(donor).total
        with open(donor + '.txt', 'w') as out_file:
            out_file.write(thank_you_specific(donor, donations, 'letter'))
    print("Your thank you letters have been written to your relative folder.")

#Called by the display report function. Build and return a new table
def create_report(donor_table):
    donor_table.sort(key = lambda x: x[1], reverse = True)
    report = (
              f"\n\n\n{'Donor Name':<18}{'| Total Given':>13}"
              f"{' | Num Gifts ':>12}{' | Average Gift':>12}\n" + ("-" * 59)
              )
    for donor in donor_table:
        report = report + ('\n{:<18}${:>12.2f}{:>8}      ${:>13.2f}'.format(*donor))
    report = report + ("\n")
    return report

#Create a report to display of the donors and their contributions
def display_report():
    donor_table = []
    donors = the_donors.donor_dict()
    for key in donors:
        count = len(donors[key])
        d_sum = f"{sum(donors[key]):.2f}"
        avg = f"{float(d_sum) / count:.2f}"
        donor_table.append([key, float(d_sum), count, float(avg)])
    print(create_report(donor_table))

#Display the thank you note or write a letter.
def thank_you_specific(donor, amount, form):
    if form == 'letter':
        body = (f"{donor}, \n\n    Your donations of ${float(amount):.2f}"
             + " have gone a long way and we value your continued support."
             + "\n\nSincerely,\nDonation Center\n(555) 555-5555")
    elif form == 'note':
        body = (f"\n{donor}, \n\n    Your donation of ${float(amount):.2f} "
                + "was received and we are forever grateful for your support."
                + "\n\nSincerely,\nDonation Center\n(555) 555-5555")
    return body

#Called by the thank you function - will gather the donation amount and add the donor
def donation_amount(name):
    while True:
        donation = input("How much is the donation? ")
        if donation.lower() == 'q':
            return
        try:
            donation = float(donation)
            if the_donors.get_donor(name):
                the_donors.get_donor(name).add_donation(donation)
            else:
                the_donors.append(Donor(name, donation))
            print(thank_you_specific(name, donation, 'note'))
            return
        except ValueError:
            print('Non Numeric Value Entered')

#Thank you function for the first available option.
def thank_you():
    print("\n(You can type \"list\" to display current donors)")
    name = input("What is the First and Last name of the recipient? ")
    if name.lower() == 'q':
        return
    while name.lower() == 'list':
        print()
        print(the_donors)
        print()
        name = input("Type a full name from the list or provide a new one? ")
        if name.lower() == 'q':
            return
    donation_amount(name)

#Function to run the calculations on the projections and output the results
def format_projections(name):
    print("\nAnswer the following questions and we will return a projection.")
    print("\"If you would like no minimum or max - just type '0' and hit enter")
    multiplier = input("Multiplier? ")
    minimum = input("Minimum Donation to calculate? ")
    maximum = input("Maximum Donation to calculate? ")
    donors = the_donors.challenge(int(multiplier), int(minimum), int(maximum))
    out_donor = donors.get_donor(name)
    out_donations = ', '.join(str(donation) for donation in out_donor.donations)
    print("\n\n-->Name: " + out_donor.name + '\n---->Projected Donations: ' + out_donations)

#Function for projections on donors inside of the current donor list.
def projections():
    print("\n(You can type \"list\" to display current donors)")
    name = input("Which donor would you like to run projections? ")
    if name.lower() == 'q':
        return
    while name.lower() == 'list':
        print()
        print(the_donors)
        print()
        name = input("Type a full name from the list or provide a new one? ")
        if name.lower() == 'q':
            return
    format_projections(name)

#First function to be called and to make sure the program runs.
def start_up():
    choices = {'q':exit, '1':thank_you, '2':display_report,'3':letters, '4':projections}
    while True:
        print("\n\nWhat would you like to do? (Enter a Number or \'q\' to quit)")
        print("TIP: \'q\' - anywhere else brings you back to this menu.")
        action = input("\n1:Send a Thank you | 2:Create a Report | "
                       "3:Send letters to everyone | 4:Projections | or quit?  ")
        choice = action.lower()
        try:
            choice = choices[choice]
            choice()
        except KeyError:
            print("Invalid Choice - Please choose again.")

if __name__ == "__main__":
    start_up()