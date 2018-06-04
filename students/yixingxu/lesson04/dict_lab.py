#!/usr/bin/env python3
# Dictionaries 1
# Create a dictionary containing 
# “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
dict = {'name': 'Chris'
        ,'city': 'Seattle'
        ,'cake': 'Chocolate'}        
print(dict)
# Delete the entry for “cake”.
dict.pop('cake')
print(dict)
# Add an entry for “fruit” with “Mango” and display the dictionary.
dict['fruit'] = 'Mango'
print(dict.keys())
print(dict.values())
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now)
print('whether or not “cake” is a key in the dictionary: ' +str('cake' in dict))
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('whether or not “Mango” is a value in the dictionary: '+ str('Mango' in dict.values()))

# Dictionaries 2
for key,value in dict.items():
    dict[key] = key.lower().count('t')
print(dict)
    
# Sets 1
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s2=set()
s3=set()
s4=set()
for i in range(21):
    if i%2 == 0:
        s2.update([i])
    if i%3 == 0:
        s3.update([i])
    if i%4 == 0:
        s4.update([i])
print(s2,'\n',s3,'\n',s4)
# Display if s3 is a subset of s2 (False)
print('s3 is a subset of s2? ', s3.issubset(s2))
# if s4 is a subset of s2 (True).
print('s4 is a subset of s2? ', s4.issubset(s2))

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
setP = set('Python')
setP.update(['i'])
# Create a frozenset with the letters in ‘marathon’.
setM = frozenset('marathon')
# display the union and intersection of the two sets.
print('union of the two sets: ',setP.union(setM))
print('intersection of the two sets: ',setP.intersection(setM))
