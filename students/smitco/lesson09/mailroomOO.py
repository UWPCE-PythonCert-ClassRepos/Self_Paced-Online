# lesson 09 mailroom object oriented
# !/usr/bin/env python3


import os
import datetime


class Donor(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def donor_email(self, name, amount):
        self.amount = amount
        print("\nThank you, {}, for your generous donation of ${} "
              "to the Brave Heart Foundation.".format(self.name, self.amount))

class AllDonors(object):
    donors = {}
    
    def __init__(self, *args, **kwargs):
        self.donors["John Travolta"] = [5000,7500]
        self.donors["Jane Fonda"] = [10000, 8000, 6500]
        self.donors["Judy Blume"] = [3000, 3000]
        self.donors["Joey Tribbiani"] = [9000]
        self.donors["Jenny Gump"] = [10300, 13750, 12500]

    def donor_append(self, name, amount):
        self.name = name
        self.amount = amount
        if self.name in self.donors:
            self.donors[self.name].append(self.amount)
        else:
            self.donors[self.name] = [self.amount]        

    def donor_details(self):
        self.donor_details = {}
        for d in self.donors:
            total = sum(self.donors[d])
            count = len(self.donors[d])
            average = total/count
            self.donor_details[d] = [total, count, average]
        sorted_details = sorted(self.donor_details.items(), 
                                key=lambda x: x[1], reverse=True)
        self.details = sorted_details
    
    def donor_report(self):
        self.donor_details()
        print("\n{:<20} {:<15} {:^12} {:<15}".format("Donor", "Total Given", 
              "Number", "Average Given"))
        for i in range(len(self.details)):
            info = {"donor_name": self.details[i][0],
                    "donor_total": self.details[i][1][0],
                    "donor_count": self.details[i][1][1],
                    "donor_avg": self.details[i][1][2]}
            print("{donor_name:<20} ${donor_total:^15.2f} "
                  "{donor_count:^12} ${donor_avg:^15.2f}".format(**info))
        print()
    
    def donor_letters(self):
        self.donor_details()
        current = datetime.datetime.now()
        date = [str(current.month), str(current.day), str(current.year)]
        current_date = "_".join(date)
        for d in self.donor_details:
            letter = ("Dear {},\n\n"
                      "Thank you for supporting The Brave Heart Foundation.\n"
                      "Your donations totaling ${} have made a\n"
                      "positive, life-changing impact for teens nationwide.\n\n"
                      "Blessings,\n"
                      "BHF".format(d, self.donor_details[d][0]))
            letter_name = (d + " " + current_date + ".txt")
            with open(letter_name, "w") as donor_letter:
                donor_letter.write(letter)
        print("\nFiles completed.\n")
            
    
def menu():
    ask = input("Please choose an action:\n"
                "1) Send a new thank you\n"
                "2) Create a report\n"
                "3) Send letters to all donors\n"
                "4) Quit\n"
                ">>")
    options = {"1": thank_you, "2": report, "3": letters, "4": quit}
    try:
        options[ask]()
    except KeyError or NameError:
        print("\nThere was an error. Please try again.\n")

def thank_you():
    flag = True
    while flag == True:
        addressee = input("\nTo whom would you like to send a thank you?\n"
                          "'List' will display current donors.\n"
                          "'Exit' will return to main menu.\n"
                          ">>") 
        donor = Donor(addressee)
        all_donors = AllDonors()
        if donor.name.lower() == "list":
            print(list(all_donors.donors.keys()))
        elif donor.name.lower() == "exit":
            print("\nExiting.\n")
            flag = False
        else:
            donation = input("\nWhat is the donation amount?\n>>")
            try:
                if donation == "exit":
                    print("\nExiting.")
                elif int(donation) >= 10**6:
                    print("\nThe amount entered is too large.")
                else:
                    donation = int(donation)
                    donor.donor_email(addressee, donation)
                    all_donors.donor_append(addressee, donation)
            except ValueError:
                print("\nInvalid entry.")


def report():
    all_donors = AllDonors()
    all_donors.donor_report()

def letters():
    all_donors = AllDonors()
    all_donors.donor_letters()

def quit():
    print("\nGoodbye.")
    exit()


if __name__ == '__main__':
    while True:
        menu()
