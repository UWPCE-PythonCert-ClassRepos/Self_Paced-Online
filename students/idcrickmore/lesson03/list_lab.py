#!/usr/bin/ python3

# Establish a global 'fruit' list variable
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

def series_1():

    # This function modifies the global 'fruit' variable
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
    
    # just the 'P' fruits
    for x in fruit:
        if(x[0]) == "P":
            print(x)
    

def series_2():
    # This function references the global 'fruit' variable 
    # But only modifies a local version, 'fruit_2'
    global fruit
    fruit_2 = fruit
    print(fruit_2)
    
    # remove the last item from the fruit list
    fruit_2 = fruit_2[0:-1]
    print(fruit_2)
    
    # Ask the user for a fruit to delete and remove it from the list
    def delete_fruit():
        fruit_deleted = False
        delete_response = input("Which fruit would you like to delete? > ")
        for x in fruit_2:
            if x == delete_response:
                fruit_2.remove(delete_response)
                fruit_deleted = True
            if fruit_deleted == False:
                print("{} is not a fruit in the list. Try again." .format(delete_response))
                print (fruit_2)
                delete_fruit()
            print(fruit_2)
            
    delete_fruit()
                
    
    