#!/usr/bin/env python3

class Donor():
    def __init__(self, name=None):
        self._name = name
        self._donations = []

    @property
    def name(self):
        """Property for the donor's name."""
        return self._name

    @name.setter
    def name(self, val):
        """Setter for the donor's name."""
        self._name = val

    @property
    def donations(self):
        """Property for the donor's list of donations."""
        return self._donations

    @donations.setter
    def donations(self, val):
        """Setter for the donor's list of donations."""
        self._donations = val


class Donor_Collection(dict):
    def __init__(self, donors):
        self._donors = donors

    @property
    def donors(self):
        """Property for the Donor_Collection's list of donors."""
        return self._donors

    @donors.setter
    def donors(self, val):
        """Setter for the Donor_Collection's list of donors."""
        self._donors = val

    def add_donor(self, donor):
        """Add a new donor to the collection."""
        self.donors[donor.name] = donor.donations

    def donate(self, name, donation):
        """Add a donation to the list of donations for a specific donor.
        If the donor doesn't exist yet, then add it to the donor collection first."""
        if name not in self.donors.keys():
            new_donor = Donor(name)
            self.add_donor(new_donor)
        if not donation.isdigit():
            raise Exception("ERROR: You didn't enter a number or a negative number.")
        else:
            self.donors[name].append(int(donation))

    def challenge(self, factor):
        for key in self.donors:
            self.donors[key] = list(map(lambda x: x*factor, self.donors[key]))


    def createfile(self, name):
        """create .txt file containing thank you letter for each person who made a donation"""
        d = {'name':name, 'donation':self.donors[name][-1]}
        outfile = open(name+'.txt', 'w')
        outfile.write("Dear {name} , \n\n".format(**d))
        outfile.write("\t Thank you very much for your generous donation of ${donation}. \n\n".format(**d))
        outfile.write("\t It will be put to very good use. \n\n")
        outfile.write("\t\t Sincerely, \n")
        outfile.write("\t\t   -The Team \n")
        outfile.close()

    def create_report(self):
        """For all donors in the Donor_Collection class, write a report containing
        the donor's name, how much he gave in total, how many gifts the donor made and
        how much the donor gave on average."""
        print(f'{"Donor Name":20s} {"|  Total Given":20s} {"|  Num Gifts  |":20s} {"Average Gift":20s}')
        print(f'{"-"*76}')
        [print(f'{name:20s} ${sum(self.donors[name]):20.2f} {len(self.donors[name]):13d}${sum(self.donors[name])/len(self.donors[name]):20.2f}') for name in self.donors.keys()]



def thankyou(donordict):
    """If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure
    and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    """
    while True:
        name = input('Please enter a name or type "list" to see a list of names > ')
        if name == 'list':
            print(donordict.donors.keys())
        else:
            break

    success = False
    while not success:
        donation = input('Please enter a donation amount > ')
        try:
            donordict.donate(name, donation)
            success = True
        except Exception as err:
            print(err.args[0])
            success = False

    d = {'name':name, 'donation':donation}
    print("Dear {name} , thank you very much for your generous donation of {donation}. Looking forward receiving even more money next time.".format(**d))
    print(donordict.donors.keys())
    print(donordict.donors.values())

def multiply(donordict):
    success = False
    while not success:
        factor = input('Please enter a factor > ')
        try:
            donordict.challenge(int(factor))
            success = True
        except Exception as err:
            print(err.args[0])
            success = False

    d = {'factor':factor}
    print("Thank you for multiplying all donations by a factor {factor}. Looking forward receiving even more money next time.".format(**d))
    print(donordict.donors.keys())
    print(donordict.donors.values())

def report(donordict):
    """call the create_report() method of the Donor_Collection class
    and write report with summary of the donations of all donors."""
    donordict.create_report()

def thankyoueveryone(donordict):
    """call the createfile() method of the Donor_Collection class
    and write thank you letter for each donor."""
    [donordict.createfile(name) for name in donordict.donors.keys()]




if __name__ == '__main__':
    donor_dict = {}
    donor_dict['papa'] = [100, 5, 15]
    donor_dict['mama'] = [12, 200, 2, 66]
    donor_dict['bompa'] = [1000]
    donor_dict['bobonne'] = [500, 500]
    donor_dict['onbekende'] = [1000000]

    DonorDict = Donor_Collection(donor_dict)
    question = 'Please choose between the following 4 actions: 1. Send a Thank You; 2. Create a Report; 3. Send letters to everyone; 4. Multiply all donations 5. quit >  '

    response = input(question)
    try:
        int(response)
    except:
        while not response.isdigit():
            print("You didn't enter a number.")
            print()
            response = input(question)
    arg_dict = {1:thankyou, 2:report, 3:thankyoueveryone, 4:multiply}

    while int(response) != 5:
        try:
            arg_dict.get(int(response))(DonorDict)

        except (TypeError, ValueError):
            print('This is an invalid choice. Please enter a number between 1 and 5.')
            print()
            response = input(question)
        else:
            response = input(question)
        finally:
            if not response.isdigit():
                response = '99999'
