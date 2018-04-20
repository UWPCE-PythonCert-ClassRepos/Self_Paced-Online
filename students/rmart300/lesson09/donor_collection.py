import os
from donor import Donor

class DonorCollection(object):

    letter_directory = 'temp/'

    def __init__(self):
        # dictionary to hold donors and list of donation amounts
        donor_list = ['Fred Smith', 'Terrie Ann', 'Murray Martin', 'Josh Jones', 'Jane Doe']
        self.donation_dict = {}
        self.donor_set = set()

        # build initial dictionary of donors and donation amounts
        amount_list = [ 500, 100, 1000]
        for name in donor_list:
            d = Donor(name)
            self.donor_set.add(d)
            self.donation_dict[name]= amount_list[:]

    def validate_and_create_thank_you(self, name, amount):
        """ send a thank you email to the donor for donation """

        try:
            amount = float(amount)
        except ValueError as e: 
            return 'invalid donation amount: ' + str(amount)

        try:
            d = Donor(name)
        except IndexError as e:
            return 'Could not send thank you.  The first and last name of donor must be provided\n'
        else:
            self.donor_set.add(d)
            amount_list = self.donation_dict.get(name, [])
            amount_list.append(amount)
            self.donation_dict[name] = amount_list
            return f"Hi {d}\nThank you for your donation of {amount} to the mailroom!\n"

    def send_thank_you(self):
        """
            prompt user for name and donation amount, add to donation dictionary
            provide list of names if user enters \'list\' as name
        """

        name = 'list'
        while name == 'list':
            name = input("Provide full name: ").strip()
            if name == 'list':
                for donor_name in self.donation_dict:
                    print(donor_name)

        amount = input("Provide a donation amount:")
        thank_you_message = self.validate_and_create_thank_you(name, amount)
        print(thank_you_message)

    def create_report(self):

        """ Print a list of donors, sorted by total historical donation amount"""
        title = "{0:20} | {1:15} | {2:10} | {3:15}".format('Donor Name','Total Given','Num Gifts','Average Gift')
        print(title)

        #sort the dictionary by descending order of the sum of values
        sorted_dict = sorted(self.donation_dict.items(), key=lambda x: sum(int(v) for v in x[1]),reverse=True)
        for donor, amount_list in sorted_dict:
            donation_count = len(amount_list)
            donation_total = sum(int(v) for v in amount_list)
            donation_average = round(donation_total/donation_count,2)
            data_row = "{0:20}  ${1:>15}   {2:>10}   ${3:>15}".format(str(donor),
                str(donation_total), str(donation_count), str(donation_average))
            print(data_row)

    def write_letters(self):
        """ write letters to every donor in dict """

        #clear files from directory before creating new ones
        for f in os.listdir(DonorCollection.letter_directory):
            if '.txt' in f:
                os.remove(DonorCollection.letter_directory + f)

        for donor in self.donor_set:
            amount_list = self.donation_dict[str(donor)]
            donation_num = 1
            for donation_amt in amount_list:
                message = f"Dear {donor.first_name} {donor.last_name},\n\n    "
                message += f"Thank you for your very kind donation of ${donation_amt}.\n\n    "
                message += f"It will be put to very good use.\n\n    Sincerely,\n"
                message += f"        -The Team"
                with open(f"{DonorCollection.letter_directory}{donor.first_name}_{donor.last_name}_{donation_num}.txt",'w') as f:
                    f.write(message)
                donation_num += 1

