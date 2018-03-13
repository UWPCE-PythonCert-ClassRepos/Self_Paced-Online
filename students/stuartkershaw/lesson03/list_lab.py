#!/usr/bin/env python3

# Series 1

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruit)

new_fruit = input('Please enter a new fruit: ')

fruit.append(new_fruit)

print(fruit)

selection = input('Please enter a number between 1 and {}: '.format(len(fruit)))

print('Fruit number {} is {}!'.format(selection, fruit[int(selection) - 1]))

fruit = ['Strawberries'] + fruit

print(fruit)

fruit.insert(0, 'Tomatoes')

print(fruit)

for el in fruit:
    if el[0] == 'P':
        print(el)

#Series 2

print(fruit)

del fruit[-1]

print(fruit)

delete_fruit = input('Please enter a fruit to delete: ')

fruit.remove(delete_fruit)

print(fruit)

fruit = fruit * 2

print(fruit)

delete_fruits = input('Please enter a fruit to delete: ')

while not delete_fruits in fruit:
    delete_fruits = input('That fruit isn\'t available! Please enter another:  ')

for el in fruit:
    if el == delete_fruits:
        fruit.remove(el)

print(fruit)

#Series 3

restart = True
while restart:
    restart = False
    for el in fruit:
        prompt = input('Do you like {}? '.format(el.lower()))
        if prompt == 'yes':
            continue
        elif prompt == 'no':
            for i in fruit:
                if i == el:
                    fruit.remove(i)
            restart = True

print(fruit)
