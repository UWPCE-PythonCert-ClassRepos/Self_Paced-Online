#Lesson 3 Assignment 4
#Mailroom Part Assignment
#Jason Virtue 01/26/2019
#UW Self Paced Python Course

#Data table of Donors

donors = ["Fred Flinstone", 100, "Fred Flinstone", 200, "Wilma Flinstone", 300, "Bambam", 50, "Bambam", 30, "Bambam", 40, "Barney", 75, "Betty", 50]

def donor_list(list):
    names = list[0::2]
    unique_name = set(names)
    return unique_name

def donor_add(list,person):
    if person not in list:
        list.append(person)
    else:
        list
    return list

def donor_select(list,person):
    if person in list:
        return True
    else:
        return False

def numeric(amt):
    return int(prompt_amount)

def thank_you(person,amount):
    return "Thank you {} ".format(person) + "for the donation in the amount of {}!".format(amount)

def report(a_list):
    print("Donor Name        Amount" )
    for num in a_list:
        print("{:<10s}{:10.2f}".format(*num))
    print("\n")
    return


#Send Thank you section
prompt_donor = input("What is the full name of the Donor?> ")

unique_donor = list(donor_list(donors))

donor_add(unique_donor,prompt_donor)

prompt_amount = input("What is the amount they donated?> ")

prompt_amount = numeric(prompt_amount)

donors.append(prompt_donor)
donors.append(prompt_amount)

print(donors)

print(thank_you(prompt_donor,prompt_amount))

#Create a report

print(report(donors))
