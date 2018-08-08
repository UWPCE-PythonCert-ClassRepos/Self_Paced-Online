#!/usr/bin/env python3

donors = [["Manny Machado",[1,2,3]],["Adam Jones",[1,2,3]]]
names = ["manny", "adam"]
# Thank you Module


loop_trigger = True

while loop_trigger == True:
    input_name = input("Enter full name: ")

    #This block checks if the input name is in the list of donors.
    for i in donors:
        if i[0] == input_name:
            #this section for if name typed is correct.
            #ask for number and add it to list of donations.
            print('match')
            loop_trigger = False
            break
        elif input_name == 'list':
            #Prints a list of donors.
            for j in donors:
                print(j[0])
        else:
            #back to input name
            break
    
    



#        for i in donors:
#            print(i[0])

#    for i in fruit3:
#    response = input("Do you like " + i.lower() + "? ")
#    while response not in ['no','yes']:
#        response = input("Respond with only 'yes' or 'no': ")
#    if response == "yes":
#        new_fruit.append(i) 
# print(new_fruit)