#Lesson 3 Assignment 4
#Mailroom Part Assignment
#Jason Virtue 01/26/2019
#UW Self Paced Python Course


#Thank You Letter Section
def send_thanks(db_name):
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
        else:
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
def crunch_numbers(db_name):
    crunch_numbers = []
    for i in db_name:
        donor = i[0]
        donations = i[1:]
        sum_gift = sum(donations)
        count = len(donations)
        avg_gift = sum_gift / count
        crunch_numbers.append([donor,sum_gift,count,avg_gift])
        crunch_numbers.sort(key=sort_key,reverse=True)
    return crunch_numbers


def sort_key(crunch_numbers):
    return crunch_numbers[1]

def create_report(db_name):
    print(f'{"Donor Name":<20}{"|":<1}{"Total Given":^15}{"|":<1}{"Num Gifts":^15}{"|":<1}{"Average Gift":>15}')
    print("-" * 68)
    sort_table = crunch_numbers(db_name)
    for item in sort_table:
        s = f'{item[0]:<20}{" ":<1}{"$":<1}{item[1]:>14}{" ":<1}{item[2]:>15}{" ":<1}{"$":<1}{item[3]:>14}'
        print(s)


#Options Menu
if __name__ == '__main__':
    donors_db = [["Fred Flintstone", 100,200],["Wilma Flintstone", 300],["Bamm-Bamm Rubble", 50,30,40],["Barney Rubble", 75],["Pebbles Flintstone",500]]
    while True:
        print("Would you like to;")
        print("1: Send a Thank You")
        print("2: Create a Report")
        print("3: Quit")
        response = input("Please select option [Enter number 1 - 3]: ")
        if response.title() == "1":
            send_thanks(donors_db)
        elif response.title() == "2":
            create_report(donors_db)
        elif response.title() == "3":
            break
        print()