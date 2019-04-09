#! /usr/bin/env python

#Series 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

response = input("New fruit? > ")
fruit.append(response)
print(fruit)

response = int(input("Number between 1 and {} > ".format(len(fruit))))
print("{} : {}".format(response,fruit[response-1]))

fruit = ["Lemon"] + fruit
print(fruit)

fruit.insert(0,"Lime")
print(fruit)

for f in fruit:
    if f[0].upper() == 'P':
        print(f)

#Series 2
print(fruit)
fruit.pop()

print(fruit)
response = input("Delete which fruit? > ")

fruitcopy = fruit[:] * 2
if response in fruit:
    fruit.remove(response)

print(fruit)


print(fruitcopy)
# if response in fruitcopy:
#     for n in range(fruitcopy.count(response)):
#         fruitcopy.remove(response)
while response not in fruitcopy:
    response = input("Delete which fruit? > ")
while response in fruitcopy:
    fruitcopy.remove(response)
print(fruitcopy)

#Series 3
print("\n")
print(fruit)
for f in fruit:
    response = ""
    while response.lower() not in ["yes", "no"]:
        response = input("Do you like {}? > ".format(f.lower()))
        if response.lower() not in ["yes", "no"]:
            print("Please answer yes or no.")
    if response.lower() == "no":
        fruit.remove(f)
print(fruit)

#Series 4
#New list with fruit names reversed.
new_fruit = []
for f in fruit:
    new_fruit.append(f[::-1].capitalize())
fruit.pop()
print(fruit)
print(new_fruit)
