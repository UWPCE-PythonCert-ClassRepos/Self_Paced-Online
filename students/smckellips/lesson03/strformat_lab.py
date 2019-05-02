#! /usr/bin/env python

#Task One
input = ( 2, 123.4567, 10000, 12345.67)
print("file_{:03d} :  {:.2f}, {:.2e}, {:.2e}".format(*input))

#Task Two
print(f"file_{input[0]:03d} :  {input[1]:.2f}, {input[2]:.2e}, {input[3]:.2e}")

#Task Three

def display_seq(seq):
    l = len(seq)
    return  ("The {} numbers are: " + ", ".join(["{}"] * l)).format(l,*seq) 

print(display_seq(input))

#Task Four
tup = ( 4, 30, 2017, 2, 27)
print( "{:02d} {} {} {:02d} {}".format(tup[3], tup[4], tup[2], tup[0], tup[1], ))

#Task Five
five = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {five[0][:-1]} is {five[1]} and the weight of a {five[2][:-1]} is {five[3]}")
print(f"The weight of an {five[0][:-1].upper()} is {five[1] * 1.2} and the weight of a {five[2][:-1].upper()} is {five[3] * 1.2}")

#Task Six
inputs = [["Mary", 18, 9.99],["Molly", 28, 999.99],["Maryann", 38, 9999.99]]
max_len = [0] * 3 
for input in inputs:
    length = [len(str(i)) for i in input]
    maxLength = [ max(max_len[e[0]], e[1]) for e in enumerate(length) ]

for input in inputs:
    print ("{:<{width0}} {:<{width1}} {:>{width2}}".format(*input,width0=maxLength[0],width1=maxLength[1], width2=maxLength[2]))

#Extra Task
tup = tuple(range(10))
print(("{:5}" * 10).format(*tup))

