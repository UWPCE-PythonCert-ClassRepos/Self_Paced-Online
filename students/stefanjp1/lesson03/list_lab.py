#!/usr/bin/env python3

# Series 1:
fruit_list_orig = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_list = fruit_list_orig[:]

print(fruit_list)

# Ask for another fruit
new_fruit = input("Enter another fruit > ")

fruit_list.append(new_fruit)

print(fruit_list)

# Ask for a fruit number
fruit_number = input("Enter a number > ")

print(fruit_number, fruit_list[int(fruit_number) - 1])

# Add more fruits
fruit_list = ["Cherries"] + fruit_list

print(fruit_list)

fruit_list.insert(0, "Blueberries")

print(fruit_list)

# Show all "P" fruits
for fruit in fruit_list:
    if fruit[0] == 'P':
        print(fruit)

        
# Series 2:
fruit_list = fruit_list_orig[:]
print(fruit_list)

del fruit_list[-1:]

print(fruit_list)

# Ask for a fruit to delete
remove_fruit = input("Enter a fruit to delete > ")

fruit_list.remove(remove_fruit)

print(fruit_list)


# Series 3:
fruit_list = fruit_list_orig[:]
dislikes = list()
for fruit in fruit_list:
    likes = input("Do you like " + fruit + "? > ")
    
    while not( likes in ['yes', 'no'] ):
        likes = input("Answer with yes or no: Do you like {}? > ".format(fruit))
    
    if likes == 'no':
        dislikes = dislikes + [fruit]
else:
    for fruit in dislikes:
        fruit_list.remove(fruit)

print(fruit_list)


# Series 4:
fruit_list = fruit_list_orig[:]

fruit_list_copy = fruit_list[:]

fruit_reversed_list = list()
for fruit in fruit_list_copy:
    fruit_reversed = fruit[::-1]
    fruit_reversed_list = fruit_reversed_list + [fruit_reversed]

fruit_list_copy = fruit_reversed_list[:]
del fruit_list[-1:]

print(fruit_list)
print(fruit_list_copy)