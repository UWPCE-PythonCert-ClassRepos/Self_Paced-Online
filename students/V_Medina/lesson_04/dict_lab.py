"""
VIctor Medina
1/19/2019
Assignment 4
"""
# Dictionaries 1
person_info={'name':'Chris',
             'city':'Seattle',
             'cake':'Chocolate'
             }
print(person_info)
person_info.pop('cake')
person_info['fruit']='Mango'
print(person_info.keys())
print(person_info.values())
print(person_info.get('cake', 'False'))
print('Mango' in person_info.values())


# Dictionaries 2
