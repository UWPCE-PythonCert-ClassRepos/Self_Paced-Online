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







