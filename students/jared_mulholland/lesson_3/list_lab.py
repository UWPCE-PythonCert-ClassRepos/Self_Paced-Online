"""Series 1


*Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
*Display the list (plain old print() is fine…). --
*Ask the user for another fruit and add it to the end of the list. --
    *Display the list. -- 
*Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).  --
    Remember that Python uses zero-based indexing, so you will need to correct.
*Add another fruit to the beginning of the list using “+” and display the list. --
*Add another fruit to the beginning of the list using insert() and display the list. --
*Display all the fruits that begin with “P”, using a for loop. -- 
"""

#!/usr/bin/env python3

fruit = ["apples","pears","oranges","peaches"]

#1
print(fruit)

#2
another_fruit = input("add another fruit to your list! > ")

fruit.append(str(another_fruit))

print(fruit)

#3

fruit_number = input("\nwhich number fruit do you want? > ")
fruit_number = int(fruit_number)

while fruit_number > len(fruit):
    print("\nYou don't have that much fruit")  
    fruit_number = input("\nenter a number of fruit that you actually have > ")
    fruit_number = int(fruit_number)
else:
    print(fruit[fruit_number-1])

#4

more_fruit = input("\nadd another fruit to your list > ")

more_fruit = [more_fruit]

fruit = fruit + more_fruit

print(fruit)

#5
print("\n")
for item in fruit:
    if item[0].lower() == "p":
        print(item, end = ' ')
    

"""Series 2

Using the list created in series 1 above:

--Display the list.
--Remove the last fruit from the list.
--Display the list.
--Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""

print("\nSeries 2")

#1
print("\n")
print(fruit)

#2

fruit = fruit[:-1]
print("\n")
print(fruit)

#3

remove_fruit = input("\nremove a fruit from your basket > ")

str(remove_fruit)

while not remove_fruit in fruit:
    remove_fruit = input("\nyou don't have that fruit in your basket. Pick another fruit > ")
    remove_fruit = str(remove_fruit)
else:
    index = fruit.index(remove_fruit)
    del fruit[index]
    print(fruit)

"""
Series 3

Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.

"""

print("\nSeries 3")

fruit = ["apples","oranges","Pear","peaches","lemon"]

print("\n")
print(fruit)

for item in fruit:
    answer = input("\ndo you like " + item.lower() + " > ")
    answer = str(answer)
    while answer not in ["yes","no"]:
        answer = input("\nthis is a yes/no question. Do you like " + item.lower() + " > ")
        answer = str(answer)
    else:
        if answer.lower() == "no":
            fruit.remove(item)
            print("remaining fruit: ") 
            print(fruit)
        else:
            print("remaining fruit: ") 
            print(fruit)


"""
Series 4 

Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
"""

fruit = ["apples","pears","oranges","peaches"]

fruit_r = fruit[:]

fruit_r = [item[::-1] for item in fruit_r]

fruit.pop(3)

print("\nComparing fruit list to copied fruit list:\n")
print(fruit)
print("\n")
print(fruit_r)
