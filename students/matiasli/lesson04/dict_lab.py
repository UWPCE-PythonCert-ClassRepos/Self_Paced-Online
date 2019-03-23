#!/usr/bin/env python3


# Part 1

# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who 
# likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)

d = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'chocolate')])

print(d)
d.pop('cake')
print(d)

d.update( [('fruit', 'Mango')] )

for key in d:
    # Iterates just through the keys, ignoring the values
    print(key)
for value in d.values(): 
    # Iterates just through value, ignoring the keys
    print(value)
print ( 'cake' in d )
print ( 'Mango' in d.values() )

# Part 2
d2 = {}
for key2 in d:
    d2[key2] = (d.get(key2)).count('t') + (d.get(key2)).count('T')

print(d2)


# sets 1
s2 = set()
s3 = set()
s4 = set()

for i in range(1,20):
    if(i%2) == 0:
        s2.add(i)
    if(i%3) == 0:
        s3.add(i)
    if(i%4) == 0:
        s4.add(i)

print(s2,'\n',s3,'\n',s4)
print(s3.issubset(s2))
print(s4.issubset(s2))


# sets 2
set2 = ('P', 'y', 't', 'h', 'o', 'n')
set2 = set(set2)

print(set2)
set2.add('i')
print(set2)

set3 = ('m', 'a', 'r', 'a', 't', 'h', 'o', 'n')
set3 = frozenset(set3)

print(set2.union(set3))
print(set2.intersection(set3))





