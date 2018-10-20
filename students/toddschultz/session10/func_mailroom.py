import os

class Donor:
    ''' Information about the individual donors '''

    def __init__(self, name, donations=None):
        self.name = name
        self.donations = donations
    
    @property
    def total_given(self):
        return sum(self.donations)

    @property
    def num_gifts(self):
        return len(self.donations)

    @property
    def average_gift(self):
        return self.total_given / self.num_gifts

    def append_donation(self, donor, current_donor, current_donation):
        ''' appends a new donation to an existing donor ''' 
        self.donations.append(float(current_donation))     

    def send_thanks(self, current_donation):
        print("\nDear", self.name, ":")
        print("Thank you very much for your generous donation.")
        print("Your gift of $" + current_donation, "will help our efforts greatly.\n")
        print("Sincerely - ACME Charity")



class DonorCollection: 
    ''' Information on the entire group of donors '''
    def __init__(self, donors=None):
        self.donors = donors

    def create_report(self): 
        print("\nDonor Name\t\t| Total Given | Num Gifts | Average Gift")
        print("-" * 64)
        everyone = []
        for donor in self.donors:
            everyone.append([donor])
        for info in everyone:
            for donor in info: 
                print("{:<22}".format(donor.name).title(), "  $", "{:11.2f}".format(donor.total_given), "\t\t{:<2}".format(donor.num_gifts), "{:2}".format("$"), "{:10.2f}".format(donor.average_gift))

    def send_letters(self):
        everyone = []
        for donor in self.donors:
            everyone.append([donor])
        for info in everyone:
            for donor in info: 
                with open('/Users/toddschultz/Projects/' + donor.name + ".txt", 'w') as f:
                    f.write("\n\n" + donor.name + ":\n\tThank you very much for your generous donations. ")
                    f.write(f"your donation total of ${donor.total_given:.2f} is awesome! ")
                    f.write("Our charity would not exist without your support.\\n")
                    f.write("Sincerely:\n\nLeadership Team at Charity X.\n\n")
        print("Letters Complete!\n")

    def does_donor_exist(self, current_donor, current_donation):
        ''' determines if the donor is already in the collection '''
        x = 0 
        for donor in self.donors:
            if donor.name == current_donor:
                donor.append_donation(donor, current_donor, current_donation)
                donor.send_thanks(current_donation) 
                break 
        else:
            self.new_donor(current_donor, current_donation)  

    def new_donor(self, current_donor, current_donation):
        ''' adds a new donor to the collection '''
        new_donor = Donor(current_donor, [int(current_donation)])
        self.donors.append(new_donor)
        new_donor.send_thanks(current_donation)

    def threshold_direction(self, num):
        return num >= 1100


    def above(self, value, threshold):
        return value > float(threshold)

    def below(self, value, threshold):
        return value < float(threshold)

    def challenge(self, donors, factor, threshold, direction):
        print("\nHere are the current donations", direction, "$", threshold, ":")
        total_a = 0
        for d in self.donors:
            gifts = filter(lambda x : self.above(x, threshold) if direction == 'above' else self.below(x, threshold), d.donations)
            for i in gifts:
                total_a = total_a + i
                print("%.2f" % i)
        print("For a total of: $", total_a)
        print("\nHere are all the donations", direction, "$", threshold, "multiplied by",factor ,":")
        total_b = 0
        for d in self.donors:
            gifts = map(lambda x : x * float(factor), \
                filter(lambda x : \
                    self.above(x, threshold) if direction == 'above' else self.below(x, threshold), d.donations))
            for i in gifts:
                total_b = total_b + i
                print("%.2f" % i)
        print("For a new total of: $", ("%.2f" % total_b))
        print("\nThis challenge would make you: $", ("%.2f" % (total_b - total_a)), "more monies!")

def quit_program():
    exit()

def its_go_time():
    ''' Keep user interactions out of the classes '''
    d1 = Donor("baby huey", [1123.00, 456.00, 1789.00])
    d2 = Donor("mighty mouse", [99.99, 9000.00])
    d3 = Donor("fred flintstone", [555.00, 5555.00])
    d4 = Donor("road runner", [199999.00, 10.00, 8.00])
    d5 = Donor("papa smurf", [1001.00, 1002.00, 1003.00, 1200.00, 12.00])
    donors = DonorCollection([d1, d2, d3, d4, d5]) 

    while True:
        selection = input("\nMAIN MENU\n"
                "what option would you like?\n"
                "1 - Send a Thank You\n"
                "2 - Create a report\n"
                "3 - Send letters\n"
                "4 - Challenge\n"
                "5 - Exit\n"
                ">>> ")
        if selection == '1':
            current_donor = input("Who would you like to send a Thank You too? ")
            current_donation = input("What was the amount of the donation? ")
            donors.does_donor_exist(current_donor, current_donation)
        elif selection == '2':
            donors.create_report()
        elif selection == '3':
            donors.send_letters()
        elif selection == '4':
            factor = input("By what factor would you like to multiply the donations? ")
            threshold = input("What threshold would you like to use? ")
            direction = input("Would you like to multiply donations above or below that threshold? ")
            donors.challenge(donors, factor, threshold, direction)
        elif selection == '5':
            quit_program()
        else:
            print("Please enter 1, 2, 3, 4 or exit")

if __name__ == "__main__":
    its_go_time()
