#$ chmod +x dict_lab.py

#Lesson 04: Dictionary Lab
#Natalie Rodriguez
# March 28, 2018

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


print("you've reached the end of the code")



