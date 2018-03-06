#!/usr/bin/env python3

###################TASK 1#######################################################
'''Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
"file_002 :   123.46, 1.00e+04, 1.23e+04"  '''
tuple_elements = ( 2, 123.4567, 10000, 12345.67)
#print('file_{0:03d} :   {}'.format(tuple_elements[0],tuple_elements[1]))
print('file_{0:03d} :  {1:.2f}, {2:.2e}, {3:.2e}'.format(tuple_elements[0],tuple_elements[1],tuple_elements[2],tuple_elements[3]))

###################TASK 2#######################################################
'''Using your results from Task One, repeat the exercise,
but this time using an alternate type of format string
(hint: think about alternative ways to use .format() (keywords anyone?),
and also consider f-strings if you’ve not used them already).'''
print(f'file_{tuple_elements[0]:03d} :  {tuple_elements[1]:.2f}, {tuple_elements[2]:.2e}, {tuple_elements[3]:.2e}')

###################TASK 3#######################################################
def formatter(*t):
    form_string = ""
    for el in t[0]:
        form_string = form_string + "{:d},"
    #delete last comma of form_string
    form_string = form_string[:-1]

    print("the "+str(len(*t))+" numbers are: " +form_string.format(*t[0]))
formatter((1,2,3,4,5,8))

###################TASK 4#######################################################
'''Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30' '''
tuple_elements2 = ( 4, 30, 2017, 2, 27)
print(f'{tuple_elements2[3]:02d} {tuple_elements2[4]:02d} {tuple_elements2[2]:02d} {tuple_elements2[0]:02d} {tuple_elements2[1]:02d}')

###################TASK 5#######################################################
''' Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1 '''
list_elements = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {list_elements[0][:-1]} is {list_elements[1]} and the weight of a {list_elements[2][:-1]} is {list_elements[3]}')
''' Now see if you can change the f-string so that it displays the names of
the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).'''
print(f'The weight of an {list_elements[0][:-1].upper()} is {list_elements[1]*1.2} and the weight of a {list_elements[2][:-1].upper()} is {list_elements[3]*1.2}')

###################TASK 6#######################################################
''' Write some Python code to print a table of several rows, each with a name,
an age and a cost. Make sure some of the costs are in the hundreds and
thousands to test your alignment specifiers.'''
names = ['Udacity','Oxford', 'Bologna', 'Harvard']
age = [10, 300, 900, 100]
cost = [2000, 20000, 1400, 100000]
for i in range(len(names)):
    print(f'{names[i]:20s} {age[i]:20d} {cost[i]:20d}')

''' And for an extra task, given a tuple with 10 consecutive numbers,
can you work how to quickly print the tuple in columns that are
5 charaters wide? It’s easily done on one short line! '''
print(' '.join(('%*s' % (5, i) for i in range(10))))
