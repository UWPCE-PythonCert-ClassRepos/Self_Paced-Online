#!/usr/bin/env python3

#series 1
list1 = ['Apples','Pears','Oranges','Peaches']
print(list1)

add_fruit = input("Please input the name of a fruit to add to the list: ")

list1.append(str(add_fruit))
print(list1)

while True:
    list_position = input("Enter a number between 1 and 5 to select a fruit from the list: ")
    try:
        list_position = int(list_position)
    except:
        print("invalid entry, enter number between 1 and 5 in integer form")
        continue
    if 0 < list_position < 6:
        break
    else:
        print("invalid entry, number must be one of the following: 1,2,3,4,5")
print('fruit index: {}'.format(list_position))
print('fruit name: {}'.format(list1[list_position-1]))

list1 = ['Plums'] + list1
print(list1)

list1.insert(0, 'Papaya')
print(list1)

for item in list1:
    if item[0] == 'P':
        print(item, end=" ")
print()

#series 2
list2 = list1[:]
print(list2)

list2.pop()
print(list2)

while True:
    remove_fruit = input("Enter the name of one of the fruits from the list above to be removed: ")
    if remove_fruit in list2:
        break
    else:
        print("invalid entry, entry must be one of the following: {}".format(list2[:5]))
        list2 = list2*2
while remove_fruit in list2:
    list2.remove(remove_fruit)
print(list2)

#series 3
list3 = list1[:]
for item in list3[:]:
    while True:
        like = input("yes or no: Do you like {}? ".format(item))
        if like in ['yes','no']:
            break
        else:
            print("invalid entry, entry must be 'yes' or 'no'")
    if like == 'no':
        list3.remove(item)
print(list3)

#series 4
list4=list1[:]
for i, item in enumerate(list1):
    list4[i] = item[::-1]
list1.pop()
print("Origninal list: {}".format(list1))
print("Copied list: {}".format(list4))