#!/usr/bin/env python3

# new file for lesson 9 work to incorporate classes.


class Donor:
    def __init__(self, name, *donation):
        self.name = name
        self.donations = donation[0]
        #Need to add code for creating without existing donation?

    @property
    def sum_donations(self):
        return sum(self.donations)


    @property
    def avg_donations(self):
        return sum(self.donations)/len(self.donations)

    
    def new_donation(self,new):
        return self.donations.append(new)




class Donors:
    def __init__(self):
        self.data = {}
    

    def new_donor(self,donor):
        #currently allows to add one individual donor with list of donations
        self.data[donor.name] = donor.donations
        #print(self.data)


    def display_list(self):
        for name in self.data.keys():
            print(name)

    
    def add_donation(self,name,amount):
        #add doination to existing donor within Donors
        self.data[name].append(amount)
        #print(self.data)


    def write_letter(self,name,amount):
        line_one = 'Dear {},'.format(name)
        line_two = "Thank you for donating ${:.2f} to the Human Fund. Your money will be used appropriately.".format(amount)
        letter = line_one + "\n" + line_two
        return letter
    

    def write_report(self): #need to add the rest of the code to prepare the data
        donors_report = []
        for name, amount in self.data.items():
            sum_donation = 0
            avg_donation = 0
            for i in amount:
                sum_donation = sum_donation + i
                num_donation = len(amount)
            avg_donation = sum_donation/num_donation
            donors_report.append([sum_donation, name, num_donation, avg_donation])
        donors_report.sort(reverse=True)
        print('Donor Name                | Total Given | Num Gifts | Average Gift')
        print('-'*67)
        for i in donors_report:
            print('{1:27}${0:11.2f}{2:12}  ${3:12.2f}'.format(*i))
    

    def letter_files(self):
        for name in self.data:
            donation = ddonors[name][0]
            with open('{}.txt'.format(name), 'w') as f:
                f.write(self.write_letter(name, donation))
        print("Letter files created.")


########################Classes above here



def thank_you():
    """Function to send a thank you letter."""
    while True:
        input_name = input("Enter full name: ")
        if input_name in donor_set.data.keys():
            while True:
                try:
                    donation = float(input("Enter donation amount:"))
                except ValueError:
                    print("Donation needs to be a number.")
                else:
                    break
            donor_set.add_donation(input_name,donation)
            #ddonors[input_name].append(donation)
            print(donor_set.write_letter(input_name,donation))
            break
        elif input_name == 'list':
            donor_set.display_list()
            
        else:
            print("Adding {} to donor database".format(input_name))
            while True:
                try:
                    donation = float(input("Enter donation amount:"))
                except ValueError:
                    print("Donation needs to be a number.")
                else:
                    break
            new_guy = Donor(input_name,[donation])
            donor_set.new_donor(new_guy)
            print(donor_set.write_letter(input_name,donation))
            #print(ddonors)
            break



 
if __name__ == "__main__":
    # Adding this to import preset data.
    a = Donor("James Hinchcliffe", [12.2,2.51,3.20])
    b = Donor("Robert Wickens", [1024.14,22.21,323.45])
    c = Donor("Sam Schmidt", [3.2,5.55,4.20])
    donor_set = Donors()
    donor_set.new_donor(a)
    donor_set.new_donor(b)
    donor_set.new_donor(c)
    main_switch_function = {"1": thank_you, "2": donor_set.write_report, "3": donor_set.letter_files, "4": exit}
    while True:
        print("What do you want to do?")
        response = input("1. Send a Thank You, 2. Create a Report, 3. Send all letters, 4. Quit: ")
        try:
            main_switch_function.get(response)()
        except TypeError:
            print("Not a valid input.")