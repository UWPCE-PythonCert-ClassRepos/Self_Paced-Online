#!/usr/bin/env python3

#TASK ONE
info = (2, 123.4567, 10000, 12345.67)
print(f"file_{info[0]:03d}: {info[1]:.2f}, {info[2]:.2E}, {info[3]:.2E}")


#TASK TWO
print("file_{:03d}: {:.2f}, {:.2E}, {:.2E}".format(info[0], info[1], info[2], info[3]))


#TASK THREE
def formatter(*x):
    temp_string1 = ""
    for i in range(len(x)):
        if temp_string1:
            temp_string1 += ", "
        temp_string1 += "{:d}" # for x = (1, 2, 3, 4) temp_string = "{:d}{:d}{:d}{:d}"
    temp_string2 = "the {:d} numbers are: ".format(len(x))
    return print(temp_string2 + temp_string1.format(*x))

formatter(1, 2, 3, 4, 5, 6)


#TASK FOUR
given_tuple = (4, 30, 2017, 2, 27)
print(f"{given_tuple[3]:02d} {given_tuple[4]:02d} {given_tuple[2]:02d} {given_tuple[0]:02d} {given_tuple[1]:02d}")


#TASK FIVE
given_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {given_list[0][:-1]} is {given_list[1]} and the weight of a {given_list[2][:-1]} is {given_list[3]}")
print(f"The weight of an {given_list[0][:-1].upper()} is {given_list[1] * 1.2} and the weight of a {given_list[2][:-1].upper()} is {given_list[3] * 1.2}")


#TASK SIX
data = (('name', 'age', 'cost'), ('Brandy', '18y', '$1,000.00'), ('Gin', 'not aged', '$55.99'), ('Whiskey', '22y', '$12,000.00'))
for row in data:
    print("{:>12}{:>12}{:>12}".format(*row))

new_given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#unsure what you want here
#way 1 - one line, not short (i.e., no automation):
print("{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(*new_given_tuple))
#way 2 - not one line, but short (i.e., uses automation):
for l in range(len(new_given_tuple)):
    print("{:>5}".format(new_given_tuple[l]), end = "")
print()