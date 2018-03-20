#!/usr/bin/env python3

# Establish a global 'fruit' list variable
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

def series_1():

    # This function modifies the global 'fruit' variable
    print("Task 4")
    global fruit
    print("the list is {}".format(fruit))
    
    # ask user for a fruit and store it as a list
    fruit_response1 = [input("What's another kind of fruit? > ")]
    
    # concatenate fruit list and response
    fruit = fruit + fruit_response1
    print(fruit)
    
    # count the list then ask the user for a number from 1 to x and save as int
    fruit_count = len(fruit)
    num_response = fruit_count + 1
    while (num_response > fruit_count) or (num_response < 1):
        num_response = int(input("choose a number from 1 to {} > ".format(fruit_count)))
        
    # concatenate the response using the 'fruit' list and user input
    print("Number {} is {}".format(num_response,fruit[num_response-1]))
    
    # add two more fruits
    fruit_response2 = [input("What's a second kind of fruit you'd like to add? > ")]
    fruit_response3 = [input("What's a third kind of fruit you'd like to add? > ")]
    
    # using +
    fruit = fruit_response2 + fruit

    # and using insert()
    fruit.insert(0,fruit_response3[0])
    
    # display the list
    print("the full list is:", end = ' ')
    
    for x in fruit:
        print (x, end = ' ')
    print("")
    
    # just the 'P' fruits
    for x in fruit:
        if(x[0]) == "P":
            print(x, end=' ')
    print("start with P")
    

def series_2():
    print("Task 2")
    # This function references the global 'fruit' variable 
    # But only modifies a local version, 'fruit_2'
    global fruit
    fruit_2 = fruit[:]
    print(fruit_2)
    
    # remove the last item from the fruit list
    fruit_2 = fruit_2[0:-1]
    print(fruit_2)
    
    # set 'fruite_deleted' sentinel to false
    fruit_deleted = False
    
    # Ask the user for a fruit to delete...
    while fruit_deleted == False:
        delete_response = input("Which fruit would you like to delete? > ")
        # ... and remove it from the list
        for x in fruit_2:
            if x == delete_response:
                fruit_2.remove(delete_response)
                fruit_deleted = True
        # if user input is bunk ask again
        if fruit_deleted == False:
            print("{} is not a fruit in the list. Try again." .format(delete_response))
            print (fruit_2)
               
    print(fruit_2)

    
def series_3():
    print("Task 3")
    # populate local 'fruit_3' variable from global 'fruit' list
    global fruit
    fruit_3 = fruit[:]
    # create an empty 'bad_fruit' list to be populated by user
    bad_fruit = []
  
    
    for x in fruit:
        # ask the user if they like the fruit. Ask and assign in lowercase
        like_fruit = input("Do you like {}?(yes/no) > ".format(str(x.lower()))).lower()
        # if input anything other than yes/no keep asking
        while like_fruit not in ['yes','no']:
            print ("Please respond with 'yes' or 'no'")
            like_fruit = input("Do you like {}?(yes/no) > ".format(str(x.lower()))).lower()    
        # if they don't like the fruit add it to the bad_fruit list
        if like_fruit == 'no':
            bad_fruit += [x]
    
    # remove all the nasty fruit from the bad_fruit list...
    for nasty in bad_fruit:
        fruit_3.remove(nasty)
    
    # ...and print the resulting list of non-nasty fruit
    print(fruit_3)

    
def series_4():
    print("Task 4")
    # create an empty 'fruit_4' list to be populated in the following loop
    fruit_4 = []
    
    # for every name in 'fruit' reverse it, and add it it to 'fruit_4'
    for name in fruit:
        fruit_4 += [name[::-1]]
    
    # copy 'fruit' list and remove last item
    chopped_fruit = fruit[:-1]
    
    # print the reversed list and the original list without the last item
    print(fruit_4)
    print(chopped_fruit)
    
    
series_1()
series_2()
series_3()
series_4()
    