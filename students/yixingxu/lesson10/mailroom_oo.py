import sys
import os

class Donor():
    def __init__(self, name):
        self._name = name
        self._donations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, donor_name):
        self._name = donor_name

    @property
    def donations(self):
        return self._donations

    def add_donation(self, donor_donation):
        self.donations.append(donor_donation)


class Donors_Collection():
    def __init__(self):
        self._donors = []

    @property
    def donors(self):
        return self._donors

    def add_new_donor(self, donor):
        self.donors.append(donor)

    def get_donors_names(self):
        name_list = []
        for donor in self._donors:
            name_list.append(donor.name)
        return name_list


    def add_donation_amount(self, name, donation_amount):
        for donor in self._donors:
            if donor.name == name:
                donor.donations.append(donation_amount)
                break

    def create_summary(self):
        summary_list = []
        for donor in self._donors:
            total = sum(donor.donations)
            number_of_gifts = len(donor.donations)
            average = total / number_of_gifts
            summary_list.append([donor.name, '$', total, number_of_gifts, '$', average])
        return summary_list

    def create_a_report(self):
        # create a summary list
        summary_list = self.create_summary()
        self.print_report(summary_list)

    def print_report(self,a_list):
        donor_name_width = 20
        total_given_width = 15
        num_gifts_width = 5
        average_gift_width = 15
        seperator_width = 2
        title = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift']
        divider = '-' * (
                    donor_name_width + total_given_width + num_gifts_width + average_gift_width + seperator_width * 5)
        print('{:<20}{:<2}{:<15}{:<2}{:<5}{:<2}{:<15}'.format(*title))
        print(divider)
        for item in a_list:
            print('{:<20}{:2}{:15.2f}  {:8} {:>2}{:12.2f}\n'.format(*item))

    def send_a_thank_you(self):
        name = input(
            "\nSend a Thank You. Please provide a name or type 'list' to display current names, or type 'back': ")
        if name != 'back':
            # If the user types ‘list’, show them a list of the donor names and re-prompt
            while name == 'list':
                print(self.get_donors_names())
                name = input('\nSend a Thank You. Please provide a name: ')
            # If the user types a name not in the list, add that name to the data structure and use it.
            if name not in self.get_donors_names():
                new_donor = Donor(name)
                self.add_new_donor(new_donor)
            # If the user types a name in the list, use it.  Once a name has been selected, prompt for a donation amount.
            if name in self.get_donors_names():
                while True:
                    donation_amount = input('\nPlease provide the amount of donation from {} : '.format(name))
                    # added exception handling in this version
                    try:
                        self.add_donation_amount(name, int(donation_amount))
                    except ValueError:
                        print('\nInvalid donation ammount. Please enter a valid number.')
                    else:
                        break
                print(f"\nDear {name},\n"
                      f"Thanks for your generous donation of ${donation_amount}"
                      )

    def send_letters_to_everyone(self):
        for item in self.create_summary():
            letter = "Dear {},\n\n        Thank you for all your very kind donations of ${}\n\n        It will be put to very good use.\n\n                       Sincerely,\n                          -The Team".format(
                item[0], item[2])
            with open(item[0] + '.txt', 'w') as wf:
                wf.write(letter)
        print("\nAll letters written to files")

def generate_prompt(dispatch_dict):
    print('Please type your selection from the above options: ')

#  prompt the user (you) to choose from a menu
def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == 'exit menu':
                break
        except KeyError:
            print('\nInvalid input. Please only choose from the availalbe options')

# quit
def quit_program():
    print('Quit')
    return 'exit menu'

def donation_history_initialization():
    # initialize a history of donations to work on
    donation_history = {'Anna': [100, 200, 300],
                        'Bob': [1000, 2000],
                        'Chuck': [10000],
                        'David': [1],
                        'Ethan': [10, 20]}
    donors_collection = Donors_Collection()

    for name, donations in donation_history.items():
        donor = Donor(name)
        for donation in donations:
            donor.add_donation(donation)
        donors_collection.add_new_donor(donor)
    return donors_collection

if __name__ == "__main__":
    donors_collection = donation_history_initialization()
    main_dispatch = {
                '1': donors_collection.send_a_thank_you,
                '2': donors_collection.create_a_report,
                '3': donors_collection.send_letters_to_everyone,
                '4': quit_program
                }
    main_prompt = ("\nYou are in the main menu now!\n"
                "Choose an action:\n\n"
                "1: Send a thank you\n"
                "2: Create a report\n"
                "3: Send letters to everyone\n"
                "4: Quit\n"
                "Type 1,2,3,4 >> "
              )
    menu_selection(main_prompt, main_dispatch)