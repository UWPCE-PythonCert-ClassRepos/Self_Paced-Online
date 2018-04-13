# Part 1 complete
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print (dict1)
dict1.pop('cake')
print (dict1)
dict1['fruit'] = 'Mango'
print(dict1)
print(dict1.keys())
print(dict1.values())
print('cake' in dict1)
print('Mango' in dict1.values())

# Part 2 complete
dict2 = {}
for key,value in dict1.items():
    dict2[key]=value.lower().count('t')
print(dict2)

s2 = set(range(0,21,2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))



s5 = set('Python')
s5.add('i')
s6=frozenset('marathon')
print(s5.union(s6))
print(s5.intersection(s6))



