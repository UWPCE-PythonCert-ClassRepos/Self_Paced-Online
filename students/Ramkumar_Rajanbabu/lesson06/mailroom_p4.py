#Mailroom Part 4

import sys

donors_db = {"William Gates, III": [653772.32, 12.17],
             "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
             "Jeff Bezos": [877.33],
             "Paul Allen": [663.23, 43.87, 1.32],
             "Ramkumar Rajanbabu": [200.30, 50.10, 5.25]}

def main():
    """Display menu with options to user."""
    
    prompt = "\n".join(("Menu: ",
                        "Please choose from below options:",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Send Letters to all donors",
                        "4 - Quit",
                        ">>> "))
    
    while True:
        #Exception Handling
        try:
            user_response = int(input(prompt))
        except ValueError: #ValueError if not integer/float
            print("Please enter a number (not a string)!")
        else:
            if user_response == 1:
                send_thanks()
            elif user_response == 2:
                display_report()
            elif user_response == 3:
                send_letters_all()
            elif user_response == 4:
                exit_program()
            elif user_response not in range(1,4):
                print("Please enter a valid number within 1-4!\n")
            
def exit_program():
    """Exit program."""
    
    print("\nYou chose to quit the program, good-bye!")
    sys.exit() #Exit script
            
def send_thanks():
    """Show a list of donors and add a new donor based on user response."""

    name = str(input("Type in the full donor name (or 'list' to view a list of donor names): "))
    if name == "list":
        view_list()
        send_thanks() #Reprompt to main menu
    else:
        add_donation(name)

def view_list():
    """To view donor names in a vertical list."""
    
    print("\nList of Donor Names:")
    for donor_name in donors_db.keys():
        print(donor_name) #Prints each name (key)
        
def add_donation(name):
    """Add new donation amount to donor list based on user response.
    
    Args:
        name: donor name
    """
    
    if name not in donors_db:
        donors_db[name] = [] #donors_db[key] = [value]

    #Exception handling
    try:
        donation_amount = float(input("Type in the donation amount: $"))
    except ValueError: #ValueError if not integer/float
        print("Please enter an integer.")
    else:
        donors_db[name].append(donation_amount) #donor_db[key].append()
        print(write_letter(name, donation_amount))            

def write_letter(name, donation_amount):
    """Generates letter based on donor name and donation amount.
    
    Args:
        name: donor name
        donation_amount (float): donation amount  
    Returns:
        letter (string): a letter in string format
    """
    
    letter = "\n\tDear {:s}, \n\n\tThank you for choosing to donate to this group. A special thank you for your generous donation of ${:0.2f}. \n\n\tSincerely, \n\tDonation Society".format(name, donation_amount)
    return letter 

def display_report():
    """Display the report (table with values)."""
    
    report = create_table()
    print(report)

def create_table():
    """Create a table with values.
    
    Returns: 
        table (string): format string with table values
    """
    
    table = create_title()
    summary = calc_donor()
    for donor_tuple in summary:
        row = "\n{:<25s}  ${:>11.2f}  {:>10d}  ${:>12.2f}".format(*donor_tuple) #f_string
        table += row
    return table

def create_title():
    """Create a title for report.
    
    Returns:
        title (string): format string with title header for table
    """
    
    title = "\n{:<25s} | {:s} | {:s} | {:s}\n".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    title += ((len(title) - 1) * "-")
    return title     

def calc_donor():
    """Calculate table values for the report.
    
    Returns:
        summary (list): a list of table values
    """
    
    #List comprehension
    summary = [(donor_name, sum(amount), len(amount), sum(amount) / len(amount)) for donor_name, amount in donors_db.items()]
    summary = sorted(summary, key=sort_key, reverse=True)
    return summary

def sort_key(summary):
    """Creates sort key for sorted function.
    
    Args:
        summary: list with donor summary
    Returns:
        summary[1]: sorts by total_given values
    """
    return summary[1]      
        
def send_letters_all():
    """Generates a thank you letter for each donor and writes each letter as a text file."""
    
    for donor_name, amount in donors_db.items():
        file_name = donor_name + ".txt"
        with open(file_name, 'w') as f:
            f.write(write_letter(donor_name, sum(amount)))
    print("\nA thank you letter to each donor is saved as a text file.")
    
if __name__ == "__main__":
    main()