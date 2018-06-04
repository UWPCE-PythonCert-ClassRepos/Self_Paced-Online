# -*- coding: utf-8 -*-
"""
Created on Sun May 20 07:03:34 2018

@author: Karl M. Snyder
"""

class Main:
    def __init__(self):
        self.menu = {1: 'Send a Thank You',
                     2: 'Create a Report',
                     3: 'Send letters to everyone',
                     4: 'Quit'}
    
    def main_menu(self):
        print('\n', 'Please select a number from the following choices:\n')
        return {(print(str(k) + ':', v)) for k, v in self.menu.items()}
    
    def selection(self):
        while True:
            input1 = input("Selection: ")
            #print(type(input1), input1)
            try:
                if int(input1) in range(1, 4):
                    if int(input1) == 1:
                        print('\nType a user\'s name or "list" to show names.')
                        input2 = input('-> ')
                        if input2 == 'list':
                            our_donors.donors()
                            continue
                        else:
                            input3 = input('Donation amount: ')
                            user = Donor(input2, input3)
                            user.send_thanks()
                    if int(input1) == 2:
                        our_donors.create_report()
                    if int(input1) == 3:
                        our_donors.send_letters_all()
                elif int(input1) == 4:
                    print("Exiting program...")
                    break
            except ValueError:
                print("You must use a menu number between 1-4; try again!")

class Donor:
    
    donor_dict = {'Karl': {'donations': [10, 20, 30], 'num_donations': 3, 
                           'avg': 20, 'total': 60},
            'Kate': {'donations': [5, 30],'num_donations': 2, 
                      'avg': 17.5, 'total': 35},
            'Christine': { 'donations': [21], 'num_donations': 1,
                          'avg': 21, 'total': 21},
            'Matt': {'donations': [40, 5, 11], 'num_donations': 3,
                     'avg': 18.67, 'total': 56},
            'Zumi': {'donations': [32], 'num_donations': 1, 
                     'avg': 32, 'total': 32}}
    
    def __init__(self, name, donations):
        self.name = name
        try:
            donations = float(donations)
            self.donations = donations
        except ValueError:
            print('You must enter a number for donation amount.')
        self.update_dict()
        
            
    def update_dict(self):
        if Donor.donor_dict.get(self.name):
            Donor.donor_dict[self.name]['donations'].append(self.donations)
            Donor.donor_dict[self.name]['num_donations'] = \
                len(Donor.donor_dict[self.name]['donations'])
            Donor.donor_dict[self.name]['total'] = \
                sum(Donor.donor_dict[self.name]['donations'])    
            Donor.donor_dict[self.name]['avg'] = \
                (Donor.donor_dict[self.name]['total'] /
                 Donor.donor_dict[self.name]['num_donations'])
        else:
            Donor.donor_dict[self.name] = {'donations': self.donations,
                'num_donations': 1, 'avg': self.donations, 
                'total': self.donations}

    @property
    def donation(self):
        return '{} made a donation of {:,.2f}'.format(self.name,
                self.donations)
        
    @staticmethod
    def sort_key(self):
        return Donor.donor_dict[self.name]['total']

    def __repr__(self):
        return "Name: {}, Sum Donated: ${:.2f}".format(
                self.name, Donor.donor_dict[self.name]['total'])
        
    def send_thanks(self):
        letter = 'Thank you {} for your donation in the amount of ${}; it is very generous.'.format(self.name, self.donations)
        with open('Thank_You - {}.txt'.format(self.name.lower().
                     replace(' ', '_')), 'w') as f:
            f.write(letter)

class Donors:
    
    donors_list = [(name, Donor.donor_dict[name]['total'], Donor.donor_dict[name]['num_donations'], Donor.donor_dict[name]['avg']) for name in Donor.donor_dict]
    
    donors_list_sort= sorted(donors_list,key=lambda i: i[1], 
                                reverse=True)
    
    letters = 'Dear {},\n\n\tThank you for your total contributions in the amount of ${}.\n\n\tYou are making a difference in the lives of others.\n\n\t\tSincerely,\n\t\t"Working for America"'
    
    def donors(self):
        {print(k) for (k, v) in Donor.donor_dict.items()}
        
    def create_report(self):
        print('\n{:<20} {:>20} {:>20} {:>20}'.format('Donor Name',
              '| Total Given', '| Num Gifts', '| Average Gift'))
        print('{}'.format('-' * 83))
        
        for object in Donors.donors_list_sort:
            print('{:<20} {:>20.02f} {:>20} {:>20.02f}'.format(object[0], object[1], object[2], object[3])) 
        
    def send_letters_all(self):
        for object in Donors.donors_list:
           with open('Thank_You - {}.txt'.format(object[0].lower().replace(' ', '_')),
                     'w') as f:
               f.write(Donors.letters.format(object[0], object[1]))
        print('\nYour letters have been printed to the current directory!')
        
if __name__ == '__main__':
    ex = Main()
    ex.main_menu()
    ex.selection()
our_donors = Donors()
        
        