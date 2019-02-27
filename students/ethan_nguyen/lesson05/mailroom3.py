
import sys, os

#create a donor_db as a dict
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Donald Trump": [50000.24, 1002]
}

prompt = "\n".join(("Welcome to the mail room",
          "Please choose from below options:",
          "S - Send a Thank You",
          "C - Create a Report",
          "L - Send letters to all donors"
          "Q - Exit"
          ">>> "))


def view_donors():
    print("\n".join(donor_db))

def quit_program():
    print ("Thank you. Bye!")
    sys.exit(0)  # exit the interactive script

#function to make sure input name is letters only and longer than 2 characters
def validate_name():
    while (True):
        try:
            input_Name = str(input("Please enter a name > "))
            if (len(input_Name) > 2 and input_Name.isalpha()):
                break
            else:
                raise TypeError
        except TypeError:
            print("Letters only or longer name, please.")
    
    return input_Name

#function to make sure input amount is numeric
def validate_amount(input_Name):
    while (True):
        try:
            input_Amount = input(f"{input_Name} please input amount > ")
            value = float(input_Amount)
            break
        except ValueError:
            print('Valid amount, please')
    return value

def send_thank_you():

    input_Name = validate_name()
    while("list" in input_Name):
        for d in sorted(donor_db.keys()):
            print(d)

        input_Name = validate_name()

    is_NewDonor = False

    if input_Name in donor_db:
        select_Donor = donor_db[input_Name]
    else: 
        #select_Donor = {input_Name: []}
        is_NewDonor = True

    value = validate_amount(input_Name)

    print(f'Dear {input_Name}, \n Thank you for your very kind donation of ${value:,.2f} \n \
        It will be put to very good use. \n Sincerely, \n -UW')

    #add Donor if he/she is not in donor_db
    if is_NewDonor:
        donor_db[input_Name] =[float(value)]
    else:
        select_Donor.append(float(value))
        donor_db[input_Name] = select_Donor

def sort_key(donor):
    return sum(donor[1])

def create_report():

    space=''
    print(f'Donor Name {space:<15}| Total Given {space:<10}| Num Gifts {space:<9}| Average Gift {space:<19}')
    print("-"*85)

    sort_Donor = sorted(donor_db.items(), key=sort_key, reverse = True)
    #sort_Donor = sorted(donor_db.items(), key=lambda x: x[1], reverse = True)

    for d in sort_Donor:
        print("{:<25} ${:>12,.2f}{:>22}{:<10}${:>12,.2f}".format(d[0], sum(d[1]), len(d[1]), space,sum(d[1])/len(d[1])))

def send_letters():

    path = os.getcwd()
    for k,v in donor_db.items():
        with open(f'{path}/{k}.txt', 'w') as f:
            f.write(f'Dear {k}, \n Thank you for your very kind donation of ${float(sum(v)):,.2f} \n \
        It will be put to very good use. \n Sincerely, \n -UW')
    
    print("Done!")

if __name__ == "__main__":
    
    arg_dict = {'S':send_thank_you, 'C':create_report, 'L':send_letters}

    while True:
        response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" L for \"Send Letters\" or Q to quit >").upper()
        arg_dict.get(response, quit_program)()
