#Mailroom Part 1

import sys

donors_db = [["William Gates, III", 653772.32, 12.17],
            ["Mark Zuckerberg", 1663.23, 4300.87, 10432.0],
            ["Jeff Bezos", 877.33],
            ["Paul Allen", 663.23, 43.87, 1.32],
            ["Ramkumar Rajanbabu", 200.30, 50.10, 5.25]]

donors = [name[0] for name in donors_db] #List as donor names

prompt = "\n".join(("Menu: ",
                    "Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    ">>> "))
def main():
    """Display menu with options to user.
    
    Args:
        None
    Returns:
        None
    
    """
    
    while True:
        response = input(prompt)
        if response == "1": #Send a Thank You
            send_a_thank_you()
        elif response == "2": #Create a Report
            create_a_report()
        elif response == "3": #Quit
            exit_program()
        else:
            print("Please enter a valid option! (1-3)\n")

def send_a_thank_you():
    """Show a list of donors and add a new donor based on user response.
    
    Args:
        None
    Returns:
        None

    """

    response = str(input("Type in the full donor name (or 'list' to view a list of donor names): "))
    if response == "list":
        view_donor_list()
        send_a_thank_you() # Reprompt to main menu
    elif response in donors:
        donation_amount(response)
    else:
        donors.append(response)
        donors_db.append([response]) #response in list because it's a new donor entry
        donation_amount(response)

def create_a_report():
    """Create a report (table with values).
    
    Args:
        None
    Returns:
        None

    """
    title_string = "{:<25s} | {:s} | {:s} | {:s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    title_bar = len(title_string) * "-"    
    
    summary = []
    for donor in donors_db:
        donor_name = donor[0]
        donations = donor[1:]

        total_given = sum(donations)
        num_gifts = len(donations)
        avg_gift = total_given / num_gifts

        summary.append((donor_name, total_given, num_gifts, avg_gift))
    summary = sorted(summary, key=sort_key, reverse=True)
    
    print()
    print(title_string)
    print(title_bar)
    for donor_tuple in summary:
        f_string = "{:<25s}  ${:>11.2f}  {:>10d}  ${:>12.2f}".format(*donor_tuple)
        print(f_string)

def exit_program():
    """Exit program.
    
    Args:
        None
    Returns:
        None
        
    """
    
    print("\nYou chose to quit the program, good-bye!")
    sys.exit() #Exit script
             
def view_donor_list():
    """To view donor names in a vertical list.
    
    Args:
        None
    Returns:
        None

    """
    
    print("\nList of Donor Names:")
    for donor_name in donors_db:
        print(donor_name[0]) #zeroth index has donor names because of double list
    
def print_email(response, donors_amount):
    """Print an email letter based on donor name and donation amount.
    
    Args:
        response: donor name
        donors_amount (float): donation amount  
    Returns:
        None

    """
    
    email = """
    Dear {:s},
    
    Thank you for choosing to donate to this group. A special thank you for your generous donation of ${:0.2f}.
    
    Sincerely, 
    Donation Society""".format(response, donors_amount)
    print(email)
    
def donation_amount(response):
    """Add new donation amount to donor list based on user response.
    
    Args:
        response: donor name
    Returns:
        None

    """
    
    donors_amount = float(input("Type in the donation amount: $"))
    donors_index = (donors.index(response)) #Returns the index value of donor name
    donors_db[donors_index].append(donors_amount)
    print_email(response, donors_amount)

def sort_key(summary):
    """Creates sort key for sorted function.
    
    Args:
        summary: list with donor summary
    Returns:
        summary[1]: sorts by total_given values

    """
    return summary[1]    

if __name__ == "__main__":
    #Guard against running code automatically if this module is imported
    main()