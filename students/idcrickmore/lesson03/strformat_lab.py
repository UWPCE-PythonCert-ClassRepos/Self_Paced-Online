#!/usr/bin/env python3

# task 1
tup = (2, 123.4567, 10000, 12345.67)

print("--------------- Task 1 ---------------")
# format tuple values as string using decimal, float and exponent .format
print("file{:0>3d}: {:.2f}, {:.2e}, {:.2e} \n"
      .format(tup[0], tup[1], tup[2], tup[3]))


# task 2
print("--------------- Task 2 ---------------")
# this time run the whole tuple through the .format instead of manually
# referencing individual values
print("file{:0>3d}: {:.2f}, {:.2e}, {:.2e} \n".format(*tup))


# task 3
print("--------------- Task 3 ---------------")


def formatter(in_tuple):
    # counts the length of the tuple
    length = len(in_tuple)
    # creates the appropriate number of curly brackets from 'length' and .join
    # then populates each one by dumping the whole tuple into .format
    formatted_string = ("the {} numbers are " +
                        ", ".join(["{}"]*length)).format(length, *in_tuple)
    print(formatted_string)
    # the instructions specifically say to 'return' the formatted string, so...
    return(formatted_string)


formatter((1, 2, 3, 4))
formatter((2, 3, 5, 7, 9))


# task 4
print("--------------- Task 4 ---------------")
# rearrange the order of date and time, and pad with zeros
d = (4, 30, 2017, 2, 27)
d2 = "{:0>2d} {:0>2d} {} {:0>2d} {:0>2d}".format(d[3], d[4], d[2], d[0], d[1])
print(d2)


# task 5
print("--------------- Task 5 ---------------")
list = ['oranges', 1.3, 'lemons', 1.1]
# use f-string to format the sentences, don't forget to drop the s's
print(f"the weight of an {list[0][:-1]} is {list[1]} and the weight of a" +
      f"{list[2][:-1]} is {list[3]}")
# add some formatting to make all caps and multiply weights
list = ['oranges', 1.3, 'lemons', 1.1]
print(f"the weight of an {list[0][:-1].upper()} is {list[1]*1.2} and the" +
      f"weight of a {list[2][:-1].upper()} is {list[3]*1.2}")

# task 6
print("--------------- Task 6 ---------------")
columns = ("NAME", "AGE", "COST")
age_cost = (["Kelp", 1, 100], ["Bamboo", 20, 300],
            ["Oak", 300, 5000], ["Sequoia", 2000, 50000])
# left align all the values in the tuples and lists into columns
print('{:<20} {:<10} {:<10}'.format(*columns))
for name in age_cost:
    print('{:<20} {:<10} ${:<10}'.format(*name))
