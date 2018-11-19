"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    November 13th 2018
"""
#!/usr/bin/env python3

#print("Starting Series 1:")# -> Used during coding/testing
fruits = ["Apples", "Pears", "Oranges", "Peaches"] #New List
print(fruits)
#Ask the user to provide a fruit and place it at the end of the list.
new_fruit = input("What fruit would you like to add to the list? > ")
fruits.append(new_fruit)
print(fruits)
number_choice = input("Give me a number? (1-5) > ") #Which index (fruit) removed.
fruit_index = int(number_choice) - 1 #Account for zero indexing.
fruit_choice = fruits[fruit_index]
#Display the number chosen and fruit located at the index
print("Your number and fruit was: " + number_choice + ', ' + fruit_choice)

#print("Starting Series 2:")# -> Used during coding/testing
fruits = ["Apples", "Pears", "Oranges", "Peaches"] #New List
print(fruits)
new_fruits = fruits[:-1] #Remove the last fruit (element)
new_fruits *= 2 #Multiply the list times two
print(new_fruits)
#Ask the user which fruit should be removed.
remove_fruit = input("Which fruit do you want to delete? (type the name) > ")
#If the fruit named does not match exactly -> keep asking.
while remove_fruit not in new_fruits:
    remove_fruit = input("Choose a fruit from the list? (check spelling) > ")
#Remove all occurences - loop ends when complete.
while remove_fruit in new_fruits:
    new_fruits.remove(remove_fruit)
print(new_fruits)

#print("Starting Series 3:") # -> Used during coding/testing
fruits = ["Apples", "Pears", "Oranges", "Peaches"] #New List
item = 0 #Counter used to go through list while manipulating.
while item < len(fruits):
    like = input("Do you like " + fruits[item].lower() + "? > ")
    while like.lower() != "yes" and like.lower() != "no": #Yes or No is needed - loop
        like = input("Do you like " + fruits[item].lower() + "? (yes or no) > ")
    if like.lower() == "no": #If no then remove the item and continue
        fruits.remove(fruits[item])
    else:
        item += 1 #If yes then increment and check the next index
print("The list of fruits you like is: " + str(fruits))

#print("Starting Series 4:")# -> Used during coding/testing
fruits = ["Apples", "Pears", "Oranges", "Peaches"] #New List
copy_of_fruits = fruits[:] #Copy used to not impact original
reversed_copy = [] #Empty list for the reversed strings
item = 0 #Counter to go through the list and manipulate
while item < len(copy_of_fruits):
    temp = copy_of_fruits[item] #Grab the item at current index
    reversed_copy.append(temp[::-1]) #Reverse the characters - put into new list
    item += 1 #Increment to go to the next index
last_removed = fruits[:-1] #Display copy without the last element.
print("The original list with the last removed: " + str(last_removed))
print("The list with letters of fruits reversed: " + str(reversed_copy))