#!/usr/bin/env python3

donors = [["Manny Machado",[12.2,2.51,3.20]],["Adam Jones",[1024.14,22.21,323.45]]]
names = ["manny", "adam"]

# Thank you Module

def displaylist():    
    for sublist in donors:
        print(sublist[0])
    return

""" def enterdonation(index,amount):
    print(donors[i][1])
    return """

def writeletter(name,amount):
    print('Dear {},'.format(name))
    print("Thank you for donating ${} to the Human Fund. Your money will be used appropriately.".format(amount))
    return

#function to send a thank you
def thankyou():
    loop_trigger = True
    while loop_trigger == True:
        input_name = input("Enter full name: ")
        for i, donor_row in enumerate(donors):
            if donor_row[0] == input_name:
                #print(donor_row[0],input_name)
                #this section for if name typed is correct.
                #ask for number and add it to list of donations.
                # print(i,donor_row)
                donation = float(input("Enter donation amount:"))
                donors[i][1].append(int(donation))
                #enterdonation(i,donation)
                print(donors)
                writeletter(donors[i][0],donors[i][1][len(donors[i][1])-1])
                loop_trigger = False
                break
            elif input_name == 'list':
                displaylist()
                break
    return



def createreport():
    donors_report = []
    sum_donation = 0
    for i, name in enumerate(donors):
        for j in donors[0][1]:
            sum_donation = sum_donation + j
        num_donation = len(donors[i][1])
        avg_donation = sum_donation/num_donation
        donors_report.append([name[0],sum_donation, num_donation,avg_donation])
        print(name[0],sum_donation, num_donation,avg_donation)
        print(donors_report)
    return












print("What do you want to do?")
response = input("1. Send a Thank You, 2. Create a Report, 3. Quit")
if response == '1':
    thankyou()
if response == '2':
    createreport()








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