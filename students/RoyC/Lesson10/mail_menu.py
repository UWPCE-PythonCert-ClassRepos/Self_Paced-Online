#!/usr/bin/env python3
# Lesson 10, functional programming mailroom menu

from mailroom_fp import Donor, DonationRecords

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
            amt = inputNum("Enter amount of donation: ")
            if (amt is not None):
                donor = donation_records.record_donation(donor_name, amt)
                print(donation_records.send_thanx(donor, amt))
                break
            
def input_num(prompt, skip=None):
    """
    Common method for entering a numeric value, testing that a valid number was
    entered before returning. The skip argument allows the entry to be skipped.
    """
    entry = input(prompt)
    if (entry == skip):
        return None
        
    while True:
        try:
            return float(entry)
        except ValueError:
            return input_num("Please enter a valid number, or 'quit'", skip="quit")
    
            
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
        
def calculate_challenge_projection():
    """
    Request challenge values and displays the result
    """
    print("\nProjecting challenge donations:")
    min = input_num("Enter minimum donation amount or 'none': ", skip="none")
    max = input_num("Enter maximum donation amount or 'none': ", skip="none")
    factor = input_num("Enter challenge factor: ")
    print("\n*** Total projected donations for these entries is ${:.2f} ***\n".format(donation_records.challenge(factor, min=min, max=max)))

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
               "\n   5 - Calculate challenge projection"
               "\n   q - Quit"
               "\nEnter your selection => "
            )

# main menu dictionary, options and associated functions            
main_menu = {"1": record_donation,
             "2": print_report,
             "3": thank_all,
             "4": clear_donor_list,
             "5": calculate_challenge_projection,
             "q": quit_menu
            }
    
if __name__ == "__main__":
    display_menu(main_prompt, main_menu)
        
 

