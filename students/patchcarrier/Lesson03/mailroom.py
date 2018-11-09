donors = [["Conrad Anker", 550, 1200, 0.02], 
          ["Tommy Caldwell", 600.50, 80], 
          ["Margo Hayes", 200, 550.50], 
          ["Alex Honnold", 0.01],
          ["Paige Claassen", 750, 800, 150.25]]

def thankyou_menu():
    """Prompt the user to enter information about a donation and record the 
    user input in the global data structure.
    
    Returns: 
    -a tuple of the form (donor_name, donation_amount) if a donor
    is specified. 
    -None otherwise
    """
    
    user_input = thankyou_prompt()
    
    # If the user inputs 'l', list all of the previous donors and continue 
    # re-prompting
    while user_input == 'l':
        
        for donor_record in donors[:]:
            print(donor_record[0])
        user_input = thankyou_prompt()
    
    # The user wants to input a donor
    if user_input == 'e':
        
        name_in = input("Enter the full name of the donor (or 'q' to return to the main menu)"
                        "\n>>> ")
        if name_in == 'q': return None
       
        amount_in = input("Enter the donation amount (or 'q' to return to the main menu)"
                          "\nEnter numbers only, do not enter special characters"
                          "\n>>> ")
        if amount_in == 'q': return None
        amount_in = float(amount_in)
        
        # check if the donor already exists, if they do, add this donation to
        # their history, otherwise, create a new donor entry in the data structure
        for ind, donor_record in enumerate(donors[:]):
            
            if name_in == donor_record[0]:
                donors[ind].append(amount_in)
                break
        
        else:
            donors.append([name_in, amount_in])
            
        return (name_in, amount_in)
    
    # if 'else' block is executed, user input must be 'q', return to the main menu
    else:
        return None


def thankyou_prompt():
    """Display the prompt and return user input for the thank you menu function.
    
    Returns:
    One of the characters 'l', 'e', or 'q'
    """
    
    prompt = """Enter:
(l) to list the names of previous donors
(e) to create a new donation entry and send a thank you email
(q) to quit and return to the main menu
>>> """   

    user_input = input(prompt)
    while user_input not in ['l','e','q']:
        print("Input character '{}' not recognized".format(user_input))
        user_input = input(prompt)
        
    return user_input       
    
    
def send_email(name, amount):
    "Send a thank you email to donor for the specified amount."
    
    body = ("\nThank you {} for your generous donation of ${:.2f} to Vertical "
          "Generation.\n\nWe greatly apprecciate your support for our cause."
          "\n\n-patchcarrier")
    print(body.format(name, amount))


def write_report():
    "Print a tabulated summary of all donors and donations to the screen."
    
    # Header
    print("{:<25s}|{:^13s}|{:^11s}|{:^14s}".format("Donor Name", 
          "Total Given","Num Gifts","Average Gift"))
    print("-" * (25 + 13 + 11 + 14 + 3))
    fstring = "{:<25s} ${:>12.2f} {:>11d} ${:>13.2f}"
    
    # Sort the global data structure by donation amount
    donors.sort(reverse=True, key=lambda list_i: sum(list_i[1:]))
    
    # Print the summar of donation data
    for record in donors:
        
        name = record[0]
        total_given = sum(record[1:])
        n_gifts = len(record) - 1
        print(fstring.format(name, total_given, n_gifts, total_given/n_gifts))



def main_prompt():
    """Display the main prompt until the user inputs one of the menu options,
    and return the user input.
    
    Returns:
    One of the characters 't', 'c', or 'q'
    """
    
    prompt = """Enter:
(t) to send a thank you letter
(c) to create a report
(q) to quit
>>> """
    user_input = input(prompt)
    while user_input not in ['t','c','q']:    
        print("Input character '{}' not recognized".format(user_input))
        user_input = input(prompt)
        
    return user_input


######  Program Block ######

if __name__ == "__main__":
    
    # Display the initial main menu prompt and get the user input
    user_input = main_prompt()
    
    # Keep re-prompting the user for action unless they specify to quit
    while user_input != 'q':
        
        if user_input == 't':
            
            t_output = thankyou_menu()
            
            if t_output is not None:
                send_email(*t_output)
            
        elif user_input == 'c':
            write_report()
        
        # Display the main menu and re-prompt the user
        user_input = main_prompt()