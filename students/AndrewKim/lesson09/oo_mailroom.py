#!/usr/bin/env python3

class Donor:

    def __init__(self, first_name, last_name, donations = None):
        self.first = first_name
        self.last = last_name
        self.donations = donations

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def add_donation(self, amount):
        return self.donations.append(amount)
        
    def total_donation(self):
        return sum(self.donations)

def name_input():
    return input("Type the donor's full name: ")
        
def donation_input():
    return float(input("Please enter the donation amount: "))

class DonorHistory:
    def __init__(self, donors = None):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    def get_all_donor_names(self):
        return [donor.full_name for donor in self.donors]
    
    def thank_you(self):
        donor_name = None
        while not donor_name:
            donor_name = name_input()
            if donor_name.lower() == "list":
                print(self.get_all_donor_names())
                donor_name = None

        donation = None
        while not donation:
            try:
                donation = donation_input();
            except ValueError:
                print("Invalid input! Please enter a number:\n")

        if donor_name not in self.get_all_donor_names():
            try:
                first, last = donor_name.split(" ")
                self.add_donor(Donor(first, last, [donation]))
            except ValueError:
                print("Please enter the full name")
        else:
            for donor in self.donors:
                if donor.full_name == donor_name:
                    donor.add_donation(donation)

        print("Thank you for the donation!\n")

    def donation_reports(self):
        reports = []
        for donor in self.donors:
            reports.append([donor.full_name, sum(donor.donations), len(donor.donations)])
        return reports

    def report(self):
        print("\nDonor Name           |  Total Given | Num Gifts | Average Gift")
        print("---------------------------------------------------------------\n")
        for donor_report in self.donation_reports():
            print("{:23}${:12.2f}{:10}   ${:12.2f}".format(donor_report[0], donor_report[1], donor_report[2],donor_report[1] / donor_report[2]))
        print("\n")

    def send_all(self):
        for donor in self.donors:
            file_name = donor.full_name + '.txt'
            with open(file_name, "w") as donor_file:
                donor_file.write("Thank you {}, for your generous donation of {}!".format(donor.full_name, donor.donations))
                        
d1 = Donor("Andrew", "Kim", [5.0, 3.0])
d2 = Donor("Jamie", "Park", [4.0])
d3 = Donor("Tim", "Duncan", [3.0])
d4 = Donor("Billy", "Yan", [2.0])

dh = DonorHistory([d1, d2, d3, d4])


def main():
    while True:
        choice = input('''Please choose from a menu of 3 actions:\n
                        1 - Send a Thank You
                        2 - Create a Report
                        3 - Send letters to everyone
                        4 - Quit\n''')
        try:
            choice = int(choice)
        except ValueError:
            print("Not a valid number! Please enter a valid number\n")
            
        if choice == 1:
            dh.thank_you()
        elif choice == 2:
            dh.report()
        elif choice == 3:
            dh.send_all()
        elif choice == 4:
            break

if __name__ == "__main__":
    main()