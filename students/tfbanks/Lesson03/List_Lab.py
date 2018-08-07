# List Lab Exercise by tfbanks

#!/usr/bin/env python3

# Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]  # Original List of Fruits

# Welcome to series 1 and tells how many fruits are in the list
print("Welcome to Series 1\nThis list has the following", len(fruits), "fruits: ", fruits, "\n")

new_fruit = input("What one fruit would you like to add to this list? ")  # Asks the user what fruit they want to add
fruits.append(new_fruit.title())  # Appends what the user inputs
print(new_fruit, "was added;  The list now has the following", len(fruits), "fruits: ", fruits, "\n")  # Tells how many fruits are in the list

num_value = int(input("Please enter a number between 1 and " + str(len(fruits)) + ": "))  # Asks for a number between 1 and the number of fruit on the list
select_num = int(num_value - 1)  # Corrects the number to Python "number"
print(fruits[select_num], "is number", num_value, "in the list of fruits\n")  # Tells what fruit and what number it is on the list

new_fruit2 = input("Name one more fruit to add to the list ")  # Asks for another fruit to add to the list
fruits = [new_fruit2.title()] + fruits

print(new_fruit2, "was added;  The list now has the following", len(fruits), "fruits: ", fruits, "\n")  # Tells how many fruits are in the list

new_fruit3 = input("Name one last fruit to add to the list ")  # Asks for one more fruit to add to the list
fruits.insert(0, new_fruit3.title())

print(new_fruit3, "was added;  The list now has the following", len(fruits), "fruits: ", fruits, "\n")  # Tells how many fruits are on the list

p_start_fruits = []
for fruit in fruits:
    if fruit[0] == 'P':
        p_start_fruits.append(fruit)
print("FYI: all the fruits that start with P are: ", p_start_fruits, "\n")
s1_fruits = fruits[:]

# Transition between Series 1 and Series 2 Exercises
continue_s2 = input("This ends Series 1, Would you like to continue to Series 2? Please enter Y/N ")
if continue_s2.title() == "Y":
    pass
else:
    print("Thank You, Have a nice day")
    exit()

# Series 2
print("\n")  # Adds some space before the next block
s2_fruits = s1_fruits[:]  # Copies the last iteration of Series 1 fruits to Series 2 list
print("Welcome to Series 2\nThe fruit list currently has the following", len(s2_fruits), "fruits: ", fruits, "\n")  # Tells how many fruits are on the list

last_fruit = s2_fruits[-1]  # Selects the last fruit on the list
s2_fruits.remove(last_fruit)  # Removed the last fruit on the list

print(last_fruit, "Was removed;  The fruit list now has the following", len(s2_fruits), "fruits: ", s2_fruits, "\n")  # Tells how many fruits are on the list

del_fruit = input("What other fruit would you like to remove from the list above? ")  # Asks what fruit to delete
s2_fruits.remove(del_fruit.title())  # Deletes the fruit that the user inputs

print(del_fruit, "Was removed; The fruit list now has the following", len(s2_fruits), "fruits: ", s2_fruits, "\n")  # Tells how many fruits are on the list

# Transition between Series 2 and Series 3 Exercises
continue_s3 = input("This ends Series 2, Would you like to continue to Series 3? Please enter Y/N ")
if continue_s3.title() == "Y":
    pass
else:
    print("Thank You, Have a nice day")
    exit()

# Series 3
print("\n")  # Adds some space before the next block
s3_fruits = s1_fruits[:]  # Copies the list of fruits from above
print("Welcome to Series 3\n")

no_no_fruit = []
for fruit in s3_fruits:
    answer = input(f"Do you like {fruit.lower()}? Please enter Yes/No ")
    while answer.lower() != "yes" and answer.lower() != "no":
        answer = input(f"Do you like {fruit.lower()}? Please enter Yes/No ")
    if answer.lower() == "no":
        no_no_fruit = no_no_fruit + [fruit.title()]

for fruits in no_no_fruit:
    s3_fruits.remove(fruits)

print("You like the following fruits: ", s3_fruits)

# Series 4
print("\n")  # Adds some space before the next block
s4_fruits = s1_fruits[:]  # Copies the last iteration of Series 1 fruits to Series 4 list
print("Welcome to Series 4\n")

fruit_backwards = []  # creates an empty list for writing fruit backwards
for fruit in s4_fruits:
    ind_backward_fruit = fruit[::-1]  # writes each fruit backwards
    fruit_backwards = fruit_backwards + [ind_backward_fruit]  # combines each fruit in the new list

del fruit_backwards[-1:]  # removes the last fruit from the list

print("The original fruit list at the end of Series 1 contained: ", s4_fruits, "\n")  # prints the original fruit
print("Here is the list with all fruit written backwards and the last item removed: ", fruit_backwards, "\n")  # prints new list

close_statement = input("Press Any key to exit")
