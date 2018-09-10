
#Start Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response = input('What other fruit would you like? > ')
fruits += [response]
print(fruits)
response = input('\n''Which number fruit would you like? > ''\n')
print('\n'"Nice Choice! You chose {number}, which corresponds to the {fruit}"'\n'.format(
number=response, fruit=fruits[int(response)-1]))

# Add another to the beginning using '+'
fruits=['tomato']+fruits
print('\n''We added tomatoes to the beginning of the list')
print(fruits)
# Add another to the beginning using 'insert'
fruits.insert(0, 'kiwi')
print('\n''We added kiwis to the beginning of the list')
print (fruits)

# Display all the fruits that begin with P, using a for loop
new_list = []
for i in fruits:
     if i[0].lower() == 'p':
        new_list += [i]
print('\n''These are the fruits that start with the letter P ')
print(new_list)
  
  
# Start Series 2
print('\n''This is the fruit list we have so far starting Series 2.''\n')
print(fruits)

# Remove the last fruit
del fruits[-1:]
print('\n''Now we remove the last fruit')
print(fruits)
# Now we will ask a user which fruit to remove. First double the fruit list.
fruits2 = fruits*2
print('\n''We Double our fruit list')
print(fruits2)
response = input('\n''Which fruit would you like to remove?')
for i in fruits2:
    try:
        del fruits2[fruits2.index(response)]
    except ValueError as error:
        break
print('\n''These are the fruits left in your basket')
print (fruits2)

# Start of Series 3


new_list = fruits[:]
for i in fruits:
    while True:
        response = input("Do you like {fruit}? yes or no > ".format(fruit=i.lower()))
        if response == 'no' or response == 'yes':
            break        
    if response == 'no':
        del new_list[new_list.index(i)]
 
print(new_list) 
        
        
# Start of Series 4
print('\n''This is the start of Series 4')
print('\n''This is our list of fruits starting Series 4')
print(fruits)
# Create a copy of fruit list and spell fruits backwards
new_list = []
for i in fruits:
    spell = [str(i[::-1])]
    new_list += spell
print('\n''This is our fruit list with fruits spelled backwards')
print(new_list)

# Delete the last item of the original list
del fruits[-1:]

print('\n''This is the original fruit list with the last item deleted')
print(fruits)


