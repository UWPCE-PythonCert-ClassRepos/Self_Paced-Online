#!/usr/bin/env python3

# new file for lesson 9 work to incorporate classes.


class Donor:
    def __init__(self, name, *donation):
        self.name = name
        self.donations = donation[0]


    @property
    def sum_donations(self):
        return sum(self.donations)


    @property
    def avg_donations(self):
        return sum(self.donations)/len(self.donations)

    
    def new_donation(self,new):
        return self.donations.append(new)



class Donors:
    def __init__(self):
        self.data = {}
    

    def new_donor(self,donor):
        #currently allows to add one individual donor with list of donations
        self.data[donor.name] = donor.donations
        #print(self.data)


    def display_list(self):
        for name in self.data.keys():
            print(name)

    
    def add_donation(self,name,amount):
        #add doination to existing donor within Donors
        self.data[name].append(amount)
        #print(self.data)


    def write_letter(self,name,amount):
        line_one = 'Dear {},'.format(name)
        line_two = "Thank you for donating ${:.2f} to the Human Fund. Your money will be used appropriately.".format(amount)
        letter = line_one + "\n" + line_two
        return letter
    

    def write_report(self): #need to add the rest of the code to prepare the data
        donors_report = []
        for name, amount in self.data.items():
            sum_donation = 0
            avg_donation = 0
            for i in amount:
                sum_donation = sum_donation + i
                num_donation = len(amount)
            avg_donation = sum_donation/num_donation
            donors_report.append([sum_donation, name, num_donation, avg_donation])
        donors_report.sort(reverse=True)
        print('Donor Name                | Total Given | Num Gifts | Average Gift')
        print('-'*67)
        for i in donors_report:
            print('{1:27}${0:11.2f}{2:12}  ${3:12.2f}'.format(*i))
    

    def letter_files(self):
        for name in self.data:
            donation = self.data[name][0]
            with open('{}.txt'.format(name), 'w') as f:
                f.write(self.write_letter(name, donation))
        print("Letter files created.")