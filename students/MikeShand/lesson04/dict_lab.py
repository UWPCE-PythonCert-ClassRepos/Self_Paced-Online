#!/usr/bin/env python

dictionary = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

print(dictionary)

dictionary.popitem()

print(dictionary)

dictionary["fruit"] = "Mango"

print(dictionary.keys())

print(dictionary.values())

print("cake" in dictionary.keys())

print("Mango" in dictionary.values())

dictionary = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

dictionary1 = dictionary.copy()
for key, value in dictionary.items():
    dictionary1[key] = value.lower().count('t')

print(dictionary1)

s2=set()
s3=set()
s4=set()

for i in range(21):
    if i%2 == 0:
        s2.add(i)
    if i%3 == 0:
        s3.add(i)
    if i%4 == 0:
        s4.add(i)

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


p=set("Python")
p.add("i")

m=frozenset('marathon')

print(p.union(m))
print(p.intersection(m))

