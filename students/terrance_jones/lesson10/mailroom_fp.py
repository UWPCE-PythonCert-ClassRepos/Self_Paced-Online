"""Mailroom functional programing written by Terrance Jone"""


#list of donors
donor_list = {'Carlos Santos':[25,50,100], 'Esperanza Gomez': [10,20,30], 'Paul Jackson':[5,10,15], 'Karl Black':[100,200,300], 'Charles Exx': [15,30,45]}


def challenge(factor):
    """mulitply all donations by factor"""
    newdic = donor_list.copy()
    for d,v in newdic.items():
        value= list(filter(lambda x: not x<5 and not x>5000, v))
        value = list(map(lambda x: x * factor,value))
        newdic[d] = value
    print ('new donations list created')
    return newdic

def predict(donor):
    """predict donations """
    contributions = donor_list[donor]
    a = list(filter(lambda x: not x<100, contributions))
    a = list(map(lambda x: x * 2, a))
    a = reduce(lambda x,y: x+y, a)
    b = list(filter(lambda x: not x<50, contributions))
    b = list(map(lambda x: x * 3, b))
    b = reduce(lambda x,y: x+y, b)
    prediction = (donor + "-Total if double contributions under $100: {}. Total if triple contributions over $50: {}").format(a,b)
    return prediction

def get_name():
    """get donor name from user"""
    name = input("Enter the full name of the donor.")
    return name

def show_donor_list():
    """Create list of donor names only. Display list of all donors"""
    for key in donor_list.keys():
        print(key)
    

def donor_exists(donor):
   return donor in donor_list


def get_amount():
    """Gets donation amount from user."""
    while True:
        try:
            amount = input("Enter the donation amount:")
            amount = float(amount)
        except ValueError:
            print("Donation amount must be a numeric value")
        
        else:
            return amount

def get_report(donor_list):
    """Returns donation report"""
    report = []

    for c in donor_list:
        name = c
        num_gifts = len(donor_list[c])
        total = sum(donor_list[c])
        average = float(round(total / num_gifts, 2))
        dic = {'name':name, 'total':total, 'num_gifts':num_gifts, 'average':average }
        new_row = "{name:<25} ${total:^10} {num_gifts:^10} ${average:^10}".format(**dic)
        report.append(new_row)

    return (report)


def add_or_update_donor(donor_name, donation_amount):
    """add donor to donor list or update donor list"""
    if donor_exists(donor_name) is True:
        donor_list[donor_name].append(donation_amount)
    else:
         donor_list[donor_name] = [donation_amount]

def thank_you_letter(donor_name, donation_amount):
    """creates donor thank you letter"""
    dic = {'name': donor_name , 'amount_donated': donation_amount}
    return("Dear {name}, \n Thank you for your ${amount_donated:,.2f} donation. \nSincerely, Mailroom.".format(**dic))
        


def letter(donor):
    """Creates donor letter"""
    output = {'name': donor}
    all_donations = donor_list[donor]
    output = {'name': donor, 'total': sum(donor_list[donor])}
   
    output['last_donation']= all_donations[len(all_donations)-1]
    letter = '''Dear {name},\n
    \tThank you for your most recent donation of ${last_donation:,.2f}.
    \tYour total support of ${total:,.2f} has been used to assist many people.\n
    Thank you,\n
    -The Mailroom'''.format(**output)

    return(letter)



def thankyou():
    """generate thank you letter"""
    donor_name = get_name()

    if donor_name == "list":
        show_donor_list()
        donor_name =get_name()

    donation_amount = get_amount()

    add_or_update_donor(donor_name, donation_amount)

    print(thank_you_letter(donor_name, donation_amount))
            


def display_report():
    """displays report of donors and donations"""
    heading = "{:<20s} | {:^10s} | {:^10s} | {:^10s} ".format("Donor Name", "Total Given", "Num Gifts", "Average")
    heading_underline = "-"
    print(heading)
    print(heading_underline * len(heading))
    
    for row in get_report(donor_list):
        print(row)
   

def letters_everyone():
    """prints letters to all donors"""
    for key in donor_list.keys():
        filename = "{}.txt".format(key)
        with open(filename, 'w') as f:
            donor_letter = letter(key)
            f.write(donor_letter)
    print("Letters have been created for each donor")


def get_prediction():
    """get predictions for donations"""
    donor = get_name()
    print(predict(donor))

   

def menu_selection(prompt, dispatch_dict):
    """displays the menu. asks for user to select option. if option is not available will throw KeyError and ask the user for new input"""
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                return
        except KeyError:
            print("Please select an option from the menu")

  
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
                "(4) Multiply Donations\n"
                "(5) Donation Predictions\n"
                "(q) Quit\n " 
                )
main_dispatch = {"1": thankyou,
                 "2": display_report,
                 "3": letters_everyone,
                 "4": challenge,
                 "5": get_prediction,
                 "q": quit,
                  }

sub_prompt =  ("What do you want to do?\n"
                "(1) Thank you letter\n"
                "(2) Create Report\n"
                "(3) Letters to all donors\n"
                "(4) Multiply Donations\n"
                "(5) Donation Predictions\n"
                "(q) Quit\n " 
                )

sub_dispatch = {"1": thankyou,
                 "2": display_report,
                 "3": letters_everyone,
                 "4": challenge,
                 "5": get_prediction,
                 "q": quit,
                 }


if __name__ == '__main__':
 
        menu_selection(main_prompt, main_dispatch)


