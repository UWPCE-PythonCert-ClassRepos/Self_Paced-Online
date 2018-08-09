#!/usr/bin/env python3

donors = [["Manny Machado",[1,2,3]],["Adam Jones",[1,2,3]]]
names = ["manny", "adam"]

# Thank you Module

def displaylist():    
    for sublist in donors:
        print(sublist[0])
    return

def enterdonation():
    return

#function to send a thank you
def thankyou():
    

    #This block checks if the input name is in the list of donors.
    loop_trigger = True
    stopint = 0
    while loop_trigger == True:
        stopint = stopint + 1
        while stopint>10:
            loop_trigger = False
        input_name = input("Enter full name: ")
        for i, donor_row in enumerate(donors):
            #print(i, donor_row)
            if donor_row[0] == input_name:
                #this section for if name typed is correct.
                #ask for number and add it to list of donations.
                print(i,donor_row)
                donation = float(input("Enter donation amount:"))
                donors[i][1].append(int(donation))
                print(donors)
                #need to add to original donors structure. need to index???
                #loop_trigger = False
                break
            elif input_name == 'list':
                displaylist()
                break
            else:
                break















print("What do you want to do?")
response = input("1. Send a Thank You, 2. Create a Report, 3. Quit")
if response == '1':
    thankyou()








""" loop_trigger = True

while loop_trigger == True:
    input_name = input("Enter full name: ")

    #This block checks if the input name is in the list of donors.
    for i in donors:
        if i[0] == input_name:
            #this section for if name typed is correct.
            #ask for number and add it to list of donations.
            donation = float(input("Enter donation amount:"))
            #need to add to original donors structure. need to index???
            loop_trigger = False
            break
        elif input_name == 'list':
            #Prints a list of donors.
            for j in donors:
                print(j[0])
        else:
            #Back to requesting input name.
            break
     """
    



#        for i in donors:
#            print(i[0])

#    for i in fruit3:
#    response = input("Do you like " + i.lower() + "? ")
#    while response not in ['no','yes']:
#        response = input("Respond with only 'yes' or 'no': ")
#    if response == "yes":
#        new_fruit.append(i) 
# print(new_fruit)