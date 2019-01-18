'''Author: Alex Filson
Updated: 1.18.19
List Lab for Lesson 3
Py210, Online Self-Paced
'''

fruit = ['Apples','Pears','Oranges','Peaches']

print(fruit)

newfruit = input('Enter the name of a fruit to be added:')

fruit.append(newfruit)

print(fruit)

num = input('Enter a number:')-1

print('The fruit at number {} is {}.'.format(num+1,fruit[num]))

newfruit = input('Add a fruit to the top of the list:')

fruit = newfruit + fruit

print(fruit)

newfruit = input('Add another fruit to the top of the list:')

fruit.insert(newfruit)

print(fruit)

print("These are all of the fruit that begin with 'P':")
for i in fruit:
    if lowercase(i[0]) == 'p':
        print i
