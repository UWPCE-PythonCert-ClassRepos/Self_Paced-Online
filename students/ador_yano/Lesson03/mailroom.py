#!/usr/bin/env python3
# mailroom.py implements the Lesson 3 - Mailroom Part 1 assignment from UWPCE Python Programming

intro = '''
UWPCE Python Programming: Lesson 3 Assignment -- Mailroom Part 1
'''
print(intro)

####################################
# Global variables
#####################################

# Donors database - initially populated with 5 donors, 1-3 donations each
# Data structure: List of lists in which first item is donor name, followed by varying number of amounts donated
donors_db = \
[["Mark Zucherberg",200.00, 300.00, 400.00],\
["William Gates, III",500.00, 600.00],\
["Paul Allen",750.00, 620.00],\
["Elon Musk",9500.00, 5500.00],\
["Jeff Bezos",700.00]]

#####################################
# Sub Functions
#####################################
# Function: introduce program and prompt user for user_input
def prompt_user(response):
    print("-" * 66)
    print("This donor management program enables you to: \n\t1. Send a Thank You\n\t2. Display a Report")
    print("Enter 1, 2, or 'quit' to get out of the program.")
    response = input("What do you want to do? ")        # Prompt user for a response
    return response                                     # Value sent back as string



# Function: show list of donors in the donors database,
def show_list():
    print("List of Donors")
    print("-" * 66)
    for donor_record in donors_db:              # Loop through the donors database for each donor
        donor_name = donor_record[0]            # Get the name of the donor
        print("{:<26}".format(donor_name))      # Display donor name

# Function: check if donor is in database
def in_list(name):
    for donor_record in donors_db:              # Loop through donor records in donors database
        if name == donor_record[0]:             # check if donor has a record already
            return True

# Function: show thank you note
def display_note(name, gift):                 # Display email to terminal
    print("Dear {}, \nThank you for your gift of ${:,.2f}. \nWe appreciate your support.\nBest regards,\nJohn Cleese".format(name, gift))

# Function: add donation
def add_donation(name, gift):
    for donor_record in donors_db:              # Loop through donor records in donors database
        if name != donor_record[0]:             # Check if donor has a record
            continue
        else:
            donor_record.append(gift)           # If donor has a record, add this new donation

# Function: add donor
def add_newdonor(name, gift):                   # Add a new donor with the first gift to the database
    donors_db.append([name, gift])

# Function: show list of donors if asked, then get donor info thank you note
def send_thanks():
    donor = input("What's the full name of the donor? (Get a list by entering 'list') ")          # Prompt for full name
    if donor == "list":
        show_list()                             # Show list if requested
    else:
        donation = float(input("How much is being donated by this donor? ")) # prompt for donation amounts (convert entry to number)
        if in_list(donor):                      # Check if donor is already in the donors database
            add_donation(donor, donation)       # If so, add the donation to his list of gifts
        else:
            add_newdonor(donor, donation)       # If not, add a new record with a new donor and first gift
        display_note(donor, donation)           # Show the thank you message to the screen


# Function: show full report of donors and their donation history
def show_report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("-" * 66)
    for donor_record in donors_db:                  # loop through each record of donors
        donor_name = donor_record[0]                # get donor name
        gifts = donor_record[1:]                    # get list of gift amounts that follow name
        num_gifts = len(gifts)                      # count number of gifts given by donor
        total_given = 0
        for gift in gifts:                          # loop through list of gifts
            total_given = total_given + gift        # add all the gift amounts for total gifts
        if num_gifts != 0:                          # check if zero gifts to prevent dividing by zero
            ave_gift = total_given//num_gifts       # get average gift amount
        else:
            ave_gift = 0                            # if not gifts, set average amount to zero
        print("{:<26} ${:>12.2f}  {:>9d}   ${:>11.2f}".format(donor_name, total_given, num_gifts, ave_gift)) # display donor database in formatted rows and columns



#####################################
# Main program
#####################################
if __name__ == '__main__':
# Main function: display menu and user interaction based on user choice
    user_choice = ''
    while user_choice != "quit":
        user_choice = prompt_user(user_choice)      # call prompt_user function until user chooses to quit
        if user_choice == '1':
            send_thanks()                           # call send_thanks function if user chooses 1
            continue                                # continue prompting user until user quits
        elif user_choice == '2':                    # call show_report function if user chooses 2
            show_report()                           # call show_report function if user chooses 2
            continue                               # continue prompting user until user quits
        else:
            continue                               # continue prompting user until user quits
    print("Goodbye.")                              # if user chooses quit, while loop stops, ending program
