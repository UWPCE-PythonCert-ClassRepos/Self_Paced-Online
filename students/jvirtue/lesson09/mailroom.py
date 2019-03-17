#Lesson 9 Assignment 1
#Mailroom Part 5 Assignment
#Jason Virtue 03/13/2019
#UW Self Paced Python Course

class Donor():
    def __init__(self, name):
        self._name = name
        self._donations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,donor_name):
        self._name = donor_name

    @property
    def donations(self):
        return self._donations
    
    #Add Donations from Dict
    def amount_add(self,donor_donation):
        self.donations.append(float(donor_donation))

    #Thank you message in console app
    def thank_you(self, name, donation):
        return "Thank you {} ".format(name) + "for the donation in the amount of {}!".format(donation)

class Donor_Collections():
    def __init__(self):
        self._donors = []
    
    @property
    def donors(self):
        return self._donors

    def donor_add(self,donor):
        self.donors.append(donor)

    #List out unique donors
    def donor_list(self):
        name_list = []
        for donor in self._donors:
            name_list.append(donor.name)
        return name_list
    
    #Add to dictionary donor and amount
    def add_donation_amount(self, name, donation_amount):
        for donor in self._donors:
            if donor.name == name:
                donor.donations.append(donation_amount)
                break
    
    #Build list of donors, amount, count of contributions and average gift amount
    def crunch_numbers(self):
        summary_list = []
        for donor in self._donors:
            total = sum(donor.donations)
            number_of_gifts = len(donor.donations)
            average = total / number_of_gifts
            summary_list.append([donor.name, total, number_of_gifts, average])
            summary_list.sort(key=self.sort_key,reverse=True)
        return summary_list

    #Sort key for donor list.  Sort by donation amount
    def sort_key(self,crunch_numbers):
        return crunch_numbers[1]

    #Print report to console
    def create_report(self):
        print("\n","-" * 68,sep="")
        print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
        print("-" * 68)
        sort_table = self.crunch_numbers()
        [print(f'{item[0]:<20}{" ":<1}{"$":<1}{item[1]:>14}{" ":<1}{item[2]:>15}{" ":<1}{"$":<1}{item[3]:>14}') for item in sort_table]

    #Thank you letter files to text file for all donors
    def thanks_file(self):
        for data in self.crunch_numbers():
            filename = data[0].replace(" ", "_") + ".txt"
            total_donation = data[1]
            letter = ('Thank you {} for you generous contributions totaling {:.2f}!'.format(data[0], total_donation))
            open(filename, 'w').write(letter)
            print(f"{data[0]}'s letter has been saved to " + filename)

    #Option menu 1 -- input donors and amounts into DICT
    def send_thanks(self):
        print("-"*40)
        name = input("What is the full name of the donor? (Name, List, Exit)> ").title()
        if name != "Exit":
            if name == "List":
                print("-"*40,"\nHere are our Donors:> \n",self.donor_list(),sep="")
            elif name not in self.donor_list():
                new_donor = Donor(name)
                self.donor_add(new_donor)
                try:
                    print("-"*40)
                    donation_amount = float(input("How much money did {} donate?> ".format(name)))
                    self.add_donation_amount(name,donation_amount)
                except ValueError:
                    print("-"*40, "\nPlease enter a valid numeric value.\n","-"*40,sep="")
                    return
                print("-"*40,"\n",Donor.thank_you(self, name, donation_amount),sep="")
            elif name in self.donor_list():
                try:
                    print("-"*40)
                    donation_amount = float(input("How much money did {} donate?> ".format(name)))
                    self.add_donation_amount(name,donation_amount)
                except ValueError:
                    print("-"*40, "\nPlease enter a valid numeric value.\n","-"*40,sep="")
                    return
                print("-"*40,"\n",Donor.thank_you(self, name, donation_amount),sep="")
        return
                
#Main menu quit program
def quit():
    return "Quit"

#Read Donations into DICT{}
def donation_read():
    donation_history = {'Fred Flintstone': [100, 200],
                        'Wilma Flintstone': [300],
                        'Bamm-Bamm Rubble': [50,30,40],
                        'Barney Rubble': [75],
                        'Pebbles Flintstone': [500]}
    donors_collection = Donor_Collections()

    for name, donations in donation_history.items():
        donor = Donor(name)
        for donation in donations:
            donor.amount_add(donation)
        donors_collection.donor_add(donor)
    return donors_collection

def main_menu():
    menu_dict = {1:donors_collection.send_thanks,2:donors_collection.create_report,3:donors_collection.thanks_file,4:quit}
    while True:
        print("\n","-"*40,"\nMailroom Main Menu;\n","1: Send a Thank You\n","2: Create a Report\n","3: Send letters to everyone\n","4: Quit\n","-"*40,sep="")
        try:
            response = int(input("Please select option [Enter number 1 - 4]: "))    
        except ValueError:
            print("-"*40,"\nValid values are numeric and does not accept characters\n","-"*40,sep="")
            continue
        try:
            if menu_dict[response]() == "Quit":
                break         
        except KeyError:
            print("-"*40,"\nPlease enter a valid number between 1 to 4.\n","-"*40,sep="")

if __name__ == '__main__':
    donors_collection = donation_read()
    main_menu()