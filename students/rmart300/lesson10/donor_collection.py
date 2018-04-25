import os
from donor import Donor

class DonorCollection(object):

    letter_directory = 'temp/'

    def __init__(self, donor_names=()):
        # list to hold donors
        self.donor_list = []

        # build initial dictionary of donors and donation amounts
        for name in donor_names:
            d = Donor(name)
            self.donor_list.append(d)

    def validate_and_create_thank_you(self, name, amount):
        """ send a thank you email to the donor for donation """

        try:
            amount = float(amount)
        except ValueError as e: 
            return 'invalid donation amount: ' + str(amount)

        if name in self.donor_list:
            for d in self.donor_list:
                if d == name:
                    amount_list = d.amount_list
                    amount_list.append(amount)
                    break
        else:
            try:
                d = Donor(name,[amount])
            except IndexError as e:
                return 'Could not send thank you.  The first and last name of donor must be provided\n'
            else:
                self.donor_list.append(d)
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
                for donor in self.donor_list:
                    print(donor)

        amount = input("Provide a donation amount:")
        thank_you_message = self.validate_and_create_thank_you(name, amount)
        print(thank_you_message)

    def create_report(self):

        """ Print a list of donors, sorted by total historical donation amount"""
        title = "{0:20} | {1:15} | {2:10} | {3:15}".format('Donor Name','Total Given','Num Gifts','Average Gift')
        print(title)

        #sort the dictionary by descending order of the sum of values
        sorted_list = sorted(self.donor_list, key=lambda d: d.donation_total, reverse=True)
        for donor in sorted_list:
            data_row = "{0:20}  ${1:>15}   {2:>10}   ${3:>15}".format(str(donor),
                str(donor.donation_total), str(donor.donation_count), str(donor.donation_average))
            print(data_row)

    def write_letters(self):
        """ write letters to every donor in dict """

        #clear files from directory before creating new ones
        for f in os.listdir(DonorCollection.letter_directory):
            if '.txt' in f:
                os.remove(DonorCollection.letter_directory + f)

        for donor in self.donor_list:
            donation_num = 1
            for donation_amt in donor.amount_list:
                message = f"Dear {donor.first_name} {donor.last_name},\n\n    "
                message += f"Thank you for your very kind donation of ${donation_amt}.\n\n    "
                message += f"It will be put to very good use.\n\n    Sincerely,\n"
                message += f"        -The Team"
                with open(f"{DonorCollection.letter_directory}{donor.first_name}_{donor.last_name}_{donation_num}.txt",'w') as f:
                    f.write(message)
                donation_num += 1

    @staticmethod
    def challenge(x,factor):
        #print(f"{x}*{factor}={x*factor}")
        return x*factor
    
    def greater_than_min_value(self, x):
        return x >= self.min_value

    def less_than_max_value(self, x):
        return x <= self.max_value

    def donation_challenge(self):
        question = "By what factor would you like to increase the donations? "
        my_factor = int(input(question))
        question = "What is the minimum allowed amount? "
        self.min_value = int(input(question)) if question is not None else 0
        question = "What is the maximum allowed amount? "
        self.max_value = int(input(question)) if question is not None else 0
        

        for donor in self.donor_list:
            print(donor,"before filters",donor.amount_list)
            donor.amount_list = list(filter(self.greater_than_min_value, donor.amount_list))
            donor.amount_list = list(filter(self.less_than_max_value, donor.amount_list))
            print(donor,"after filters",donor.amount_list)

            factor_list = [my_factor]*len(donor.amount_list)
            challenge_list = list(map(DonorCollection.challenge, donor.amount_list, factor_list))
            donor.amount_list = challenge_list[:]
            print(donor.amount_list)

        

 
