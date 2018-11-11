# object oriented mailroom program
# Donor class holds individual donor information
# Manager class accesses a text file storing all donors and manages that info

class Donor:

    def __init__(self, name, *args):
        self._name = name
        self._donations = list(args)

    def append(self, addon):
        self._donations.append(addon)

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    def total_given(self):
        total = sum(self._donations)
        return total

    def number_of_gifts(self):
        number = len(self._donations)
        return number

    def average_gift(self):
        ave = sum(self._donations)/len(self._donations)
        return ave

    def write_letter(self):
        letter = "Dear {},\nThank you for your generous donation of ${:.2f}.\nSincerely,\n Generic Charities".format(self._name, self._donations[-1])
        return letter


class Manager:

    def __init__(self, database):
        self.database = database
        self.record = list()
        for line in open(database):
            self.record.append(Donor(line))

    def append(self, addname, adddonation):
        self.record.append(Donor(addname, adddonation))

    def report(self):
        print(f"Donor name" + " " * 7 + " | Total Given | Num Gifts | Average Gift\n")
        for item in self.record:
            print(f"{item.name:<18}${item.total_given():12.2f}{item.number_of_gifts():10}   ${item.average_gift():13.2f}\n")

    def check_name(self, name):
        new = False
        for item in self.record:
            if item.name == name:
                new = True
        return new

    def letters_all(self):
        for item in self.record:
            filename = item.name + ".txt"
            f = open(filename, "w")
            f.write(item.write_letter())
            f.close()

    def save_data(self):
        f = open(database, "w")
        for item in record:
            f.write(f"{item.name}, {', '.join(item.donations)}\n")
        f.close()

    def add_donation(self, name, amount):
        new = self.check_name(name)
        if new == True:
            self.append(name, amount)
        else:
            for item in self.record:
                if name == item.name:
                    item.append(amount)

    def list_donors(self):
        for item in self.record:
            print(f"{item.name}\n")


donors = Manager("donors.txt")


# this section contains input-related functions
def new_donation():
    name = input("Enter the donor's full name or \"list\" for a list of donors: ")
    if name == "list":
        donors.list_donors()
        name = input("Enter the donor's full name: ")
    amount = float(input("Enter the donation amount: "))
    donors.add_donation(name, amount)



# main function
if __name__ == "__main__":
    choice = 5
    while choice != 0:
        choice = int(input("Please enter 1 to enter a new donation, 2 to generate a report, 3 to generate letters for all donors, or 0 to quit"))
        if choice == 1:
            new_donation()
        elif choice == 2:
            donors.report()
        elif choice == 3:
            donors.letters_all()
