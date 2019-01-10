"""
Mailroom9.py
Written by Terrance Jones
Assignment for lesson 9 UW Selfpaced Online course
"""

class Donor:
    """Creates a donor with name and and empty dontation list """
    def __init__(self, name, donation):
        self.name = name
        self.donations = [donation]

    @property
    def number_donations(self):
        """retern number of donations"""
        return len(self.donations)

    @property
    def total_donations(self):
        """return total of all donations"""
        return sum(self.donations)

    @property
    def average_donation(self):
        """return  average of donations"""
        return float(sum(self.donations) / len(self.donations))
   
    def add_donation(self, value):
        """adds value to list of donations"""
        self.donations.append(value)

    def show_donations(self):
        """returns all donations for a donor"""
        return self.donations

    @staticmethod
    def thank_you_letter(donor,amount):
        """returns a thank you letter to donon"""
        return "Dear {}, \n Thank you for your generous donation of {}!".format(donor, amount)

    def report(self):
        name = self.name
        num_gifts = self.number_donations
        total = self.total_donations
        average = self.average_donation
        dic = {'name':name, 'total':total, 'num_gifts':num_gifts, 'average':average }
        
        return "{name:<25} ${total:^10} {num_gifts:^10} ${average:^10}".format(**dic)     


class DonorCollection:
  
    def __init__(self, *args):
        self.donors = {d.name: d for d in args}

    def add_donation(self, donor, donation):
        if self.donors.get(donor):
            self.donors[donor].add_donation(donation)
        else:
            self.donors[donor] = Donor(donor, donation)

    def show_donors(self):
        donor_list = []
        for d in self.donors:
            donor_list.append(d)
        return donor_list

    def create_report(self):
        report_list = []
        heading = "{:<20s} | {:^10s} | {:^10s} | {:^10s} ".format("Donor Name", "Total Given", "Num Gifts", "Average")
        heading_underline = "-"
        print(heading)
        print(heading_underline * len(heading))
        for d in self.donors.values():
            report_list.append(d.report())
        return report_list

#OUTSIDE OF DONOR COLLECTION AND DONOR CLASSES

def menu_selection(prompt, dispatch_dict):
        while True:
            response = input(prompt)
            try:
                if dispatch_dict[response]() == "exit menu":
                    return
            except KeyError:
                print("Please select an option from the menu")

def sub_menu():
        while True:
            menu_selection(sub_prompt, sub_dispatch)


def get_name():
    name = input("Enter the full name of the donor.")
    if name == "list":
        a = DonorCollection()
        print (a.donors)
        name = get_name()
    else:
        return name

def get_amount():
    while True:
        try:
            amount = input("Enter the donation amount:")
            amount = float(amount)
        except ValueError:
            print("Donation amount must be a numeric value")
        
        else:
            return amount
    
def quit():
    print("Quitting this menu now")
    return "exit menu"


def print_thank_you():
        a = DonorCollection()
        donor_name = get_name()
        donation_amount = get_amount()
        a.add_donation(donor_name, donation_amount)
        print (Donor.thank_you_letter(donor_name,donation_amount))
        

def display_report():
        a = DonorCollection()
        print (a.create_report())


main_prompt = ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(q) Quit\n " 
                )
main_dispatch = {"1": print_thank_you,
                 "2": display_report,
                 "q": quit,
                 }

sub_prompt =  ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(q) Quit\n " 
                )

sub_dispatch = {"1": print_thank_you,
                 "2": display_report,
                 "q": quit,
                 }


if __name__ == '__main__':
      menu_selection(main_prompt, main_dispatch)

  
                

