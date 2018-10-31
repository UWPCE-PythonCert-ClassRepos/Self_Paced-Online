d = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
print(d)
d.pop('cake')
print(d)
d['fruit'] = 'Mango'
d.keys()
d.values()
print('cake' in d)
print('Mango' in d.values())

d = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
d2 = {}
d2['name'] = d['name'].count('t')
d2['city'] = d['city'].count('t')
d2['cake'] = d['cake'].count('t')
print(d2)

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if i % 2 == 0:
        s2.update([i])
    if i % 3 == 0:
        s3.update([i])
    if i % 4 == 0:
        s4.update([i])
print("s2 is ", s2)
print("s3 is ", s3)
print("s4 is ", s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

s2 = set()
for i in "Python":
    s2.update([i])
s2.update(['i'])
print(s2)

fs1 = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
print(s2.union(fs1))
print(s2.intersection(fs1))

import os
place = os.getcwd()
for root, dirs, files in os.walk(".", topdown=False):
    print (place, '\\', files[0])