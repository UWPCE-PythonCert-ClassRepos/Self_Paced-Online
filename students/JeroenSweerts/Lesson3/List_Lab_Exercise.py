#!/usr/bin/env python3
##########################SERIES1###############################################
'''Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.'''
fruitlist = ['Apples', 'Pears', 'Oranges','Peaches']

'''Display the list (plain old print() is fine…).'''
print(fruitlist)

'''Ask the user for another fruit and add it to the end of the list.'''
response = input("Please enter a fruit to add to the list > ")
fruitlist.append(response)

'''Display the list.'''
print("New list with appended fruit > "+response)
print(fruitlist)
print('')

'''Ask the user for a number and display the number back to the user and
    the fruit corresponding to that number (on a 1-is-first basis).
    Remember that Python uses zero-based indexing, so you will need to correct.'''
response = input("Please enter the number of the fruit of the list to display > ")
print("you selected fruit " + response + " : " + fruitlist[int(response)-1])

'''Add another fruit to the beginning of the list using “+”
and display the list.'''
fruitlist = ['banana'] + fruitlist
print("New list with banana added as first element: ")
print(fruitlist)
print('')

'''Add another fruit to the beginning of the list using insert()
and display the list.'''
fruitlist.insert(0, 'Cherries')
print("New list with Cherries added as first element: ")
print(fruitlist)
print('')

'''Display all the fruits that begin with “P”, using a for loop.'''
print("Now we display all fruits starting with a P")
for fruits in fruitlist:
    if fruits[0] == 'P' or fruits[0] == 'p':
        print(fruits)
print('')
##########################SERIES2###############################################
'''Using the list created in series 1 above:'''
'''Display the list.'''
fruitlist = ['Apples', 'Pears', 'Oranges','Peaches']
print('Starting with a fresh fruitlist :')
print(fruitlist)
print('')

'''Remove the last fruit from the list.'''
del fruitlist[-1]

'''Display the list.'''
print("New list with last fruit deleted: ")
print(fruitlist)
print('')

'''Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found.
Once found, delete all occurrences.)'''
found = False
while not found:
    response = input("Please enter the name of fruit to delete > ")
    for index, fruit in enumerate(fruitlist):
        if fruit == response:
            found = True
            del fruitlist[index]
            print(fruitlist)
    if not found:
        fruitlist = 2*fruitlist
        print(fruitlist)
print('')
##########################SERIES3###############################################
fruitlist = ['Apples', 'Pears', 'Oranges','Peaches']
print('Starting agaian with a fresh fruitlist :')
print(fruitlist)
'''Ask the user for input displaying a line like “Do you like apples?” for
each fruit in the list (making the fruit all lowercase).'''
fruitlist2 = fruitlist[:]
for fruit in fruitlist:
    response = input("Do you like "+ fruit.lower() + '? > ')
    '''For any answer that is not “yes” or “no”, prompt the user to answer
    with one of those two values (a while loop is good here)'''
    while response not in ['no', 'n', 'yes', 'y']:
        response = input('please respond with yes or no > ')
    if response in ['no', 'n']:
        '''For each “no”, delete that fruit from the list.'''
        print('Then we delete '+fruit+' for you.')
        del fruitlist2[fruitlist2.index(fruit)]
    else:
        print('Then we keep '+fruit+' for you.')
    '''Display the list.'''
    print(fruitlist2)
print('')
##########################SERIES4###############################################
fruitlist = ['Apples', 'Pears', 'Oranges','Peaches']
print('Starting with a fresh fruitlist :')
print(fruitlist)
'''Make a copy of the list and reverse the letters in each fruit in the copy.'''
fruitlist2 = fruitlist[:]
for i, fruit in enumerate(fruitlist2):
    fruitlist2[i] = fruit[::-1]
'''Delete the last item of the original list. Display the original list and the copy.'''
del fruitlist[-1]
print("Fruitlist with letters reversed: ")
print(fruitlist2)
print("Original fruitlist with last item deleted: ")
print(fruitlist)
