#!/usr/bin/python
from operator import itemgetter

# Lesson 09, Mailroom Part 5 Assignment


class UserInputs(object):

    @staticmethod
    def get_menu_option():
        sel_ = input("------> "
                     "Select an option from the menu: ")
        return sel_

    @staticmethod
    def get_donation_amount(donor_name_):
        amount_ = input("\nEnter the donation amount for {} ".format(donor_name_))
        return amount_

    @staticmethod
    def get_donors_name():
        name_ = input("\nPlease enter the donor's full name: ")
        return name_


class DonorData(object):

    def __init__(self):
        self.donor_data_ = {}

    @property
    def donor(self):
        pass

    @donor.setter
    def donor(self, name):
        self.donor_data_[name] = []

    def delete_donor(self, name):
        self.donor_data_.pop(name)

    def add_donation(self, name, donation):
        if not(name in self.donor_data_):
            self.donor_data_[name] = donation
        else:
            self.donor_data_[name].append(donation)
            print("adding printer")

    def list_display(self):
        print("\n---- List of all Donors ----")
        [print("- {}".format(item)) for item in self.donor_data_]
        print("----------------------------")

    @staticmethod
    def list_details(data):
        header = "\n{:<18}| {:<12}| {:<10}| {:<12}".format("Donor Name", "Total "
                                                                         "Given", "Num Gifts",
                                                           "Average Gift")
        buffer = "------------------------------------------------------------------"
        print(header)
        print(buffer)
        for item in sorted(data, key=itemgetter(-2), reverse=True):
            print("{:<18} $  {:>9.2f}  {:>10}  $   {:>9.2f}".format(item[0], item[2], item[1], item[3]))

    def calc_data(self):
        summary_data = [[] for data in self.donor_data_]
        for i, item in enumerate(self.donor_data_.keys()):
            donations_quantity = len(self.donor_data_[item])
            donations_value = sum(self.donor_data_[item])
            donations_average = (float(donations_value / donations_quantity))
            summary_data[i].extend([item, donations_quantity, donations_value, donations_average])
        return summary_data


# ------- Global Assignments -------
donor_data = {'John Marks': [5000.34, 2500, 1267],
              'Matt Smith': [750],
              'Kelsey Rodgers': [55.76],
              'John Williams': [500, 1898],
              'Morgan Stanley': [12000.98, 8670],
              'Roger Johnson': [264, 942.23],
              'Sherry Wilson': [4000, 2324.1, 1352],
              'Alex Grant': [8739, 4312]}
# ----------------------------------


def menu_display():
    print("\n\n----- MENU -----\n"
          "1: Send a Thank You\n"
          "2: Create a Report\n"
          "3: Send letters to everyone\n"
          "4: Quit\n")
    menu_sel_ = UserInputs.get_menu_option()
    return menu_sel_


def compose_email(donor_name, donation_amount):
    greeting_email = "\nDear {},".format(donor_name)
    body_email = "\nThank you very much for your generous donation of {}".format(donation_amount)
    print(greeting_email, body_email)


def add_donation(donor_name):
    donation_amount = UserInputs.get_donation_amount(donor_name)
    donord.add_donation(donor_name, int(donation_amount))
    compose_email(donor_name, donation_amount)


def thank_you(donor_name):
    if donor_name == 'list':
        donord.list_display()
    else:
        if donor_name in donord.donor_data_:
            add_donation(donor_name)
        else:
            donord.donor = donor_name
            try:
                add_donation(donor_name)
            except ValueError:
                print("Donation amount must be a number with no commas or currency symbols")
                donord.delete_donor(donor_name)


def thank_you_input():
    donor_name_ = UserInputs.get_donors_name()
    thank_you(donor_name_)


def report():
    summary_data = donord.calc_data()
    donord.list_details(summary_data)


def send_all_letters():
    print("hello")
    summary_data = donord.calc_data()
    for item in summary_data:
        filename_format = "{}_{}.txt".format(item[0].split()[0], item[0].split()[1])
        thank_you_text = open(filename_format, 'w+')
        thank_you_text.write("Dear {},\n\nThank you very much for your {} generous donations totalling ${}.\n"
                             "\nYour donations will significantly aid our scholarship fund\n\n"
                             "Sincerely,\n - Advancement Office".format(item[0], item[1], item[2]))
        thank_you_text.close()
    print("\nAll thank you letters drafted")


def exit_program():
    exit()


def main_exec():

    menu_map = {'1': thank_you_input, '2': report, '3': send_all_letters, '4': exit_program}

    while True:
        try:
            menu_sel = menu_display()
            menu_map[menu_sel]()
        except KeyError:
            print("\nMenu selection must be one of the following:\n")
            for key in menu_map:
                print("- {}".format(key))


if __name__ == "__main__":
    # initialize class and populate with global data
    donord = DonorData()
    for donor in donor_data.keys():
        donord.add_donation(donor, donor_data[donor])
    # donord.printer()

    main_exec()

