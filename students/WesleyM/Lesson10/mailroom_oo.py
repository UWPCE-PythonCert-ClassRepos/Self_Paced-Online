from functools import reduce

class Donor:
    def __init__(self, name, donation=None):
        self.donation = donation if donation is not None else []
        self.name = name
    @property
    def total(self): 
        return sum(self.donation)

    @property
    def average(self):
        if donation:
            return self.total/len(self.donation)
        else:
            return 0
    
    def add_donation(self, amount):
        self.donation.append(amount)
        self.total += amount
        self.average = self.total / len(self.donation)
    
    def factor_donation(self, factor, min_donation, max_donation):
        return list(map(lambda x: x * factor,
                        self.filter_donations(self.donation,
                                              min_donation, max_donation)))
    
    @staticmethod
    def filter_donations(donations, min_donation, max_donation):
        if max_donation is None:
            return list(filter(lambda x: x >= min_donation, donations))
        else:
            return list(filter(lambda x: min_donation <= x <= max_donation,
                               donations))

class DonorDatabase:

    def __init__(self, name=None):
        self.donors = [] if name is None else name
    
    def add_donor(self, name):
        self.donors.append(name)
        
    def get_donor(self, name):
        for d in self.donors:
            if d.name == name:
                return d

    def get_all_donor_names(self):
        return [donor.name for donor in self.donors]
        
    def sort_donors(self):
        return sorted(self.get_all_donor_names())
    
    def donor_input(self):
        return input("Enter a donor name or input 'List' for a list of donors\n>")
    
    def send_thankyou(self):
        don_input = None
        while not don_input:
            don_input = self.donor_input()
            if don_input.lower() == "list":
                print(self.sort_donors())
                don_input = None

        donation = None
        while not donation:
            try:
                donation = self.donation_prompt()
            except ValueError:
                print("Enter donations numerically")

        if don_input in self.get_all_donor_names():
            for d in self.donors:
                if d.name == don_input:
                    d.add_donation(donation)
        else:
            try:
                d2 = Donor(don_input, [donation])
                self.add_donor(d2)
            except ValueError:
                print("Please enter a name")

        print("Thank you {} for your donation of ${:.2f}"
              .format(don_input, donation))
    
    def donation_prompt(self):
        return float(input("Enter a donation amount \n>"))
    
    def send_letters(self):
        for d in self.donors:
            file_name = d.name.lower().replace(' ', '_', 3) + '.txt'
            with open(file_name, 'w') as f:
                f.write("""Dear Ms./Mrs./Mr./Dr. {x}, \n We are thankful for your donation of ${y}. Your donation will be used for (insert harmful activity here). We hope you donate again soon!""".format(x = d.name, y = d.total))

    def create_report(self):
        print("Donor Name           | Total Given   | Num Gifts     | Average Gift  |\n" + "-"*70)
        for d1 in self.donors:
            print('{:20} | {:13} | {:13} | {:15}'.format(d1.name, d1.total, len(d1.donation), d1.total / len(d1.donation)))
    
    def close_program(self):
        print('\nClosing Program\n')

    def challenge(self, factor, min_donation=0, max_donation=None):
        donor_db2 = DonorDatabase()
        for donor in self.donors:
            d1 = donor.factor_donation(factor, min_donation, max_donation)
            donor_db2.add_donor(Donor(donor.name, d1))
        donor_db2.create_report()
        return donor_db2

    def projection(self, projection_input):
        factor = projection_input[0]
        min_donation = projection_input[1]
        max_donation = projection_input[2]
        donor_db2 = self.challenge(factor, min_donation, max_donation)
        total = reduce(lambda x, y: x + y,
                       map(lambda x: x.total, donor_db2.donors))
        print(f'\nProjected Contribution is ${total:.2f}')

def user_input():
    try:
        action = int(input("\nChoose one of six actions: \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letter to Everyone \n 4. Create Challenge Factor Report \n 5. Create Projections \n 6. Quit \n>"))
    except ValueError:
        print("\nEnter 1 to 'Send a Thank You', 2 to 'Create a Report',\n3 to 'Send Letter to Everyone', 4 to 'Create a Challenge Factor Report', 5 to 'Create Projections', or 6 to 'Quit'\n")
    else:
        if action not in choices:
            print("\nEnter 1 to 'Send a Thank You', 2 to 'Create a Report',\n3 to 'Send Letter to Everyone', 4 to 'Create a Challenge Factor Report', 5 to 'Create Projections', or 6 to 'Quit'\n")
    return action

def factor_input():
    while True:
        try:
            return float(input('Input challenge factor: '))
        except ValueError:
            print('\nChallenge factor must be numerical. Please try again.')

def projection_input():
    while True:
        try:
            projection1 = int(input('\nEnter a challenge factor > \n'))
            projection2 = int(input('\nEnter a minimum donation > \n'))
            projection3 = int(input('\nEnter a maximum donation > \n'))
            return [projection1, projection2, projection3]
        except ValueError:
            print('\nChallenge factor, min donation, and max donation must be numerical. Please try again.')


donors = [
    Donor('Alice Adams Ron', [20]),
    Donor('Bob Be-Lake', [100]),
    Donor('Charles Cruz', [30, 50, 10]),
    Donor('Denise Dnice', [10, 5]),
    Donor('Edward Eduardo', [25, 20, 20, 20, 10])
    ]
    
donor_db = DonorDatabase(donors)

choices = {1: donor_db.send_thankyou, 2: donor_db.create_report, 3: donor_db.send_letters, 4: lambda: donor_db.challenge(factor_input()), 5: lambda: donor_db.projection(projection_input()), 6: donor_db.close_program}
    
def main():
    action = 0

    while action != 6:
        try:
            action = user_input()
            choices[action]()
        except KeyError:
            print("Please enter a number from the options given")

if __name__ == "__main__":
    main()
