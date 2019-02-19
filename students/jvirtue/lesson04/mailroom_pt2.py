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
            amount = int(input("How much money did {} donate?> ".format(response)))
            donors_db = amount_add(response, amount, db_name)
            print("----------------------------------------")
            print(thank_you(response, amount))
            print(db_name)

def donor_list(db_name):
    return [item for item in db_name]

def amount_add(name, amt, db_name):
    return db_name.setdefault(name,[]).append(amt)

def thank_you(person,amount):
    return "Thank you {} ".format(person) + "for the donation in the amount of {}!".format(amount)

#Thank you letter files
def thanks_file(db_name):
    for data in db_name:
        filename = data.replace(" ", "_") + ".txt"
        total_donation = sum(db_name[data])
        letter = ('Thank you {} for you generous contributions totalling {:.2f}!'.format(data, total_donation))
        open(filename, 'w').write(letter)
        print(f"{data}'s letter has been saved to " + filename)

#Create a report
def crunch_numbers(db_name):
    crunch_numbers = []
    for i in db_name:
        donor = i
        sum_gift = sum(db_name[i])
        count = len(db_name[i])
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


def quit(db_name):
    return "Quit"

#Options Menu
if __name__ == '__main__':
    #donors_db = [["Fred Flintstone", 100,200],["Wilma Flintstone", 300],["Bamm-Bamm Rubble", 50,30,40],["Barney Rubble", 75],["Pebbles Flintstone",500]]
    donors_db = {'Fred Flintstone': [100,200],'Wilma Flintstone': [300],'Bamm-Bamm Rubble': [50,30,40],'Barney Rubble' : [75],'Pebbles Flintstone': [500]}
    menu_dict = {1:send_thanks,2:create_report,3:thanks_file,4:quit}
    while True:
        print("Would you like to;")
        print("1: Send a Thank You")
        print("2: Create a Report")
        print("3: Send letters to everyone")
        print("4: Quit")
        response = int(input("Please select option [Enter number 1 - 4]: "))
        if menu_dict[response](donors_db) == "Quit":
            break
        print()