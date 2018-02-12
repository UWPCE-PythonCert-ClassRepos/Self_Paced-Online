"""
•Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
•Display the dictionary.
•Delete the entry for “cake”.
•Display the dictionary.
•Add an entry for “fruit” with “Mango” and display the dictionary. 
•Display the dictionary keys.
•Display the dictionary values.
•Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
•Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""
def dictionary1(person_dict):
    print(person_dict)
    person_dict.pop('cake')
    print(person_dict)
    person_dict['fruit']='Mango'
    print(person_dict)
    print('keys in dict')
    for k in person_dict:
        print(k)

    print('values in dict')
    for v in person_dict.values():
        print(v)

    print('Is cake a key in the dict? {}'.format(str('cake' in person_dict)))
    print('Is Mango a value in the dict? {}'.format(str('Mango' in person_dict.values())))

def dictionary2(person_dict):
    for k,v in person_dict.items():
        person_dict[k] = v.lower().count('t')

    print(person_dict)     


if __name__ == '__main__':

    person_dict = { 'name':'Chris', 'city':'Seattle', 'cake':'Chocolate' }
    dictionary1(person_dict.copy())
    dictionary2(person_dict.copy())

