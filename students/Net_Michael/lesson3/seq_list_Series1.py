#!/usr/bin/env python
# coding: utf-8

# series 1

# Create and display the given list 

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

# Ask the user for another fruit
# add it to the end of the list
# display the list
new_fruit = input("Add new fruit to the end of list ")
output = fruit.append(new_fruit)
print(fruit)

# Ask the user for a number 
# display the number back to the user 
def sel_fruit(f, fruit = fruit):
    m = len(fruit) + 1
    while f <= m:
        for i in range(1,m):
            if f == i : 
                sel_fr = fruit[i-1]
                return(sel_fr)

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
index = input("Fruits indexed by ")
print("are " + sel_fruit(int(index)) + ".")

# add another fruit to the list using +
new_fruit = input("Add new fruit to the list ")
output = [new_fruit] + fruit
print( output)

# add new fruit at the begining of the list
add_fruit = input("Add new fruit at the begining of the list ")
output = fruit.insert(0, "Banana")
print(fruit) 
      
# display all the fruits that begin with "P" 
            
def letterP(fruit, word_a):
    m = len(fruit)
    for i in range(m):
        if word_a in fruit[i]:
            print(fruit[i])


# display all the fruits that contain "P" or "p"
def letterP(fruit, word_a):
    m = len(fruit)
    fruits = [item.lower() for item in fruit]
    for i in range(m):
        if word_a in fruits[i]:
            print(fruit[i])