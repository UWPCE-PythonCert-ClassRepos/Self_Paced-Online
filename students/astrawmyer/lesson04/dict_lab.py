#!/usr/bin/env python3

dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)
dict1.pop('cake')
print(dict1)
dict1['fruit'] = 'Mango'
print(dict1.keys())
print(dict1.values())


if 'cake' in dict1:
    print(True)
else:
    print(False)

for value in dict1.values():
    if value == "Mango":
        print(True)


dict2 = dict1.copy()

for key in dict2:
    t = dict2[key].count("t")
    t = t + dict2[key].count("T")
    dict2[key] = t
print(dict2)


#Set exercises

s2 = set([2,4,6,8,10,12,14,16,18,20])
s3 = set([3,6,9,12,15,18])
s4 = set([4,8,12,16,20])

print(s3.issubset(s2))
print(s4.issubset(s2))