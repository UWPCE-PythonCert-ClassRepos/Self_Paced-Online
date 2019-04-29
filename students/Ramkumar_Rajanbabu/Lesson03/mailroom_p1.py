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
    """Purpose.
    
    Args:
        None
    Returns:
        None
    
    """
    
    while True:
        response = input(prompt)  #continuously collect user selection
        if response == "1": #Send a Thank You
            send_a_thank_you()
        elif response == "2": #Create a Report
            create_report()
        elif response == "3": #Quit
            exit_program()
        else:
            print("Please enter a valid option! (1-3)\n")

def send_a_thank_you():
    """Purpose.
    
    Args:
        None
    Returns:
        None

    """

    response = str(input("Type in the full donor name (or 'list' to view a list of donor names): "))
    if response == "list": #Maybe #response.lower()
        view_donor_list()
        send_a_thank_you() # Reprompt to main menu
    elif response in donors:
        donation_amount(response)
    else:
        donors.append(response)
        donors_db.append([response]) #response in list because it's a new donor entry
        donation_amount(response)

def create_report():
    """Create a report (table with values).
    
    Args:
        donor_name:
        total_given:
        num_gifts:
        average_gift:
    Returns:
        None

    """
    title_string = "{:<25s} | {:s} | {:s} | {:s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    title_bar = len(title_string) * "-"    
    
    donor_name = []
    total_given = []
    num_gifts = []
    avg_gift = []

    for donor in donors_db:
        name = donor[0]
        donor_name.append(name)

        amount = donor[1:]
        total = sum(amount)
        total_given.append(total)

        gifts = len(amount)
        num_gifts.append(gifts)

        avg = total / gifts
        avg_gift.append(avg)
    
    print()
    print(title_string)
    print(title_bar)
    for index in range(len(donor_name)):
        f_string = "{:<25s}  ${:>11.2f}  {:>10d}  ${:>12.2f}".format(donor_name[index], total_given[index], num_gifts[index], avg_gift[index])
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
    """Purpose.
    
    Args:
        None
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
    """Purpose.
    
    Args:
        None
    Returns:
        None

    """
    
    donors_amount = float(input("Type in the donation amount: $"))
    donors_index = (donors.index(response)) #Returns the index value of donor name
    donors_db[donors_index].append(donors_amount)
    print_email(response, donors_amount)
    
if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()