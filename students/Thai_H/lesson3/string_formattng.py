print ('task one:'.title())
eg_tuple = ( 2, 123.4567, 10000, 12345.67)
print ('file_{:03}: {:.2f} {:.2e} {:.2e}'.format(eg_tuple[0], eg_tuple[1], eg_tuple[2], eg_tuple[3]) )

print ('\ntask two:'.title())
eg_tuple = ( 2, 123.4567, 10000, 12345.67)
print ('file_{file_name}: {float_num:.2f} {sci2:.2e} {sci3:.2e}'.format(file_name=str(eg_tuple[0]).zfill(3), float_num=eg_tuple[1], sci2=eg_tuple[2], sci3=eg_tuple[3] ) )

print ('\ntask three:'.title())
def dyn_formatter(in_tuple):
    format_string = ''
    for idx in in_tuple:
        format_string += '{:d}'
        if idx != len(in_tuple):
            format_string += ', '
    #
    return 'The {} numbers are: '.format(len(in_tuple)) + format_string.format(*in_tuple)
# Test formatter function
print ( dyn_formatter((1,2,3,4)) )
print ( dyn_formatter((1,2,3,4,500, 600, 70000)) )
#
print ('\ntask four:'.title())
eg_tuple = ( 4, 30, 2017, 2, 27)
print ('{3:0>2d} {4} {2} {0:0>2d} {1}'.format(*eg_tuple))
#'02 27 2017 04 30'
#
print ('\ntask five:'.title())
eg_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {eg_list[0][:-1]} is {eg_list[1]} and the weight of a {eg_list[2][:-1]} is {eg_list[3]}' )
print(f'The weight of an {eg_list[0][:-1].upper()} is {eg_list[1]*1.2} and the weight of a {eg_list[2][:-1].upper()} is {eg_list[3]*1.2}' )
#
print ('\ntask six:'.title())
eg_data = ('Colin', 38, 1111, 'Bob', 59, 222222, 'Vincent', 26, 3, 'Justin', 33, 444, 'Julie',  21, 5555)
while eg_data:
    print("{:<10}{:>2d}    ${:>8,d}".format(*eg_data))
    eg_data = eg_data[3:]
#
print ('\ntask six - EXTRA:'.title())
eg_tuple = (100,20,3000,444,55,667,789,89,99,1001)
print (('{:>5d}' * len(eg_tuple)).format(*eg_tuple))