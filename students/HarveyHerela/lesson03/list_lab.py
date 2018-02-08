#!/usr/bin/env python3

# Starting list of fruits
my_fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(my_fruits)

# Query the user for another fruit
response = input("Fruit to add: ")
my_fruits.append(response.title())
print(my_fruits)

# Ask for a fruit index
response = 'a'
while not response.isdigit():
    response = input("Index of a fruit to display: ")
    # Verify it's an int
    if response.isdigit():
        fruit_index = int(response)
        # Verify it's in range
        if fruit_index > len(my_fruits):
            response = 'a'
    
print(fruit_index, my_fruits[fruit_index - 1])

# Query the user for another fruit: +
response = input("Fruit to add: ")
my_fruits = [response.title()] + my_fruits
print(my_fruits)

# Query the user for another fruit: insert
response = input("Fruit to add: ")
my_fruits.insert(0, response.title())
print(my_fruits)

# Display all fruits that start with a p using a for loop
print("Displaying all fruits that start with the letter 'p'")
for fruit in my_fruits:
    if fruit[0] == 'P':
        print(fruit, end=' ')
print('\n')


# Start of series 2
print("Start of series 2")
# Display the list.
print(my_fruits)

# Remove the last fruit from the list.
# Display the list.
print("Removing the last fruit")
my_fruits.pop(len(my_fruits)-1)
print(my_fruits)

# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
my_fruits = my_fruits * 2
num = 0
while num == 0:
    print("List of fruit: ", my_fruits)
    response = input("Fruit to delete (must exist): " )
    num = my_fruits.count(response.title()) 
while num > 0:
    my_fruits.remove(response.title())
    num = my_fruits.count(response.title()) 
print(my_fruits)

# Start of series 3
print("Start of series 3")
# This series is easier if each fruit only appears once
my_fruits = list(set(my_fruits))
print(my_fruits)

# Ask the user for input displaying a line like "Do you like apples?" for each fruit in the list (making the fruit all lowercase).
# For each "no", delete that fruit from the list.
# For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here)

# I don't want to invalidate my iterator, so make a copy of the list
# to use for looping
my_fruits_loop = list(my_fruits)
for fruit in my_fruits_loop:
   response = "maybe"
   while response != 'yes' and response != 'no':
      query = "Do you like " + fruit + "('yes' or 'no')? "
      response = input(query)
      response = response.lower()
   
   if response == 'no':
      my_fruits.remove(fruit)

# Display the list.
print(my_fruits)
print()

# Start of series 4
print("Start of series 4")
# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy.
reverse_fruits = list()
for fruit in my_fruits:
    reverse_fruits.append(fruit[::-1])
my_fruits.pop(len(my_fruits) - 1)
print(my_fruits)
print(reverse_fruits)
