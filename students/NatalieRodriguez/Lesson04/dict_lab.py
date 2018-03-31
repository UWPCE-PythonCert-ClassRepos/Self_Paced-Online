#$ chmod +x dict_lab.py

#Lesson 04: Dictionary Labs
#Natalie Rodriguez
# March 28, 2018

#Dictionaries1

d = {} #created a blank dictionary to populate
d['Name'] = 'Chris'
d['City'] = 'Seattle'
d['Cake'] = 'Chocolate'

print(d)

d.pop('Cake')
print(d)

d['Fruit'] = 'Mango'
print(d)

for key, value in d.items() :
    print (key)

for key, value in d.items() :
    print (value)

if 'Cake' == key:
    print(True)
else: print("There is no cake in this dictionary.")

if 'Mango' == value:
    print(True)
else: print("there are no mangos in this dictionary.")


#Dictionaries2

dict_two = {'Name': 'Natalie Rodriguez', 'City': 'Kansas City', 'Cake': 'Funfetti'}

new_dict = {'Name': dict_two['Name'].lower().count('t'),
            'City': dict_two['City'].lower().count('t'),
            'Cake': dict_two['Cake'].lower().count('t')}
print('\n', new_dict, '\n')

print("You've reached the end of the code.")



