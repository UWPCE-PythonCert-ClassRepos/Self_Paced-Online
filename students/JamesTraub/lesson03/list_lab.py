#!/usr/bin/env python3

# Lesson 3 - Series 1

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Create and display a list of fruit.")
print(fruit)
print()

inp_fruit = input('Please enter a name of a fruit to add to the end of list. ')
fruit.append(inp_fruit)
print(fruit)
print()

fruit_number = int(input('Please enter the number that correspends with one fruit in the list. '))
for i, nfruit in enumerate(fruit):
    if fruit_number == (i + 1):
        print(fruit_number, nfruit)
print()

add_fruit2 = []
inp_fruit2 = input('Please enter a fruit to add to the beginning of the list. ')
fruit = [inp_fruit2,] + fruit
print(fruit)
print()

add_fruit3 = []
add_fruit = input('Please enter a fruit to add to the beginning of the list. ')
add_fruit3.insert(0, add_fruit)
fruit = add_fruit3 + fruit
print(fruit)
print()

first_letter = [i[0] for i in fruit]
for x in first_letter:
    if x.title() == "P":
        print(x, end=' ')
print()


# Lesson 3 - Series 2
print(fruit)
print()

fruit.pop()
print(fruit)
print()

del_fruit = input('Please enter the name of a fruit in the list to delete. ')
if del_fruit in fruit:
    fruit.remove(del_fruit)
print(fruit)
print()


# Lesson 3 - Series 3
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
print()


# Lesson 3 - Series 4
new_fruit = fruit.copy()
reversed_list = []
for tree in new_fruit:
    new_tree = tree[::-1]
    reversed_list.append(new_tree)
fruit.pop()
print(fruit)
print(reversed_list)
