#!/usr/bin/env python3

def donor_names():
    """Return a list of donor names."""
    names = list()
    for name in donor_db:
        names = names + [name[0]]
    return names


def send_thank_you():
    """Create thank you card formatting."""
    full_name = input("Enter the donor's full name > ")
    
    donors = donor_names()
    
    if full_name == 'list':
        #Print the donor names and restart the function
        for name in donors:
            print(name)
            
        send_thank_you()
    
    if full_name not in donors:
        donor_db.append([(full_name)])
    
    amount = float( input("Enter the donation amount > ") )
    
    for index, row in enumerate(donor_db):
        if row[0] == full_name:
            new_row = row + [amount]
            
            donor_db.pop(index)
            donor_db.append((new_row,))
            
            
    print("Thank you, {}! Your generous donation of ${:.2f} will go a long way to feed the needy.".format(full_name, amount))
    
    
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
donor_db = [('William Gates, III', 1000, 2000, 8000),
            ('Mark Zuckerberg', 666),
            ('Jeff Bezos', 9000, 1500),
            ('Paul Allen', 16000),
            ('Donald Trump', 2)]


if __name__ == '__main__':
    prompt = ''
    while(prompt != 'quit'):
        # Prompt the user to “Send a Thank You”, “Create a Report” or “quit”
        prompt = input("Enter: Send a Thank You, Create a Report or quit > ")
        
        if prompt == 'Send a Thank You':
            send_thank_you()
            
        if prompt == 'Create a Report':
            create_report()