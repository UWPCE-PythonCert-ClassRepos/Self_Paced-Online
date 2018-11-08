"""
Author: Alyssa Hong
Date: 10/25/2018
Update:
Lesson3 Assignments > String Formatting Lab Exercise
"""
#!/usr/bin/env python3

# Task One
a_tuple = (2, 123.4567, 10000, 12345.67)

#The first element:make a formatting to get the right sort order(“pad” the numbers with zeros)
#The second element:with 2 decimal places shown
#The third value:interger/scientific notation, with 2 decimal places shown
#The fourth value:flost/scientific notation with 3 significant figures.
print("file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}".format(*a_tuple))


# Task Two
# think about alternative ways to use and consider f-strings
result_task_one = ('file_0002', 123.46, 1.00e+04, 1.23e+04)
#print(fr'{result_task_one}')
print(f'{result_task_one[0]:s}: {result_task_one[1]:.2f}, {result_task_one[2]:.2e}, {result_task_one[3]:.2e}')


#Task Three
#Dynamically Building up Format Strings
def formatter(in_tuple):
    l = len(in_tuple)
    return ("the {} numbers are:" + ", ".join(["{}"] * l)).format(l, *in_tuple)

print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))

#Task Four
#Given a 5 element tuple:(4, 30, 2017, 2, 27)
#output: '02 27 2017 04 30'
new_tuples = (4, 30, 2017, 2, 27)
#'{3},{4},{2},{0},{1}'.format(*new_tuples)
print('{3:0>2d} {4} {2} {0:0>2d} {1}'.format(*new_tuples))


#Task Five
#Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
#Write an f-string that will display:
#Display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
#displays the names of the fruit in upper case,
#and the weight 20% higher (that is 1.2 times higher).
fruits = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruits[0].upper():s} is {fruits[1]:.2f} and the weight of a {fruits[2]:s} is {fruits[3]:.2f}")
print(f"The weight 20% higher of an {fruits[0].upper():s} is {fruits[1]*1.2:.2f} and the weight 20% higher of a {fruits[2]:s} is {fruits[3]*1.2:.2f}")


#Task Six
#Write some Python code to print a table of several rows, each with a name, an age and a cost.
#Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
list_col = ('Name','Age','Cost')
list_row = (('Fred', '25', '1000'),('Alex', '26', '20000'),('Hannah', '27', '30000'),('Alyssa', '28', '7000'))
print('{:^10} {:^10} {:^10}'.format(*list_col))
for row in list_row:
    print('{:<10} {:^10} ${:<10}'.format(*row))

#an extra Task
#given a tuple with 10 consecutive number
#can you work how to quickly print the tuple in columns that are 5 charaters wide?
con_numbers = (1,2,3,4,5,6,7,8,9,10)
print(('{:<5}'*10).format(*con_numbers))
