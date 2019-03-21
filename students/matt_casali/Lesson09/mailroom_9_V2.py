#!/usr/bin/env python3

import datetime, sys
now = datetime.datetime.now()

class Donor:
    def __init__(self, first_name, last_name, donation_amount):
        self.first = first_name
        self.last = last_name
        self.donation = donation_amount

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    def add_donation(self, amount):
        return self.donation.append(amount)

    def sum_donation(self):
        return sum(self.donation)

    def average_donation(self):
        return sum(self.donation)/len(self.donation)

    def number_donations(self):
        return len(self.donation)


class Donor_Actions:
    def __init__(self, donors):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    def all_donor_names(self):
        return [donor.full_name for donor in self.donors]

    @staticmethod
    def letter_text(name, amount):
        return f"Dear {name},\nThank you very much for your donation of ${amount:,.2f}.\nSincerely,\nMatt Casali"

    @staticmethod
    def create_name(name):
        return name + f" {now.year}{now.month:0>2d}{now.day:0>2d}" + ".txt"

    def write_letter(self, file_name, name, amount):
        with open(file_name, "w") as f:
            f.write(self.letter_text(name, amount))
        print("A thank you message has been created.")

    def send_thank_you(self, name, amount):
        donor_name = name
        donation_amount = amount

        if donor_name not in self.all_donor_names():
            try:
                first, last = donor_name.split(" ")
                self.add_donor(Donor(first, last, [donation_amount]))
                letter_name = self.create_name(donor_name)
                self.write_letter(letter_name, donor_name, donation_amount)
            except ValueError:
                print("Please try again and enter the donor's full name")
        else:
            for donor in self.donors:
                if donor.full_name == donor_name:
                    donor.add_donation(donation_amount)
            letter_name = self.create_name(donor_name)
            self.write_letter(letter_name, donor_name, donation_amount)

    def create_report(self):
        reports = []
        for donor in self.donors:
            reports.append([donor.full_name, donor.sum_donation(), donor.number_donations(), donor.average_donation()])
        return reports

    def print_report(self):
        print("      Donor Name       | Total Given | Num Gifts | Average Gift\n")

        for donor_report in self.create_report():
            print("{:23}${:12.2f}{:10}   ${:12.2f}".format(donor_report[0], donor_report[1], donor_report[2], donor_report[3]))

    def send_all_letters(self):
        for donor in self.donors:
            file_name = donor.full_name + '.txt'
            with open(file_name, "w") as donor_file:
                donor_file.write(f"Thank you {donor.full_name}, for your generous donation of ${sum(donor.donation):,.2f}!")
        print("Letters have been created and saved for every donor.")


d1 = Donor("William", "Gates, III", [326892.23, 326892.25])
d2 = Donor("Mark", "Zuckerberg", [500.00, 800.00, 2.00])
d3 = Donor("Jeff", "Bezos", [877.33])
d4 = Donor("Paul", "Allen", [750.23, 23.53, 999.99])
d5 = Donor("Dakota", "Dakota", [10.00, 100.00, 1000.00])

dh = Donor_Actions([d1, d2, d3, d4, d5])

def get_name():
    return input("Who would you like to thank? If you would like a list of donors, enter 'list'. ")


def get_amount():
    try:
        return float(input(f"How much did this person donate? "))
    except ValueError:
        print("You did not enter a numeric value. Please try again.")
        sys.exit()

def main():
    choices_dic = {"1": dh.send_thank_you, "2": dh.print_report, "3": dh.send_all_letters}
    while True:
        print("Please choose: \n1: Send Thank You\n2: Create Report\n3: Send Letters to Everyone\n4: Quit")
        choice = input("Choice: ")

        try:
            if choice == "4":
                break
            elif choice == "1":
                name = get_name()
                if name.lower() == "list":
                    print(dh.all_donor_names())
                    name = get_name()
                    amount = get_amount()
                    choices_dic.get(choice)(name, amount)
                else:
                    amount = get_amount()
                    choices_dic.get(choice)(name, amount)
            else:
                choices_dic.get(choice)()
        except TypeError:
            print("You have made an invalid choice. Goodbye.")
            break


if __name__ == '__main__':
    main()