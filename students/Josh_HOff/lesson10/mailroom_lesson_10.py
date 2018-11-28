import sys
import copy
import pathlib

donors = {'Josh Hoff': [25, 75], 'Tatsiana Kisel': [35, 105.55]}

#This class handles all input from the user
class Input(object):

#    donors = {'Josh Hoff': [25, 75], 'Tatsiana Kisel': [35, 105.55]}

    def __init__(self=None):
        pass
    
    def thank_you(self=None):
        while True:
            donor_name = input('\nWhat is the name of the donor?: ')
            if donor_name == 'list':
                DonorCollection().show_list()
                continue
            elif donor_name == 'quit':
                break
            while True:
                try:
                    donation = float(input('\nWhat is the donation amount?: '))
                except ValueError:
                    print('\nPlease give a number instead.')
                    continue
                break
            DonorCollection().add_donor(donor_name, donation)
            break
            
    def quitting(self):
        sys.exit()
        
    def continuing(self):
        print('Try Again.\n')

#this class handles all donor management
class Donor(object):
    def __init__(self=None, name = ''):
        global donors
        self._donors = donors
        self._gifts = len(self._donors.get(name))
        self._total = sum(self._donors.get(name))
        self._average = round((self._total / self._gifts), 2)
        self._recent_gift = self._donors.get(name)[-1]
        self._first_gift = self._donors.get(name)[0]
                
    @property
    def gifts(self):
        return self._gifts
        
    @gifts.deleter
    def gifts(self):
        del self._gifts
        
    @property
    def total_donations(self):
        return self._total
        
    @total_donations.deleter
    def total_donations(self):
        del self._total
        
    @property
    def average(self):
        return self._average
        
    @average.deleter
    def average(self):
        del _average
        
    @property
    def recent_gift(self):
        return self._recent_gift
        
    @recent_gift.deleter
    def recent_gift(self):
        del _recent_gift
        
    @property
    def first_gift(self):
        return self._first_gift
        
    @first_gift.deleter
    def first_gift(self):
        del self._first_gift
        
        
class DonorCollection(object):
    def __init__(self=None):
        pass
        
    @staticmethod
    def report():
        global donors
        y = '|'
        rows = ''
        top = f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift\n'
        top += ('-' * 63)
        sorted_donors = DonorCollection().sorted_donators()
        for name, donations in sorted_donors:
            d = Donor(name)
            gift = d.gifts
            total_donations = d.total_donations
            average = d.average
            rows += f'\n{name:<23} $ {total_donations:>11.2f} {gift:>11} {average:>11.2f}'
        top += rows
        print(f'\n{top}')
        
    @staticmethod
    def letters():
        tab = '    '
        global donors
        for name, val in donors.items():
            with open(f'{name}.txt', 'w') as outfile:
                d = Donor(name)
                donation = d.total_donations
                val = d.recent_gift
                outfile.write(f'Dear {name}, \n\n{tab}Thank you very much for your most recent donation \
of ${val:.2f}! \n\n{tab}You have now donated a total of ${donation:.2f}. \n\n{tab}Your support \
is essential to our success and will be well utilized. \n\n{tab*2}Sincerely, \n{tab*3}-The Company')
    @staticmethod
    def show_list():
        print('')
        global donors
        for i in donors:
            print(i)

    @staticmethod
    def add_donor(donor_name='Jacob', donation=30):
        global donors
        if donor_name in donors:
            donors[donor_name] += [donation]
        else:
            donors[donor_name] = [donation]
            
    @staticmethod
    def sorted_donators():
        global donors
        return sorted(donors.items(), key=lambda k: sum(k[1]), reverse=True)

    
class Functions(object):

    def __init__(self):
        pass
    
    @staticmethod
    def challenge(factor, min_donation=0, max_donation=9999999999999999999):
        global donors
        modified_donors = copy.deepcopy(donors)
        lower_donors = copy.deepcopy(donors)
        higher_donors = copy.deepcopy(donors)
        final_donors = {}

        for name in donors:
            modified_donors[name] = list(filter(lambda x : x > min_donation, modified_donors[name]))
            modified_donors[name] = list(filter(lambda x : x < max_donation, modified_donors[name]))
            
            lower_donors[name] = list(filter(lambda x : x < min_donation, lower_donors[name]))            
            higher_donors[name] = list(filter(lambda x : x > max_donation, higher_donors[name]))
            
        for name in donors:
            modified_donors[name] = list(map(lambda x : x*factor, modified_donors[name]))
            
        for name in donors:
            modified_donors[name] += lower_donors[name]
            modified_donors[name] += higher_donors[name]
            
        print(modified_donors)
        return modified_donors
        
    @staticmethod
    def projections():
        d = Functions()
        print(d.challenge(2, 0, 100))
        print(d.challenge(3, 50))
        
        
switch_func_dict = {'1':Input().thank_you, '2':DonorCollection().report, '3':DonorCollection().letters, '4':Functions().projections, '5':Input().quitting, 'quit':Input().quitting, 'list':DonorCollection().show_list}

#main function: adjusted to use classes
if __name__ == '__main__':
    while True:
        choice = input('\n1: Send a Thank You \n2: Create a Report \n3: Send Letters to Everyone \n4: Run Projections \n5: Quit \n\nChoose an Option: ')
        c = switch_func_dict.get(choice, Input().continuing)()