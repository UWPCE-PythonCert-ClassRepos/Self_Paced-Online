#!/usr/bin/env python3
import sys
import ast
import copy
from datetime import date
from functools import reduce


###
class Individual_Donor:
    # _donations = {'Date1': [Donation1], 'Date2': [Donation2, Donation3]}

    def __init__(self, donor_name, donation_amt, donation_date=str(date.today())):
        self._name = donor_name
        self._donations = {}
        self.add_dollars(donation_amt, donation_date)

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def length(self):
        return len(self.donations)

    def __getitem__(self, key):
        if key not in self.donations:
            raise KeyError(key)
        else:
            return(self.donations[key])

    def __setitem__(self, key):
        pass  # use add_dollars instead

    def add_dollars(self, donation_amt, donation_date=str(date.today())):
        if donation_date in self.donations:
            self.donations[donation_date].append(float(donation_amt))
        else:
            self.donations[donation_date] = [float(donation_amt)]

    def report_total_donations(self):
        return round(sum(amt for day in self.donations for amt in self.donations[day]), 2)

    def report_total_num_gifts(self):
        total_num_gifts = 0
        for day in self.donations:
            for amt in self.donations[day]:
                total_num_gifts += 1
        return total_num_gifts

    def latest_donation(self):
        dates = []
        for k in self.donations:
            dates.append(k)
        dates.sort(reverse=True)
        return dates[0]
###


###
class Group_Donors:
    # list of Individual_Donor objects

    def __init__(self):
        self._donor_obj_list = []

    @property
    def donor_obj_list(self):
        return self._donor_obj_list

    @property
    def donor_list(self):
        return [obj.name for obj in self.donor_obj_list]

    @property
    def length(self):
        return len(self.donor_list)

    def __getitem__(self, data):
        if type(data) is int:
            if data >= self.length:
                raise IndexError('list index out of range')
            else:
                return self.donor_list[data]
        elif type(data) is str:
            if data in self.donor_list:
                return self.donor_obj_list[self.donor_list.index(data)]
            else:
                raise KeyError(data)

    def __setitem__(self, num, name):
        pass

    #
    # Donor methods
    def add_donor(self, name):
        if type(name) == Individual_Donor:
            self._donor_obj_list.append(name)
        else:
            raise TypeError('object must be type \'Individual_Donor\'')

    def add_donation(self, name, amt, day=str(date.today())):
        if name in self.donor_list:
            self[name].add_dollars(amt, day)
        else:
            self.add_donor(Individual_Donor(name, amt, day))

    #
    # Saving methods
    def save_donor_list(self, filename):
        temp_dict = {}
        for obj in self.donor_obj_list:
            temp_dict[obj.name] = obj.donations
        with open(filename, 'w') as outfile:
            outfile.write(str(temp_dict))

    def load_donor_list(self, filename):
        self._donor_obj_list = []
        temp_str = open(filename).read()
        temp_data = self.parser(temp_str)
        for name in temp_data:
            for day in temp_data[name]:
                for amt in temp_data[name][day]:
                    self.add_donation(name, amt, day=day)

    def parser(self, str):
        return ast.literal_eval(str)

    #
    # new Donor List methods
    def create_challenge_list(self, factor, min_donation, max_donation):
        gd_challenge = self.create_obj_copy()
        gd_challenge.filter_donations(min_donation, max_donation)
        gd_challenge.challenge_list_maker(factor)

        filename = input("Enter file name for Challenge file> ")
        gd_challenge.save_donor_list(filename)
        # instructions say to return new group_donor object, but I think saving
        # it as a seperate file (which can be loaded later) is better

    def create_obj_copy(self):
        new_copy = copy.deepcopy(self)
        return new_copy

    def challenge_list_maker(self, factor):
        for donor in self.donor_list:
            for day in self[donor]._donations:
                self[donor]._donations[day] = list(map(lambda x: round(x * factor, 2), self[donor]._donations[day]))

    def filter_donations(self, min_donation, max_donation):
        if min_donation:
            for donor in self.donor_list:
                for day in self[donor]._donations:
                    self[donor]._donations[day] = list(filter(lambda x: x > min_donation, self[donor]._donations[day]))
        if max_donation:
            for donor in self.donor_list:
                for day in self[donor]._donations:
                    self[donor]._donations[day] = list(filter(lambda x: x < max_donation, self[donor]._donations[day]))


###


### User interactions ###
# mode 1 - add a donation and send a thank you
def input_name(obj):
    name = input("Please enter a full name (or type \'list\', or hit \'return\' to go back)> ")
    if name == "list":
            print('\n')
            print('\n'.join(obj.donor_list))
            print('\n')
    elif name == "":
        return None
    else:
        return name


def input_dollars(name, obj):
    dollars = input("Please enter a donation amount (ex: 500.05)> ")
    try:
        float(dollars)
        if float(dollars) > 0:
            obj.add_donation(name, float(dollars))
            return float(dollars)
        else:
            return None
    except ValueError:
        raise ValueError("Donation amounts must be numbers")


def thank_you(name, dollars):
    print(f"Dear {name},\n\nThank you for your donation of {dollars:.2f}.\n\nLove,\nThe Charity Org")


def add_donation_to_list(obj):
    while True:
        name = input_name(obj)
        if not name:
            break
        dollars = input_dollars(name, obj)
        if name and dollars:
            thank_you(name, dollars)


# mode 2 - "create a report"
def sort_by_dollars(donor_lists):
    try:
        donor_lists.sort(key=lambda k: k[1], reverse=True)
    except IndexError:
        print('This list can not be sorted.')
        print(donor_lists)


def create_donor_list(obj, max_length = 4):
    # create [[donor name, total donations, # gifts, avg gift], [donor 2 info]]
    temp_list = []
    for i, name in enumerate(obj.donor_list):
        temp_list.append([name, obj[name].report_total_donations(), obj[name].report_total_num_gifts(), (obj[name].report_total_donations() / obj[name].report_total_num_gifts())])
    sort_by_dollars(temp_list)

    for lst in temp_list:
        for i in range(4 - max_length):
            lst.pop()

    return temp_list


def print_donor_report(temp_donor_list):
    if len(temp_donor_list[0]) == 2:
        print('\n')
        print("Donor Name                | Total Given ")
        print("----------------------------------------")
        for row in temp_donor_list:
            print("{:<27}{:>14.2f}".format(*row))
        print('\n')

    elif len(temp_donor_list[0]) == 4:
        print('\n')
        print("Donor Name                | Total Given |   Num Gifts |  Average Gift")
        print("---------------------------------------------------------------------")
        for row in temp_donor_list:
            print("{:<27}{:>14.2f}{:>14}{:>14.2f}".format(*row))
        print('\n')


def create_report(obj):
    temp_donor_list = create_donor_list(obj)
    print_donor_report(temp_donor_list)


# mode 3 - "send letters"
def plural_donate(n):
    if n > 1:
        return 'donations totaling'
    else:
        return 'donation of'


def send_letters(obj):
    for name in obj.donor_list:
        with open(name + '.txt', 'w') as outfile:
            outfile.write(f"Dear {name},\n\tThank you for your {plural_donate(obj[name].length)} {obj[name].report_total_donations():.2f}.\n\tIt will be put to good use.\n\n\tSincerely,\n\t- The Team")


# mode 4 - "save_list"
def save_list(obj):
    location = input("Enter file name> ")
    try:
        obj.save_donor_list(location)
        print("File saved")
    except FileNotFoundError:
        print("File not found")


# mode 5 - "load list"
def load_list(obj):
    print("Loading a list will erase current list.")
    location = input("Enter a file name to continue, or press 'Enter' to return to menu> ")
    if location:
        try:
            obj.load_donor_list(location)
            print("File loaded")
        except FileNotFoundError:
            print("File not found")


# mode 6 - challenges
def parse_filter(filt):
    if filt[0] == '>':
        return float(filt[1:]), None
    elif filt[0] == '<':
        return None, float(filt[1:])
    else:
        raise SyntaxError("filter must start with '<' or '>'")


def challenge(obj):
    print("Enter factor by which to multiply current donations, or press 'Enter' to return to menu")
    print("(i.e., if \"2\", then donations 10, 50, 100 become 20, 100, 200")
    factor = float(input("> "))
    if not factor:
        return

    print("Enter a filter to include specific donations. To include all donations, press 'Enter'")
    filt = input("(e.g., '<50' will include donations under 50. '>100' will include donations over 100)> ")
    if filt:
        min_donation, max_donation = parse_filter(filt)

    obj.create_challenge_list(factor, min_donation, max_donation)  # uses filter() and map()


# mode 7 - Display challenge
def display_challenge(obj):
    filename = input("Enter file name of challenge you want to display> ")
    temp_gd = Group_Donors()
    temp_gd.load_donor_list(filename)
    temp_donor_list = create_donor_list(temp_gd, max_length=2)  # uses sum()
    print_donor_report(temp_donor_list)


# mode 8 - "quit"
def end_program(obj):
    print("Thanks for playing along.")
    sys.exit()


# main
def main():
    gd = Group_Donors()
    menu_dict = {"1": add_donation_to_list, "2": create_report, "3": send_letters, "4": save_list, "5": load_list, "6": challenge, "7": display_challenge, "8": end_program}
    while True:
        print("Choose a number:")
        print("(1) Add a donation")  # and send a thank you
        print("(2) Create a Report")
        print("(3) Send letters to everyone")
        print("(4) Save current donor list")
        print("(5) Load donor list")
        print("(6) Create donor challenge list")
        print("(7) Display challenge")
        print("(8) quit")
        mode = input("> ")
        if mode in menu_dict:
            menu_dict.get(mode)(gd)
        else:
            print("Please enter a number 1 - 7")
            continue


if __name__ == '__main__':
    main()

def make_group_for_testing():
    gd1 = Group_Donors()
    gd1.add_donor(Individual_Donor('John Doe', 500.05))
    gd1.add_donor(Individual_Donor('Jane Doe', 333.33))
    return gd1