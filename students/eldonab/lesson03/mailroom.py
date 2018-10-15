#!/usr/bin/env python3
#create a list of at least 5 donors.
donors_list = [["John Smith", 50000, 600000], ["Bill Gates", 100000, 400, 7000], ["Andy Jones", 400000, 600000], ["Hannah Jones", 30000, 40000], ["Anna Allen", 80000,90000, 1000]] 


# to add a new donation amount to an existing donor's name.
def add_donation_to_list(res_name):
    """Add a new donation amount to an existing donor's name."""
    amount = float(input("How much is the new donation amount? "))
    for donor in donors_list:
        if res_name in donor:
            donor.append(amount)


# to add a new donor name&donation amount:
def add_new_donor(new_donor):
    """Add a new donor name and donation amount."""
    amount = float(input("How much is the new donation amount? "))
    donors_list.append([new_donor, amount])
    

# to check whether donor already exists in the list.
def is__in_list(donor_name):
    """Check whether donor already exists in the list of donors."""
    for donor in donors_list:
        if donor_name in donor:
            return True


# to show existing list of donor names:
def show_list():
    """Show existing list of donor names"""
    for donor in donors_list:
        print(donor[0])


# If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.

def thank_you_note():
    name = input("Please, type the full name of a sponsor: ")
    while name == "list":
        show_list()
        name = input("Please, type the full name of a sponsor: ")
    else:
        if is__in_list(name):
            add_donation_to_list(name)
        else:
            add_new_donor(name)
    print(f"Dear {name}, thank you for your generous donation!")
        


# to print donation statistics for each donor:

def stat_donors():
    """Print donation statistics for each donor"""
    for donor in donors_list:
        a_donor = donor[0]
        total_don = sum(donor[1:])
        number_of_don = len(donor[1:])
        average_don = total_don//number_of_don
        print("{:<20} ${:>12,.2f}{:^12} ${:>12,.2f}".format(a_donor, total_don, number_of_don, average_don))



          
# to print a list of donors sorted by name, total donated amount, number of donations, and average donation amount:

def create_report():
    """Print a list of donors sorted by name, total donated amount, number of donation, and average donation amount"""
    print("{0:<20}{1:>12}{2:>12}{3:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("--------------------------------------------------------------------------------------------")
    stat_donors()



#Running the main interaction in if __name__ == '__main__':


if __name__ == '__main__':
    while True:
        action = input("Please tell us what you would like to do: 'send a thank you', 'create a report', 'quit' ")
        if action == "send a thank you":
            thank_you_note()
        elif action == "create a report":
            create_report()
        elif action == "quit":
            break

    
