#!/usr/bin/env python3
# Lesson_3 Activity 2 List Lab

# Series 1
series_1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(series_1)

# get user input for new fruit and add it to the end of the list
add_fruit = raw_input('Enter an additional fruit name: ')
series_1.append(add_fruit)
print(series_1)

# get a number from user and diplay that number and the fruit in that position
while True:
    try:
        user_num = int(raw_input('Pick a fruit in the list between 1 and {}: '
                       .format(len(series_1))))
    except ValueError:
        print "you have made an invalid choice, try again."
        continue
    if user_num > 0 and user_num < len(series_1)+1:
        print('The fruit that is number {} in the list is {}'
              .format(user_num, series_1[user_num-1]))
        break
    print "you have made an invalid choice, try again."

# add string to font of list using +
add_fruit_2 = raw_input('Enter a fruit to add to the front of the list: ')
series_1 = [add_fruit_2] + series_1
print(series_1)

# add string to fruont of list using insert
add_fruit_3 = raw_input('Enter another fruit to add
                        to the front of the list: ')
series_1.insert(0, add_fruit_3)
print(series_1)

# display the the fruits that begin with the letter p
p_list = []
for i in series_1:
    if str.lower(i[0]) == 'p':
        p_list.append(i)
print("The fruits in this list that start with p are: \n{}".format(p_list))


# Series 2
print("---------------------------------")

# print the series, remove the last item in the list, and then print again
series_2 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(series_2)
series_2.pop()
print(series_2)

# multiply series by 2
series_2 = series_2*2
print("The fruits had babies \n {}".format(series_2))

# While loop to check for proper input and remove fruit from list
while True:
    rem_fruit = raw_input('Please select a fruit from the list to remove: ')
    if rem_fruit in series_2:
        while rem_fruit in series_2:
            series_2.remove(rem_fruit)
        break
    print("That fruit is not on the list, please
          check spelling and capitalization and try again")
print(series_2)


# Series 3
print("---------------------------------")
series_3 = ['Apples', 'Pears', 'Oranges', 'Peaches']

# While loop to check for proper input and
# remove fruit from list based on user tastes
gross_fruit = []
for f in series_3:
    while True:
        yorn = raw_input('Do you like {}? (y/n): '.format(f.lower()))
        if yorn[0].lower() == 'n':
            gross_fruit += [f]
            print("me neither they are gross af")
            break
        elif yorn[0].lower() == 'y':
            print("awesome me too!!")
            break
        print("Please respond y or n")
for item in gross_fruit:
    while item in series_3:
        series_3.remove(item)

print("A list of gross fruit: {}".format(gross_fruit))
print("A list of non gross fruit: {}".format(series_3))


# Series 4
print("---------------------------------")
series_4 = ['Apples', 'Pears', 'Oranges', 'Peaches']

rev_series = []
for item in series_4:
    rev_series += [item[::-1]]
series_4.pop()
print(rev_series)
print(series_4)
