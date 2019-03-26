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

    @staticmethod
    def letter_text(name, amount):
        return f"Dear {name},\nThank you very much for your donation of ${amount:,.2f}.\nSincerely,\nMatt Casali"

    @staticmethod
    def create_name(name):
        return name + f" {now.year}{now.month:0>2d}{now.day:0>2d}" + ".txt"

    @staticmethod
    def donations_multiplier(multiplier, donations_list):
        new_donations = list(map(lambda x: x * multiplier, donations_list))
        format_donations = [f"${d:.2f}" for d in new_donations]
        return format_donations

    def filter_donations(self, min_donation, max_donation):
        return list(filter(lambda x: min_donation <= float(x) <= max_donation, self.donation))

    def donations_under(self, value):
        return list(filter(lambda x: float(x) < value, self.donation))

    def donations_over(self, value):
        return list(filter(lambda x: float(x) > value, self.donation))


class DonorActions:
    def __init__(self, donors):
        if donors is None:
            self.donors = []
        else:
            self.donors = donors

    def add_donor(self, donor):
        self.donors.append(donor)

    def all_donor_names(self):
        return [donor.full_name for donor in self.donors]

    def write_letter(self, file_name, name, amount):
        with open(file_name, "w") as f:
            f.write(Donor.letter_text(name, amount))
        print("A thank you message has been created.")

    def add_donations(self, name, amount):
        donor_name = name
        donation_amount = amount

        if donor_name not in self.all_donor_names():
            try:
                first, last = donor_name.split(" ")
                self.add_donor(Donor(first, last, [donation_amount]))
            except ValueError:
                print("Please try again and enter the donor's full name")
        else:
            for donor in self.donors:
                if donor.full_name == donor_name:
                    donor.add_donation(donation_amount)

    def send_thank_you(self, name, amount):
        self.add_donations(name, amount)
        letter_name = Donor.create_name(name)
        self.write_letter(letter_name, name, amount)

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

    def challenge(self, factor, min_donation, max_donation):
        print("\nNew Donation Amounts:\n")
        for donor in self.donors:
            filtered_donations = Donor.filter_donations(donor, min_donation, max_donation)
            print(f"{donor.full_name}:{Donor.donations_multiplier(factor, filtered_donations)}")
        print("\n")

    def projection(self, donations_under, donations_over):
        for donor in self.donors:
            double_donation = Donor.donations_under(donor, donations_under)
            triple_donation = Donor.donations_over(donor, donations_over)
            print(f"{donor.full_name}'s current donations are ${sum(donor.donation):.2f}.")
            print(f"If donations under ${donations_under:.2f} were doubled, their donations project to ${sum(double_donation):.2f}.")
            print(f"If donations over ${donations_over:.2f} were tripled, their donations project to ${sum(triple_donation):.2f}.\n")


d1 = Donor("William", "Gates, III", [326892.23, 326892.25])
d2 = Donor("Mark", "Zuckerberg", [500.00, 800.00, 20.00])
d3 = Donor("Jeff", "Bezos", [49.00, 877.33])
d4 = Donor("Paul", "Allen", [750.23, 23.53, 999.99])
d5 = Donor("Dakota", "Dakota", [10.00, 100.00, 1000.00])

dh = DonorActions([d1, d2, d3, d4, d5])

def get_name():
    return input("Who would you like to thank? If you would like a list of donors, enter 'list'. ")


def get_amount():
    try:
        return float(input(f"How much did this person donate? "))
    except ValueError:
        print("You did not enter a numeric value. Please try again.")
        sys.exit()

def multiply_donations():
    try:
        return float(input("How much would you like to multiply the donations amount by? "))
    except ValueError:
        print("Please try again and use a numeric value.")
        sys.exit()

def get_min_donations():
    try:
        return float(input("What is the minimum donation you would like to include in this multiplier? "))
    except ValueError:
        print("Please try again and use a numeric value.")
        sys.exit()

def get_max_donations():
    try:
        return float(input("What is the maximum donation you would like to include in this multiplier? "))
    except ValueError:
        print("Please try again and use a numeric value.")
        sys.exit()

def get_donations_under():
    try:
        return float(input("Under what amount would you like to double projected donations? "))
    except ValueError:
        print("Please try again and use a numeric value.")
        sys.exit()

def get_donations_over():
    try:
        return float(input("Over what amount would like to triple project donations? "))
    except ValueError:
        print("Please try again and use a numeric value.")
        sys.exit()

def main():
    choices_dic = {"1": dh.send_thank_you, "2": dh.print_report, "3": dh.send_all_letters, "4": dh.challenge,
                   "5": dh.projection}
    while True:
        print("Please choose: \n1: Send Thank You\n2: Create Report\n3: Send Letters to Everyone\n"
              "4: Multiply Donations\n5: Project Donations\n6: Quit")
        choice = input("Choice: ")

        try:
            if choice == "6":
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
            elif choice == "4":
                multiplier = multiply_donations()
                min_don = get_min_donations()
                max_don = get_max_donations()
                choices_dic.get(choice)(multiplier, min_don, max_don)
            elif choice == "5":
                under = get_donations_under()
                over = get_donations_over()
                choices_dic.get(choice)(under, over)
            else:
                choices_dic.get(choice)()
        except TypeError:
            print("You have made an invalid choice. Goodbye.")
            break


if __name__ == '__main__':
    main()
