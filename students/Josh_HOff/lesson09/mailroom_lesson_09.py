import sys
import copy
import pathlib

#this class handles all donor management
class Donor:
    def __init__(self, name = '', donations = None):
        self._donations = donations
        self._name = name
                
    @property
    def gifts(self):
        self._gifts = len(self._donations)
        return self._gifts
                
    @property
    def total_donations(self):
        self._total = sum(self._donations)
        return self._total
                
    @property
    def average(self):
        total = self.total_donations
        gifts = self.gifts
        self._average = round((total / gifts), 2)
        return self._average
                
    @property
    def recent_gift(self):
        self._recent_gift = self._donations[-1]
        return self._recent_gift
                
    @property
    def first_gift(self):
        self._first_gift = self._donations[0]
        return self._first_gift
        
        
class DonorCollection:
    
    def __init__(self):
        self._donors = {'Josh Hoff': [25, 75], 'Tatsiana Kisel': [35, 105.55]}
        
    @property
    def donors(self):
        return self._donors
        
    @donors.setter
    def donors(self, new_dict):
        self._donors = copy.deepcopy(new_dict)
        return self._donors

        
    def report(self):
        y = '|'
        rows = ''
        top = f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift\n'
        top += ('-' * 63)
        sorted_donors = sorted(self._donors.items(), key=lambda k: sum(k[1]), reverse=True)
        for name, donations in sorted_donors:
            d = Donor(name, donations)
            gift = d.gifts
            total_donations = d.total_donations
            average = d.average
            rows += f'\n{name:<23} $ {total_donations:>11.2f} {gift:>11} {average:>11.2f}'
        top += rows
        print(f'\n{top}')
        
    def letters(self):
        tab = '    '
        for name, val in self._donors.items():
            with open(f'{name}.txt', 'w') as outfile:
                d = Donor(name, val)
                donation = d.total_donations
                val = self._donors.get(name)[-1]
                outfile.write(f'Dear {name}, \n\n{tab}Thank you very much for your most recent donation \
of ${val:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company')
    
    def show_list(self):
        print('')
        for i in self._donors:
            print(i)

    def add_donor(self, donor_name='Jacob', donation=30):
        if donor_name in self._donors:
            self._donors[donor_name] += [donation]
        else:
            self._donors[donor_name] = [donation]
        return self._donors
        
        
def thank_you():
    while True:
        donor_name = input('\nWhat is the name of the donor?: ')
        if donor_name == 'list':
            a.show_list()
            continue
        elif donor_name == 'quit':
            return
        while True:
            try:
                donation = float(input('\nWhat is the donation amount?: '))
            except ValueError:
                print('\nPlease give a number instead.')
                continue
            break
        a.donors = a.add_donor(donor_name, donation)
        return
        
def quitting():
    sys.exit()
    
def continuing():
    print('Try Again.\n')

a = DonorCollection()
    
switch_func_dict = {'1':thank_you, '2':a.report, '3':a.letters, '4':quitting, 'quit':quitting, 'list':a.show_list}

#main function: adjusted to use classes
if __name__ == '__main__':
    while True:
        choice = input('\n1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Quit \nChoose an Option: ')
        c = switch_func_dict.get(choice, continuing)()