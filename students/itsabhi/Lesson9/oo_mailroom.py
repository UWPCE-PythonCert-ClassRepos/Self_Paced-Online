#! /usr/bin/env python3


class Donor:

    donor_name = ""
    donations = []

    def __init__(self, donor, donations):
        self.donor_name = donor
        self.donations = donations

    def add_donation(self, amount):
        self.donations.append(amount)

    def sum_donations(self):
        return sum(self.donations)


class Donors:

    donors = []

    def __init__(self, initial_dlist):
        self.donors = initial_dlist

    def list_donors(self):
        # Prints donor name for each Donor object in donors list
        for d in self.donors:
            print(d.donor_name)

    def search_donors(self, donor):
        for d in self.donors:
            if donor == d.donor_name:
                return d
            else:
                return False

    def add_donor(self, new_donor):
        self.donors.append(new_donor)


def sending_thanksv2(d1):
    # If already exists, add donation amt to history, else update records as a new donor & then print thank you letter.
    donor = input("Type the Full Name of the donor here or type List to display current donors : ")
    if donor == "list":
                d1.list_donors()
                donor = input("Type the Full Name of the donor here: ")
    donor_object = d1.search_donors(donor)
    if isinstance(donor_object, Donor):
        while True:
            amount = input("Enter Donation value: ")
            try:
                donor_object.add_donation(int(amount))
            except ValueError:
                print("Invalid donation entered..")
            else:
                break
    else:
        while True:
            amount = input("Enter Donation value: ")
            try:
                new_donor = Donor(donor, [int(amount)])
                d1.add_donor(new_donor)
            except ValueError:
                print("Invalid donation entered..")
            else:
                break
    send_to = {"name": donor, "charity": int(amount)}
    print("Hello {name}, Just wanted to drop a note of thanks for your recent donation of ${charity}.".format(**send_to))
    return True


def create_report(d1):

    print("{:20s} | {:10s} | {:10s} | {:10s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for item in d1.donors:
        print("{:20s} $ {:>10d}   {:>10d} $ {:>.2f}".format(item.donor_name, item.sum_donations(), len(item.donations),
                                                            item.sum_donations()/len(item.donations)))
    return True


def sending_letters(d1):
    for item in d1.donors:
        fh = open(item.donor_name + ".txt", "w")
        fh.write("Hello {}, \nJust wanted to drop a note of thanks for your recent donation of ${}.\n"
                 .format(item.donor_name, item.donations[-1]))  #Includes the last donation amount, which is the last element of list of each dict value
        fh.writelines(["It will be put to very good use.\n\n", "Sincerely,\n\n", "The Team\n"])  # Example of writelines
        fh.close()
    return True


def quitting(d1):
    print("Quitting...")
    return False


def main():

    bill = Donor("Bill Gates", [100000, 60000, 200000])
    jeff = Donor("Jeff Bezos", [20000, 40000])
    paul = Donor("Paul Allen", [5000])
    mark = Donor("Mark Zuckerberg", [1000000])
    howard = Donor("Howard Schultz", [25000])

    initial_dlist = [bill, jeff, paul, mark, howard]
    d1 = Donors(initial_dlist)

    switch_func_dict = {'1': sending_thanksv2,
                        '2': create_report,
                        '3': sending_letters,
                        '4': quitting
                        }
    while True:
        option = input("Enter 1 to Send a Thank You!, 2 to Create a Report or 3 to Send TY Letters or 4 to Quit: ")
        try:
            if not switch_func_dict.get(option)(d1):
                break
        except TypeError:
            print("Error: Invalid option selected...{}".format(option))


if __name__ == '__main__':
    main()
