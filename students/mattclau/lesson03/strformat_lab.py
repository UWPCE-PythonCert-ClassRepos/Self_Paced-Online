#String format exercise

#test data
data_set = (2, 123.4567, 10000, 12345.67)

#Task 1 format data as specified
def string_formatter (x):
    """Returns values from tuple formatted as requested"""
    return 'file_{:0>3}, {:.2f}, {:.2e}, {:.2e}'.format(data_set[0], data_set[1], data_set[2], data_set[3])

print(string_formatter(data_set))

#Task 2 format data as specified using different method
print(f'file_{data_set[0]:0>3}, {data_set[1]:.2f}, {data_set[2]:.2e}, {data_set[3]:.2e}\n')

# check that the 2 methods match
assert string_formatter(data_set) == f'file_{data_set[0]:0>3}, {data_set[1]:.2f}, {data_set[2]:.2e}, {data_set[3]:.2e}'

#Task 3: dynamic format string
tup_3 = (1,2,3)
tup_5 = (1,2,3,4,5)

def dynamic_formatter(tup):
    """Returns numbers in format requested dynamically for any number of elements"""
    formed_string =  'the ' + str(len(tup)) +' numbers are: ' +','.join(['{}']*len(tup))
    return formed_string.format(*tup)

print(dynamic_formatter(tup_3))
print(dynamic_formatter(tup_5), '\n')

#Task 4: format elements of tuple
task_four = (4,30,2017,2,27)

print(f'{task_four[3]:0>2} {task_four[4]:0>2} {task_four[2]} {task_four[0]:0>2} {task_four[1]:0>2}\n')

#Task 5: f-stirngs
task_five = ['oranges', 1.3, 'lemons', 1.1]
#Original statement
print(f'The weight of an {task_five[0][:-1]} is {task_five[1]} and the weight of a {task_five[2][:-1]} is {task_five[3]}')

#With 20% increase
print(f'Some large {task_five[0].upper()} may weigh {task_five[1]*1.2} and some large {task_five[2].upper()} {task_five[3]*1.2}\n')

#Task 6: Columns
row1 = ('John', '21', 'Cost:', '$88.09')
row2 = ('Paul', '15', 'Cost:', '$888.09')
row3 = ('Matthew', '45', 'Cost:', '$8888.09')
row4 = ('Elizabeth', '26', 'Cost:', '$88888.09')

def row_formatter(tup):
    """Formets tuples into rows and columns for a table"""
    return f'{tup[0]:10}{tup[1]:10}{tup[2]:10}{tup[3]:10}'

print(row_formatter(row1))
print(row_formatter(row2))
print(row_formatter(row3))
print(row_formatter(row4),'\n')

#Extra task - print all elements of tuple in columns of 5
long_tup = (1,2,3,4,5,6,7,8,9,0)

print(*(f'{i:<5}' for i in long_tup))