#!/usr/bin/env python3

input_tuple = (2, 123.4567, 10000, 12345.67)

#Task One

task_one = 'file_{0:0>3}: {1:.2f}, {2:.2e}, {3:.2e}'.format(2, 123.4567, 10000, 12345.67)
#print(task_one)

#Made it generic for inputs.
asd = 'file_{0:0>3}: {1:.2f}, {2:.2e}, {3:.2e}'.format(*input_tuple)
#print(asd)

#Task Two


#Task Three

def formatter(input_tuple):
    num_values = len(input_tuple)
    value_string = "{:d}, " * num_values
    value_string = value_string[0:-2]
    format_string = "the " + str(num_values) + " numbers are: " + value_string
    return format_string.format(*input_tuple)
    # ???Do I need a print function here???

#formatter((1,2,3,4))

#Task Four

four = (4, 30, 2017, 2, 27)
out_four = '{3:0>2} {4} {2} {0:0>2} {1}'.format(*four)
print(out_four)