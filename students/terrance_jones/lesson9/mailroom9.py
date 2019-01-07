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
        return sum(self.donations) / len(self.donations)
   
    def add_donation(self, value):
        """adds value to list of donations"""
        self.donations.append(value)

    def show_donations(self):
        """returns all donations for a donor"""
        return self.donations

    def thank_you_letter(self):
        """returns a thank you letter to donon"""
        return "Dear {}, \n Thank you for your generous donation of ${}. \nSincerely, Mailroom.".format(self.name, self.donations)



class DonorCollection:
    #donor_list = {'Carlos Santos':[25,50,100], 'Esperanza Gomez': [10,20,30], 'Paul Jackson':[5,10,15], 'Karl Black':[100,200,300], 'Charles Exx': [15,30,45]}
    def __init__(self, *args):
        self.donors = {d.name: d for d in args}


    def donor_list(self):
        dlist = []
        for d in self.donors:
            dlist.append(d)
        return dlist

    def donor_exists(self, donor):
        return donor in self.donors.keys()

    def add_donation(self, donor, donation):
        if self.donors.get(donor):
            self.donors[donor].add_donation(donation)
        else:
            self.donors[donor] = Donor(donor, donation)







class cli_main:

    def get_name(self):
        """get donor name from user"""
        while True:
            name = input("Enter the full name of the donor.")
            if name == "list":
                DonorCollection.show_donor_list()
                
            else:
                return name

    def get_amount(self):
        """Gets donation amount from user."""
        while True:
            try:
                amount = input("Enter the donation amount:")
                amount = float(amount)
            except ValueError:
                print("Donation amount must be a numeric value")
        
            else:
                return amount

    
    def thankyou(self):
        donor_name = cli_main.get_name()
        donation_amount = cli_main.get_amount()

        DonorCollection.add_or_update_donor(donor_name, donation_amount)

        print(Donor.thank_you_letter(donor_name, donation_amount))

  
    def display_report(self):   
        heading = "{:<20s} | {:^10s} | {:^10s} | {:^10s} ".format("Donor Name", "Total Given", "Num Gifts", "Average")
        heading_underline = "-"
        print(heading)
        print(heading_underline * len(heading))
    
        for row in DonorCollection.get_report():
            print(row)

    @classmethod
    def menu_selection(self, prompt, dispatch_dict):
        """displays the menu. asks for user to select option. if option is not available will throw KeyError and ask the user for new input"""
        while True:
            response = input(prompt)
            try:
                if dispatch_dict[response]() == "exit menu":
                    return
            except KeyError:
                print("Please select an option from the menu")

    @classmethod
    def sub_menu(self):
        while True:
            menu_selection(sub_prompt, sub_dispatch)


    @classmethod
    def quit(self):
        print("Quitting this menu now")
        return "exit menu"


main_prompt = ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(q) Quit\n " 
                )

main_dispatch = {"1": cli_main.thankyou,
                 "2": cli_main.display_report,
                 "q": cli_main.quit,
                 }

sub_prompt =  ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(q) Quit\n " 
                )

sub_dispatch = {"1": cli_main.thankyou,
                 "2": cli_main.display_report,
                 "q": cli_main.quit,
                 }


if __name__ == '__main__':
    cli_main.menu_selection(main_prompt, main_dispatch)

  
                




        


