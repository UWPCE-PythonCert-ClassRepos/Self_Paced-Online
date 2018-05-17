#!/usr/bin/env python3

#Series 1

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

#Ask another fruit to user
answer_fruit = input("Enter the name of another fruit: ")
fruits.append(answer_fruit)
print(fruits)

#Ask fruit index
index_fruit = int(input("Enter the number of a fruit: "))
print("Your fruit number: {} corresponds to {}".format(index_fruit, fruits[index_fruit - 1]))

#Ask user for another fruit with +
answer_fruit2 = input("Enter the name of another fruit to add: ")
fruits = [answer_fruit2] + fruits
print(fruits)

#Ask user for another fruit with insert
answer_fruit3 = input("Enter the name of another fruit to add: ")
fruits.insert(0, answer_fruit3)
print(fruits)

#Display all the fruits that begin with “P”, using a for loop.
print("Displaying all fruits that begin with the letter 'P'")
for fruit in fruits:
    if fruit[0] == "P":
      print(fruit)

#Series 2

#Display list
print("List for start of series 2")
print(fruits)

#Remove the last fruit from the list.
print("Removing the last fruit")
fruits.pop(len(fruits)-1)
print(fruits)


#Ask the user for a fruit to delete, find it and delete it.
#(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits_double = fruits + fruits
print(fruits_double)
answer_fruit4 = input("Enter the name of a fruit to delete: ")

for fruit in fruits_double:
    if fruit == answer_fruit4:
        fruits_double.remove(fruit)
print("{} are left in your list".format(fruits_double))


#Series 3
#Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
#For each “no”, delete that fruit from the list.
#For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
#Display the list.

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
list_fruits = fruits[:]
for fruit in fruits:
    answer_fruit5 = input("Do you like {}?\n".format(fruit))
    while answer_fruit5.lower() != 'yes' and answer_fruit5.lower() != 'no':
        answer_fruit5 = input("Please answer Yes or No.\n")
    if answer_fruit5.lower() == 'no':
        list_fruits.remove(fruit)
print("The fruits you like are {}".format(list_fruits))

#Series 4

#Make a copy of the list and reverse the letters in each fruit in the copy.
#Delete the last item of the original list. Display the original list and the copy.

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
list_fruits1 = fruits[:]
for a in range(len(list_fruits1)):
    list_fruits1[a] = list_fruits1[a][-1::-1]
fruits.pop()
print(list_fruits1)
print(fruits)

