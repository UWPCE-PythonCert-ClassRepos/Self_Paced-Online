"""Series 1
    - Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    - Display the list (plain old print() is fine…).
    - Ask the user for another fruit and add it to the end of the list.
    - Display the list.
    - Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    - Add another fruit to the beginning of the list using “+” and display the list.
    - Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""
print("Series 1...")
fruits = ['Apples','Pears','Oranges','Peaches']

for item in fruits:
    print(item)
    
question = input("Please enter the name of a fruit: ")
fruits.append(question)
print(fruits)

number = int(input("Please enter a number: "))
print('')
print(fruits[number])
print('')

new_fruit = ['Nectarine']
new_list = new_fruit + fruits
print(new_list)
print('')

new_list.insert(0,'banana')
print(new_list)
print('')

for item in new_list:
    if item[0] == "P":
        print(item)



"""Series 2
Using the list created in series 1 above:

    - Display the list.
    - Remove the last fruit from the list.
    - Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""
print("Series 2...")
print(new_list)
print('')

revised_list = new_list[:-1]
print(revised_list)
print('')

deletion = input("Please name a fruit to delete: ")
for item in revised_list:
    if item == deletion:
        revised_list.remove(item)
print(revised_list)


"""Series 3
Again, using the list from series 1:

    - Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    - For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    - Display the list.

"""
print("Series 3...")
fruits = ['Apples','Pears','Oranges','Peaches']
for item in fruits:
    while True:
        answer = input("Do you like " + item + "?")
        if answer in ("yes", "no"):
                break
    if answer == "no":
        fruits.remove(item)
print(fruits)

"""Series 4
Once more, using the list from series 1:
    Make a copy of the list and reverse the letters in each fruit in the copy.
    Delete the last item of the original list. Display the original list and the copy.
"""

print("Series 4...")

fruits = ['Apples','Pears','Oranges','Peaches']

fruit_copy = []

for item in fruits:
    fruit_copy.append(item)


for item in temp:
    return item[::-1]
    print(item)


#for item in fruit_copy:
 #   new_item = item[::-1]

#fruit_copy.append(new_item)
    
print(fruits)
print(fruit_copy)
print(temp)
