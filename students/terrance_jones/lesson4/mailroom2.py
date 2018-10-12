
#VARIABLES
d1={'first_name': 'Carlos', 'last_name':'Santos', 'full_name':'Carlos Santos', 'donation_1': 25.00, 'donation_2':50.00, 'donation_3':100.00}
d2={'first_name': 'Esperanza', 'last_name':'Gomez', 'full_name':'Esperanza Gomez', 'donation_1': 10.00, 'donation_2':20.00, 'donation_3':30.00}
d3={'first_name': 'Paul', 'last_name':'Jackson', 'full_name':'Paul Jackson', 'donation_1': 5.00, 'donation_2':10.00, 'donation_3':15.00}
d4={'first_name': 'Karl', 'last_name':'Black', 'full_name': 'Karl Black', 'donation_1': 100.00, 'donation_2':200.00, 'donation_3':300.00}
d5={'first_name': 'Charles', 'last_name':'Exx', 'full_name':'Charles Exx', 'donation_1': 15.00, 'donation_2':30.00, 'donation_3':45.00}

donor_list = [d1,d2,d3,d4,d5]





"""
FUNCTIONS NEEDED FOR SCRIPT TO RUN
"""
def get_name():
    """get donor name from user"""
    name = input("Enter the full name of the donor.")
    return name

def show_donor_list():
    """Create list of donor names only. Display list of all donors"""
    donor_names = []
    for item in donor_list:
        print(item['full_name'] )
        


def find_donor(x):
    for i in donor_list:
       if i['full_name'] == x:
        print(i['full_name'])

 
def get_amount():
    """Gets donation amount from user"""
    amount = input("Enter the donation amount:")
    amount = float(amount)
    return amount

def add_to_existing_donor(i, a):
    """adds donation amount to donor in list. d is donor name. a is amount of donation"""
    
    i.append(a)
    

def create_new_donor(d, a):
    """Creates a new donor list. adds new list to current donor list"""
    new_donor_list=[]
    new_donor_list.append(d)
    new_donor_list.append(a)
    donor_list.append(new_donor_list)


def print_row():
    
        

        

#thank you function gets a donors name and amount of donation. then prints out a thank you email
def thankyou():
    donor_name = get_name()
    while donor_name == "list":
        show_donor_list()
        donor_name =get_name()

    if find_donor(donor_name)== donor_name: 
        donation_amount = get_amount()
        add_to_existing_donor(i, donation_amount)
        dic = {'name': donor_name , 'amount_donated': donation_amount}
        print("Dear {name}, \n Thank you for your {amount_donated} donation. \nSincerely, Mailroom.".format(**dic))
        
    else:
        
        donation_amount = get_amount()
        create_new_donor(donor_name, donation_amount)
        dic = {'name': donor_name , 'amount_donated': donation_amount}
        print("Dear {name}, \n Thank you for your {amount_donated} donation. \nSincerely, Mailroom.".format(**dic))
        
            


def create_report():
    
    heading = "{:<25s} | {:^20s} | {:^10s} | {:^20s} ".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(heading)
    print("-" * len(heading))
    print_row()
    menu()
 

def menu_selection(prompt, dispatch_dict):
    response = input(prompt)
    if dispatch_dict[response]() == "exit menu":
        return

  
def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)

def quit():
    print("Quitting this menu now")
    return "exit menu"

main_prompt = ("\nYou are in the main menu now!\n"
                "What do you want to do?\n"
                "Type 1,2,3 or 4 to get a submenu.\n"
                "or q to exit>>"
                )
main_dispatch = {"1": thankyou,
                 "2": create_report,
                 "3": sub_menu,
                 "q": quit,
                 }

sub_prompt =  ("\nYou are in the sub menu now!\n"
                "What do you want to do?\n"
                "Type 1,2,3 or 4 to get a submenu.\n"
                "or q to exit>>"
                )

sub_dispatch = {"1": thankyou,
                 "2": create_report,
                 "3": sub_menu,
                 "q": quit,
                 }


if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)

  
                




        
