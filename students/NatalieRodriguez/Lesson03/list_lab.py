#Lesson 03: Lists
#Natalie Rodriguez
# 3/16/2018

#she-bang line
#!/usr/bin/env python3


#_______________________________________
#Series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruits)

more_fruit = input("Please add another fruit."'\n')
fruits.append(more_fruit)
more_fruit2 = input("Add one more fruit."'\n')
fruits.append(more_fruit2)

print(fruits)

which_fruit = int(input("What number fruit from the list would you like to see?" '\n'))
if 0 <= which_fruit < len(fruits):
    print(fruits[which_fruit -1])
else:
    print("There are not that many fruits.")

front_fruit = input("Add another fruit to the front of the list."'\n')
front_fruit2 = input("And one more!"'\n')
fruits_longlist = [front_fruit,] + fruits
fruits_longlist.insert(1, front_fruit2)

print(fruits_longlist)

for item in fruits_longlist:
    if item[0] == 'p':
        print(item)
    elif item[0] == 'P':
        print(item)
    else: pass

#input("Press enter to exit this fruity list.")

#___________________________________________
#Series 2

print("Here is your fruit list!", fruits_longlist)

fruits_longlist = fruits_longlist[:-1]

print("Your fruit list, without the last item, is:", fruits_longlist)

delete_fruit = input("Which fruit would you like to remove from the list?"'\n')

if delete_fruit in fruits_longlist:
    fruits_longlist.remove(delete_fruit)
    print(delete_fruit, "have been removed from the list."'\n')
else:
    print(delete_fruit, "cannot be deleted because it is not in the list."'\n')

print("Your fruit list now has", len(fruits_longlist), "fruits:", fruits_longlist, '\n')


#___________________________________________
#Series 3

yes = []
no = []

for item in fruits_longlist:
    if not item in yes and not item in no:
        prompt = input('Do you like {}? '.format(item.lower()))
        while not prompt == 'yes' and not prompt == 'no':
            prompt = input('Do you like {}? (yes/no) '.format(el.lower()))
        if prompt == 'yes':
            yes.append(item)
        else:
            no.append(item)

print("The fruits you enjoy are:", yes,'\n')

#___________________________________________
#Series 4

fruit_copy = fruits_longlist[:]
fruit_reversed = []

for fruit in fruit_copy:
    fruit_reversed.append(fruit[::-1])

del yes[-1]

print("Your full fruit list:", fruit_copy)
print("Your fruit list, backwards!", fruit_reversed)








