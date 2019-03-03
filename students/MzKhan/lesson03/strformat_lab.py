'''
    Name: Muhammad Khan
    Date: 02/28/2019
    Assignment03

'''

# Task 1.
print('Task 1')
# Format ( 2, 123.4567, 10000, 12345.67) to
#        'file_002 : 123.46, 1.00e+04, 1.23e+04'
print('file_{:0>3}: {:.2f}, {:.2e}, {:.2e}'.format(2,123.4567,10000,12345.67))

# Task 2
print('\nTask 2')
# pack the tuple in the formatting.
tuple_val = ( 2, 123.4567, 10000, 12345.67)
print('file_{:0>3}: {:.2f}, {:.2e}, {:.2e}'.format(*tuple_val))

# Task # 3
print('\nTask 3')
# Dynamically build the format string.

def formatter(in_tuple):
    # This method takes a sequence of integers and returns all the items of the
    # sequence in a formatted string.
    # parm: a tuple.
    # return: string
    l = len(in_tuple)
    strf_format = "The {:d} numbers are: "+"{:d}, "*(l-1)+"{:d}"
    return strf_format.format(l,*in_tuple)

tup = (2, 3, 5, 7, 9)
print(formatter(tup))
a_list = list(range(10))
print(formatter(a_list))

# Task # 4.
print('\nTask 4')
def formatter_with_index(a_tuple):
    # This method uses the index of a sequence to format the string
    # Instead of packing
    # parm: sequence of integers of length 5.
    # return: formatted string.
    strf_format = '{:0>2d} {:d} {:d} {:0>2d} {:d}'
    return strf_format.format(a_tuple[3],a_tuple[4],a_tuple[2],a_tuple[0],
                              a_tuple[1])

a_tuple = ( 4, 30, 2017, 2, 27 )
print(formatter_with_index(a_tuple))

# Task # 5
print('\nTask 5')
# Use the f string formatting to print the formatted string.
def f_string(aList, textFormat = 0, ratio = 0):
    # This function takes the data mixed of strings and integers and
    # prints the formatted string.
    # parm: sequence    (required)
    # parm: integer     (optional kwarg)
    # parm: integer     (optional kwarg represents percent)
    if textFormat:
        aList[0] = aList[0].upper()
        aList[2] = aList[2].upper()
    ratio = 1+ratio/100
    print(f"The weight of an {aList[0][:-1]} is {aList[1]*ratio}"
            f" and the weight of a {aList[2][:-1]} is {aList[3]*ratio}")
data = ['oranges', 1.3, 'lemons', 1.1]
f_string(data)
f_string(data,1,20)

# Task # 6
# Write some Python code to print a table of several rows, each with a name,
# an age and a cost. Make sure some of the costs are in the hundreds and
# thousands to test your alignment specifiers.

print('\nTask 6')

test_data = [ ['Muhammad',30,100000],
             ['Lindsay',35,1234.568],
             ['Sarah',28,343.9048],
             ['Adam',20,100],
             ['John',18,123458945],
             ['James',49,300],
             ['Lauren',31,1500000000],
             ['Benny',2,10] ]

def align_data(dataset):
    # This method prints the data in rows and columns with all data fields
    # aligned to the left.
    # parm: a sequence
            # each sequence entry must contain a string, integer, and a float
            # data respectively.
    print('{:15} {:10} {:20}'.format('Name','Age','Cost'))
    for data in dataset:
        print('{:15} {:<10d} $ {:<.2f}'.format(data[0],data[1],data[2]))

align_data(test_data)
print('\nExtra Task')
tuple_data = tuple(range(10))
print(('{:<5d} '*len(tuple_data)).format(*tuple_data))

# End.