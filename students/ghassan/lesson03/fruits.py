#!/usr/bin/env python3

# series1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
new_fruit = input('Enter a new fruit: ')
fruits.append(new_fruit)
print(fruits)
fruit_index = input('Enter a fruit index: ')
print(fruits[int(fruit_index)-1])
another_fruit = input('Enter another fruit: ')
fruits = [another_fruit] + fruits
print(fruits)
yet_another_fruit = input('Enter yet another fruit: ')
fruits.insert(0, yet_another_fruit)
print(fruits)
print([fruit for fruit in fruits if fruit.startswith('P')])

# series 2

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
fruits.pop()
print(fruits)
del_fruit = input('Enter a fruit to delete: ')
fruits.remove(del_fruit)

# series 3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
for fruit in fruits:
    qq = input('Do you like {}?'.format(fruit.lower()))
    while qq.lower() != 'yes' and qq.lower() != 'no':
        qq = input('Enter either "yes" or "no"\n')
    if qq.lower() == 'no':
        fruits.remove(fruit)

print(fruits)

# series 4

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruitsy = []
for fruit in fruits:
    fruitsy.append(
        fruit[::-1])
fruitsy.pop()
print(fruit)
print(fruitsy)
