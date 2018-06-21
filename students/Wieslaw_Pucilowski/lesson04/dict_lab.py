#!/usr/bin/env python3
__author__="Wieslaw Pucilowski"

# Dictionaries 1

dict1 = {'name': 'Chris', 'citi': 'Seattle', 'cake': 'Chocolate'}

print(dict1)
for k, v in dict1.items():
    print('Key: {:<10} Value: {:<20}'.format(k,v))

dict1.pop('cake')
print(dict1)
for k, v in dict1.items():
    print('Key: {:<10} Value: {:<20}'.format(k,v))

dict1['fruit']='Mango'

# print keys and values
print('Dictionary values: '+( ', '.join(["{}"]*len(dict1.values())) ).format(*dict1.values()) )
print('Dictionary keys: '+( ', '.join(["{}"]*len(dict1.keys())) ).format(*dict1.keys()) )

# check key , values
print('checks if \'{}\' is a key: {}'.format('cake', 'cake' in dict1.keys()))
print('checks if \'{}\' is a value: {}'.format('Mango', 'cake' in dict1.values()))


# Dictionary 2
dict2={}
for k, v in dict1.items():
    dict2[k] = v.lower().count('t')

print(dict2)

# Set 1
# •Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
# Display the sets.
# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).

# create sets
s2=set()
s3=set()
s4=set()

for i in range(0,21):
    if i%2 == 0:
        s2.update([i])
    if i%3 == 0:
        s3.update([i])
    if i%4 == 0:
        s4.update([i])
        
print('{}: {}'.format('s2',s2))
print('{}: {}'.format('s3',s3))
print('{}: {}'.format('s4',s4))

print('Check if {} is subset of {}: {}'.format('s3','s2',s3.issubset(s2)))
print('Check if {} is subset of {}: {}'.format('s4','s2',s4.issubset(s2)))

# Set 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
# Create a frozenset with the letters in ‘marathon’.
# display the union and intersection of the two sets.

s=set(list('Python'))
s.add('i')
fs=frozenset(list('marathon'))
print('set {} union with set {}: {}'.format('s','fs',s.union(fs)))
print('set {} intersection with set {}: {}'.format('s','fs',s.intersection(fs)))
