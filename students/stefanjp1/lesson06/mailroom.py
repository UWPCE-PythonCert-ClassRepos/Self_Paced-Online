#!/usr/bin/env python3
import sys
import collections

def donor_names():
    """Return a list of donor names."""
    return list(donor_db.keys())


def send_thank_you():
    """Create thank you card formatting."""
    full_name = input("Enter the donor's full name > ")
    
    donors = donor_names()
    
    if full_name == 'list':
        #Print the donor names and restart the function
        for name in donors:
            print(name)
            
        send_thank_you()
    
    try:
        amount = float( input("Enter the donation amount > ") )
    except ValueError:
        print('Donation must be a valid dollar amount, without a "$"\nRetry Send a Thank You.')
        return
    
    for k, v in donor_db.items():
         if k == full_name:
             donor_db[full_name] = v.append(amount)
             break
    else:
         donor_db[full_name] = amount  

    print( thank_you_letter(thanks_dict = {full_name: amount})[full_name] )
    

def thank_you_letter(thanks_dict):
    thanks = {}
    for k, v in thanks_dict.items():
        if type(v) == list:
            v = float(v[-1])
        
        thanks[k] = "Dear {},\n\n\tThank you for your kind donation of ${:.2f}.\n\n\tIt will go a long way to feed the needy. \n\n\t\tSincerely, \n\n\t\t  -The Team".format(k, v) 
    
    return thanks


def send_letters():
    letters = thank_you_letter(thanks_dict = donor_db)
    print(letters)
    for name, letter in letters.items():
        file_path = name + '.txt'
        with open(file_path, 'w') as outfile:
            outfile.write(letter)
            
    print('Letters saved to disk.')



def create_report():
    """Return a report with metadata about the donors"""
    report = list()
    for name, donations in donor_db.items():
        report.append([name, sum(donations), len(donations), sum(donations) / len(donations)])
    
    sorted_report = sorted(report, key=lambda x: -x[1])
    
    print("Donor Name                | Total Given | Num Gifts | Average Gift\n")
    print('------------------------------------------------------------------')
    for row in sorted_report:
        print("{:25} ${:13.2f}{:11d} ${:13.2f}".format(row[0], row[1], 
                                            row[2], row[3]))
    return "report printed successfully"
    


# Database set up
donor_db = {'William Gates, III': [1000, 2000, 8000],
            'Mark Zuckerberg': [666],
            'Jeff Bezos': [9000, 1500],
            'Paul Allen': [16000],
            'Donald Trump': [2]}


if __name__ == '__main__':
    
    while True:
        prompt = input("Enter:\n Send a Thank You (1)\n Create a Report (2)\n Send Letter to Everyone (3)\n or quit (4) > ")
        
        try:
            prompt = int(prompt)
        except ValueError:
            print("Input must be an integer, try again.")
            continue
        
        prompt_dict = {1: send_thank_you,
                       2: create_report,
                       3: send_letters,
                       4:'quitting program'}
        
        try:
            user_choice = prompt_dict[prompt]
        except KeyError:
            print("Input integer was outside range of choices, try again.")
            continue
        
        if prompt != 4:
            user_choice()
        else:
            print(user_choice)
            sys.exit()