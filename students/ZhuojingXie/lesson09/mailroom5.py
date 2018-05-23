import sys
import os
from collections import defaultdict
donor_data = defaultdict(list,{'Andy':[960,256,123.5,40],'Bryce':[30,45,27],
                            'Charile': [25,50], 'David':[10], 'Elaine' :[75,26]})

class Donor():


    """this is Donor class to save donor's information"""
    def __init__(self, name, donation):
        self.name = name
        self.donation = donation


    def add_donor_in_data(self):
        return donor_data[self.name].append(self.donation)


class Collection:

    def __init__(self, donor_data):
        self.donor_data = donor_data

    def all_donor(self):
        temp_keys=[]
        for keys in self.donor_data:
            temp_keys.append(keys)
        return temp_keys

    def sum_donation(self,name):
        return sum(self.donor_data[name])

    def last_donation(self, name):
        return self.donor_data[name][-1]

    def send_a_thank_you(self):
        print('\n')
        print(self.all_donor())
        donor_name =input('\n\nPlease input the name or the donator > ')
        donation = input('\n\nThank you for donation , please type '
                    'the money you want to donate > ')
        while not donation.isdigit():
            donation = input('\n\nPlease type number only > ')

        temp_donor = Donor(donor_name,float(donation))
        temp_donor.add_donor_in_data()
        menu_selection(main_prompt,main_dispatch) # I dont know why i have to put this to go back main_menu
                                                #otherwise i cannot quit loop here.


    def creat_a_report(self):
        print('{:<20}'.format('Donor Name')+'| '+
              '{:<15}'.format('Total Given')+'| '+'{:<15}'.format('Num Gifts')+'| '+'{:<15}'.format('Average Gift'))
        print('='*68)

        order_data = []
        for i in self.donor_data:
            order_data.append([i, sum(donor_data[i])])

        order_data = sorted(order_data, key=lambda order_data: order_data[1], reverse = True)

        for info in order_data:
            print(f'{info[0]:<20}'+ f'$ {self.sum_donation(info[0]):<16}'
            + f'{len(self.donor_data[info[0]]):<16}'
            + f'$ {self.sum_donation(info[0])/len(self.donor_data[info[0]]):<16}')


    def send_letters_to_everyone(self):
        for info in self.donor_data:
            name = info
            amount =  self.last_donation(name)
            t_amount = self.sum_donation(name)
            with open(name+'.txt', 'w') as wf, open("template.txt", 'r') as rf:
                for line in rf:
                    wf.write(line.replace('{name}', name).replace('{amount:.2f}',str(amount)).replace('{t_amount:.2f}',str(t_amount)))
        print('\n\nCreat report to everyone successfuly!')



def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == 'back to upper menu':
                break
        except KeyError:
            print('\nError: Please input right instruction')

def main_menue():
    menu_selection(main_prompt,main_dispatch)

def sub1_menu():
    menu_selection(sub1_prompt,sub1_dispatch)

def go_back():
    return 'back to upper menu'

main_prompt = ('\n\nPlease select a action: \n1 Send a Thank You!'
               ' \n2 Create a Report  \n3 Send letters to everyone \n4 Quit \n\n  >')
sub1_prompt = ('\n\nType "list" to show a list of the donor names, \n'
                'Or type "back" to Back\n')

main_dispatch ={'1':sub1_menu,'2':Collection(donor_data).creat_a_report,'3':Collection(donor_data).send_letters_to_everyone,'4': sys.exit}
sub1_dispatch ={'list':Collection(donor_data).send_a_thank_you, 'back':go_back}

def main():
    menu_selection(main_prompt,main_dispatch)

if __name__ == "__main__":
    main()
