#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""
basic ins and outs of list (4 series)
:param a_list_n: list of fruits
:param user_input_n: User input information
:param : i, j, k : fruit in the list
:returns: the nth term in the sequence
"""

print("++++Series 1++++")

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
a_list_1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(a_list_1)

# Ask the user for another fruit and add it to the end of the list
user_input_1 = input("Please add another fruit to the end of the list: ")
a_list_1.append(user_input_1)
print(a_list_1)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
user_input_2 = int(input("Please enter a number that corresponding to the fruit:"))
answer = str(user_input_2) + ": " + a_list_1[user_input_2 - 1]
print(answer)

a_list_1 = ["Banana"] + a_list_1
print(a_list_1)

a_list_1.insert(0, "Melon")
print(a_list_1)

for i in a_list_1:
    if i[0] == 'P':
        print(i)
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
a_list_1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(a_list_1)

print("++++Series 2++++")

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
a_list_2 = ["Apples", "Pears", "Oranges", "Peaches"]
print(a_list_2)

# Remove the last fruit from the list.
del a_list_2[-1:]
print(a_list_2)


# Ask the user for a fruit to delete, find it and delete it
user_input_3 = input("Enter a fruit that you want  to delete:")
a_list_2.remove(user_input_3)
print(a_list_2)

print("++++Series 3++++")

a_list_3 = ["Apples", "Pears", "Oranges", "Peaches"]
for j in a_list_3:
    user_input_4 = None

    while user_input_4 != "y" and user_input_4 != "n":
        user_input_4 = input("Do you like {} ?(y/n)". format(j).lower())
        if user_input_4 == "n":

            a_list_3.remove(j)
print(a_list_3)


print("++++Series 4++++")

# Make a copy of the list and reverse the letters in each fruit in the copy.
a_list_4 = ["Apples", "Pears", "Oranges", "Peaches"]
copy_list = a_list_4
reverse_list = []
for k in copy_list:
    reverse_list.append(k[::-1])
copy_list = reverse_list
# Delete the last item of the original list. Display the original list and the copy.
a_list_4.remove(a_list_4[-1])

print(copy_list)
print(a_list_4)

