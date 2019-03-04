#Lesson 6 Assignment 1
#Mailroom Part 4 Assignment
#Jason Virtue 02/25/2019
#UW Self Paced Python Course

#Data Set
donors_db = {'Fred Flintstone': [100,200],'Wilma Flintstone': [300],'Bamm-Bamm Rubble': [50,30,40],'Barney Rubble' : [75],'Pebbles Flintstone': [500]}

#Option menu 1 -- input donors and amounts into DICT
def send_thanks(db_name):
    print("-"*40)
    response = input("What is the full name of the donor? (Name, List, Exit)> ").title()
    if response == "Exit":
        return
    elif response == "List":
        print("-"*40,"\nHere are our Donors:> \n",donor_list(db_name),sep="")
    else:
        try:
            print("-"*40)
            amount = int(input("How much money did {} donate?> ".format(response)))
            donors_db = amount_add(response,amount,db_name)
        except ValueError:
            print("-"*40, "\nPlease enter a valid numeric value.\n","-"*40,sep="")
            return
        print("-"*40,"\n",thank_you(response, amount),sep="")

#List out unique donors
def donor_list(db_name):
    return [item for item in db_name]  #Changed to list comprehension

#Add to dictionary donor and amount
def amount_add(name, amt, db_name):
    return db_name.setdefault(name,[]).append(amt)

#Thank you message in console app
def thank_you(person,amount):
    return "Thank you {} ".format(person) + "for the donation in the amount of {}!".format(amount)

#Thank you letter files to text file for all donors
def thanks_file(db_name):
    for data in db_name:
        filename = data.replace(" ", "_") + ".txt"
        total_donation = sum(db_name[data])
        letter = ('Thank you {} for you generous contributions totaling {:.2f}!'.format(data, total_donation))
        open(filename, 'w').write(letter)
        print(f"{data}'s letter has been saved to " + filename)

#Build list of donors, amount, count of contributions and average gift amount
def crunch_numbers(db_name):
    crunch_numbers = [[donor,sum(db_name[donor]),len(db_name[donor]),sum(db_name[donor])/len(db_name[donor])] for donor in db_name] #changed to list comprehension
    return crunch_numbers

#Sort key for donor list.  Sort by donation amount
def sort_key(crunch_numbers):
    return crunch_numbers[1]

#Print report to console
def create_report(db_name):
    print("\n","-" * 68,sep="")
    print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
    print("-" * 68)
    sort_table = crunch_numbers(db_name)
    [print(f'{item[0]:<20}{" ":<1}{"$":<1}{item[1]:>14}{" ":<1}{item[2]:>15}{" ":<1}{"$":<1}{item[3]:>14}') for item in sort_table]

#Main menu quit program
def quit(db_name):
    return "Quit"

#Main menu function
def main_menu():
    menu_dict = {1:send_thanks,2:create_report,3:thanks_file,4:quit}
    while True:
        print("\n","-"*40,"\nMailroom Main Menu;\n","1: Send a Thank You\n","2: Create a Report\n","3: Send letters to everyone\n","4: Quit\n","-"*40,sep="")
        try:
            response = int(input("Please select option [Enter number 1 - 4]: "))    
        except ValueError:
            print("-"*40,"\nValid values are numeric and does not accept characters\n","-"*40,sep="")
            continue
        try:
            if menu_dict[response](donors_db) == "Quit":
                break         
        except KeyError:
            print("-"*40,"\nPlease enter a valid number between 1 to 4.\n","-"*40,sep="")

#Options Menu
if __name__ == '__main__':
    main_menu()