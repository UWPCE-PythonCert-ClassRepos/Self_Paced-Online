# Dictionaries 1
# Create a dictionary containing “name”, “city”, and “cake” for “Chris”
# from “Seattle” who likes “Chocolate” (so the keys should be: “name”,
# etc, and values: “Chris”, etc.)

d = {'name': 'Chris',
     'city': 'Seattle',
     'cake': 'Chocolate'}

#Display the dictionary.
print(d)

# delete the entry for "cake"
d.pop('cake')

#Display the dictionary.
print(d)

#Add an entry for “fruit” with “Mango” and display the dictionary.
d['fruit'] = 'Mango'
print(d)

# Display the dictionary keys.
print(d.keys())

# Display the dictionary values.
print(d.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in d.keys())

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Mango' in d.values())

# Dictionaries 2
# Using the dictionary from item 1: Make a dictionary using the same keys but
# with the number of ‘t’s in each value as the value (consider upper and
# lower case?).
dt = {}
for entry in d:
    dt[entry] = entry.lower().count('t')

# quick tests to verify above worked
assert dt['name'] == 0
assert dt['city'] == 1
print(dt)

# Sets 1
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s2 = set(range(0,21,2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))

# Display the sets.
print(f's2: {s2}')
print(f's3: {s3}')
print(f's4: {s4}')

# Display if s3 is a subset of s2 (False)
print (f's3 subset of s2: {s3 <= s2}')

# and if s4 is a subset of s2 (True).
print(f's3 subset of s2: {s4 <= s2}')

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
letters = set('Python')
letters.update('i')
print(letters)

# Create a frozenset with the letters in ‘marathon’.
frozen_letters = frozenset('marathon')

# display the union and intersection of the two sets.
print(f'union: {letters.union(frozen_letters)}')
print(f'intersection: {letters & frozen_letters}')
