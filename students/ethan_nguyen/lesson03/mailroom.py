
import sys

#create a donor_db as a list
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Donald Trump", [50000.24, 1002])
            ]

prompt = "\n".join(("Welcome to the mail room",
          "Please choose from below options:",
          "S - Send a Thank You",
          "C - Create a Report",
          "Q - Exit",
          ">>> "))


def view_donors():
    print("\n".join(donor_db))

def quit_program():
    print ("Thank you. Bye!")
    sys.exit(0)  # exit the interactive script

def send_thank_you():
    
    input_Name = input("Please enter a name > ")
    while("list" in input_Name):
        for d in donor_db:
            print(d[0])
        input_Name = input("Please enter a name > ")
    
    is_NewDonor = False

    for d in donor_db:
        if input_Name in d[0]:
            select_Donor = d
            break
    else: 
        select_Donor = (input_Name, [])
        is_NewDonor = True

    input_Amount = input(f"{input_Name} please input amount > ")
    select_Donor[1].append((float(input_Amount)))

    print(f'Thank you {select_Donor[0]} for your generous donation of ${float(input_Amount):,.2f}')

    #add Donor if he/she is not in donor_db
    if is_NewDonor:
        donor_db.append(select_Donor)

def sort_key(donor):
    return sum(donor[1])

def create_report():

    space=''
    print(f'Donor Name {space:<15}| Total Given {space:<10}| Num Gifts {space:<9}| Average Gift {space:<19}')
    print("-"*85)

    sort_Donor = sorted(donor_db, key=sort_key, reverse = True)
    for d in sort_Donor:
        print("{:<25} ${:>12,.2f}{:>22}{:<10}${:>12,.2f}".format(d[0], sum(d[1]), len(d[1]), space,sum(d[1])/len(d[1])))

if __name__ == "__main__":
    
    while True:
        response = input("Please select S for \"Send a Thank You\" C for \"Create a Report\" or Q to quit >").upper()
        if response == "S":
            send_thank_you()
        elif response == "C":
            create_report()
        elif response == "Q":
            quit_program()
