# Description: Mailroom Program - FP
# Author: Andy Kwok
# last Updated: 10/2/18
# ChangeLog:
# v1.0 - Initialization
# v2.0 - Modified per instructor comments

from functools import reduce

#!/usr/bin/env python3


class Donor():
    ''' Class to hold donor name and donation information'''
    def __init__(self, first=None, last=None, donation_record=[]):
        self.first = first
        self.last = last
        self.donation_record = donation_record

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    def __lt__(self, other):
        return self.last < other.last

    def AddDonation(self, Amount):
        self.donation_record.append(Amount)


class DonorInfo(object):
    ''' Class to hold all methods and data for a list of donors'''
    donor_list = []

    def AddDonor(Donor):
        DonorInfo.donor_list.append(Donor)

    def Display():
        print('Donor Name' + ' '*10 + '| Total Given' +
              ' '*5 + '| Num Gifts' + ' '*5 + '| Average Gift')
        print('-'*75)
        for j in DonorInfo.donor_list:
            print('{:20}'.format(j.first + ' ' + j.last) +
                  '$ {:>10.2f} {:7}'.format(sum(j.donation_record),
                                            len(j.donation_record)) +
                  ' '*14 +
                  '$ {:>10.2f}'.format(sum(j.donation_record)/ 
                                       len(j.donation_record)))

    def SentLetters(Donor):
        printout = 'To {} {},'.format(Donor.first, Donor.last) + '\n' + 'Thank you for your donation of' + '${:.2f}.'.format(sum(Donor.donation_record)) + '\n'*2 + '\t'*5 + '-System Generated Email'    
        return printout

    def SortList():
        # Sort per first name
        DonorInfo.donor_list.sort()

    def Multi(array, value):
        return array*value

    def Challenge(value, min_donation, max_donation):
        for count, i in enumerate(DonorInfo.donor_list):
            i.donation_record = list(filter(lambda x:
                                     min_donation <= x <= max_donation,
                                     i.donation_record))
            if i.donation_record:
                DonorInfo.donor_list[count].donation_record = list(map(DonorInfo.Multi,
                                                                   i.donation_record,
                                                                   [int(value)]*len(i.donation_record)))
            else:
                DonorInfo.donor_list[count].donation_record = [0]                                              
             

    def Forecast():
        for i in DonorInfo.donor_list:
            print('Donation Projection for donor {}:'.format(i.fullname))
            double_contribution = list(map(DonorInfo.Multi,
                                           list(filter(lambda x: x < 100,
                                                i.donation_record)),
                                           [2]*len(i.donation_record)))
            if double_contribution:
                double = reduce(lambda x, y: x+y, double_contribution)
            else:
                double = 0
            print('Total donation if donation under $100 are doubled: $', double)
            triple_contribution = list(map(DonorInfo.Multi,
                                       list(filter(lambda x: x > 50,
                                            i.donation_record)),
                                       [3]*len(i.donation_record)))
            if triple_contribution:
                triple = reduce(lambda x, y: x+y, triple_contribution)
            else:
                triple = 0
            print('Total donation if donation over $50 are tripled: $', triple)
        #For testing
        return (double, triple)

DonorInfo.donor_list = [Donor("Guest", "1", [10, 30, 50]),
                        Donor("Guest", "C", [500]),
                        Donor("Guest", "A", [200, 400])]

if __name__ == '__main__':
    option = 'start'
    while option.lower() != 'quit':
        print(
            '''
            1 - Sent a Thank you
            2 - Create a Report
            3 - Send Letters to Everyone
            4 - Quit
            5 - Challenge the Donors!
            6 - Donation Forecast
            '''
            )
        try:
            option = input('Please select an option> ')
        except KeyError:
            print('Option does not exist...Please try again')
        if option == '1':
            # Modify list
            value = input('Enter donor\'s name to search' +
                          'or \'list\' to show all donors> ')
            Name = value.split(' ')
            if value.lower() == 'list':
                DonorInfo.Display()
            else:
                stop = False
                new = True
                while stop is False:
                    try:
                        Donation = float(input('How much does {} want to donate? '.format(value)))
                    except ValueError:
                        print("Please enter a real donation amount.")
                    else:
                        # Scan for existing donor
                        for count, item in enumerate(DonorInfo.donor_list):
                            if item.fullname.lower() == value.lower():
                                DonorInfo.donor_list[count].AddDonation(Donation)
                                new = False
                                stop = True
                        # Add new donor if non exist
                        if new is True:
                            Newdonor = Donor()
                            Newdonor.first = Name[0]
                            Newdonor.last = Name[1]
                            Newdonor.AddDonation(Donation)
                            DonorInfo.AddDonor(Newdonor)
                            stop = True
        elif option == '2':
            # Report out
            DonorInfo.SortList()
            DonorInfo.Display()
        elif option == '3':
            # Send letters to everyone
            for item in DonorInfo.donor_list:
                with open(item.first + ' ' + item.last + '.txt', 'w') as doc:
                    doc.write(DonorInfo.SentLetters(item))
        elif option == '4':
            # Quit
            option = 'quit'
        elif option == '5':
            value = input('How many times are you ' +
                          'challenging the donors to donate? ')
            min_donation = input('How much should minimum donation be? $')
            max_donation = input('How much should maximum donation be? $')
            DonorInfo.Challenge(value, int(min_donation), int(max_donation))
        elif option == '6':
            DonorInfo.Forecast()
