#!/usr/bin/env python3

# Series 1

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
add_fruit = input('Please enter the name of a fruit to add to the end of list. ')
fruit.append(add_fruit)
print(fruit)


fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit_number = int(input('Please enter the number that correspends with one fruit in the list. '))
for i, numfruit in enumerate(fruit):
    if fruit_number == (i + 1):
        print(fruit_number, numfruit)


fruit = ["Apples", "Pears", "Oranges", "Peaches"]
add_fruit = []
beg_fruit = input('Please enter a fruit to add to the beginning of the list. ')
add_fruit.insert(0, beg_fruit)
new_list = add_fruit + fruit
print(new_list)


fruit = ["Apples", "Pears", "Oranges", "Peaches"]
add_fruit = input('Please enter a fruit to add to the beginning of the list. ')
fruit.insert(0, add_fruit)
print(fruit)


fruit = ["Apples", "Pears", "Oranges", "Peaches"]
first_letter = [i[0] for i in fruit]
for x in first_letter:
    if x.title() == "P":
        print(x, end=' ')
print()


# Series 2
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

fruit.pop()
print(fruit)

del_fruit = input('Enter the name of a fruit to delete. ')
if del_fruit in fruit:
    fruit.remove(del_fruit)
print(fruit)


# Series 3
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

copy_fruit = fruit[:]
for i in fruit:
    prompt_y_n = input("Do you like {}? ".format(i))
    prompt_y_n = prompt_y_n.lower()
    while prompt_y_n != "yes" and prompt_y_n != "no":
        prompt_y_n = input('Please enter yes or no. ')
        prompt_y_n = prompt_y_n.lower()
    if prompt_y_n == "no":
        copy_fruit.remove(i)
print(copy_fruit)
print(fruit)


# Series 4
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

new_fruit = fruit.copy()
reversed_list = []
for tree in new_fruit:
    new_tree = tree[::-1]
    reversed_list.append(new_tree)
fruit.pop()
print(fruit)
print(reversed_list)
