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