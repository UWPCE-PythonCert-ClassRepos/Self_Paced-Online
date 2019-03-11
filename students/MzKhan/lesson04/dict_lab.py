'''
Name: Muhammad Khan
Date: 03/05/2019
Assignment04

'''

# Activity 1: Dictionary and Set Lab.

# Dictionaries 1

# Create a dictionary.

d = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}

# display the dictionary.

print(d)

# delete the entry for cake.

d.pop('cake')

print(d)

# •Add an entry for “fruit” with “Mango” and display the dictionary.

d.update({'fruit':'Mango'})

print(d)

# Display the dictionary keys.

print(d.keys())

# Display the dictionary values.

print(d.values())

# Display whetehr or not "cake" is a key in the dictionary.
# iter(d) is equivalent of d.keys()
# (for key in d) is equivalent of (for key in d.keys()).

print( 'cake' in d.keys())

# Display whether or not “Mango” is a value in the dictionary (i.e. True).

print('Mango' in d.values())

# Dictionary 2.
d = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
new_d = {}
for key in d.keys():
    new_d[key] = d[key].count('t')+d[key].count('T')
print(new_d)



# Set 1.
# create sets.
s2 = set(); s3 = set(); s4 = []
for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.append(i)
else:
    s4 = set(s4)       # convert the list to a set using the set constructor.
# Display the sets.
print("s2: ",s2)
print("s2: ",s3)
print("s4: ",s4)

# Display if s3 is a subset of s2. (false)

print(s3.issubset(s2))

# Display if s4 is a subset of s2. (true)

print(s4.issubset(s2))

# Set 2.

# Create a frozen set with teh letters in 'Python' and add i' to the set.

frozen_set = frozenset('python')     # Frozen set is immutable adn it doesn't allow add operation.

# Create a frozenset with the letters in ‘marathon’.

frozen_set2 = frozenset('marathon')

# display the union and intersection of the two frozen sets.

print(frozen_set.union(frozen_set2))
print(frozen_set.intersection(frozen_set2))






