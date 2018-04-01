
user_dict = {'name':'chris', 'city':'Seattle', 'cake':'chocolate'}

# Dictionaries 1 #

print(user_dict)
del user_dict['cake']
print(user_dict)
user_dict['fruit'] = 'Mango'
print(user_dict)

print(user_dict.keys())
print('\nCake in user_dict? ' + str(('cake' in user_dict.keys())))
print('Mango in user_dict?  ' + str(('Mango' in user_dict['fruit'])))
print(user_dict)

# Dictionaries 2 #

new_user_dict = {}

for key, value in user_dict.items():
    new_user_dict[key] = value.lower().count('t')
print(new_user_dict)