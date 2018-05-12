#!/usr/bin/env python

#Lesson 4 Dictionary Lab

#Dictionaries 1
dict_1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake':'Chocolate'}
print(dict_1)

dict_1.pop('cake')
print(dict_1)

dict_1['fruit'] = 'Mango'
print(dict_1)
print(dict_1.keys())
print(dict_1.values())
print('cake' in dict_1)
print('Mango' in dict_1.values())


#Dictionaries 2
dict_t = dict()
for k, v in dict_1.items():
    dict_t[k] = v.count('t')
print(dict_t)


#Sets 1
s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if not i % 2:
        s2.add(i)
    if not i % 3:
        s3.add(i)
    if not i % 4:
        s4.add(i)
print(s2, s3, s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
s = set('Python')
s.add('i')
print(s)
fs = frozenset('marathon')
print(fs)
print(s.union(fs))
print(s.intersection(fs))