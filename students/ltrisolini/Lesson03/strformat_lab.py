#!/usr/bin/env python3

#Task1

values = (2, 123.4567, 10000, 12345.67)
strformat = 'file_{:03d}: {:05.2f}, {:.2E}, {:.2E}'
output = strformat.format(*values)

print("Task1 : "+ output)

#Task2

strformat2 = 'file_{a[0]:03d}: {a[1]:05.2f}, {a[2]:.2E}, {a[3]:.2E}'
output1 = strformat2.format(a=values)

output2 = f'file_{values[0]:03d}: {values[1]:05.2f}, {values[2]:.2E}, {values[3]:.2E}'

print("Task2 : "+ output1)
print("Task2 : "+ output2)

#Task3


def strformat(seq):
    l = len(seq)
    return (('The {} numbers are: ' + ", ".join(['{}']*l)).format(l, *seq))

print("Task3 : "+ strformat(values))

#Task4

tup = (4, 30, 2017, 2, 27)

print("Task4 : "+f"{tup[3]:02d} {tup[4]:02d} {tup[2]:02d} {tup[0]:02d} {tup[1]:02d}")

#Task5

given = ['oranges', 1.3, 'lemons', 1.1]
output3 = f"The weight of an {given[0][:-1]} is {given[1]} and the weight of a {given[2][:-1]} is {given[3]}"
output4 = f"The weight of an {given[0][:-1].upper()} is {given[1]*1.2} and the weight of a {given[2][:-1].upper()} is {given[3]*1.2}"

print("Task5 : "+output3)
print("Task5 : "+output4)

#Task6

wines = [("Brunello", 120, 4), ("Chianti", 50, 6), ("Pinot", 76, 15), ("Cabernet", 500, 30), ("Chardonnay", 12, 5)]
for wine in wines:
    print("Task6 : "+"{:10} ${:7,} {:6} years old".format(*wine))

list1 = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
list2 = []
for x in list1:
    list2.append(x*500)

print("Task6 : "+("{:5}" * 10).format(*list1))
print("Task6 : "+("{:5}" * 10).format(*list2))
