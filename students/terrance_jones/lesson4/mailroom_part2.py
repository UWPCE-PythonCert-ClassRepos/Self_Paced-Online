
#VARIABLES
d1={'full_name':'Carlos Santos', 'donations': [25.00, 50.00, 100.00]}
d2={'full_name':'Esperanza Gomez', 'donations': [10.00, 20.00, 30.00]}
d3={'full_name':'Paul Jackson', 'donations': [5.00, 10.00, 15.00]}
d4={'full_name': 'Karl Black', 'donations': [100.00, 200.00, 300.00]}
d5={'full_name':'Charles Exx', 'donations': [15.00, 30.00, 45.00]}

donor_list = {'Carlos Santos':[25,50,100], 'Esperanza Gomez': [10,20,30], 'Paul Jackson':[5,10,15], 'Karl Black':[100,200,300], 'Charles Exx': [15,30,45]}


"""
FUNCTIONS NEEDED FOR SCRIPT TO RUN
"""
def get_name():
    """get donor name from user"""
    name = input("Enter the full name of the donor.")
    return name

def show_donor_list():
    """Create list of donor names only. Display list of all donors"""
    for key in donor_list.keys():
        print(key)
    

def find_donor(x):
    for key in donor_list.keys():
        if key == x:
            return True
        

def get_amount():
    """Gets donation amount from user"""
    amount = input("Enter the donation amount:")
    amount = float(amount)
    return amount

def add_to_existing_donor(d, a):
    """adds donation amount to donor in list. d is donor name. a is amount of donation"""
    donor_list[d].append(a)

def create_new_donor(d, a):
    donor_list[d] = [a]

def print_rows():
    for c in donor_list:
        name = c
        num_gifts = len(donor_list[c])
        total = sum(donor_list[c])
        average = total / num_gifts
        average = round(average,2)
        
        print("{:<25} ${:^20}  {:^15} ${:>20}".format(name,total,num_gifts,average))


def letter(donor):
    output = {'name': donor}
    all_donations = donor_list[donor]
    output = {'name': donor, 'total': sum(donor_list[donor])}
   
    output['last_donation']= all_donations[len(all_donations)-1]
    letter = '''Dear {name},\n
    \tThank you for your most recent donation of ${last_donation:,.2f}
    \tYour total support of {total:,.2f} has been used to assist many people.\n
    Thank you,\n
    -The Mailroom'''.format(**output)

    return(letter)



#thank you function gets a donors name and amount of donation. then prints out a thank you email
def thankyou():
    donor_name = get_name()
    if donor_name == "list":
        show_donor_list
        donor_name =get_name()

    if find_donor(donor_name) is True: 
        donation_amount = get_amount()
        add_to_existing_donor(donor_name, donation_amount)
        
        dic = {'name': donor_name , 'amount_donated': donation_amount}
        print("Dear {name}, \n Thank you for your {amount_donated:,.2f} donation. \nSincerely, Mailroom.".format(**dic))
        
    else:
        
        donation_amount = get_amount()
        create_new_donor(donor_name, donation_amount)
        dic = {'name': donor_name , 'amount_donated': donation_amount}
        print("Dear {name}, \n Thank you for your {amount_donated:,.2f} donation. \nSincerely, Mailroom.".format(**dic))
       
            


def create_report():
    
    heading = "{:<25s} | {:^20s} | {:^10s} | {:^20s} ".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(heading)
    print("-" * len(heading))
    print_rows()
   

def letters_everyone():
    for key in donor_list.keys():
        filename = "{}.txt".format(key)
        with open(filename, 'w') as f:
            donor_letter = letter(key)
            f.write(donor_letter)
    print("Letters have been created for each donor")
   

def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            return

  
def sub_menu():
    while True:
        menu_selection(sub_prompt, sub_dispatch)

def quit():
    print("Quitting this menu now")
    return "exit menu"

main_prompt = ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(3) Letters to all donors\n"
                "(q) Quit\n " 
                )
main_dispatch = {"1": thankyou,
                 "2": create_report,
                 "3": letters_everyone,
                 "q": quit,
                 }

sub_prompt =  ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(3) Letters to all donors\n"
                "(q) Quit\n " 
                )

sub_dispatch = {"1": thankyou,
                 "2": create_report,
                 "3": letters_everyone,
                 "q": quit,
                 }


if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)

  
                




        
