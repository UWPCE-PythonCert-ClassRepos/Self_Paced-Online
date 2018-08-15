#!/usr/bin/env python3
# Lesson 3, Mailroom

# Donor data
donors = [
    ["Homer Simpson", 253.64, 772.50, 99.99],
    ["Ned Flanders", 1200.25, 850.35],
    ["Edna Krabappel", 55.43, 118.67, 75.23],
    ["Moe Szylak", 54.23],
    ["Martin Prince", 12.22, 19.56]
]

def print_thank_you_letter(donor_name, amt):
    """
    Print a thank you letter to the given donor for the given donation amount
    Arguments:
        donor_name - name of this donor
        amt - amount of the donation (floating point)
    """
    print("\nDear {},\n".format(donor_name))
    print("Thank you for your generous donation of ${:.2f}.".format(amt))
    print("Your kind help is greatly appreciated.")
    print("\nKindest regards, Monty Burns\n")
    
def send_thanx():
    """
    Prompt operator for donor name, or 'list' to see names of donors on record.
    Take name entered and either use existing donor, or add new record.
    Then prompt for amount of this donation, then save the donation record and
    print a thank you note.
    """
    while True:
        donor_name = input("\nEnter full name of donor (or 'list' to see names of donors): ")
        if donor_name == "list":
            for d_list in donors:
                print(d_list[0])
            print()
        else:
            donor = [donor_name]
            for d in donors:
                if d_list[0] == donor_name:
                    donor = d_list
                    break
            else:
                donors.append(donor)
            amt = float(input("Enter amount of donation: "))
            donor.append(amt)
            print_thank_you_letter(donor_name, amt)
            break
    

def create_report():
    pass

if __name__ == "__main__":
    while True:
        print("Please choose one of these options:")
        print("  1 - Send a Thank You")
        print("  2 - Create a Report")
        print("  3 - Quit")
        choice = input("Enter your selection => ")
        
        if choice == "1":
            send_thanx()
        elif choice == "2":
            create_report()
        elif choice == "3":
            break;
