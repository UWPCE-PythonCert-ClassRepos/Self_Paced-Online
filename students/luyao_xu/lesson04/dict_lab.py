#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

""" Basic ins and outs of python dictionaries and sets"""

"""Dictionaries 1"""
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
diction = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
# Display the dictionary
print(diction)
# Delete the entry for “cake”
dict.popitem(diction)
# Display the dictionary
print(diction)
# Add an entry for “fruit” with “Mango” and display the dictionary
diction['fruit'] = 'Mango'
# Display the dictionary keys
print(diction.keys())
# Display the dictionary values
print(diction.values())
# Display whether or not “cake” is a key in the dictionary
print('cake' in diction.keys())
# Display whether or not “Mango” is a value in the dictionary
print('Mango' in diction.values())
diction = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}


"""Dictionaries 2"""

# Using the dictionary from item 1
diction = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
item_copy = diction.copy()
# Make a dictionary using the same keys but with the number of ‘t’s in each value as the value
for i in item_copy:
    item_copy[i] = item_copy[i].lower().count('t')
print(item_copy)


"""Sets 1"""
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4
s2 = set(range(0, 20, 2))
s3 = set(range(0, 20, 3))
s4 = set(range(0, 20, 4))
# Display the sets.
print(s2)
print(s3)
print(s4)
# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))
# Display if s4 is a subset of s2 (True)
print(s4.issubset(s2))




