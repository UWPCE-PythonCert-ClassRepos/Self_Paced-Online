# Brandon Henson
# 5/16/18
# Lesson 09 mailroom_5.py
# Refactoring

class Donor(object):

    donor_history = {'Brandon Henson': [1005.49, 3116.72, 5200],
                    'Alicia Henson': [21.47, 1500],
                    'Michael Green': [2400.54],
                    'Brandon Henson Jr': [355.42, 579.31],
                    'Kaiya Henson': [636.9, 850.13, 125.23]}

    name_list = [i for i in donor_history]

    def __init__(self,name,*donation):
        self.donations = []
        self.name = name
        self.donation = donation
        for i in self.donation:
            self.donations.append(i)
        Donor.name_list.append(self.name)
        Donor.donor_history[self.name]=self.donation

    @property
    def total(self):
        return sum(self.donations)

    @property
    def average(self):
        return self.total/self.num_of_donations

    @property
    def num_of_donations(self):
        return len(self.donations)






def main_menu():
    arg_dict = {
        '1': menu_1,
        '2': menu_2,
        '3': email_all,
        '4': exit
    }

    prompt = '\nSelect an option:\n' \
             '[1] Send a Thank You\n' \
             '[2] Create a Report\n' \
             '[3] Send letters to everyone\n' \
             '[4] Exit\n' \

    menu_selection(prompt, arg_dict)


def menu_selection(prompt, arg_dict):
    try:
        while True:
            response = input(prompt)
            arg_dict[response]()
    except KeyError:
        print("Enter 1,2,3, or 4")


def menu_1():
    try:
        fullname = input("Enter a full name or 'list' to view all\n")
        if fullname.lower() == 'list':
            print(Donor.name_list)

        elif str(fullname) in Donor.donor_history:
            amount = int(input("Donation amount? \n"))
            newvalue = Donor.donor_history.get(fullname) + [amount]
            donor_history[fullname] = newvalue
            print("Dear {}\nThank you for your generous donation of ${}\nIt will \
     be put to good use.\n\n Sincerely,\n\
            -The Team".format(fullname, amount))
        elif str(fullname) not in Donor.donor_history:
            amount = int(input("Donation amount? \n"))
            Donor.donor_history[fullname] = amount
            print("Dear {}\nThank you for your generous donation\
     of ${}\nIt will be put to good use.\n\n Sincerely,\n\
            -The Team".format(fullname, amount))
    except ValueError:
        print("Please enter a number for the amount.")


def menu_2():
    try:
        print("\nDonor Name         |  Total Given | Num Gifts | Average Gift")
        print("------------------------------------------------------------\n")
        report = list()
        for donor, total in Donor.donor_history.items():
            report.append([donor, sum(total), len(total), sum(total)/len(total)])
        sorted_report = sorted(report, key=lambda x: -x[1])

        for i in sorted_report:
            print("{:<20}   ${:>8} {:>8}        ${:<1}".format(
                i[0], i[1], i[2], i[3]))
    except TypeError:
        print()


def email_all():
    for key, values in Donor.donor_history.items():
        filename = str(key)+'.txt'
        with open(filename, 'w') as fileobj:
            total = sum(values)
            numgifts = len(values)
            fileobj.write("Dear {}\nThank you for your {} generous donations \
totaling ${}\nThe money will be put to good use.\n\n\
        Sincerely, \n                -The Team".format(key, numgifts, total))
        fileobj.close()


if __name__ == '__main__':
    main_menu()

