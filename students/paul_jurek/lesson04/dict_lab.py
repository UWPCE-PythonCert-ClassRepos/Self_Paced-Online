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