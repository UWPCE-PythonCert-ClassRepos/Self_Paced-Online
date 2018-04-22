d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)

d.pop('cake')
print(d)

d.update({'fruit': 'Mango'})
print(d)

print(d.keys())
print(d.values())

print('cake' in d)
print('fruit' in d)

dict2 = {}
for k, v in d.items():
  dict2[k] = v.count('t') + v.count('T')

print(dict2)

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if not i%2:
        s2.add(i)
    if not i%3:
        s3.add(i)
    if not i%4:
        s4.add(i)

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

s = set('Python')
s.add('i')
print(s)

fs = frozenset('marathon')
print(fs)
print("union:", s.union(fs))
print("intersection:", s.intersection(fs))
