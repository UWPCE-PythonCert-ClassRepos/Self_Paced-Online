#!/usr/bin/env python3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print('Initial fruits:\n', fruits)

new_fruit = input('What fruit would you like to add?')
fruits.append(new_fruit)

print('New list:\n', fruits)

number = input('Enter a number 1-5:')

print('Your number is {number}. Fruit {number} in the list is {fruit}'.format(number = number, fruit = fruits[int(number)-1]))

fruits = ['Grapes'] + fruits

print('I added Grapes. Now the list is:\n', fruits)

fruits.insert(0, 'Plums')

print('And now I added Plums. The list is now:\n', fruits)

print('Here are the fruits in my list that begin with P:')

for fruit in fruits:
    if fruit.lower().startswith('p'):
        print(fruit)

# Series2

print('Ok here is the list again:\n', fruits)

fruits = fruits[:-1]

print('And here is the list after I removed the last element:\n', fruits)

while True:
    fruit_to_delete = input('What fruit would you like to remove?')

    if fruit_to_delete in fruits:
        fruits = [fruit for fruit in fruits if not fruit==fruit_to_delete]
        print('Removed {}. Here is the list now:\n'.format(fruit_to_delete), fruits)
        break
    else:
        print('{} was not in the list'.format(fruit_to_delete))
        fruits = fruits*2
        print('Here is the list of fruits now:\n', fruits)

# Series3
fruits = list(set(fruits))

print('Here is the list of unique fruits:\n', fruits)
for fruit in fruits:
    while True:
        response = input('Do you like {}?'.format(fruit)).lower()
        if response == 'no':
            fruits.remove(fruit)
            print('I removed {}'.format(fruit))
            break
        elif response == 'yes':
            print('Ok')
            break
        else:
            print('Please answer yes or no')
    print('Here is the list of fruits now:\n', fruits)

# Series4

fruits_copy = fruits.copy()
fruits_copy = [i[::-1] for i in fruits_copy]
fruits = fruits[:-1]

print('This is the original list:\n', fruits)
print('This is the copied list:\n', fruits_copy)

print('')
