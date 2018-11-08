# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:26:39 2018

@author: denni
"""

"""This exercise reinforces the important concepts of string formatting"""

#Task One
#Write a format string that will take the following four element tuple:
#( 2, 123.4567, 10000, 12345.67) and produce 'file_002 :   123.46, 1.00e+04, 1.23e+04'
input = (2, 123.4567, 10000, 12345.67)
output = "file_{:0=3} :   {}, {:.2e}, {:.2e}".format(input[0], round(input[1],2), input[2], input[3])
print('Task One output:')
print(output)
print()

#Task Two
#Using your results from Task One, repeat the exercise, 
#this time using an alternate type of format string 
#(hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already).
output_newformat = f'file_{input[0]:0=3} :   {round(input[1],2)}, {input[2]:.2e}, {input[3]:.2e}'
print('Task Two output:')
print(output_newformat)
print()

#Task Three
#Dynamically Building up Format Strings
#Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#to take an arbitrary number of values.
#Hint: You can pass in a tuple of values to a function with a *:
def formatter(in_tuple):
    nums = len(in_tuple)
    form_string = "The {} numbers are : " + "{:d},"*nums
    return form_string[:-1].format(nums,*in_tuple)
print('Task Three output:')
print(formatter((1,3,4,5,6,7)))
print()

#Task Four
#Given a 5 element tuple: ( 4, 30, 2017, 2, 27)
#use string formating to print: '02 27 2017 04 30'
#Hint: use index numbers to specify positions.
a_tuple = ( 4, 30, 2017, 2, 27)
output_task4 = f'{a_tuple[3]:0=2} {a_tuple[4]} {a_tuple[2]} {a_tuple[0]:0=2} {a_tuple[1]}'
print('Task Four output:')
print(output_task4)
print()

#Task Five
#Here’s a task for you: Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
#Write an f-string that will display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1
#Also change the f-string so that it displays the names of the fruit in upper case, 
#and the weight 20% higher (that is 1.2 times higher).
a_list = ['oranges', 1.3, 'lemons', 1.1]
output_task5a = f'The weight of an {a_list[0][:-1]} is {a_list[1]} and the weight of a {a_list[2][:-1]} is {a_list[3]}'
output_task5b = f'The weight of an {a_list[0][:-1].capitalize()} is {a_list[1]*1.2} and the weight of a {a_list[2][:-1].capitalize()} is {a_list[3]*1.2}'
print('Task Five outputs:')
print(output_task5a)
print(output_task5b)
print()

#Task Six
#Write some Python code to print a table of several rows, each with a name, 
#an age and a cost. Make sure some of the costs are in the hundreds and thousands 
#to test your alignment specifiers.
#And for an extra task, given a tuple with 10 consecutive numbers, can you work how to 
#quickly print the tuple in columns that are 5 charaters wide? 
#It’s easily done on one short line!

#Part 1
data = (('Dennis',45,'$350.00'),('Julie',35,'$20.00'),('Ethan',18,'$2240.00'),('Tyler',9,'$55.00'))
print('Task Six outputs:')
for row in data:
    print(f'{row[0]: <10}{row[1]: <5}{row[2]: <15}')
    
#Part 2
a_tuple = (0,1,2,3,4,5,6,7,8,9)
[print(f'{item: <5}', end="") for item in a_tuple]

