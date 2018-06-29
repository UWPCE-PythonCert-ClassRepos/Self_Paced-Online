#!/usr/bin/env python3

def donor_names():
    """Return a list of donor names."""
    return donor_db.keys()


def send_thank_you():
    """Create thank you card formatting."""
    full_name = input("Enter the donor's full name > ")
    
    donors = donor_names()
    
    if full_name == 'list':
        #Print the donor names and restart the function
        for name in donors:
            print(name)
            
        send_thank_you()
    
    amount = float( input("Enter the donation amount > ") )
    
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
    donors = donor_names()
    
    total_given = list()
    num_gifts = list()
    average_gift = list()
    for row in donor_db:
        total_given.append(sum(row[1:]))
        num_gifts.append(len(row[1:]))
        average_gift.append(sum(row[1:]) / len(row[1:]))
    
    print("Donor Name                | Total Given | Num Gifts | Average Gift\n")
    print('------------------------------------------------------------------')
    for row in range(len(donors)):
        print("{:25} ${:13.2f}{:11d} ${:13.2f}".format(donors[row], total_given[row], 
                                            num_gifts[row], average_gift[row]))
    


# Database set up
donor_db = {'William Gates, III': [1000, 2000, 8000],
            'Mark Zuckerberg': [666],
            'Jeff Bezos': [9000, 1500],
            'Paul Allen': [16000],
            'Donald Trump': [2]}


if __name__ == '__main__':
    prompt = ''
    while prompt != 'q':
        # Prompt the user to “Send a Thank You”, “Create a Report” or “quit”
        prompt = input("Enter:\n Send a Thank You ('ty')\n Create a Report ('cr')\n Send Letter to Everyone ('l')\n or quit ('q') > ")
        
        prompt_dict = {'ty': send_thank_you,
                       'cr': create_report,
                       'l': send_letters,
                       'q':'quitting program'}
        
        user_choice = prompt_dict.get(prompt, 'Invalid Input')
        
        if user_choice not in ['Invalid Input', 'quitting program']:
            user_choice()
        else:
            print(user_choice)