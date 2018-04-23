# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:38:02 2018

@author: Karl M. Snyder
"""

#[[fill]align][sign][#][0][minimumwidth][.precision][type]

from collections import defaultdict

donor_dict = defaultdict(list, {'Karl Stick': [10, 20, 30],
              'Kate Stam': [5, 30],
              'Christine Goose': [21],
              'Matt Hen':  [40, 5, 11],
              'Zumi Was': [32]})

def menu():
        menu_dict = {'1:': 'Send a Thank You',
                     '2:': 'Create a Report',
                     '3:': 'Send letters to everyone',
                     '4:': 'Quit'}
        for k,v in menu_dict.items():
            print(k, v)
            
def thank_you_greeting():
    print('{} {}'.format('\nType a user\'s name or "list" to show names.', print()))
    
def donations():
    return float(input('Donor Amount: '))
    
def send_thanks():
    thank_you_greeting()
#    print()
    input1 = input('-> ')
    print(' ')
    if input1 == 'list':
        for name in list(donor_dict):
            print(name)
    else:
       input2 = donations()
       donor_dict[input1.title()].append(input2)
       
def create_report():
    sum_data = [(k, sum(v), len(v), sum(v)/len(v)) for k,v in donor_dict.items()]
    sum_data = sorted(sum_data, key=lambda x: x[2], reverse=True)
    print('{:<20} {:>20} {:>20} {:>20}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift'))
    print('{}'.format('-' * 83))
    for item in sum_data:
        print('{:<20} {:>20.02f} {:>20} {:>20.02f}'.format(*item))
        
letters = 'Dear {},\n\n\tThank you for your total contributions in the amount of ${}.\n\n\tYou are making a difference in the lives of others.\n\n\t\tSincerely,\n\t\t"Working for America"'

def send_letters_all():
   for name, value in donor_dict.items():
       f = open('Thank_You - {}.txt'.format(name.lower().replace(' ', '_')), 'w')
       f.write(letters.format(name, sum(value)))
   print('\nYour letters have been printed to the current directory!')
        

if __name__ == "__main__":
    user_input = None
    while user_input != 4:
        print('\n', 'Please select a number from the following choices:\n')
        menu()
        user_input = int(input('Selection: '))
        if user_input == 1:
            send_thanks()
        elif user_input == 2:
            create_report()
        elif user_input == 3:
            send_letters_all()
    