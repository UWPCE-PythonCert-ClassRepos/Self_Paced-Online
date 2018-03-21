#!/usr/bin/env python3

donors = [
        ["Galileo Galilei", 348, 8377, 123],
        ["Giovanni Cassini", 209],
        ["Christiaan Huygens", 9135, 39],
        ["Edmond Halley", 399, 1100, 357],
        ["Edwin Hubble", 1899]
        ]


def menu():
    print("\n------------------ MENU ------------------\n")
    print("PLEASE CHOOSE FROM THE FOLLOWING THREE OPTIONS\n")
    print("1. Send Thank You\n2. Create a Report\n3. Quit\n")

    # the 'option' function calls an appropriate function based on user input
    def options():
        # save user input to 'choice' as a lowercase string
        choice = input("-> ").lower()
        # user input can be a number or a string
        # if its a string, just look at the first letter
        if choice[0] == '1' or choice[0] == 's':
            thankyou()
        elif choice[0] == '2' or choice[0] == 'c':
            report()
        elif choice[0] == '3' or choice[0] == 'q':
            print("you chose 'quit'")
            # break
        else:
            # if the user input does not match one of the 3 options,
            # call the menu function again
            menu()

    options()


def thankyou():
    global donors
    print("\n------------------ THANK YOU ------------------\n")
    
    
    # simple function to list all the donors
    # calls the 'thankyou' function at the end to ask for user input
    def list():
        print("\n------------------ DONOR LIST ------------------\n")
        
        for name in donors:
            print(name[0])
            
        thankyou()

        
    # asks for a name from the user, or for the 'list' prompt 
    name_check = input("Enter the first and last name of a donor" +
                 "(type 'list' to see options)\n\n-> ").lower()

    if name_check == 'quit':
        menu()
    if name_check == 'list':
        list()
    else:
        # 'new' sentinel check to see if the user input already
        # exists in the 'donors' list
        new = True
        name_location = -1
        
        for name in donors:
            if name_check == name[0].lower():
                # if the name is already a recorded donor
                # the 'new' sentinel is set to False.
                new = False
            # update the 'name_location' counter
            name_location += 1
    
        # a false sentinel value will append the donor list
        # with the new name in title caps
        if new is True:
            donors.append([name_check.title()])
            # sets the name location to he last spot 'donors' 
            name_location = len(donors)-1
            
        # promp the user for a donation amount
        donation = input("What is the donation amount? -> ")
        if donation == 'quit':
            menu()
        donation = float(donation)
        donors[name_location].append(donation)
        #print(donors[name_location])
        
        print("\n---------------------------------------------\n")
        print(("\nDear {},\n\nYou rock.\nYour fat contribution" +
              " of ${:,}\nwill go a long way to lining my pockets." +
              "\n\nSincerely,\nScrooge McDuck").format(donors
              [name_location][0], donation))
        
        menu()
        
def report():
    column = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]   
    name_location = 0
    donors_report = []    
    
    for name in donors:
        sum_don = sum(donors[name_location][1:])
        num_don = len(donors[name_location])-1
        ave_don = sum_don / num_don
        donors_report += [[donors[name_location][0], sum_don, num_don, ave_don]]
        name_location += 1
    
    second_value = lambda donation: donation[1]
    donors_report.sort(key = second_value, reverse = True)
    
    print(donors_report)
    
    print("{:<25}{:<15}{:<12}{:<15}".format(*column))
    print("---------------------------------------------------------------")
    
    #for name in donors_report:    
    #    print("{:<25}{:<15}{:<12}{:<15}".format(*donors_report))

    menu()



menu()
