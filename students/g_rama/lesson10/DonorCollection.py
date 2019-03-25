#!/usr/bin/env python3
from CLI import CLI

class DonorCollection:

    donors_collection_data = {"John": [200, 20, 35.5],
                   "Jeff": [500, 20],
                   "Susan": [1000, 20, 70],
                   "Rob": [250, 20],
                   "Ross": [200]}

    def display_donors(self):
        """Display donors if user enters list"""
        for name in self.donors_collection_data.keys():
            print('{}'.format(name))

    def donor_details(self, **data):
        """Print the Donor table"""
        print(f'{"Donor Name":<20} |{"Total Given":>20} |{"Num Gifts":<20} |{"Average Gift":>20.4}')
        print('-' * 90)
        sorted_d = sorted(data.items(), key=lambda x: sum(x[1]), reverse=True)
        for row in sorted_d:
            print(f'{row[0]:<20} ${sum(row[1]):>20} {len(row[1]):>20} ${(sum(row[1]) / len(row[1])):>10.4}')
            # return f'{row:<20} ${sum(data[row]):>20} {len(data[row]):>20} ${(sum(data[row])/len(data[row])):>10.4}\n'

    def create_report(self):
        """Call the function to create the donor details"""
        self.donor_details(**self.donors_collection_data)

    def send_letters_all(self, **data):
        for name in data:
            with open('{}'".txt".format(name), 'w') as outfile:
                outfile.write("Dear {},\n"
                              "Thank you for your very kind donation of ${}\n"
                              "It will be put to very good use.\n"
                              "                     Sincerely\n"
                              "                      -The team".format(name, sum(data[name])))

    def send_letters(self):
        """Call the function to create the donor details"""
        self.send_letters_all(**self.donors_collection_data)

    def multiply_factor(self, factor=1, **data):
        """Function to multiply the Donors's donated amount by an agreed factor"""
        for name in data:
            donation_values = list(data[name])
            data[name] = list(map(lambda x1: x1 * factor, donation_values))
        self.donor_details(**data)

    def challenge_factor(self):
        """A function to take the multiple """
        factor = CLI.mulfactor_input()
        self.multiply_factor(factor, **self.donors_collection_data)






    #
    #     factor_donation_list = [donation * factor for donation in donation_list]
    #     return factor_donation_list
    #
    # #list(map(lambda x1: x1 * 5, [1, 2, 3]))
    # # test_data = list(donors.donors_collection_data.values())[0]
    # #
    # # multiplied_donor_data = map(donors.multiply_factor, test_data, list(str(2)))
    # #
    # # print(list(multiplied_donor_data))









