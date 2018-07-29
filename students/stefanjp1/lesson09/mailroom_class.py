import sys

class Donor:
    
    def __init__(self, name, donations=None):
        self.name = name
        
        donation_list = []
        if donations:
            for donation in donations:
                donation_list.append(donation)
        
        self.donations = donation_list
        
    @property
    def donations_sum(self):
        return sum(self.donations)
    
    @property
    def donations_count(self):
        return len(self.donations)
    
    @property
    def donations_avg(self):
        return sum(self.donations) / len(self.donations)
    
    def new_donation(self, donation):
        self.donations.append(donation)
    
    def send_thank_you(self):
        return """Dear {},\n\n\tThank you for your kind donation of ${:.2f}.\n\n\t
        It will go a long way to feed the needy. \n\n\t\tSincerely, \n\n\t\t  -The Team""".format(self.name, self.donations[-1])
    
    def __lt__(self, other):
        return self.donations_sum < other.donations_sum

    def __gt__(self, other):
        return self.donations_sum > other.donations_sum

    def __eq__(self, other):
        return self.donations_sum == other.donations_sum

    def __ne__(self, other):
        return self.donations_sum != other.donations_sum



class Donor_DB:
    
    def __init__(self, donors=None):
        donor_list = []
        if donors:
            for donor in donors:
                donor_list.append(donor)
        
        self.donors = donor_list
    
    def add_donor(self, donor):
        self.donors.append(donor)
        
    def display_names(self):
        return [n.name for n in self.donors]
    
    def send_letters(self):
        for donor in self.donors:
            name = donor.name
            letter = donor.send_thank_you()
            
            file_path = name + '.txt'
            with open(file_path, 'w') as outfile:
                outfile.write(letter)

        return print('Letters saved to disk.')
    
    def create_report(self):
        sorted_report = sorted(self.donors, reverse=True)

        print("Donor Name                | Total Given | Num Gifts | Average Gift\n")
        print('------------------------------------------------------------------')
        for row in sorted_report:
            print("{:25} ${:13.2f}{:11d} ${:13.2f}".format(row.name, row.donations_sum, 
                                                row.donations_count, row.donations_avg))
        return "report printed successfully"
    
def send_thank_you():
    full_name = input("Enter the donor's full name > ")
    
    donor_names = [n.name for n in db.donors]
    
    if full_name == 'list':
        #Print the donor names and restart the function
        for n in donor_names:
            print(n)
            
        send_thank_you()
    
    try:
        amount = float( input("Enter the donation amount > ") )
    except ValueError:
        print('Donation must be a valid dollar amount, without a "$"\nRetry Send a Thank You.')
    
    if full_name in donor_names:
        match = donor_names.index(full_name)
        db.donors[match].new_donation(amount)
        return print(db.donors[match].send_thank_you())
    
    else:
        new_donor = Donor(full_name, [amount])
        db.add_donor(new_donor)
        return print(new_donor.send_thank_you())
        
    
def create_report():
    db.create_report()
    
def send_letters():
    db.send_letters()
    
    
if __name__ == '__main__':
    
    db = Donor_DB()
    db.add_donor(Donor('William Gates, III', [1000, 2000, 8000]))
    db.add_donor(Donor('Mark Zuckerberg', [666]))
    db.add_donor(Donor('Jeff Bezos', [9000, 1500]))
    db.add_donor(Donor('Paul Allen', [16000]))
    db.add_donor(Donor('Donald Trump', [2]))
    
    while True:
        prompt = input("Enter:\n Send a Thank You (1)\n Create a Report (2)\n Send Letter to Everyone (3)\n or quit (4) > ")
        
        try:
            prompt = int(prompt)
        except ValueError:
            print("Input must be an integer, try again.")
            continue
        
        prompt_dict = {1: send_thank_you,
                       2: create_report,
                       3: send_letters,
                       4:'quitting program'}
        
        try:
            user_choice = prompt_dict[prompt]
        except KeyError:
            print("Input integer was outside range of choices, try again.")
            continue
        
        if prompt != 4:
            user_choice()
        else:
            print(user_choice)
            sys.exit()