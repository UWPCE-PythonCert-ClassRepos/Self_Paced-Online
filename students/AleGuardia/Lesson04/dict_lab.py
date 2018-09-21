#!/usr/bin/env python3

dict_example = {"name":"Chris","city":"Seattle","cake":"Chocolate"}

# Dictionary 1

print(dict_example)
dict_example.pop("cake")
dict_example['fruit'] = "Mango"
dict_example.keys()
dict_example.values()
"cake" in dict_example
"Mango" in dict_example.values()


# Dictionary 2

# Using the dictionary from item 1: Make a dictionary
# using the same keys but with the number of ‘t’s in each value as the value
# (consider upper and lower case?).

dict_example2 = {}
for i in dict_example:
    dict_example2[i] = dict_example[i].lower().count('t')

