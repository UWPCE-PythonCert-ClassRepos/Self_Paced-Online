#!/usr/bin/env python3
"""
Victor Medina
1/12/2019
Lesson 3: List Lab
"""
# Series 1
orig_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(orig_list)
new_fruit = input('What fruit would you like to add?')
orig_list.append(new_fruit)
print(orig_list)
n = int(input('Provide a number:'))
print(n, orig_list[n - 1])
orig_list = ['Watermelon'] + orig_list
print(orig_list)
orig_list.insert(0, 'strawberry')
print(orig_list)
for fruit in orig_list:
    if fruit[0] == 'P':
        print(fruit)
print('The series 1 list is: ', orig_list)
series1_list = orig_list[:]

# Series 2
series2_list = series1_list[:]
series2_list *= 2
print(series2_list)
del series2_list[-1]
print(series2_list)
fruit_to_delete = input('Which fruit would you like to delete?')
series2_list.remove(fruit_to_delete)
while fruit_to_delete in series2_list:
    series2_list.remove(fruit_to_delete)
print('The series 2 list is: ', series2_list)

# Series 3
series3_list = series1_list[:]
print('The list is: ', series3_list)
for fruit in series3_list[:]:
    response = input('Do you like {}? Please answer "yes" or "no".'.format(fruit))
    while response != 'yes' and response != 'no':
        response = input('Do you like {}? Please answer "yes" or "no".'.format(fruit))
    if response == 'no':
        series3_list.remove(fruit)
print('The series 3 list is: ', series3_list)

# Series 4
series4_list = series1_list[:]
print('The list is: ', series4_list)
for index, fruit in series4_list[:]:
    series4_list[index] = fruit[::-1]
