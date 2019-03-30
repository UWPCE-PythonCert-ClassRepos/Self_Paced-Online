#!/usr/bin/env python3

# Update your mailroom program to:
# Use dicts where appropriate
# Try to use a dict and the .format() method to do the letter as one big template rather than building up a big string in parts.


#a_namespace = [ ['Bob', [40, 5, 25]], ['Alice', [100, 100, 100]], ['Zin', [30, 15, 50]], ['Chloe', [40, 13, 19]], ['James', [15]] ]
a_dict = dict( [ ( 'Bob', [40, 5, 25]), ('Alice', [100, 100, 100]), ('Zin', [30, 15, 50]), ('Chloe', [40, 13, 19]), ('James', [15]) ])


# prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
response = 0

while response != '3':
    response = input("Select number: \n 1 - Send thank you \n 2 - Create report \n 3 - quit> ")
    if response == '1':
        response2 = input("What is the name to thank? or type 'list' to see all the names >")
        if response2 == 'list':
            # show full list
            for key in a_dict:
                # Iterates just through the keys, ignoring the values
                print(key)
        else:
            if response2 in a_dict:
                response3 = input("What is amount they donated? >")
                a_dict[response2].insert(len(a_dict[response2]), int(response3))
                #name[1].insert(len(name[1]), int(response3))
            else:
                #a_namespace.insert(len(a_namespace), (response2,[]))
                a_dict.update( [(response2, [] )] )


            print("email of thanks to {} for your donation".format(response2))

    if response == '2':
        # Include Donor Name, total donated, number of donations and average donation amount as values in each row
        print(len(a_dict))
        for (key2, value2) in a_dict.items(): 
            print('Donor Name {:<10}  |  Total Donated {:<6} |  Num Donations  {:<6}  | Average Donation {:<6} '.format(key2, sum(value2), len(value2), sum(value2)//len(value2) ) )
