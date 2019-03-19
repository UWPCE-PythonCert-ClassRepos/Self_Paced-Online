#!/usr/bin/env python3


class Donors:

    donors_data = {"John": [200, 20, 35.5],
                   "Jeff": [500, 20],
                   "Susan": [1000, 20, 70],
                   "Rob": [250, 20],
                   "Ross": [200]}

    def display_donors(self):
        donors_data = self.donors_data
        """Display donors if user enters list"""
        for name in donors_data.keys():
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
        donors_data = self.donors_data
        self.donor_details(**donors_data)

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
        donors_data = self.donors_data
        self.send_letters_all(**donors_data)
