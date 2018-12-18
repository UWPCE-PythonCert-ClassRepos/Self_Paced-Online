#!/usr/bin/env python3

#*** Series 1 ***
fruits = ['Apples', 'Pears','Oranges','Peaches']
series1 = fruits[:]

#display beginning list
print(series1, '\n')

#ask user for fruit to add to list and display
series1.append(input('Please enter the name of a fruit: ').capitalize())

print(series1, '\n')

#get length of list for index
list_length = str(len(series1))

#ask user for number of fruit from list and display
num = int(input('Please enter a number between 1 and '+ list_length + ': '))-1

print(str(num+1)+':',series1[num], '\n')

#add new fruit to beginning user 2 different methods and display
series1 = ['Blueberries'] + series1

print(series1, '\n')

series1.insert(0,'Cranberries')

print(series1, '\n')

#print all in list that begin with p.
for fruit in series1:
    if fruit.startswith('P'):
        print(fruit)


#***Series 2***
#display current list, remove last fruit, display list again
series2 = fruits[:]
print(series2, '\n')

series2.pop()

print(series2, '\n')

#get fruit from user and delete from list, double list if fruit not found
user_fruit = ''

while user_fruit not in series2:
    user_fruit = input('Please enter the name of fruit to delete from list: ').capitalize()
    if user_fruit not in series2:
        print('Error! Fruit not in list.')
        series2 = series2 * 2
        print(series2)

series2[:] = [fruit for fruit in series2 if fruit != user_fruit]

print(series2, '\n')


#***Series 3***
#ask user about fruit preferences
series3 = fruits[:]
print(series3)
answer = ''

for fruit in series3[:]:
    while answer not in ['Yes', 'No']:
        answer = input('Do you like ' + fruit.lower() + '? ').capitalize()
        if answer not in ['Yes', 'No']:
            print('Please answer "Yes" or "No".')
    if answer == 'No':
        series3.remove(fruit)
    answer = ''

print(series3, '\n')

#***Series 4***
#make copy of original list and reverse names of all fruits
series4 = [fruit[::-1].capitalize() for fruit in fruits]

#delete last item of fruits
fruits.pop()

#display results
print(series4)
print(fruits)