#lesson 03 lists lab

#!/usr/bin/env python3


fruit= ["apples", "pears", "oranges", "peaches"]


#series 1
fruit1 = fruit[:]
print(fruit1)

response = input("Add a new fruit to our list: ")
fruit1.append(response)
print(fruit1)

response = input("Pick a number between 1 and 5: ")
print("You picked " + fruit1[int(response)-1])

response = input("Add another fruit: ")
fruit1 = [response] + fruit1
print(fruit1)

response = input("One more: ")
fruit1.insert(0, response)
print(fruit1)

def startcheck(basket):
    withp = []
    for f in basket:
        if f.startswith("p") or f.startswith("P"):
            withp.append(f)
    return withp
    
print("Fruit starting with P: ", startcheck(fruit1))
print()
print()


#series 2
fruit2 = fruit1[:]
print(fruit2)

print("We have too many kinds of fruit")
fruit2.remove(fruit2[-1])
print(fruit2)

response = input("What other fruit should be removed? ")
fruit2.remove(response)
print(fruit2)

print("Our fruit basket multipled!")
doublefruit2= fruit2*2
print(doublefruit2)

response = input("What else should go? ")
for f in (doublefruit2):
    if f == response:
        doublefruit2.remove(response)
print(doublefruit2)
print()
print()


#series 3
fruit3 = fruit[:]
print(fruit3)
def tastetest(food):
    newfruit3 = []
    for f in food:
        response = input("Do you like " + f + "? ")
        while response not in ("yes", "no"):
            response = input("Please try that again (yes or no): ")
        if response == "yes":
            newfruit3.append(f)
    return newfruit3

print(tastetest(fruit3))
print()
print()


#series 4
fruit4 = fruit1[:]
print("Here is our fruit")
print(fruit4)

fruit4rev = fruit4[:]
def reverse(food):
    rev = []
    for name in food:
        rev.append(name[::-1])
    return rev
        
print("We made a copy basket and reversed it")
print(reverse(fruit4rev))

del fruit4[-1]
print("We removed a fruit from the original basket")
print(fruit4)
print("The copy basket is unchanged")
print(fruit4rev)