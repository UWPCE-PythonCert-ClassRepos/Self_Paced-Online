#!/usr/bin/env python3

# Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
response = input("Add fruit type: ")
fruits.append(response)
print(fruits)
i = 0
while (i < 1 or i > 5):
    i = int(input("Enter a number between 1-5: "))
print("Fruit {} is {}".format(i, fruits[i-1]))
fruits = ["Strawberries"] + fruits
print(fruits)
fruits.insert(0, "Blueberries")
print(fruits)
print("Fruits that start with P: ")
for fruit in fruits:
    if(fruit.startswith("P")):
        print(fruit)

# Series 2
print(fruits)
fruits.pop()
print(fruits)
# create a copy of the list for the bonus since it didnt' make sense for series 3 to have 2 entries for each fruit (assuming i'm understanding the insructions)
fruits2 = fruits * 2
fruit_to_remove = ""
while (fruit_to_remove == ""):
    fruit_to_remove = input("Enter a fruit to remove: ")
    if (fruit_to_remove not in fruits2):
        fruit_to_remove = ""
fruits.remove(fruit_to_remove)
for fruit in fruits2[:]:
        if(fruit == fruit_to_remove):
            fruits2.remove(fruit)
print(fruits2)

# Series 3
for fruit in fruits[:]:
    yes_no = input("Do you like {}: ".format(fruit.lower())).lower()

    while (True):
        if(yes_no == "no"):
            fruits.remove(fruit)
            break
        elif(yes_no == "yes"):
            break
        else:
            yes_no = input("Please enter yes or no: ")
print(fruits)

# Series 4
fruits4 = fruits[:]
for i, fruit in enumerate(fruits4):
    fruits4[i] = fruit[::-1]

fruits.pop()
print("original: ")
print(fruits)
print("copy: ")
print(fruits4)
