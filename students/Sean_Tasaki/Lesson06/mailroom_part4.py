"""
Sean Tasaki
5/21/2018
Lesson06.mailroom_part_4
"""
from collections import defaultdict

donor_dict = defaultdict(lambda : [0, 0, 0], {'Bob Dylan': [20000.00, 3, 40000.00], 'Leonard Cohen' : [600.00, 2, 300.00], 'Soren Kierkegaard' : [1000.00, 2, 500.00], 'Italo Calvino' : [20000.00, 4, 5000.00], 'Florence Feist' : [300.00, 3, 100.00]})


def main_menu():
    main_menu_dict = {'1': thank_you, '2': create_report, '3': create_thank_you_letters, '4': quit}
    main_prompt = "Enter 1-4 from the following options: (1) Send a Thank You to a Donor, (2) Create a Report, (3) Write a Thank You Letter to All Donors (4) Quit\n >> "  
    main_menu_response(main_prompt, main_menu_dict)

def main_menu_response(prompt, main_menu_dict):
    try:
        while True:
            response = input(prompt)
            main_menu_dict.get(response)()
            if main_menu_dict[response]() == "exit menu":
                exit()
    except TypeError:
        print("Enter a number between 1-4.")    
        return main_menu()

def thank_you():
    name = input("Enter the first and last name of the donor or enter 'list' to see a list of previous donor names or enter Q to exit to main menu\n> ")
    if name.lower() == 'list':
        for donor in donor_dict:
            print(donor)
        thank_you()
    elif name.upper() == 'Q':
        main_menu()
    else:
        add_donor_to_dict(name.title())
    try:
        if donor_dict[name.title()][1] == 0:
            amount = input(f"{name.title()} is a new donor. Enter the donation amount.\n>> ")
            add_donor_amount(name.title(), amount)
            print(f"Thank you {name.title()} for becoming a new donor to our charity! Your genereous donation of ${float(amount):.2f} is much appreciated.")
        else:
            amount = input(f"{name.title()} is a previous donor. Enter the donation amount.\n>> ")
            add_donor_amount(name.title(), amount)
            print(f"Thank you {name.title()} for your loyal support to our charity! Your genereous donation of ${float(amount):.2f} is much appreciated.")


    except ValueError:
        print("Invalid input. Please enter a numerical donation amount.")
        
        thank_you()
    

def add_donor_to_dict(name):
    if isinstance(name, str) is False:
        print('Please enter a valid name')
        add_donor_to_dict()
    else:
        donor_dict[name]

def add_donor_amount(name, amount):
        donor_dict[name][0] += float(amount)
        donor_dict[name][1] += 1
        donor_dict[name][2] = float(donor_dict[name][0]/donor_dict[name][1])     
        
            
    

def quit():
    return "exit menu"

def create_report():
    lis = []
    lis = [[donor, values] for donor, values in donor_dict.items()]
    # Sort lis by total given
    lis.sort(key = lambda x: x[1][0], reverse = True) 
    print("Donor Name           |   Total Given   |   Num Gifts  |    Average Gift")
    print("-----------------------------------------------------------------------")
    for donor in lis:
        print(f"{donor[0]:20} ${donor[1][0]:>17.2f}    {donor[1][1]:>6}     ${donor[1][2]:>16.2f}")  
    main_menu()

def create_thank_you_letters():
    # Creates a letter for each donor that gets a file in the working dir based on donor's name.
    try:
        # Separate donors based on whether they gave multiple donations or a single donation
        file_donor_names=  [(donor + '.txt') for donor in donor_dict]
        file_object_for_donations = [open(file, 'w') for file in file_donor_names]
        for count, donor in enumerate(donor_dict):
            file_object_for_donations[count].write(thank_you_letter_template(donor)) 
    except IOError:
        print("There was an error with creating the letter files")
    else:
        print("Thank you letters created. Look in the directory for the new files.")
        main_menu()
    finally: 
        for file in file_object_for_donations:
            file.close()
def thank_you_letter_template(dk):
    if donor_dict[dk][1] > 1:
        return "Dear {},\nThank you for your {} generous donations of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format(dk, donor_dict[dk][1], donor_dict[dk][0])
    else:
        return "Dear {},\nThank you for your generous donation of ${:.2f}. Your support helps our charity stay in business.\n\nSincerely,\n-The Team".format(dk, donor_dict[dk][1], donor_dict[dk][0])

if __name__ == '__main__':
    main_menu()