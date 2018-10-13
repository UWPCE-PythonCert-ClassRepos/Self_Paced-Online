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


# Sets 1

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    for j in range(2,5):
        if i%j == 0:
            globals()["s{}".format(j)].update([i])
        else:
            continue

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2

s_p = set("Python")
s_p.update("i")
mar = frozenset('marathon')
print(s_p.intersection(mar))
print(s_p.union(mar))