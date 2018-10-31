# Task one
formatted = 'file_{:03}: {:06.2f}, {:.2e}, {:.2e} '.format(2, 123.4567, 10000, 12345.67)
print(formatted)

#Task Two

formatted_two_index = 'file_{0:03}: {1:06.2f}, {2:.2e}, {3:.2e} '.format(2, 123.4567, 10000, 12345.67)
print(formatted_two_index)

formatted_two = 'file_{ind_one:03}: {ind_two:06.2f}, {ind_three:.2e}, {ind_four:.2e}'.format(ind_one = 2, ind_two = 123.4567, ind_three = 10000, ind_four = 12345.67)
print(formatted_two)


# Task three
# Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)" to take an arbitrary number of values.

def formatter(t):
    l = len(t)
    listed = " ,".join(["{}"] * l)
    my_str = f"The {l} numbers are: " + listed #this is a minor changed. Used an f string to include the count of numbers. 
    return (my_str).format(*t)


print(formatter((2,3,5)))
print(formatter((3, 4, 5, 6, 2, 4)))


# Task Four
# Given a 5 element tuple: ( 4, 30, 2017, 2, 27). use string formating to print: '02 27 2017 04 30'

formatter_position = "{3:02} {4:} {2:} {0:02} {1:}".format(4, 30, 2017, 2, 27)
print(formatter_position)

# Task Six

# Write some Python code to print a table of several rows, each 
# with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

header = ("Name", "Age", "Cost")
diana = ("Diana", 22, 100300)
john = ("John", 34, 12000)
brittany = ("Brittany", 54, 3900)
hannah = ("Hannah", 15, 300)
print("{0:<10}{1:>10}{2:>14}".format(*header))
print("{0:<10}{1:>10}{2:>14}".format(*diana))
print("{0:<10}{1:>10}{2:>14}".format(*john))
print("{0:<10}{1:>10}{2:>14}".format(*brittany))
print("{0:<10}{1:>10}{2:>14}".format(*hannah))

#Extra Task
#Given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide?  
given_t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(("{:>5}" * 10).format(*given_t))

