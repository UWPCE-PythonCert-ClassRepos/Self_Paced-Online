#!/usr/bin/env python3

donors = {"Conrad Anker":[550, 1200, 0.02], 
          "Tommy Caldwell":[600.50, 80], 
          "Margo Hayes":[200, 550.50], 
          "Alex Honnold":[0.01],
          "Paige Claassen":[750, 800, 150.25]}


def menu(prompt, disp_dict):
    """Execute the commands specified by the user until they specify to quit.
    
    :param prompt:    Prompt to display to the user with acceptable commands
    :param disp_dict: A dictionary with string keys corresponding to the acceptable
                      commands and function object values.
    """
    
    # Get initial user input (only accept user inputs that are in the dispatch
    # dictionary keys)
    user_input = input(prompt)
    
    # Continue asking for user input until they specify to quit
    while user_input != 'q':
        try:
            disp_dict[user_input]()
        except KeyError:
            print("\nInput character '{}' not recognized".format(user_input))
        user_input = input(prompt) 
        

def thankyou_menu():
    """Prompt the user to enter information about a donation and record the 
    user input in the global data structure.
    """
    
    thanks_prompt = """\nSpecify Donation Menu
Enter:
(l) to list the names of previous donors
(e) to create a new donation entry and send a thank you email
(q) to quit and return to the main menu
>>> """     

    thanks_disp_dict = {'l':list_donors, 'e':enter_donor, 'q': lambda : None}
    menu(thanks_prompt, thanks_disp_dict)
    

def list_donors():
    "List all of the donors in the global data structure."
    
    print()
    for donor_i in donors:
        print(donor_i)
        
        
def enter_donor():
    """Enter the donor name and donation amount into the global data structure
    and send a thank you email.
    """
    
    name_in = input("\nEnter the full name of the donor (or 'q' to quit)"
                    "\n>>> ")
    if name_in == 'q': return
   
    amount_in = input("\nEnter the donation amount (or 'q' to quit)"
                      "\nEnter numbers only, do not enter special characters"
                      "\n>>> ")
    if amount_in == 'q': return
    
    while True:
        try:
            amount_in = float(amount_in)
            break
        except ValueError:
            print('Error: Input must be numeric')
            amount_in = input("\nEnter the donation amount (or 'q' to quit)"
                      "\nEnter numbers only, do not enter special characters"
                      "\n>>> ")
            if amount_in == 'q': return
    
    # check if the donor already exists, if they do, add this donation to
    # their history, otherwise, create a new donor entry in the data structure
    if name_in in donors:
        donors[name_in].append(amount_in)
    else:
        donors[name_in] = [amount_in]
        
    send_email(dict(name=name_in, amount=amount_in))
    
    
def send_email(donation_dict):
    "Send a thank you email to donor for the specified amount."
    
    body = ("\n\nThank you {name} for your generous donation of ${amount:.2f} to "
          "Vertical Generation.\n\nWe greatly appreciate your support for our cause."
          "\n\n-patchcarrier")
    print(body.format(**donation_dict))
     
    
def write_report():
    "Print a tabulated summary of all donors and donations to the screen."
    
    # Header
    print("\n{:<25s}|{:^13s}|{:^11s}|{:^14s}".format("Donor Name", 
          "Total Given","Num Gifts","Average Gift"))
    print("-" * (25 + 13 + 11 + 14 + 3))
    fstring = "{:<25s} ${:>12.2f} {:>11d} ${:>13.2f}"
    
    # Sort the global data structure by donation amount
    donor_names = list(donors.keys())
    donor_names.sort(reverse=True, key=lambda donor_i: sum(donors[donor_i]))
    
    # Print the summary of donation data
    for name_i in donor_names:
        
        total_given = sum(donors[name_i])
        n_gifts = len(donors[name_i])
        print(fstring.format(name_i, total_given, n_gifts, total_given/n_gifts))
       
        
def send_letters():
    
    email_text = """Dear {name},
    
Thank you for your continued support of Vertical Generation. 

Your {num_donations:d} donation{s_string1} totaling ${donation_sum:.2f} help{s_string2} us continue to share rock climbing
with the underserved youth in Seattle.

Sincerely,
-patchcarrier
""" 
    
    for donor_i in donors:
        
        filename_i = donor_i + '.txt'
        filename_i = filename_i.replace(' ','_')
        
        with open(filename_i,'w') as outfile:
            
            #check the number of donations for the current donor, if it's only
            #one, donations should not be plural
            num_donations = len(donors.get(donor_i))
            
            if num_donations > 1:
                s_string1 = 's'
                s_string2 = ''
            else:
                s_string1 = ''
                s_string2 = 's'               
                
            donation_sum = sum(donors[donor_i])
            
            outfile.write(email_text.format(name=donor_i,
                                            num_donations=num_donations,
                                            s_string1=s_string1,
                                            s_string2=s_string2,
                                            donation_sum=donation_sum))
        
        
###############  Program Block ###############
main_prompt = """\nMain Menu
Enter:
(t) to send a thank you letter
(c) to create a report
(s) to send letters to everyone
(q) to quit
>>> """

main_disp_dict = {'t':thankyou_menu, 'c':write_report,
                      's':send_letters, 'q': lambda : None}

if __name__ == "__main__":
    menu(main_prompt, main_disp_dict)
    