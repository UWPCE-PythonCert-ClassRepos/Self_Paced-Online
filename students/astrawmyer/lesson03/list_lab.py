#!/usr/bin/env python3

# Series 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
response = input("Add another fruit: ")
fruit.append(response)
print(fruit)

number = int(input("Input a number: "))
print(number, fruit[number-1])

first = input("And another one: ")
first_list = [first]
fruit = first_list + fruit
print(fruit)

first = input("And another one: ")
fruit.insert(0, first)
print(fruit)
j=0
p_fruit=[]
for i in fruit:
    if fruit[j][0]=="P":
        p_fruit.append(fruit[j])
    j=j+1
print(p_fruit)


# Series 2
# Made fruit2 so list from first sequence unchanged for series 3 and 4.
fruit2 = fruit.copy()
print(fruit2)
fruit2.pop()
print(fruit2)
response = input("Type a fruit to delete:")
fruit2.remove(response)
print(fruit2)


# Series 3

# Using the remove() function in the for loop causes the next iteration to skip the next item
# in the list because the next utem slides up to the current index.
# getting around this an am making a separate copy of the list.

#fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit3 = fruit.copy()
new_fruit = []
for i in fruit3:
    response = input("Do you like " + i.lower() + "? ")
    while response not in ['no','yes']:
        response = input("Respond with only 'yes' or 'no': ")
    if response == "yes":
        new_fruit.append(i) 
print(new_fruit)


# Series 4

#fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit4 = fruit.copy()
fruit_reverse = fruit.copy()
for i, f in enumerate(fruit4):
    fruit_reverse[i] = f[::-1]
fruit4.pop()
print(fruit)
print(fruit4)
print(fruit_reverse)