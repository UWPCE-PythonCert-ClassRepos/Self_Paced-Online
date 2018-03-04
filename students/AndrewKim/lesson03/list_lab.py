#!/usr/bin/env python3

#Series 1
series1 = ["Apples", "Pears", "Oranges", "Peaches"]

print(series1)

user_input = input('Give me another fruit: ')

series1.append(user_input)

print(series1)

user_input = input('Give me a number: ')

num = int(user_input)

print(series1[num-1])

series1 = ['Grapes'] + series1

print(series1)

series1.insert(0, 'Banana')

print(series1)

for item in series1:
    if item[0] == 'P':
        print(item)

#Series 2
print(series1)

series1.pop()

print(series1)

user_input = input('Give me the fruit to delete: ')
    
for item in series1:
    if item == user_input:
        series1.remove(item)

print(series1)

#Series 3
for item in series1:
    user_input = input('Do you like {}?'.format(item.lower()))
    while user_input != 'yes' and user_input != 'no':
        user_input = input('Please enter yes or no')
    if user_input == 'no':
        series1.remove(item)

print(series1)

#Series 4
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


some_series = series1[:]
for index, item in enumerate(some_series):
    def reverse(some_series):
        if not some_series:
            return ""
        else:
            front_part = reverse(some_series[1:])
            back_part = some_series[0]
            
        return front_part + back_part[0]
    some_series[index] = reverse(item)

print(some_series)

series1.pop()

print(series1)
print(some_series)