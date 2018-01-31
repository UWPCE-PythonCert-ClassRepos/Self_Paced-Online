#!/usr/bin/env python3

def fruit_series1():
    fruits = ["Apples","Pears","Oranges","Peaches"]
    print(fruits)
    new_fruit = input("I'm hungry. Give me another fruit >")
    fruits.append(new_fruit)
    print(fruits)
    num = int(input("Guess how many fingers I'm holding up (one hand) >"))
    while num<1 or num > 5:
        num = int(input("I have a normal hand. Guess how many fingers I'm holding up >"))
    print("{:d}: {}".format(num, fruits[num-1]))
    fruits=["Tomato"]+fruits
    print(fruits)
    fruits.insert(0,"Pancakes")
    print(fruits)
    for fruit in fruits:
        if fruit[0] == 'P':
            print(fruit, end=' ')
    print()
    return fruits

fruit_series1()
