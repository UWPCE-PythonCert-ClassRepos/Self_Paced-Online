#!/usr/bin/env python3


#Dictionaries 1
d1 = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}
print(d1)

d1.pop('cake')
print(d1)

d1['fruit'] = 'Mango'
print(d1.keys())
print(d1.values())
print('cake' in d1.keys())


#Dictionaries 2
d2 = d1.copy()
for key in d2:
    d2[key] = d2[key].lower().count('t')
print(d2)

#Set1
s2 =set()
s3 =set()
s4 =set()

for i in range(0,21):
    if i % 2 ==0:
        s2.add(i)
    if i % 3 ==0:
        s3.add(i)
    if i % 4 ==0:
        s4.add(i)

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

#set2
s = set('Python')
s.add('i')
print(s)
fs=frozenset('marathon')
print(s.union(fs))
print(s.intersection(fs))
