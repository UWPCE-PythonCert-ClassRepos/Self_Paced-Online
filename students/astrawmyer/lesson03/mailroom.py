#!/usr/bin/env python3

donors = [["Manny Machado",[1,2,3]],["Adam Jones",[1,2,3]]]
names = ["manny", "adam"]
# Thank you Module

input_name = input("Enter full name: ")
loop = True
while loop == True:
    
    # Print list of donor names.
    if input_name == "list":
        for i in donors:
            print(i[0])
        loop = false
    elif input_name not in names:
        input_name = input("agane")


"""     for i in fruit3:
    response = input("Do you like " + i.lower() + "? ")
    while response not in ['no','yes']:
        response = input("Respond with only 'yes' or 'no': ")
    if response == "yes":
        new_fruit.append(i) 
print(new_fruit) """