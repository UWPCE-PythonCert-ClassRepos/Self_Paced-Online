#!/usr/bin/env python3
class DonorCollection:

    donors_collection_data = {"John": [200, 300, 400],
                   "Jeff": [200, 500, 600, 700, 800],
                   "Susan": [1000, 2000, 1500],
                   "Rob": [250, 300, 500],
                   "Ross": [600, 700]}

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
            if len(row[1]) > 0:
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

    def multiply_factor(self, factor=1,min_donation=0, max_donation=0, **data):
        """Function to multiply the Donors's donated amount by an agreed factor"""
        for name in data:
            donation_values = list(data[name])
            min_max_donation_values = list(filter(lambda min_max_amt: (min_donation < min_max_amt < max_donation),
                                                  donation_values))
            data[name] = list(map(lambda amount: amount * factor, min_max_donation_values))
        self.donor_details(**data)
