#!/usr/bin/env python3

# Dictionaries 1
d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(d)
d.pop("cake")
print(d)
d["fruit"] = "Mango"
print(d)
print(d.keys())
print(d.values())
print("cake is key: " + str("cake" in d))

# Dictionaries 2
d = {"name":"Chris".lower().count('t'), "city":"Seattle".lower().count('t'), "cake":"Chocolate".lower().count('t')}
print(d)

#Sets 1
s2 = set(range(2, 21, 2))
s3 = set(range(3, 21, 3))
s4 = set(range(4, 21, 4))
print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
s = set('python')
s.add('i')
s2 = frozenset('marathon')
print(s2.union(s))
print(s2.intersection(s))