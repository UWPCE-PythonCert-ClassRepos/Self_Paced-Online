#!/usr/bin/env python3

# task 1 - print formatted string line from tuple values
tuple1 = (2, 123.4567, 10000, 12345.67)
print("{}{:0>3d}: {:.2f}, {:.2e}, {:.3e}".format("file_",tuple1[0],tuple1[1],tuple1[2], tuple1[3]))
print("")
# task 2 - repeat task 1 with different format codes
print(f"file_{tuple1[0]:0>3d}: {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.3e}")
print("")
# task 3 - 
tuple3 = (1,2,3)
print("the 3 numbers are: {:d}, {:d}, {:d}".format(*tuple3))


print("")
# task 4 - 

print("")
# task 5 - f-string
list5 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {list5[0][:-1]} is {list5[1]} and the weight of a {list5[2][:-1]} is {list5[3]}")
print(f"The weight of an {list5[0][:-1].upper()} is {list5[1] * 1.2} and the weight of a {list5[2][:-1].upper()} is {list5[3] * 1.2}")
print("")
# task 6 - 

