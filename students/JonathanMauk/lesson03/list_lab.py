# Series 1

fruits = ["apples", "pears", "oranges", "peaches"]

print("Fruit list: ")
print(fruits)

fruits += [input("Please add a fruit: ")]

print("Fruit list: ")
print(fruits)

fruitdex = input("Enter a fruitdex number: ")

print("#" + fruitdex + ": " + fruits[int(fruitdex) - 1])

print("Adding 'pineapples' to list...")
fruits = ["pineapples"] + fruits
print(fruits)

print("Adding 'kiwis' to list...")
fruits.insert(0, "kiwis")
print(fruits)

print("Displaying all fruits that start with 'p'...")

for fruit in fruits:
    if fruit[0] == ("p" or "P"):
        print(fruit)

# Series 2

print("Showing current list: ")
print(fruits)

print("Removing last item from list: ")
fruits = fruits[:-1]
print(fruits)

delete_fruit = input("Please enter a fruit to delete: ")
fruits.remove(delete_fruit)
print("Current list status: ")
print(fruits)
