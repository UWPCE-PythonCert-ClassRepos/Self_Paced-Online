# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:56:00 2018

@author: Karl M. Snyder
"""

class Main:
    def __init__(self):
        self.menu = {1: 'Send a Thank You',
                     2: 'Create a Report',
                     3: 'Send letters to everyone',
                     4: 'Projections',
                     5: 'Quit'}
    
    def main_menu(self):
        print('\n', 'Please select a number from the following choices:\n')
        return {(print(str(k) + ':', v)) for k, v in self.menu.items()}
    
    def selection(self):
        while True:
            input1 = input("Selection: ")
            #print(type(input1), input1)
            try:
                if int(input1) in [1,2,3,4]:
                    if int(input1) == 1:
                        print('\nType a user\'s name or "list" to show  names.')
                        input2 = input('-> ')
                        if input2 == 'list':
                            our_donors.donor_names()
                            self.main_menu()
                        else:
                            input3 = float(input('Donation amount: '))
                            user = Donor(input2, [input3])
                            user.send_thanks()
                            self.main_menu()
                    if int(input1) == 2:
                        our_donors.create_report()
                        self.main_menu()
                    if int(input1) == 3:
                        our_donors.send_letters_all()
                        self.main_menu()
                    if int(input1) == 4:
                        factor = int(input('Provide Factor: '))
                        min = int(input('Provide Min Contribution: '))
                        max = int(input('Provide Max Contribution: '))
                        print()
                        print(our_donors.challenge(factor, min, max))
                elif int(input1) == 5:
                    print("Exiting program...")
                    break
            except ValueError:
                print("You must use a menu number between 1-4; try again!")

class Donor:
    def __init__(self, name, donations=None):
        self.name = name
        self.donations = donations
        self.donor = {self.name: {'donations': self.donations,
                'num_donations': len(self.donations),
                'total': sum(self.donations),
                'avg': sum(self.donations)/len(self.donations)}}
        
    @property
    def prnt(self):
        print(self.name, "$"+repr(sum(self.donations)))

    @property
    def donation(self):
        return 'Thanks you {} for making a donation in the amount of ${}, it is very generous.'.format(self.name, self.donations[-1])
        
    @staticmethod
    def sort_key(self):
        return self.donor[self.name]['total']

    def send_thanks(self):
        letter = 'Thank you {} for your donation in the amount of ${}; it is very generous.'.format(self.name, self.donations[-1])
        with open('Thank_You - {}.txt'.format(self.name.lower().
                     replace(' ', '_')), 'w') as f:
            f.write(letter)
        print('Your thank you letter was saved in the local directory')

class Donors:
    def __init__(self):
        self.donors = {}

    def donor_names(self):
        for k, v in self.donors.items():
            print(k)
            
    @property
    def donors_list(self):
        return [(name, self.donors[name]['total'], self.donors[name]['num_donations'], self.donors[name]['avg']) for name in self.donors]
    
    @property
    def donors_sort(self):
        return [sorted(self.donors_list, key=lambda i: i[1], reverse=True)]
    
    def challenge(self, factor, min=0, max=10000000):
        l = []
        for name in self.donors:
            for d in self.donors[name]['donations']:
                l.append(float(d))
        fl = list(filter(lambda x: x >= min and x <= max, l))
        mp = list(map(lambda x: x * factor, fl))
        mp = [round(x, 2) for x in mp]
        return "By using a factor of {}, with a minimum of ${:.2f} and a maximum of ${:.2f}, the original individual contributions of {}  are modified to {}, while the total match changes from ${:,.2f} to ${:,.2f}.".format(factor, min, max, l, mp, sum(l), sum(mp))
    
    def create_report(self):
        print('\n{:<20} {:>20.02f} {:>20} {:>20}'.format('Donor Name',
              '| Total Given', '| Num Gifts', '| Average Gift'))
        print('{}'.format('-' * 80))
        for x in self.donors_sort:
            for y in x:
                print('{:<20} {:>20.02f} {:>20} {:>20.02f}'.format(y[0], 
                      y[1], y[2], y[3]))
                
    letters = 'Dear {},\n\n\tThank you for your total contributions in the amount of ${}.\n\n\tYou are making a difference in the lives of others.\n\n\t\tSincerely,\n\t\t"Working for America"'
    
    def send_letters_all(self):
        for i in self.donors_list:
            with open('Thank_You - {}.txt'.format(i[0].lower().replace(' ',
                      '_')), 'w') as f:
                f.write(self.letters.format(i[0], i[1]))
        print('\nYour letters have been printed to the current directory!')
    
if __name__ == "__main__":
    ex = Main()
    ex.main_menu()
    ex.selection()
    p1 = Donor('Karl', [333])
    p2 = Donor('Zulu', [150.55, 24.98])
    p3 = Donor('Monte', [12, 48, 200])
    our_donors = Donors()
    our_donors.donors.update(p1.donor)
    our_donors.donors.update(p2.donor)
    our_donors.donors.update(p3.donor)
    
    
    
    
