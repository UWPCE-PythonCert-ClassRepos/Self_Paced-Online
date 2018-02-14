#!/usr/bin/env python3

# Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit_list)

new_fruit = input("Please input a fruit to add to the list. ")

fruit_list.append(new_fruit.capitalize())

print(fruit_list)

boolInput_Check = False
while boolInput_Check == False:

    try:
        user_number = int(input("Please input a number: "))
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

new_fruit_list = []
new_fruit2 = str(input("Please input a second fruit to the list. "))

new_fruit_list.append(new_fruit2.capitalize())

fruit_list2 = new_fruit_list + fruit_list

print(fruit_list2)

new_fruit3 = str(input("Please input a third fruit to the list. "))

fruit_list2.insert(0,new_fruit3.capitalize())

print(fruit_list2)

for x in fruit_list2:
    for y in x:
        if y[0] == "P":
            print(x)

# Series 2
print(fruit_list2)

fruit_list2.pop(-1)

print(fruit_list2)





