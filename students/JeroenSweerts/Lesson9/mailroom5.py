#!/usr/bin/env python3

class Donor():
    def __init__(self, name=None):
        self.name = name
        self.donations = []


class Donor_Collection(dict):
    def __init__(self, donors):
        self.donors = donors

    def add_donor(self, donor):
        self.donors[donor.name] = donor.donations

    def donate(self, name, donation):
        if name not in self.donors.keys():
            new_donor = Donor(name)
            self.add_donor(new_donor)
        self.donors[name].append(int(donation))

    def createfile(self, name):
        '''create .txt file containing thank you letter for each person who made a donation'''
        d = {'name':name, 'donation':self.donors[name][-1]}
        outfile = open(name+'.txt', 'w')
        outfile.write("Dear {name} , \n\n".format(**d))
        outfile.write("\t Thank you very much for your generous donation of ${donation}. \n\n".format(**d))
        outfile.write("\t It will be put to very good use. \n\n")
        outfile.write("\t\t Sincerely, \n")
        outfile.write("\t\t   -The Team \n")
        outfile.close()

    def create_report(self):
        print(f'{"Donor Name":20s} {"|  Total Given":20s} {"|  Num Gifts  |":20s} {"Average Gift":20s}')
        print(f'{"-"*76}')
        [print(f'{name:20s} ${sum(self.donors[name]):20.2f} {len(self.donors[name]):13d}${sum(self.donors[name])/len(self.donors[name]):20.2f}') for name in self.donors.keys()]



def thankyou(donordict):
    """If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure
    and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to
    crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for their
    generous donation. Print the email to the terminal and return to the original
    prompt."""
    while True:
        name = input('Please enter a name or type "list" to see a list of names > ')
        if name == 'list':
            print(donordict.donors.keys())
        else:
            break
    try:
        donation = input('Please enter a donation amount > ')
        donordict.donate(name, donation)
    except ValueError:
        while not donation.isdigit():
            print("You didn't enter a valid amount.")
            donation = input('Please enter a donation amount > ')
        donordict.donate(name, donation)
    d = {'name':name, 'donation':donation}
    print("Dear {name} , thank you very much for your generous donation of {donation}. Looking forward receiving even more money next time.".format(**d))
    print(donordict.donors.keys())
    print(donordict.donors.values())

def report(donordict):
    donordict.create_report()

def thankyoueveryone(donordict):
    [donordict.createfile(name) for name in donordict.donors.keys()]


if __name__ == '__main__':
    donor_dict = {}
    donor_dict['papa'] = [100, 5, 15]
    donor_dict['mama'] = [12, 200, 2, 66]
    donor_dict['bompa'] = [1000]
    donor_dict['bobonne'] = [500, 500]
    donor_dict['onbekende'] = [1000000]

    DonorDict = Donor_Collection(donor_dict)

    response = input('Please choose between the following 3 actions:\
    1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >  ')
    try:
        int(response)
    except:
        while not response.isdigit():
            print("You didn't enter a number.")
            print()
            response = input('Please choose between the following 3 actions:\
            1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >  ')
    arg_dict = {1:thankyou, 2:report, 3:thankyoueveryone}

    while int(response) != 4:
        try:
            arg_dict.get(int(response))(DonorDict)

        except (TypeError, ValueError):
            print('This is an invalid choice. Please enter a number between 1 and 4.')
            print()
            response = input('Please choose between the following 3 actions:\
            1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >  ')
        else:
            response = input('Please choose between the following 3 actions:\
                1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. quit >   ')
        finally:
            if not response.isdigit():
                response = '99999'
