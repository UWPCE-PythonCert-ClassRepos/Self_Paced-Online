#!/usr/bin/env python3
print("")

# Dictionaries 1
print("Dictionaries 1")
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)
print(dict1.get('cake'))
print(dict1)
dict1['fruit'] = 'mango'
print(dict1.keys())
print(dict1.values())
result = 'cake' in dict1
print("cake in dictionary: ", result)
result = 'mango' in dict1.values()
print("mango in dictionary: ", result)
print("")

# Dictionaries 2
print("Dictionaries 2")
# make copy of dict1
dict2 = dict1.copy()
print("dict2: ", dict2)
# replace dict2 values with count of "t" in each value
for k,v in dict2.items():
    dict2[k] = v.count('t')
print("dict2: ", dict2)
print("")

# sets 1 - create sets s2, s3 and s4, test if issubset
s2 = set()
for number in range(0, 21):
    #print(number)
    if number % 2 == 0:
        s2.update([number])
    if number % 4 == 0:
        s2.update([number])
    if number % 5 == 0:
        s2.update([number])
print(s2)
s3 = s2.copy()
s4 = s2.copy()
print("set2: ", s2)
print("set3: ", s3)
print("set4: ", s4)
print("s3 is subset of s2: ", s3.issubset(s2))
print("s4 is subset of s2: ", s4.issubset(s2))
print("")

# sets 2 - create sets with string and add 'i' to set, create frozen set and display union and intersection of the two sets
set5 = set()
print(set5)
for letter in "Python":
    set5.update([letter])
set5.update(["i"])
print("set5: ", set5)
set6 = set()
for letter in "marathon":
    set6.update([letter])
set6fs = frozenset(set6)
print("frozen set6: ", set6fs)
# display union and intersection between set5 and set6fs
set7 = set()
set7 = set5.union(set5,set6fs)
print("union: ", set7)
set8 = set5.intersection(set5,set6fs)
print("intersection: ", set8)
print("")


    

