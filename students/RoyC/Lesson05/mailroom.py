#!/usr/bin/env python3
# Lesson 5, Mailroom with exception handling and Comprehension

# Donor data dictionary
donors = {
    "Ned Flanders": [1200.25, 850.35],
    "Martin Prince": [12.22, 19.56],
    "Edna Krabappel": [55.43, 118.67, 75.23],
    "Homer Simpson": [253.64, 772.50, 99.99],
    "Moe Szylak": [54.23]
}

# template used to format thank you letter
ltr_template = ("\n\nDear {donor_name},"
                "\n\nThank you for your generous donation of ${amt}."
                "\nThis brings your to-date total of donations to ${total}!"
                "\nYour kind help is greatly appreciated."
                "\n\nKindest regards, Monty Burns\n\n"
               )

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
                print(d)
            print()
        else:
            amt = 0.0
            donations = donors.setdefault(donor_name, [])
            while True:
                try:
                    amt = float(input("Enter amount of donation: "))
                except ValueError:
                    print("Not a valid donation format, please enter a number")
                else:
                    break
            donations.append(amt)
            record = {'donor_name' : donor_name, 'amt' : "{:.2f}".format(amt), 'total' : "{:.2f}".format(get_total(donations))}
            print(ltr_template.format(**record))
            break
    
def thank_all():
    """
    Write thank you letters for all donors to separate files
    """
    for donor, donations in donors.items():
        f = open(donor.replace(' ',  '_') + ".txt", 'w')
        last_donation = donations[-1:][0]
        donor_record = {'donor_name' : donor, 'amt' : "{:.2f}".format(last_donation), 'total' : "{:.2f}".format(get_total(donations))}
        f.write(ltr_template.format(**donor_record))
    print("\n{:d} thank you letters have been written!\n".format(len(donors)))

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
    
def total_sort(row_datum):
    """
    Sort donors for donor report based on total donations
    """
    return row_datum[1]

def create_report():
    """
    Print out a report listing historical donor totals to date
    """
    # print the report header
    header_row = "\n\n{:25} | {:11} | {:9} | {:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header_row)
    print("-" * len(header_row))
    # create list of row data from donors
    row_data = [[donor, get_total(donations), len(donations), get_avg(donations)] for donor, donations in donors.items()]
    # sort the list of donors (total donations, most to least) before printing report
    row_data.sort(key=total_sort, reverse=True)
    # iterate sorted donor list printing formatted rows
    for row_datum in row_data:
        print("{:28}${:>10.2f}{:>12}   ${:>12.2f}".format(row_datum[0], row_datum[1], row_datum[2], row_datum[3]))
    print("\n\n")
    
def quit_menu():
    """
    Return text to indicate operator selects quit
    """
    return "quit selected"

def display_menu(prompt, menu_dict):
    """
    Continually display the given options prompt, then prompt for a selection and invoke
    associated function from menu dict. If function returns exit string, then break loop.
    """
    while True:
        choice = input(prompt)
        try:
            if menu_dict[choice]() == "quit selected":
                break;
        except KeyError:
            print("\nThat is not one of the choices!\n")

# main menu prompt text
main_prompt = ("\nPlease choose one of these options:"
               "\n   1 - Send a Thank You"
               "\n   2 - Create a Report"
               "\n   3 - Send letters to Everyone"
               "\n   q - Quit"
               "\nEnter your selection => "
            )

# main menu dictionary, options and associated functions            
main_menu = {"1": send_thanx,
             "2": create_report,
             "3": thank_all,
             "q": quit_menu
            }
    
if __name__ == "__main__":
    display_menu(main_prompt, main_menu)