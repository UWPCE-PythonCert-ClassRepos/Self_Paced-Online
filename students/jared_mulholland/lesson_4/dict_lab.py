
#Dictionaries 1

#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
#Display the dictionary.
#Delete the entry for “cake”.
#Display the dictionary.
#Add an entry for “fruit” with “Mango” and display the dictionary.
#Display the dictionary keys.
#Display the dictionary values.
#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
#Display whether or not “Mango” is a value in the dictionary (i.e. True).

print("Dictionaries\n")

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print("\n1. Create and display dictionary\n")
print(d.items())

print("\n2. Delete the entry for 'cake' and display dictionary\n")
d.pop('cake')
print(d.items())

print("\n3. Add an entry for \"fruit\" with \"Mango\" and display the dictionary.\n")
d['fruit'] = 'Mango'
print(d.items())

print("\n4. Display the dictionary keys\n")
print(d.keys())

print("\n5. Display the dictionary values\n")
print(d.values())

print("\n6. Display whether or not \"cake\" is a key in the dictionary\n")
print("cake" in d)

print("\n7. Display whether or not \"Mango\" is a value in the dictionary\n")
print("Mango" in d.values())


#Dictionaries 2

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).

print("\nDictionaries 2\n")

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

d = {'name': 'Chris'.lower().count('t'), 'city': 'Seattle'.lower().count('t'), 'cake': 'Chocolate'.lower().count('t')}

print(d.items())


