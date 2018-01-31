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
    p_fruits = [p_fruit for p_fruit in fruits if p_fruit[0]=='P']
    print(p_fruits)
    return fruits

def fruit_series2(fruits):
    print(fruits)
    fruits.pop(len(fruits)-1)
    print(fruits)


yummy = fruit_series1()
