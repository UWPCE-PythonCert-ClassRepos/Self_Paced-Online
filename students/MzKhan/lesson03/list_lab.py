'''
    Name: Muhammad Khan
    Date: 02/28/2019
    Assignment03

'''
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit_list_1 = ["Apples","Pears","Oranges","Peaches"]
# Create a shallow copy of list 1.
# Note: because list is a mutable object, we need to create a shallow copy to
# work with.
fruit_list_2 = fruit_list_1[:]
# Create a shallow copy using the copy method.
fruit_list_3 = fruit_list_1.copy()
fruit_list_4 = fruit_list_1.copy()


def display(seq):
    # This method prints the list using the string formatting.
    print("\nThe Fruit list contains the following fruits: \n{}\n".format(seq))

print("Series: 1")
# Series 1.

# Display the list.
display(fruit_list_1)
# Ask the user for another fruit
new_fruit = input("What fruit would you like to add in the list? ")
# Add it to the end of the list.
fruit_list_1.append(new_fruit.capitalize())
# Display the list.
display(fruit_list_1)
# Ask the user for the number.
num = input("Please provide the number for the fruit you want: ")
num = int(num)
# Display the number and the corresponding fruit to the user.
print(num, fruit_list_1[num-1])
# Add another fruit to the beginning of the list using “+” and display the list.
new_fruit = input("What fruit would you like to add in the list? ")
fruit_list_1 =[new_fruit.capitalize()]+fruit_list_1
display(fruit_list_1)
# Add another fruit_list_1 to the beginning of the list using insert() and
# display the list.
new_fruit = input("What fruit would you like to add in the list? ")
fruit_list_1.insert(0,new_fruit.capitalize())
display(fruit_list_1)
# Display all the fruits that begin with “P”, using a for loop
print("The fruits that start with 'P'")
for fruit in fruit_list_1:
    if fruit.startswith("P"):
        print(fruit)

print("\nSeries: 2")
# Series 2.

# Display the list.
display(fruit_list_2)
print("Removing the last item from the list...")
# Remove the last fruit from the list.
fruit_list_2.pop()
# Display the list.
display(fruit_list_2)
# Ask the user for a fruit to delete, find it and delete it
fruit = input("Which fruit would you like to delete from the list? ")
fruit_list_2.remove(fruit.capitalize())
display(fruit_list_2)
# (Bonus: Multiply the list times two. Keep asking until a match is found.
# Once found, delete all occurrences.)
print("bonus: ")
fruit_list_2 *=2
display(fruit_list_2)
fruit = input("Which fruit would you like to delete from the list? ")
fruit = fruit.capitalize()
count = fruit_list_2.count(fruit)
if ( count > 0):
    print(f"Removing all the occurances of {fruit.upper()}  from the list ...")
    for i in range(count):
        fruit_list_2.remove(fruit)
display(fruit_list_2)

print("Series: 3")
# Series 3

# index initialized--starting from 0.
index = 0
# User a shallow copy of fruit_list_3 in the loop BECAUSE list are mutable.
# fruit_list_3[:] is a shallow copy.
fruit_list_3_copy = fruit_list_3[:]
while ( index < len(fruit_list_3_copy )):
    reponse = input("Do you like {}? yes/no: "
                    .format(fruit_list_3_copy[index].lower()))
    reponse = reponse.lower()
    if reponse not in ["yes","no"]:
        continue
    if reponse == "no":
        fruit_list_3.remove(fruit_list_3_copy[index])
    index+=1

else:
    display(fruit_list_3)

print("Series: 4\n")
# series 4
original_list = fruit_list_4[:]
for index, item in enumerate(original_list):
    # Reverse the letters of the item located at the index.
    fruit_list_4[index] = item[::-1].lower()
original_list.pop()
print("Original List with last item removed:")
print(original_list)
print("copied list with reversed letters for each item: ")
print(fruit_list_4)

# Note: When we create the shallow copy, the pop operation (or any operation)
#in the original list doesn't have any affect on the shallow copy.












