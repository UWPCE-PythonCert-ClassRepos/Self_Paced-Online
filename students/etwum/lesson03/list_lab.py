#!/usr/bin/env python3

# Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit_list)

new_fruit = input("Please input a fruit to add to the list. ")

fruit_list.append(new_fruit.capitalize())

print(fruit_list)
print("----------------------------------------------------------------" + "\n")
boolInput_Check = False
while boolInput_Check == False:

    try:
        user_number = int(input("Please input a number to display a fruit: "))
        if user_number > len(fruit_list):
            raise Exception

    except ValueError as x:
        print("Please input a whole number")
        print(x)

    except Exception:
        print("The number you entered is too high")

    else:
        boolInput_Check = True

x = user_number - 1
print("Here is your fruit selection: %d." % user_number, fruit_list[x])
print("----------------------------------------------------------------" + "\n")

new_fruit_list = []
new_fruit2 = str(input("Please input a second fruit to add to the beginning of the list. "))

new_fruit_list.append(new_fruit2.capitalize())

fruit_list2 = new_fruit_list + fruit_list

print(fruit_list2)
print("----------------------------------------------------------------" + "\n")

new_fruit3 = input("Please input a third fruit to add to the beginning of the list. ")

fruit_list2.insert(0, new_fruit3.capitalize())

print(fruit_list2)
print("----------------------------------------------------------------" + "\n")


print("Here are the fruits from the list which begin with a P:")
for x in fruit_list2:
    for y in x:
        if y[0] == "P":

            print(x)
print("----------------------------------------------------------------" + "\n")

# Series 2
print(fruit_list)
print("Removing the last item from the list")
fruit_list.pop(-1)

print(fruit_list)
print("----------------------------------------------------------------" + "\n")


boolDelete = False
while boolDelete == False:
    delete_fruit = input("What fruit would you like to delete from the list? ")

    for x in fruit_list:
        if x == delete_fruit.capitalize():
            fruit_list.remove(delete_fruit.capitalize())
            print("Fruit deleted from list!")
            print(fruit_list)
            boolDelete = True
            print("----------------------------------------------------------------" + "\n")

    if boolDelete == False:
        print("Fruit not found in list")


# Series 3

boolValidInput = False
answer = " "
removal_list = []
list_index = 0


while list_index != 2:

    for x in fruit_list:
        try:
            answer = input("Do you like %s?" % x.lower())
            if answer == "yes":
                print("Glad you like %s" % x)
            elif answer == "no":
                removal_list.append(x)
            else:
                raise Exception
        except Exception:
            print("Please input yes or no")
    list_index = fruit_list.index(x)
    print(list_index)

for x in removal_list:
    fruit_list.remove(x)

print(fruit_list)
print("----------------------------------------------------------------" + "\n")


# Series 4

copy_fruit_list = []

for x in fruit_list:
    y = x[::-1]
    copy_fruit_list.append(y)

print(copy_fruit_list)
print(fruit_list)














