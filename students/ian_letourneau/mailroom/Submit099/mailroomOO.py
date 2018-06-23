#!/usr/bin/env python3
# Ian Letourneau
# 5/11/2018
# A script that stores values for donors and their donations.
# The script can process requests from the user on various functions
# to utilize these values
import datetime

# Build a dictionary of existing donors


class Donor:
    """An object that contains information for donors and their donations.
        attribute name: donors name.
        attribute donation_list: a list of given donations."""

    def __init__(self, name, donations=None):
        """Initialization for Donor objects.

        Params name: Will be the name given to Donor object
        Params donations: a value or list of values to be 
            combined into donation_list attribute."""
        self.name = name
        if isinstance(donations, list):
            self.donation_list = donations
        elif donations == None:
            self.donation_list = []
        else:
            self.donation_list = [donations]

    @property
    def total(self):
        """Getter for donation total."""
        return sum(self.donation_list)

    @property
    def name_length(self):
        """Getter for donor name length."""
        return len(self.name)

    @property
    def don_num(self):
        """Getter for number of donations."""
        return len(self.donation_list)

    @property
    def average(self):
        """Getter for average donation amount."""
        return (self.total/len(self.donation_list))

    def append(self, donation):
        """Append function to tack on future donations."""
        self.donation_list.append(donation)

    def __eq__(self, other):
        """Override equals comparison method."""
        return self.total == other.total

    def __lt__(self, other):
        """Override less than comparison method."""
        return self.total < other.total

    def send_thank_you(self, donation):
        """A function to send thank you letter utilizing given amount and
        referenced donor object."""

        # Append the amount to the running donation_list.
        self.append(donation)

        out_string = ('Dear {}, we wanted to say thank you for your generous'
                      ' donation of ${:.2f}!'.format(self.name, donation))
        print("")
        return out_string


class DList(list):
    """A list object that holds donor objects and applies specific
    functions to those objects."""

    def __init__(self, *args):
        """Initialization for donor_lists.

        params *args: take in all donor objects and create a list
            of donors."""
        self.out_list = []
        list.__init__(self, list(args))

    def longest_name(self):
        """Return length od longest donor name in DList."""
        names = []
        for donor in self:
            names.append(donor.name)
        return len(max(names, key=len))

    def create_report(self):
        """A function that loops through all donor objects and creates
        an output string attribute that holds the report string variable."""
        for donor in self:
            self.out_list.append("{},{:.2f},{},{:.2f}".format(
                donor.name, donor.total, donor.don_num, donor.average))

    def display_report(self):
        """A function that displays the report string variable for each
        donor object, sorted by total amount donated."""

        # Print header line of table adjusting column length by length of name
        print("")
        print("{:{align}{width}} | {:<10} | {:<10} | {:<10}".format(
            "Donor Name", "Total Given", "Num Gifts", "Average Gift",
            align='<', width=str((self.longest_name()+1))))
        print("-"*(self.longest_name()+43))

        # Sort List in descending order using total donation amount."""
        self.sort(reverse=True)

        # Print donor rows of table.
        for donor in self:
            print("{:{align}{width}} $ {:>11.2f}   {:>10d} $ {:>10.2f}".format(
                donor.name, donor.total, donor.don_num, donor.average,
                align='<', width=str((self.longest_name())+2)))

    def send_all(self):
        """A function that sends a Thank You letter to every donor in the form of
        creating and writing to a .txt file titled with their name and the current
        date. The .txt includes their name and their total donations within the
        thank you memo."""
        now = datetime.datetime.now()
        letters = []
        # Loop through each donor in the list and calculate total donations.
        for donor in self:
            donorFile = donor.name.replace(" ", "")
            # Format .txt filename using the donors name and the current date.
            # Then create file and write thank you letter within open .txt
            # file.
            filename = "{}_{}_{}_{}.txt".format(
                donorFile, now.year, now.month, now.day)
            f = open(filename, "w+")
            f.write('Dear {}, we wanted to say thank you for your generous'
                    ' total donations of ${:.2f}! We hope to continue seeing'
                    ' you in the future!'.format(
                        donor, float(donor.total)))
            f.close()
            letters.append(filename)
        letter_string = ("{} "*len(letters)).format(*letters)
        print("The following letters have been created: {}".format(
            letter_string))
        return letters


def name_amount_veri():
    """A function that goes through various input validation loops to ensure
    user input will run through the funcion. 'q' will quit back to the main
    menu."""
    print("")
    name_prompt = ("Please enter a full name to send to or enter"
                   " 'list' for a full list of donors('q' to quit"
                   " to menu): ")
    name = input(name_prompt)
    if name == 'q':
        return 0, 0
    # If list is chosen, print a list of donors and reprompt for a
    #  name, 'q' # to quit to main menu
    while name == 'list':
        for donor in donors:
            print(donor.name)
        name = input(name_prompt)
    if name == 'q':
        return 0, 0
    # Once name is input, prompt for a donation amount, 'q' to quit
    amount = input(
        "Please enter the amount that was donated('q' to quit"
        " to menu): ")
    if amount == 'q':
        return 0, 0
    while True:
        try:
            amount = float(amount)
        except ValueError:
            amount = input(
                "Invalid. Please enter the amount that was donated: ")
            continue
        break
    return name, amount


def menu():
    """A function to store the menu prompt. Called first in __main__"""
    print("""\nHello User! What would you like to do?
1) Send a Thank You card
2) Create a report of donors
3) Send a Thank You to everyone
4) Quit \n""")


if __name__ == '__main__':
    """This area is always exectued by the script. It contains the main menu
    prompt as well as the calls to the previous two functions depending on
    which option was chosen. The third option allows the user to quit the
    script."""

    LBdonations = [6578921.00, 3.50, 23400.00, 7234.00]
    BGdonations = [1235544.00, 456789.50, 2347899.75]
    JKdonations = [456.37, 25.67, 999876.00, 2134.78, 3.14]
    d1 = Donor("LeBron James", LBdonations)
    d2 = Donor("Bill Gates", BGdonations)
    d3 = Donor("Jimmy Kimmel", JKdonations)
    donors = DList(d1, d2, d3)

    response = ''
    while True:
        menu()
        prompt = ("Please input a numerical value for"
                  " what you would like to do: ")
        response = input(prompt)
        while response not in ('1', '2', '3', '4'):
            response = input("Invalid input. " + prompt)

        # Once response has been verified and is not 3 to quit, call the
        # appropriate function
        if response == '1':
            name, amount = name_amount_veri()
            if name == 0:
                continue
            for donor in donors:
                if donor.name == name:
                    donor.send_thank_you(amount)
            else:
                donors.append(Donor(name))
                donors[-1].send_thank_you(amount)
        elif response == '2':
            donors.create_report()
            donors.display_report()
        elif response == '3':
            donors.send_all()
        elif response == '4':
            break
