#Mailroom Part 2

import sys

donors_db = {"William Gates, III": [653772.32, 12.17],
             "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
             "Jeff Bezos": [877.33],
             "Paul Allen": [663.23, 43.87, 1.32],
             "Ramkumar Rajanbabu": [200.30, 50.10, 5.25]}

def main():
    """Display menu with options to user.
    
    Args:
        None
    Returns:
        None

    """
    
    prompt = "\n".join(("Menu: ",
                    "Please choose from below options:",
                    "1 - Send a Thank You to a single donor",
                    "2 - Create a Report",
                    "3 - Send Letters to all donors",
                    "4 - Quit",
                    ">>> "))
    
    while True:
        user_response = input(prompt)
        if user_response == "1":
            send_thanks()
        elif user_response == "2":
            create_report()
        elif user_response == "3":
            send_letters_all()
        elif user_response == "4":
            exit_program()
        else:
            print("Please enter a valid option! (1-4)\n")

def send_thanks():
    """Show a list of donors and add a new donor based on user response.
    
    Args:
        None
    Returns:
        None

    """

    name = str(input("Type in the full donor name (or 'list' to view a list of donor names): "))
    if name == "list":
        view_list()
        send_thanks() #Reprompt to main menu
    else:
        add_donation(name)

def create_report():
    """Create a report (table with values).
    
    Args:
        None
    Returns:
        None
        
    """
    title_string = "{:<25s} | {:s} | {:s} | {:s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    title_bar = len(title_string) * "-"
    
    summary = [] #Summary list to create report
    for donor_name, amount in donors_db.items(): #for key and value in dictionary (items include key and value)
        total_given = sum(amount)
        num_gifts = len(amount)
        avg_gift = sum(amount) / len(amount)
        summary.append((donor_name, total_given, num_gifts, avg_gift))
    summary = sorted(summary, key=sort_key, reverse=True)
    
    print()
    print(title_string)
    print(title_bar)
    for donor_tuple in summary:
        print("{:<25s}  ${:>11.2f}  {:>10d}  ${:>12.2f}".format(*donor_tuple)) #f_string

def send_letters_all():
    """Generates a thank you letter for each donor and writes each letter as a text file.
    
    Args:
        None
    Returns:
        None

    """
    
    for donor_name, amount in donors_db.items():
        file_name = donor_name + ".txt"
        with open(file_name, 'w') as f:
            f.write(write_letter(donor_name, sum(amount)))
    print("A thank you letter to each donor is saved as a text file.")
    
def exit_program():
    """Exit program.
    
    Args:
        None
    Returns:
        None
        
    """
    
    print("\nYou chose to quit the program, good-bye!")
    sys.exit() #Exit script
             
def view_list():
    """To view donor names in a vertical list.
    
    Args:
        None
    Returns:
        None

    """
    
    print("\nList of Donor Names:")
    for donor_name in donors_db.keys():
        print(donor_name) #Prints each name (key)
    
def write_letter(name, donation_amount):
    """Generates letter based on donor name and donation amount.
    
    Args:
        name: donor name
        donation_amount (float): donation amount  
    Returns:
        letter (string): a letter in string format

    """
    
    letter = """
    Dear {:s},
    
    Thank you for choosing to donate to this group. A special thank you for your generous donation of ${:0.2f}.
    
    Sincerely, 
    Donation Society""".format(name, donation_amount)
    return letter
    
def add_donation(name):
    """Add new donation amount to donor list based on user response.
    
    Args:
        name: donor name
    Returns:
        None

    """
    
    #Exception handling
    try:
        if name not in donors_db:
            donors_db[name] = [] #donors_db[key] = [value]
            
        donation_amount = float(input("Type in the donation amount: $"))
        donors_db[name].append(donation_amount) #donor_db[key].append()
        print(write_letter(name, donation_amount))
    except ValueError: #ValueError because user enters anything other than integer/float
        print("Please enter an integer.")

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