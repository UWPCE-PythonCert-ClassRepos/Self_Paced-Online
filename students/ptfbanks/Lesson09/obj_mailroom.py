#!/usr/bin/env python3
# Lesson09 Object Mailroom exercise - ptfbanks


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

letter = ("Dear {},\n"
   "\t Thank you for your very kind donation(s) totaling $ {}.\n"
   "It will be put to very good use.\n\n"
   "\t\t Sincereley,\n"
   "\t\t   -The Team")


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
                    
        print(letter.format(donor_name, donation))

    def donation_reports(self):
        reports = []
        for donor in self.donors:
            reports.append([donor.full_name, sum(donor.donations), len(donor.donations)])
        return reports

    def report(self):
        print("|   DonorName    | TotaL Given | Num Gifts   | Avrage Gift |")
        print("|----------------|-------------|-------------|-------------|")
        for donor_report in self.donation_reports():
            print("|{:^16}|{:>13,.02f}|{:^13}|{:>13,.02f}|".format(donor_report[0], donor_report[1], donor_report[2],donor_report[1] / donor_report[2]))
        print("|----------------|-------------|-------------|-------------|") 
    def send_all(self):
        for donor in self.donors:
            file_name = donor.full_name + '.txt'
            with open(file_name, "w") as donor_file:
                donor_file.write("Thank you {}, for your generous donation of {}!".format(donor.full_name, donor.donations))

d1 = Donor('Bob', 'Williams', [5580.00, 3245.50, 1000])
d2 = Donor('Tom', 'Haskell', [345.05, 3245.90, 243.05])
d3 = Donor('Earl', 'Jackson', [4553.45, 45.6, 345.00])
d4 = Donor('Les', 'Thomas', [34.00, 325.00, 3665.00])
d5 = Donor('James', 'Black', [154, 1300, 21])
d6 = Donor('Ed', ' Jones', [35, 1])

dh = DonorHistory([d1, d2, d3, d4,d5, d6])


def main():
    while True:
        pick = input("Please select:\n"
            "     1    to enter a new donation\n"
            "     2    for a report of donors and gift history\n"
            "     3    to generate thank you letters, for one or all donors\n"
            "     4    to quit\n"
            " your selection:")
        if pick =='4':
            print('So long.....')
            break
        try:
            pick = int(pick)
        except KeyError:
            print('You request was not understood.  Plese try again.\n')            
        if pick == 1:
            dh.thank_you()
        elif pick == 2:
            dh.report()
        elif pick == 3:
            dh.send_all()

if __name__ == "__main__":
    main()
