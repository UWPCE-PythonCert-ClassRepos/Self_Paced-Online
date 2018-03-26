#!/usr/bin/env python3

# Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit_list)

new_fruit = input("Please input a fruit to add to the list. ")

# adding a new fruit to the end of the fruit_list
fruit_list.append(new_fruit.capitalize())

print(fruit_list)
print("----------------------------------------------------------------" + "\n")

# boolean to stop or continue the while loop
user_number = None
boolInput_Check = False
while boolInput_Check == False:
    # loops until the user inputs a valid number which is less than or equal length of the fruit list
    try:
        # get user input in order to display a fruit
        user_number = int(input("Please input a number to display a fruit: "))
        if user_number > len(fruit_list):
            raise Exception
    # exception raised if the value entered isnt a whole number
    except ValueError as x:
        print("Please input a whole number")
        print(x)
    # exception raised if number is greater than the list length
    except Exception:
        print("The number you entered is too high")

    else:
        boolInput_Check = True

# takes the user input and substracts by 1 in order to deal with the issue of python starting a list at zero
x = user_number - 1
print("Here is your fruit selection: %d." % user_number, fruit_list[x])
print("----------------------------------------------------------------" + "\n")

# add a fruit to the beginning of fruit list by using +
new_fruit_list = []
new_fruit2 = str(input("Please input a second fruit to add to the beginning of the list. "))

new_fruit_list.append(new_fruit2.capitalize())

fruit_list2 = new_fruit_list + fruit_list

print(fruit_list2)
print("----------------------------------------------------------------" + "\n")

# add a fruit to the beginning of fruit list by using insert
new_fruit3 = input("Please input a third fruit to add to the beginning of the list. ")

fruit_list2.insert(0, new_fruit3.capitalize())

print(fruit_list2)
print("----------------------------------------------------------------" + "\n")


print("Here are the fruits from the list which begin with a P:")
# takes each fruit from the list beginning with P and displays it
for x in fruit_list2:
    for y in x:
        if y[0] == "P":

            print(x)
print("----------------------------------------------------------------" + "\n")

# Series 2
print(fruit_list)
print("Removing the last item from the list")
# remove last item from the fruit list
fruit_list.pop(-1)

print(fruit_list)
print("----------------------------------------------------------------" + "\n")

# boolean used in the while loop to determine whether or not an item was deleted from the fruit list
boolDelete = False
#
while boolDelete == False:
    # get user input for deleting an item in the fruit list
    delete_fruit = input("What fruit would you like to delete from the list? ")

    for x in fruit_list:
        # if the user input fruit is in teh lst them it gets deleted
        if x == delete_fruit.capitalize():
            fruit_list.remove(delete_fruit.capitalize())
            print("Fruit deleted from list!")
            print(fruit_list)
            boolDelete = True
            print("----------------------------------------------------------------" + "\n")

    # if the user input item wasnt found in the list then the print statement is executed
    if boolDelete == False:
        print("Fruit not found in list")


# Series 3

#default values
answer = " "
removal_list = []
list_index = 0


while list_index != 2:
    # while loop continues until the list reaches index 2 from the fruit list
    # uses the modified fruit list from Series 2
    for x in fruit_list:
        # user whether or not he or she likes a fruit from the list
        # user must input yes or no; exception raised if the input isn't yes or no
        try:
            answer = input("Do you like %s?" % x.lower())
            if answer == "yes":
                print("Glad you like %s" % x)
            elif answer == "no":
                # creates a removal list used later to remove items the user doesnt like
                removal_list.append(x)
            else:
                raise Exception
        except Exception:
            print("Please input yes or no")
    list_index = fruit_list.index(x)
    print(list_index)

# uses the removal list to remove items from the original list the user doesnt like
for x in removal_list:
    fruit_list.remove(x)

print(fruit_list)
print("----------------------------------------------------------------" + "\n")


# Series 4

copy_fruit_list = []

# creates a copy of the fruit list from series 3 then puts letters of the fruits in reverse
for x in fruit_list:
    y = x[::-1]
    copy_fruit_list.append(y)

print(copy_fruit_list)
print(fruit_list)














