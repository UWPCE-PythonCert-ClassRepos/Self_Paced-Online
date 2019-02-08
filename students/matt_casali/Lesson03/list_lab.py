#!/usr/bin/env python3

# Series 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
response = input("What other fruit would you like to add: ")
fruit.append(response)
print(fruit)
response_2 = input("Pick a number between 1 and 5: ")

# Check to make sure number chosen is in range of list
if int(response_2) > 0 and int(response_2) < 6:
    print(fruit[int(response_2) - 1])
else:
    print("You picked a number that was out of range. ")

fruit += ["Watermelon"]
print(fruit)

fruit.insert(0, "Mangos")
print(fruit)

for x in fruit:
    if x.upper().startswith("P"):
        print(x)

# Series 2
print(fruit)
fruit.pop()
print(fruit)
response_3 = input("Choose a fruit from the list to delete: ")

if response_3 in fruit:
    fruit.remove(response_3)
else:
    print("The fruit you have chosen cannot be found in the list. ")

print(fruit)

# Series 3
for x in fruit:
    response_4 = input("Do you like {}?".format(x.lower()))
    while response_4.lower() != "yes" and response_4.lower() != "no":
        response_4 = input("Do you like {}? Please enter 'Yes' or 'No': ".format(x.lower()))
    if response_4.lower() == "no":
        fruit.remove(x)

    print(fruit)

# Series 4
fruit_reversed = []
for x in fruit:
    fruit_reversed.append(x[::-1])

fruit.pop()

print(fruit)
print(fruit_reversed)

