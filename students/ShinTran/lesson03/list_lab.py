'''
Shin Tran
Python 210
Lesson 3 Assignment
'''

# !/usr/bin/env python3
# python list_lab.py


'''
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
'''
series1 = ["Apples","Pears","Oranges","Peaches"]
print(series1)
response = int(input("Type a number to return the index of the list > "))
print(series1[response-1])
series1 = ["Strawberries"] + series1
print(series1)
series1.insert(0,"Blueberries")
print(series1)
for fruit in series1:
    if (fruit[0] == "P"):
        print(fruit)
print()

'''
Using the list created in series 1 above:
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
'''
series2 = series1[:]
print(series2)
series2 = series2[:-1]
print(series2)
series2 = series1 * 2
print(series2)
response2 = ''
new_series2 = series2[:]
while (response2 not in series2):
    response2 = input("Type a fruit to remove from the list > ")
    new_series2[:] = (value for value in new_series2 if value != response2)
print(new_series2)
print()

'''
Again, using the list from series 1:
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
'''
series3 = series1[:]
new_series3 = series3[:]
for fruit in series3:
    response3 = input("Do you like {} (yes/no)? ".format(fruit))
    while (response3 not in ["yes","no"]):
        response3 = input("Do you like {} (yes/no)? ".format(fruit))
    if response3 == "no":
        new_series3.remove(fruit)
print(new_series3)
print()

'''
Once more, using the list from series 1:
Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
'''
series4 = series1[:]
new_series4 = []
for fruit in series4:
    new_series4.append(fruit[::-1])
series4.pop()
print(series4)
print(new_series4)



