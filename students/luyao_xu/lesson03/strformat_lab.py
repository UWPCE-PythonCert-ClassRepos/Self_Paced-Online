#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
tpl_1 = (2, 123.4567, 10000, 12345.67)
# task 1
def task_1():
    # Write a format string that will take the following four element tuple:
    # ( 2, 123.4567, 10000, 12345.67)
    # Produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    return f'file_{tpl_1[0]:03d}, {tpl_1[1]:.2f},{tpl_1[2]:.2e},{tpl_1[3]:.2e}'

# task 2
def task_2():
    # Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
    return 'file_{:03d}:  {:.2f},{:.2e},{:.2e}'.format(tpl_1[0], tpl_1[1], tpl_1[2], tpl_1[3])


# task 3
def formatter(in_tuple):
    # make a form_string that was the right length for an arbitrary tuple
    l = len(in_tuple)
    form_string = "'the {} numbers are :" + " {:d}'," * l
    return form_string[:-1].format(l, *in_tuple)


def task_3():
    return formatter(in_tuple = (1, 2, 3, 4, 5))


# print(formatter((2, 3, 5)))
# print(formatter((2, 3, 5, 7, 9)))

# task 4
def task_4():
    # Use string format to print 5 element tuple (4, 30, 2017, 2, 27)
    tpl_2 = (4, 30, 2017, 2, 27)
    return f'{tpl_2[3]:02d}, {tpl_2[4]:2d}, {tpl_2[2]:4d}, {tpl_2[0]:02d}, {tpl_2[1]:2d}'


# task 5
def task_5():
    # Use f-string to display 4 elements list['oranges', 1.3, 'lemons', 1.1]

    list_1 = ['oranges', 1.3, 'lemons', 1.1]
    fruit_1 = list_1[0]
    fruit_2 = list_1[2]
    weight_1 = list_1[1]
    weight_2 = list_1[3]
    return f'The weight of an {fruit_1[:-1]} is {weight_1} and the weight of a {fruit_2[:-1]} is {weight_2} '
    # change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher


def task_5_1():
    list_1 = ['oranges', 1.3, 'lemons', 1.1]
    fruit_1 = list_1[0]
    fruit_2 = list_1[2]
    weight_1 = list_1[1]
    weight_2 = list_1[3]
    return f'The weight of an {fruit_1[:-1].upper()} is {weight_1 * 1.2} and the weight of a {fruit_2[:-1].upper()} is '
    f'{weight_2 * 1.2} '


# task 6
def task_6():
# Use alignment specifiers to print a table of several rows, each with a name, an age and a cost.
    rows = (('Name', 'Age','Costs'), ("Sam", 10, '$200.90'), ("Amy", 20, '$1000.00'), ("David", 30, '$999.99'))
    for row in rows:
        print('{:<10} {:>10} {:>20}'.format(*row))

# Given a tuple with 10 consecutive numbers
# Print the tuple in columns that are 5 charaters wide
    tpl_3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return ('{:<5}'*10).format(*tpl_3)


if __name__ == '__main__':

    print(task_1())
    print(task_2())
    print(task_3())
    print(task_4())
    print(task_5())
    print(task_6())




