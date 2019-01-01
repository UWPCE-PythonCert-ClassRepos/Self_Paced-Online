#!/usr/bin/env python3
"""Assignmet 3 List Lab
Ian Sahlberg
Python 210
12/26/2018
"""

#Series 1
fruit_basket = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_basket)

user_fruit = input("Tell me another fruit to add to your basket...")
fruit_basket.append(user_fruit)
print(fruit_basket)

user_number = int(input("Can you give me a number 1 thru " + str(len(fruit_basket)) + " ?"))
print("Your number is", user_number, "and the corresponding fruit is", fruit_basket[user_number - 1])

user_fruit = input("Tell me another fruit to add to your basket...")
fruit_basket = [user_fruit] + fruit_basket

user_fruit = input("Tell me another fruit to add to your basket...")
fruit_basket.insert(0,user_fruit)

for fruit in fruit_basket:
    if fruit[0] == "P":
        print(fruit)

#Series 2

fruit_basket = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_basket)

del fruit_basket[-1]
print(fruit_basket)

delete_fruit = input("What fruit would you like removed from your basket?")

if delete_fruit in fruit_basket:
    fruit_basket.remove(delete_fruit)

else:    #multiply list x2 each time fruit is not in basket, delete occurances when match is found.
    match = False
    while not match:
        fruit_basket *= 2
        print(fruit_basket)
        delete_fruit = input("What fruit would you like removed from your basket?")
        while delete_fruit in fruit_basket:
            #for fruit in fruit_basket:
            fruit_basket.remove(delete_fruit)
            match = True
        else:
            continue


#Series 3

for fruit in fruit_basket:

    while fruit:
        user_preference = input("Do you like " + fruit + "?   Yes or No.").lower()
        if user_preference == "no":
            while fruit in fruit_basket:
                fruit_basket.remove(fruit)
            break
        elif user_preference == "yes":
            break
        else:
            print("Please choose Yes or No")
            print(fruit_basket)


