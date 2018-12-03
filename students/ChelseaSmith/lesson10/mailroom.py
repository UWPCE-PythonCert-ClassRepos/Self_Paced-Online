# functional mailroom program
# Donor class holds individual donor information
# Manager class accesses a text file storing all donors and manages that info
# additional functions

from functools import reduce

class Donor:

    def __init__(self, name, gifts):
        self._name = name
        self._donations = gifts

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

    def multiply_gift(self, multiple):
        newgift = [x * multiple for x in self._donations]
        newdonor = Donor(self._name, newgift)
        return newdonor



class Manager:

    def __init__(self, dictin): # changed this so I'm not pulling donor info from a file
        self.record = list()
        for k in dictin:
            self.record.append(Donor(k, dictin[k]))

    def __iter__(self):
        return iter(self.record)

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


# reverted to dictionary with donor info
record = {"James Smith": [85, 100, 75],
          "Alex Jones": [25, 25, 25],
          "Kate Smith": [100],
          "Kate Jones": [175, 50],
          "Alex Smith": [200, 200, 200]}

donors = Manager(record)


# this section contains input-related functions
def new_donation():
    name = input("Enter the donor's full name or \"list\" for a list of donors: ")
    if name == "list":
        donors.list_donors()
        name = input("Enter the donor's full name: ")
    amount = float(input("Enter the donation amount: "))
    donors.add_donation(name, amount)


# new function to create database with multiplied donations
def challenge(multiple, donors, min = 0, max = float("inf")):
    newdonors = Manager({})
    for item in donors:
        newdonors.append(item.name, map(lambda x: x * multiple, filter(lambda x: min <= x <= max, item.donations)))
    return newdonors

# function to generate total value of donation match challenge
def projection(multiple, donors, min = 0, max = float("inf")):
    record = challenge(multiple, donors, min, max)
    l = list()
    for item in record:
        l.append(item.total_given())
    totalmatch = reduce(lambda x,y: x+y, l)
    return totalmatch


#gets input for projection function
def new_projection():
    multiple = int(input("Enter match multiplier (2 to double contributions, 3 to triple contributions, etc.): "))
    min_check = input("Press Y to set a minimum donation to be matched, or any other key to continue.")
    if min_check.lower() == "y":
        min = float(input("Enter minimum donation amount: "))
    else:
        min = 0
    max_check = input("Press Y to set a maximum donation to be matched, or any other key to continue.")
    if max_check.lower() == "y":
        max = float(input("Enter maximum donation amount: "))
    else:
        max = float("inf")
    print("The total value of the match is ")
    print(projection(multiple,donors, min, max))



# main function
if __name__ == "__main__":
    choice = 5
    while choice != 0:
        choice = int(input("Please enter 1 to enter a new donation, 2 to generate a report, 3 to generate letters for all donors, 4 to create a match challenger projection, or 0 to quit"))
        if choice == 1:
            new_donation()
        elif choice == 2:
            donors.report()
        elif choice == 3:
            donors.letters_all()
        elif choice == 4:
            new_projection()
