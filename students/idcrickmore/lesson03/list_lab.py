#!/usr/bin/ python3

def series_1():
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print("the list is {}".format(fruit))
    
    fruit_response = input("What's another kind of fruit? > ")
    
    # change response type from string to list
    fruit_response = [fruit_response]
    
    # concatenate fruit list and response
    fruit = fruit + fruit_response
    print(fruit)
    
    # count the list then ask the user for a number from 1 to x and save as int
    fruit_count = len(fruit)
    num_response = fruit_count + 1
    while (num_response > fruit_count) or (num_response < 1):
        num_response = int(input("choose a number from 1 to {} > ".format(fruit_count)))
        
    # concatenate the response using the 'fruit' list and user input
    print("Number {} is {}".format(num_response,fruit[num_response-1]))
    
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    # add two more fruits
    two_more_fruit = ["Persimmon", "Avocado"]
    
    # using +
    fruit = two_more_fruit[:1] + fruit[:]
    print(fruit)

    # and using insert()
    fruit.insert(0,two_more_fruit[1])
    print(fruit)
    
    # just the 'P' fruits
