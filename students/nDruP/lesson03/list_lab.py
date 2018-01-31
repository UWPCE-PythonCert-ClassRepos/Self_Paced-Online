#!/usr/bin/env python3

def fruit_series1():
"""
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
"""
    fruits = ["Apples","Pears","Oranges","Peaches"]
    print(fruits)
    new_fruit = input("I'm hungry. Give me another fruit >")
    fruits.append(new_fruit)
    print(fruits)
    num = int(input("Guess how many fingers I'm holding up (one hand) >"))
    while num<1 or num > 5:
        print("I have a normal hand.")
        num = int(input("Guess how many fingers I'm holding up >"))
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
"""
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""
    print(fruits)
    fruits.pop(len(fruits)-1)
    fruits*=2
    print(fruits)
    rm_fruit = input("I have too many fruits! Choose which fruit to ditch >")
    while rm_fruit not in fruits:
        print("I don't have that fruit!")
        fruits *=2
        print(fruits)
        rm_fruit = input("Oh god they're multiplying! Choose which fruit to ditch! >")
    while rm_fruit in fruits:
        fruits.remove(rm_fruit)
    print("My remaining fruit: ")
    #print([chosen_fruit for chosen_fruit in fruits if chosen_fruit!=rm_fruit])
    print(fruits)
    return


def fruit_series3(fruits):
"""
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
"""
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

    
def fruit_series4(fruits):
"""
Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
"""
    rev_fruits = []
    for tiurf in fruits:
        rev_fruits+=[tiurf[::-1]]
    fruits.pop(len(fruits)-1)
    print(fruits)
    print(rev_fruits)

print("fruit_series1")
yummy = fruit_series1()

print("\n\n fruit_series2")
fruit_series2(yummy[:])

print("\n\n fruit_series3")
fruit_series3(yummy[:])

print("\n\n fruit_series4")
fruit_series4(yummy[:])
