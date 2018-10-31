#!/usr/bin/env python3
# Lesson 3, Mailroom

# Donor data
donors = [
    ["Ned Flanders", [1200.25, 850.35]],
    ["Martin Prince", [12.22, 19.56]],
    ["Edna Krabappel", [55.43, 118.67, 75.23]],
    ["Homer Simpson", [253.64, 772.50, 99.99]],
    ["Moe Szylak", [54.23]]
]

def print_thank_you_letter(donor_name, amt):
    """
    Print a thank you letter to the given donor for the given donation amount
    Arguments:
        donor_name - name of this donor
        amt - amount of the donation (floating point)
    """
    print("\n\nDear {},\n".format(donor_name))
    print("Thank you for your generous donation of ${:.2f}.".format(amt))
    print("Your kind help is greatly appreciated.")
    print("\nKindest regards, Monty Burns\n\n")
    
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
            for d in donors:
                print(d[0])
            print()
        else:
            donor = [donor_name, []]
            for d in donors:
                if d[0] == donor_name:
                    donor = d
                    break
            else:
                donors.append(donor)
            amt = float(input("Enter amount of donation: "))
            donor[1].append(amt)
            print_thank_you_letter(donor_name, amt)
            break
    
def get_total(donations):
    """
    Return the total of the given list of donations
    Argument:
        donations - list of donation amounts (floating point nums)
    """
    total = 0;
    for donation in donations:
        total += donation
    return total

def get_avg(donations):
    """
    Return the average of the given list of donations
    Argument:
        donations - list of donation amounts (floating point nums)
    """
    return get_total(donations) / len(donations)
    
def total_sort(donor):
    """
    Sort donors for donor report based on total donations
    """
    return get_total(donor[1])

def create_report():
    """
    Print out a report listing historical donor totals to date
    """
    # print the report header
    header_row = "\n\n{:25} | {:11} | {:9} | {:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header_row)
    print("-" * len(header_row))
    # sort the list of donors (total donations, most to least) before printing report
    donors.sort(key=total_sort, reverse=True)
    # iterate sorted donor list printing formatted rows
    for d in donors:
        print("{:28}${:>10.2f}{:>12}   ${:>12.2f}".format(d[0], get_total(d[1]), len(d[1]), get_avg(d[1])))
    print("\n\n")
    

if __name__ == "__main__":
    while True:
        print("\nPlease choose one of these options:")
        print("  1 - Send a Thank You")
        print("  2 - Create a Report")
        print("  3 - Quit")
        choice = input("\nEnter your selection => ")
        
        if choice == "1":
            send_thanx()
        elif choice == "2":
            create_report()
        elif choice == "3":
            break;
