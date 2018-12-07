#!/usr/bin/env python3

# task 1 - print formatted string line from tuple values
tuple1 = (2, 123.4567, 10000, 12345.67)
print("{}{:0>3d}: {:.2f}, {:.2e}, {:.3e}".format("file_",tuple1[0],tuple1[1],tuple1[2], tuple1[3]))
print("")

# task 2 - repeat task 1 with different format codes
print(f"file_{tuple1[0]:0>3d}: {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.3e}")
print("")

# task 3 - function with tuple input of variable amount. output is count of tuple items and formatted values
tuple3 = (1, 2, 3, 4, 5, 6, 7)
def func_task3(input3):
    len1 = len(input3)
    form_string = "{:d}," * len1
    print("the ", len1, "numbers are: ", form_string.format(*input3))
    
func_task3(tuple3)
print("")

# task 4 - output tuple items in string format specific index order
tuple5 = (4, 30, 2017, 2, 27)
print(f"{tuple5[3]:0>2d} {tuple5[4]} {tuple5[2]} {tuple5[0]:0>2d} {tuple5[1]}")
print("")

# task 5 - f-string
list5 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {list5[0][:-1]} is {list5[1]} and the weight of a {list5[2][:-1]} is {list5[3]}")
print(f"The weight of an {list5[0][:-1].upper()} is {list5[1] * 1.2} and the weight of a {list5[2][:-1].upper()} is {list5[3] * 1.2}")
print("")

# task 6 - print aligned data columns
arr6 = [['Joey', 30, 199.99], ['Jan', 36, 29999.97], ['Bob', 55, 999999.99]] 
len6 = len(arr6)
count1 = 0
print(len6)
while count1 < len6:
    print("{:10} {:3} {:>20}".format(arr6[count1][0], arr6[count1][1], arr6[count1][2]))
    count1 += 1
print("")

# task 6 XC - print 5 column tuple
tup6 = (1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000)
print("{:5},{:5},{:5},{:5},{:5},{:5},{:5},{:5},{:5},{:5}".format(*tup6))
    
    
