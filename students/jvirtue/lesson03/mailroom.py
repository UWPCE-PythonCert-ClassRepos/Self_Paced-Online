#Lesson 3 Assignment 4
#Mailroom Part Assignment
#Jason Virtue 01/26/2019
#UW Self Paced Python Course


#Thank You Letter Section
def Send_Thanks(db_name):
    response = "Not a donor or the word list"
    while response not in db_name:
        print("----------------------------------------")
        response = input("What is the full name of the donor?>(Name, List, Exit) ")
        response = response.title()
        if response == "Exit":
            break
        elif response == "List":
            print("----------------------------------------")
            print("Here are our Donors:> ")
            print(donor_list(db_name))
        elif response != "List":
            print("----------------------------------------")
            amount = int(input("How much money did {} donate?> ".format(response)))
            if response not in donor_list(db_name):
                donors_db = donor_add(response,db_name)
                donors_db = amount_add(response, amount, db_name)
            else:
                donors_db = amount_add(response, amount, db_name)
            print("----------------------------------------")
            print(thank_you(response, amount))
            print(db_name)

def donor_list(db_name):
    return [item[0] for item in db_name]

def donor_add(name,db_name):
    return db_name.append([name])

def amount_add(name, amt, db_name):
    return db_name[donor_list(db_name).index(name)].append(amt)

def thank_you(person,amount):
    return "Thank you {} ".format(person) + "for the donation in the amount of {}!".format(amount)

#Create a report
def Sum_Gift(donor, db_name):
    total = 0
    for i in db_name:
        if i[0] == donor:
            total = sum(i[1:])
    return total

def donation_count(donor, db_name):
    count = 0
    for i in db_name:
        if i[0] == donor:
            count = len(i[1:])
    return count

def Create_Report(db_name):
    dnrNames = donor_list(db_name)
    print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
    print("-" * 68)
    iCount = 1
    for i in dnrNames:
        iTotalGift = Sum_Gift(i, db_name)
        iCount = donation_count(i, db_name)
        iAveGift = iTotalGift / iCount
        s = f'{i:<20}{" ":<1}{"$":<1}{iTotalGift:>14}{" ":<1}{iCount:>15}{" ":<1}{"$":<1}{iAveGift:>14}'
        print(s)

#Options Menu
if __name__ == '__main__':
    donors_db = [["Fred Flintstone", 100,200],["Wilma Flintstone", 300],["Bamm-Bamm Rubble", 50,30,40],["Barney Rubble", 75],["Pebbles Flintstone",50]]
    while True:
        print("Would you like to;")
        print("1: Send a 'Thank You'")
        print("2: Create a 'Report'")
        print("3: 'Quit'")
        response = input("Please select option: ")
        if response.title() == "Thank You":
            Send_Thanks(donors_db)
        elif response.title() == "Report":
            Create_Report(donors_db)
        elif response.title() == "Quit":
            break
        print()