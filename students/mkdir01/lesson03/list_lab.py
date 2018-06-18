#!/usr/bin/env python3

#SERIES 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list (plain old print() is fine…).
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
response_fruits = input("Type another fruit: ")
fruits.append(response_fruits)

# Display the list.
print(fruits)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
response_num = input("Type a number: ")
print(response_num)
print(fruits[int(response_num) - 1])


# Add another fruit to the beginning of the list using “+” and display the list.
fruits = ["Berries"] + fruits[:]
print(fruits)

# Add another fruit to the beginning of the list using insert() and display the list.
fruits.insert(0, "Plums")
print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for i in range(len(fruits)):
    if "P" in fruits[i]:
        print(fruits[i])


# SERIES 2

# Display the list.
print(fruits)

# Remove the last fruit from the list.
fruits.pop()

# Display the list.
print(fruits)

# Ask the user for a fruit to delete, find it and delete it.
response_del = input("Type a fruit to delete: ")
fruits.remove(response_del)


# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruits = fruits[:] * 2
while True:  # we'll break out of loop once we've found a match and deleted the fruits
    match = 0
    response_new_fruit = input("Type a new fruit to delete: ")
    for n in range(len(fruits)):
        if response_new_fruit == fruits[n]:
            match += 1  # counting number of matches makes this extensible to a list with any # of repetitions
    if not match:
        print("Fruit not found in list.")
        match -= 1  # sets match to -1 to avoid the break statement
    while match > 0:
        fruits.remove(response_new_fruit)
        match -= 1
    if not match:
        break  # breaks the top loop if match == 0, i.e. if all found fruits were removed


# SERIES 3

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
tracker = [] #this will track which fruits to remove()
for fruit in fruits:
    response_r = input("Do you like {}? ".format(fruit.lower()))
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    while (response_r.lower() != "yes"): # i.e., Yes, YES, yes, etc.
        if response_r.lower() == "no":
            tracker.append(fruit) # if we remove() now, we will be off by one in our list
            break
        else:
            print("Answer with \"yes\" or \"no\" only.")
            response_r = input("Do you like {}? ".format(fruit.lower()))

# For each “no”, delete that fruit from the list.
for fruit in tracker:
    fruits.remove(fruit)

# Display the list.
print(fruits)


#SERIES 4

#Make a copy of the list and reverse the letters in each fruit in the copy.
fruits_copy = []
for i in range(len(fruits)):
    fruits_copy.append(fruits[i][::-1]) # append(fruits_list[a_particular_fruit[read backwards]])

#Delete the last item of the original list. Display the original list and the copy.
fruits.pop()
print(fruits)
print(fruits_copy)

