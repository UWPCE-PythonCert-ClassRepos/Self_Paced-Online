"""
Goal: Learn the basic ins and outs of Python lists.

Series 1: DONE
DONE-Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
DONE-Display the list (plain old print() is fine…).
DONE-Ask the user for another fruit and add it to the end of the list.
DONE-Display the list.
DONE-Ask the user for a number and display the number back to the user and the 
fruit corresponding to that number (on a 1-is-first basis). 
Remember that Python uses zero-based indexing, so you will need to correct.
DONE-Add another fruit to the beginning of the list using “+” and display the 
list.
DONE-Add another fruit to the beginning of the list using insert() and display 
the list.
DONE-Display all the fruits that begin with “P”, using a for loop.

Series 2: DONE
Using the list created in series 1 above:

DONE-Display the list.
DONE-Remove the last fruit from the list.
DONE-Display the list.
DONE-Ask the user for a fruit to delete, find it and delete it.
INCOMPLETE-(Bonus: Multiply the list times two. Keep asking until a match is 
found. Once found, delete all occurrences.)

Series 3:
Again, using the list from series 1:

-Ask the user for input displaying a line like “Do you like apples?” for each 
fruit in the list (making the fruit all lowercase).
DONE-For each “no”, delete that fruit from the list.
-For any answer that is not “yes” or “no”, prompt the user to answer with one 
of those two values (a while loop is good here)
DONE-Display the list.

Series 4:
Once more, using the list from series 1:

-Make a new list with the contents of the original, but with all the letters 
in each item reversed.
-Delete the last item of the original list. Display the original list and the 
copy.
"""

#Series 1
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

fruit = str(input("Enter the fruit to add to the list: ")) #Ask user to add fruit to list
list1.append(fruit) #Add fruit to end of list
print(list1) #Display list 

num = int(input("Enter the number to choose the fruit from the list: ")) #Ask user to choose number for fruit
num -= 1 #Using -1 since items in list is chosen from index of 0
if num < 0 : 
    print("Please enter a number of 1 or above.") #User can't choose 0 as an option
else:
    print(list1[num]) #Display list
    
list2 = ["Pineapple"] #Creating a new list to add item to existing list
list1 = list2 + list1 #Adding item to the beginning of the list
print(list1) #Display list

list1.insert(0, "Watermelon") #Using insert to add item to beginning of list
list1 #Display list

for fruit in list1: #For every fruit in the list
    if fruit.startswith("P"): #If statement looks for fruits that start with P
        print(fruit) #Prints the fruit from the list
        
#Series 2
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

list1.pop() #removes last item in list
print(list1)

answer = str(input("Enter the name of the fruit to delete: "))
if answer == "Apples":
    list1.remove("Apples")
elif answer == "Pears":
    list1.remove("Pears")
elif answer == "Oranges":
    list1.remove("Oranges")
elif answer == "Peaches":
    list1.remove("Peaches")
else:
    print("Please choose a fruit to delete that is within the list.")
print(list1)

#Series 3
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

while True:
    answer = str(input("Do you like apples? "))
    if answer == "no":
        list1.remove("Apples")
        print(list1)

    answer = str(input("Do you like pears? "))
    if answer == "no":
        list1.remove("Pears")
        print(list1)

    answer = str(input("Do you like oranges? "))
    if answer == "no":
        list1.remove("Oranges")
        print(list1)

    answer = str(input("Do you like peaches? "))
    if answer == "no":
        list1.remove("Peaches")
        print(list1)
    else:
        print("Please answer between yes or no.")
        
#Series 4
list1 = ["Apples", "Pears", "Oranges", "Peaches"] #Create a list
print(list1) #Display list

reverse = (list1[0][::-1], list1[1][::-1], list1[2][::-1], list1[3][::-1])
print(reverse)

