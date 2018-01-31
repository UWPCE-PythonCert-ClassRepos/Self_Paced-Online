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
    fruits=["Tomatoes"]+fruits
    print(fruits)
    fruits.insert(0,"Pancakes")
    print(fruits)
    #print([p_fruit for p_fruit in fruits if p_fruit[0]=='P'])
    for p in fruits:
        if p[0]=='P':
            print(p, end = ' ')
    print()
    return fruits

def fruit_series2(fruits):
    print(fruits)
    fruits.pop(len(fruits)-1)
    print(fruits)
    rm_fruit = input("I have too many fruit. Choose which fruit to ditch >")
    while rm_fruit not in fruits:
        print("I don't have that fruit!")
        fruits = fruits*2
        print(fruits)
        rm_fruit = input("Oh god they're multiplying! Choose which fruit to ditch! >")
    while rm_fruit in fruits:
        fruits.remove(rm_fruit)
    print("My remaining fruit: ")
    #print([chosen_fruit for chosen_fruit in fruits if chosen_fruit!=rm_fruit])
    print(fruits)

def fruit_series3(fruits):
    no_fruits = []
    for like_fruit in fruits:
        yes_no = input("Do you like "+str(like_fruit.lower())+
                       "? (yes/no) >").lower()
        while yes_no not in ["yes","no"]:
            print("Please answer yes or no")
            yes_no = input("Do you like "+str(like_fruit.lower())+
                           "? (yes/no) >").lower()
        if yes_no=="no":
            no_fruits+=[like_fruit]
    for rm_fruit in no_fruits:
        while rm_fruit in fruits:
            fruits.remove(rm_fruit)
    print(fruits)
            
yummy = fruit_series1()
#fruit_series2(yummy)
fruit_series3(yummy)
