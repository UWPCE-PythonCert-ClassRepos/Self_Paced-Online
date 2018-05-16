#!/usr/bin/env python3
# Description: This program will teach the user about string formatting.
# Developer: Ryan Hamersky
# Date: 05/12/2018
# Rev: A - 05/15/2018 add comments to the code.

#'file_002 :   123.46, 1.00e+04, 1.23e+04'

# -----Data Section-----

t = (2,123.4567,10000,12345.67)

# print(t)  # --> Used to display the tuple for testing purposes.

# -----Process Section-----
print("Part 1")
print()  # --> Formatting

string1 = "file_{:03d}: {:.2f}, {:.2E}, {:.2E}"

# print(string1)  # --> Used during testing and be bugging.

print(string1.format(*t))  # --> String formatting method 1 used.

print()  # --> Formatting
print("Part 2")
print()  # --> Formatting

string2 = "file_%03d: %.2f, %.2E, %.2E"

print(string2%t)  # --> String formatting mathod 2 used.

#"the 3 numbers are: {:d}, {:d}, {:d}".format(*t)

print()  # --> Formatting
print("Part 3")
print()  # --> Formatting

def tupleformatter(in_tuple):
    '''
    Tuple formatter
    :param in_tuple: Tuple passed in to function.
    :return: Returns fstring
    '''
    length = len(in_tuple)  # --> Gets length of tuple
    fstring = ("the {} numbers are: " + ", ".join(["{}"]*length))
    return fstring.format(length, *in_tuple)

print(tupleformatter(t))

print()  # --> Formatting
print("Part 4")
print()  # --> Formatting

t2 = (4, 30, 2017, 2, 27)

string3 = "0{0[3]} {0[4]} {0[2]} 0{0[0]} {0[1]}"  # --> Reorganizes the tuple and formats it.

print(string3.format(t2))

print()  # --> Formatting
print("Part 5")
print()  # --> Formatting

l = ["oranges", 1.3, "lemons", 1.1]

string4 = f"The weight of an {l[0]} is {l[1]} and the weight of a {l[2]} is {l[3]}"

print(string4)

string5 = f"The weight of an {l[0].upper()} is {l[1]*1.2} and the weight of a {l[2].upper()} is {l[3]*1.2}"

print(string5)

print()  # --> Formatting
print("Part 6")
print()  # --> Formatting

t3 = (["Ashely", "20", "$90.00"],["Bill", "38", "$200.00"],["Tony", "83", "$4000.00"])

# Formats tuple into a readable table.
max_length = max(len(word)for row in t3 for word in row)
for list in t3:
    for item in list:
        print(("{0:{padding}}".format(item,padding=max_length)), end=" ")
    print()

# print(*t3)  # --> Used for testing


print()  # --> Formatting
print("Extra Task")
t4 = (0,1,2,3,4,5,6,7,8,9)

print("{:{width}} {:{width}} {:{width}} {:{width}} {:{width}} "
      "{:{width}} {:{width}} {:{width}} {:{width}} {:{width}}".format(*t4, width=5))

input("\n" + "Press enter to exit. ")
