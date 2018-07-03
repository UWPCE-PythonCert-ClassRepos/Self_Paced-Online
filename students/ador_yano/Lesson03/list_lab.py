#!/usr/bin/env python3
# list_lab.py implements the Lesson 3 - List Lab Exercise assignment from UWPCE Python Programming

intro = '''UWPCE Python Programming: Lesson 3 Assignment -- List Lab Exercise
'''
print(intro)

Fruits = ["Apples", "Pears", "Oranges","Peaches"]   # create main list for all exercises

# Series 1
print("Series 1 exercises")
Fruits1 = Fruits[:]                                 # Make copy of main list
print("Fruit list:", Fruits1)                  # display list
fruit = input("Add another fruit: ")                # ask user for another fruit
Fruits1.append(fruit)                                # add user input to end of list
print(fruit,"added at end:", Fruits1)                       # display expanded list
order = input("Enter a number: ")                   # ask user for a number
if 0 < int(order) < len(Fruits1):                        # check if choice is available
    print("The fruit you picked is: ", Fruits1[int(order) - 1])
else:                                               # let user know if out of bounds
    print("No fruit for you!")
fruit = input("Add another fruit: ")                # ask user for anothe fruit
Fruits1 = [str(fruit)] + Fruits1                      # add new fruit to beginning of list using "+"
print(fruit, "added at start:", Fruits1)                       # show newly expanded list
fruit = input("Add another fruit: ")                # ask user for another fruit
Fruits1.insert(0, str(fruit))                        # add new fruit to beginning of list using insert()
print(fruit, "added at start:", Fruits1)                       # show newly expanded list
print("Fruits starting with 'P': ")
for fruit in Fruits1:                                # loop through each fruit in the list
    if fruit[0] == 'P':                             # check each fruit's first letter
        print(fruit, end=" ")                       # show all fruits beginning with "P" using for-loop

# Series 2
print("\n\nSeries 2 exercises")
Fruits2 = Fruits[:]                                 # Make copy of main list
print("Fruit list: ", Fruits2)                    # show list of Fruits
del Fruits2[-1]                                      # remove last fruit
print("Last fruit removed: ", Fruits2)               # show shortened list
fruit = input("Which fruit to delete?: ")           # ask user which fruit to delete
if fruit in Fruits2:                                 # check if in list of Fruits
    Fruits2.remove(fruit)                            # remove if found
    print(fruit, "deleted: ", Fruits2)                # show resulting list
Fruits2 = Fruits2 * 2
print("Bonus: ", Fruits2)
while fruit not in Fruits2:
    fruit = input("Which fruit to delete?: ")
while fruit in Fruits2:
    Fruits2.remove(fruit)
print("All occurences of", fruit,"deleted: ", Fruits2)

# Series 3
print("\n\nSeries 3 exercises")
Fruits3 = Fruits[:]                                 # Make copy of main list
print("Fruit list: ", Fruits3)                      # show list of Fruits
for fruit in Fruits:                                # loop through each fruit on the list
    choice = input("Do you like " + fruit.lower() + "? ") # ask user for preference
    while choice not in ['yes', 'no']:              # check for valid answer
        choice = input("Please answer 'yes' or 'no': ") # keep asking user if not valid answer
    if choice == 'no':                              # if user does not like this fruit
        Fruits3.remove(fruit)                       # remove from the list
print("Preferred fruits: ", Fruits3)                # show list of fruits user likes

# Series 4
print("\n\nSeries 4 exercises")
Fruits4 = Fruits[:]                                 # Make copy of main list
print("Fruit list: ", Fruits4)                      # show list of Fruits
for fruit in Fruits:                                # loop through list
    reversed_fruit = fruit[::-1]                    # reverse name of each fruit
    Fruits4.remove(fruit)                           # remove fruit from list copy
    Fruits4.append(reversed_fruit)                  # add reversed name of fruit to list
print("Reversed fruit names: ", Fruits4)            # show list copy with reversed fruit names
print("Original Fruit list: ", Fruits)            # show initial list of Fruits
del Fruits[-1]                                      # remove last item in list
print("Last fruit deleted: ", Fruits)               # show initial list with last item deleted
print("Fruit list copy: ", Fruits4)                 # show list copy for comparison
