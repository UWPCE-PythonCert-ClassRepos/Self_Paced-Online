"""
Mailroom9.py
Written by Terrance Jones
Assignment for lesson 9 UW Selfpaced Online course
"""

class Donor:
    """Creates a donor with name and and empty dontation list """
    def __init__(self, name, donations=None):
        self._name = name
        if donations is None:
            self._donations = []
        else:
            self._donations = [donations]
       
    @property
    def name(self):
        """Returns donor name"""
        return self._name

    @property
    def donations(self):
        """Returns donations list for donor"""
        return self._donations

    def append_donations(self, value):
        self.donations.append(value)

    @classmethod
    def thank_you_letter(self, donor_name, donation_amount):
        dic = {'name': donor_name , 'amount_donated': donation_amount}
        return("Dear {name}, \n Thank you for your generous donation of ${amount_donated:,.2f}. \nSincerely, Mailroom.".format(**dic))


class DonorCollection:

    global donor_list
    donor_list = {'Carlos Santos':[25,50,100], 'Esperanza Gomez': [10,20,30], 'Paul Jackson':[5,10,15], 'Karl Black':[100,200,300], 'Charles Exx': [15,30,45]}

    @classmethod
    def donor_exists(self, donor):
        return donor in donor_list

    @classmethod    
    def show_donor_list(self):
        """Display list of all donors"""
        for key in donor_list.keys():
            print(key)

    @classmethod
    def add_or_update_donor(self, donor_name, donation_amount):
        if self.donor_exists(donor_name) is True: 
            donor_list[donor_name].append(donation_amount)
        else:
            donor_list[donor_name] = [donation_amount]

    @classmethod
    def get_report(self):
        """Returns a list of rows with donor name, total amount of donations, number of donations, and average donation """
        report = []
        
        for item in donor_list:
            name = item
            num_gifts = len(donor_list[item])
            total = sum(donor_list[item])
            average = float(round(total / num_gifts, 2))
            dic = {'name':name, 'total':total, 'num_gifts':num_gifts, 'average':average }
            new_row = "{name:<25} ${total:^10} {num_gifts:^10} ${average:^10}".format(**dic)
            report.append(new_row)
            new_row = ""
            report.append(new_row)
        return (report)


class cli_main:

    @classmethod
    def get_name(self):
        """get donor name from user"""
        while True:
            name = input("Enter the full name of the donor.")
            if name == "list":
                DonorCollection.show_donor_list()
                
            else:
                return name

    @classmethod
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

    @classmethod
    def thankyou(self):
        donor_name = cli_main.get_name()
        donation_amount = cli_main.get_amount()

        DonorCollection.add_or_update_donor(donor_name, donation_amount)

        print(Donor.thank_you_letter(donor_name, donation_amount))

    @classmethod
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

  
                




        


