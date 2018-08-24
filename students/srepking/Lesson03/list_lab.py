
#Start Series 1
fruits=['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response=input('What other fruit would you like? > ')
fruits+=[response]
print(fruits)
response=input('\n''Which number fruit would you like? > ''\n')
print('\n'"Nice Choice! You chose {number}, which corresponds to the {fruit}"'\n'.format(
number=response,fruit=fruits[int(response)-1]))
#Add another to the beginning using '+'
fruits=['tomato']+fruits
print(fruits)
#Add another to the beginning using 'insert'
fruits.insert(0,'kiwi')
print (fruits)

#Display all the fruits that begin with P, using a for loop
new_list=[]
for i in fruits:
     if i[0]=='P':
        new_list+=[i]
print(new_list)
  
  
#Start Series 2
print('\n''This is the fruit list we have so far starting Series 2.''\n')
print(fruits)

#Remove the last fruit
del fruits[-1:]
print(fruits)
#Now we will ask a user which fruit to remove. First double the fruit list.
fruits=fruits*2
print(fruits)
response=input('\n''Which fruit would you like to remove?')
for i in fruits:
    try:
        del fruits[fruits.index(response)]
    except ValueError as error:
        break

print (fruits)

#Start of Series 3
fruits=['Apples', 'Pears', 'Oranges', 'Peaches']

new_list=fruits[:]
for i in fruits:
    while True:
        response=input("Do you like {fruit}? yes or no > ".format(fruit=i.lower()))
        if 'no' in response or 'yes' in response:
            break
    if 'no' in response:
        del new_list[new_list.index(i)]
 
print(new_list) 
        
        
