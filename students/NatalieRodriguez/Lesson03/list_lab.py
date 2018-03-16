#Lesson 03: Lists
#Natalie Rodriguez
# 3/16/2018

#she-bang line
#!/usr/bin/env python3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruits)

more_fruit = input("Please add another fruit."'\n')
fruits.append(more_fruit)
more_fruit2 = input("Add one more fruit."'\n')
fruits.append(more_fruit2)

print(fruits)

which_fruit = int(input("What number fruit would you like to see?" '\n'))
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
