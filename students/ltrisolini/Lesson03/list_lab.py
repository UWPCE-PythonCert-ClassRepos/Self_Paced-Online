#!/usr/bin/env python3
#List Lab Exercise


#Series1
my_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(my_list)

user_input = input('Write another fruit: ')

my_list.append(user_input)

print(my_list)

user_input = input('Write a number between 1-5: ')

num = int(user_input)

print(my_list[num - 1])

my_list = ['Cherry'] + my_list

print(my_list)

my_list.insert(0, 'Kiwi')

print(my_list)

for item in my_list:
    if item[0] == 'P':
        print(item)

#Series2
print(my_list)

my_list.pop()

print(my_list)

user_input = input('Write the fruit to delete: ')

for item in my_list:
    if item == user_input:
        my_list.remove(item)

print(my_list)

#Series3
for item in my_list:
    user_input = input('Do you like {}? '.format(item.lower()))
    while user_input != 'yes' and user_input != 'no':
        user_input = input('Enter yes or no ')
    if user_input == 'no':
        my_list.remove(item)

print(my_list)


#Series4
def reverse(rev):
    if len(rev) == 0:
        return rev
    else:
        return reverse(rev[1:]) + rev[0]


new_list = my_list[:]
for index, item in enumerate(new_list):
    def reverse(new_list):
        if not new_list:
            return ""
        else:
            front_part = reverse(new_list[1:])
            back_part = new_list[0]

        return front_part + back_part[0]


    new_list[index] = reverse(item)

print(new_list)

my_list.pop()

print(my_list)
print(new_list)