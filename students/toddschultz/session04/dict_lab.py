#!/usr/bin/env python3

# Dictionaries 1

d = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
print(d)
d.pop('cake')
print(d)
d['fruit'] = 'Mangos'
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
d.get('Mangos')

vals = d.values()
if 'cake' in vals:
    print("We have cake!")
else:
    print("We have no cake.")

if 'Mangos' in vals:
    print("We have Mangos!")
else:
    print("We have no Mangos.")

# Dictionaries 2
def dictionaries2(s):
    count = dict()
    for i in s:
        count = d[i].count('t') + d[i].count('T')
        d[i] = count
    print(d) 
dictionaries2(d)

# Sets 1

s2 = set([])
s3 = set([])
s4 = set([])
for i in range(21):
    if i % 2 == 0:
        s2.update([i])
for i in range(21):
    if i % 3 == 0:
        s3.update([i])
for i in range(21):
    if i % 4 == 0:
        s4.update([i])
print(s2)
print(s3)
print(s4)

if s3.issubset(s2):
    print("S3 is a subset of S2")
else:
    print("S3 is not a subset of S2")

if s4.issubset(s2):
    print("S4 is a subset of S2")
else:
    print("S4 is not a subset of S2")


# Sets 2
s5 = set(["p", "y", "t", "h", "o", "n"])
s5.update("i")
s6 = set(("m", "a", "r", "a", "t", "h", "o", "n"))
print(s6.union(s5))
print(s6.intersection(s5))












