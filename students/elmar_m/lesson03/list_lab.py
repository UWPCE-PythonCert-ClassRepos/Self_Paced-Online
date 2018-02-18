#!/usr/bin/env python3
'''
series 1:
'''
'''
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response = input("Please add a fruit: > ")
fruits.append(response)
print(fruits)
response = input("Please enter a number to see the fruit having that number: ")
print('Fruit number', response, 'is:', fruits[int(response) -1])
print()

print('This is fruitlist now:', fruits)

print()

input('Press enter to add bananas at the beginning using "+" ...')
anotherfruit = ['Bananas']
fruits = anotherfruit + fruits
print('This is fruitlist now:', fruits)
print(anotherfruit[0], 'have been added successfully.')

print()

input('Now press enter to add cherries at the beginning using insert()...')
fruits.insert(0, 'Cherries')
print('See fruitlist once again:', fruits)
print('Cherries have been added successfully too.')

print()

''' 
# series 2:
'''
input('Now we wanna remove the last fruit from the list. Please press enter to continue...')
fruits.pop()
print("Here's the result:", fruits)
print('The last fruit has been removed.')
print()

response = input("Now it's up to you. Please type in a fruit to delete: >")
fruits.remove(response)
print('These are still in the list now:', fruits)
print(response, 'have been removed successfully.')
print()

print('But wait... suddenly the list grew double the size... look:')
fruits = fruits + fruits
print(fruits)
print()



rmfruit = input('We have to remove some more. Please tell me which one: >')

# fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
while rmfruit not in fruits:
    print(rmfruit, 'is not in the list')
    print('current list is: ', fruits)
    rmfruit = input('Please choose a fruit which is available in the list: >')

print('Ok, will remove', rmfruit, 'from the list. Are you sure?')
input('Press enter to continue... >')

while rmfruit in fruits:
    fruits.remove(rmfruit)

print('OK,', rmfruit, 'was removed.')
print('Now this is still in the list:', fruits)
print()
'''

'''
series 3:
'''
# fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits = ['Apples', 'Oranges', 'Peaches']
for i in fruits[:]:
    print('Do you like', i, '?', 'Type "yes" or "no"')
    answer = input()

    while (answer != 'yes') and (answer != 'no'):
        answer = input('Please type either "yes" or "no":')
    
    if (answer == 'yes'):
        print('answer was yes,', i, 'remain in list')
    elif (answer == 'no'):
        print('answer was no, removing', i)
        fruits.remove(i)
        
print(fruits)
    





