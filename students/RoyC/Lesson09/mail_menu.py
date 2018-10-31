#!/usr/bin/env python3
# Lesson 9, mailroom menu

from mailroom import Donor, DonationRecords

# initialize array of donors
donor_array = [
    Donor("Ned Flanders", [1200.25, 850.35]),
    Donor("Martin Prince",[12.22, 19.56]),
    Donor("Edna Krabappel",[55.43, 118.67, 75.23]),
    Donor("Homer Simpson",[253.64, 772.50, 99.99]),
    Donor("Moe Szylak",[54.23])
]

# create a donor records set
donation_records = DonationRecords(donor_array)

def record_donation():
    """
    Prompt operator for donor name, or 'list' to see names of donors on record.
    Take name entered and either use existing donor, or add new record.
    Then prompt for amount of this donation, then save the donation record
    and print a thank you note.
    """
    while True:
        donor_name = input("\nEnter full name of donor (or 'list' to see names of donors): ")
        if donor_name == "list":
            for d in donation_records.donors:
                print(d.name)
            print()
        else:
            amt = 0.0
            while True:
                try:
                    amt = float(input("Enter amount of donation: "))
                except ValueError:
                    print("Not a valid donation format, please enter a number")
                else:
                    break
            donor = donation_records.record_donation(donor_name, amt)
            print(donation_records.send_thanx(donor, amt))
            break
            
def print_report():
    """
    Print the donor report to the screen
    """
    print(donation_records.create_report())
            
def thank_all():
    """
    Write thank you letters for all donors to separate files
    """
    donation_records.thank_all()
    
def clear_donor_list():
    """
    Clear the donor list
    """
    confirm = input("\n\nYou are about to clear all donor records! Are you sure? (Enter YES):")
    if confirm == "YES":
        # create a new DonationRecords object to clear
        donation_records.clear_donations()
        print("\nDonor records have been cleared\n")
        
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
               "\n   1 - Record Donation"
               "\n   2 - Create a Report"
               "\n   3 - Send letters to Everyone"
               "\n   4 - Clear donor data"
               "\n   q - Quit"
               "\nEnter your selection => "
            )

# main menu dictionary, options and associated functions            
main_menu = {"1": record_donation,
             "2": print_report,
             "3": thank_all,
             "4": clear_donor_list,
             "q": quit_menu
            }
    
if __name__ == "__main__":
    display_menu(main_prompt, main_menu)
        
 

