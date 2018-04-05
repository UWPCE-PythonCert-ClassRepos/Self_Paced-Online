#! /usr/bin/env python

#Series 1
print('Series 1:')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

fruit_to_add = input('\nWhat fruit should be added? > ')
fruits.append(fruit_to_add)
print(fruits)

fruit_to_disp = int(input('\nWhat fruit to view (1 to 5)? >'))
print(fruit_to_disp,fruits[fruit_to_disp-1],'\n')

fruits = ['Pineapples'] + fruits
print(fruits)

fruits.insert(0, 'Bananas')
print(fruits,'\n')
  
for fruit in fruits:
    if fruit[0] == 'P':
        print(fruit)

        
#Series 2
print('\n\nSeries2:')
fruits2 = fruits[:]
print(fruits2)

del fruits2[-1]
print(fruits2,'\n')

fruits2 = fruits2 * 2
while True:
    fruit_to_del = input('What fruit should be deleted? > ')
    if fruit_to_del in fruits2:
        while fruit_to_del in fruits2:
            fruits2.remove(fruit_to_del)
        break
    else:
        print("I couldn't find that fruit, please try again.\n")
print(fruits2)

#Series 3
print('\n\nSeries3:')
fruits3 = fruits[:]

for fruit in fruits3[:]:
    while True:
        user_like = input('Do you like {}? > '.format(fruit.lower()))
        if user_like == 'no':
            fruits3.remove(fruit)
            break
        elif user_like == 'yes':
            break
        else:
            print('Please answer the question "yes" or "no".\n')
print(fruits3)

#Series 4
print('\n\nSeries 4:')
rev_fruits = [fruit[::-1] for fruit in fruits]
del fruits[-1]
print(fruits)
print(rev_fruits)
