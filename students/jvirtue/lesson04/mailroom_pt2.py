#Lesson 4 Assignment 1
#Mailroom Part 2 Assignment
#Jason Virtue 02/02/2019
#UW Self Paced Python Course
#Lesson 4 Assignment 1
#Mailroom Part 2
#Jason Virtue 02/05/2019
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
            amount = float(input("How much money did {} donate?> ".format(response)))
            if response not in donor_list(db_name):
                donors_db = donor_add(response,db_name)
                donors_db = amount_add(response, amount, db_name)
            else:
                donors_db = amount_add(response, amount, db_name)
            print("----------------------------------------")
            print(thank_you(response, amount))

def donor_list(db_name):
    return [item[0] for item in db_name]

def donor_add(name,db_name):
    return db_name.update({name:0})

def amount_add(name, amt, db_name):
    return db_name.setdefault(name,[]).append(amt)

def thank_you(person,amount):
    return "Thank you {} ".format(person) + "for the donation in the amount of {}!".format(amount)

def thank_you_letter(db_name):
    return f"""Dear {db_name["name"]},\nThank you for your very generous donation of ${db_name["amount"]:.2f}.\n{"Sincerely":>40}\n{"Fred Flintstone":>50}"""

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
    #donors_db = [["Fred Flintstone", 100,200],["Wilma Flintstone", 300],["Bamm-Bamm Rubble", 50,30,40],["Barney Rubble", 75],["Pebbles Flintstone",500]]
    donors_db = {'Fred Flintstone': [100,200],'Wilma Flintstone': [300],'Bamm-Bamm Rubble': [50,30,40],'Barney Rubble' : [75],'Pebbles Flintstone': [500]}
    while True:
        print("Would you like to;")
        print("1: Send a Thank You")
        print("2: Create a Report")
        print("3: Send letters to everyone")
        print("4: Quit")
        response = input("Please select option [Enter number 1 - 4]: ")
        if response.title() == "1":
            send_thanks(donors_db)
        elif response.title() == "2":
            create_report(donors_db)
        elif response.title() == "3":
            thank_you_letter(donors_db)    
        elif response.title() == "4":
            break
        print()