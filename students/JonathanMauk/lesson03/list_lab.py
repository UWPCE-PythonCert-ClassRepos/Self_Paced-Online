# Series 1
print("---------- SERIES 1 ----------")

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

print("Fruit list: ")
print(fruits)

fruits += [input("Please add a fruit: ")]

print("Fruit list: ")
print(fruits)

fruitdex = input("Enter a fruitdex number: ")
print("#" + fruitdex + ": " + fruits[int(fruitdex) - 1])

print("Adding 'pineapples' to list...")
fruits = ["Pineapples"] + fruits
print(fruits)

print("Adding 'kiwis' to list...")
fruits.insert(0, "Kiwis")
print(fruits)

print("Displaying all fruits that start with 'p'...")

for fruit in fruits:
    if fruit[0] == "p" or fruit[0] == "P":
        print(fruit)

# Series 2
print("---------- SERIES 2 ----------")

print("Showing current list: ")
print(fruits)

print("Removing last item from list: ")
fruits = fruits[:-1]
print(fruits)

delete_fruit = input("Please enter a fruit to delete: ")
fruits.remove(delete_fruit)
print("Series 2 list status: ")
print(fruits)

# # Series 3
print("---------- SERIES 3 ----------")

new_fruits = fruits[:]


def fruit_liker():
    for fruit in fruits:
        fruit_like = input("Do you like " + fruit.lower() + "? ")
        if fruit_like.lower() == "no" or fruit_like.lower() == "n":
            print("Deleting " + fruit.lower() + ".")
            new_fruits.remove(fruit)
        elif fruit_like.lower() == "yes" or fruit_like.lower() == "y":
            continue
        else:
            print("Please enter 'yes/y' or 'no/n' only. Restarting...")
            fruit_liker()

fruit_liker()
print("Current list status: ")
fruits = new_fruits[:]
print(fruits)

# Series 4
print("---------- SERIES 4 ----------")

print("Reversing letters in each fruit...")
reverse_fruits = []
for fruit in fruits:
    reverse_fruits.append(fruit[::-1])
print(reverse_fruits)

print("Removing last fruit from original list...")
fruits.pop()

print("Original list status:")
print(fruits)

print("Reversed list status:")
print(reverse_fruits)
