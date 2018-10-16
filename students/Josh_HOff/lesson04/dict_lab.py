def dictionary1():
    personal_details = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(personal_details)
    del personal_details['cake']
    print(personal_details)
    personal_details['fruit'] = 'Mango'
    print(personal_details)
    print(personal_details.keys())
    print(personal_details.values())
    print('cake' in personal_details)
    print('Mango' in personal_details.values())
    
def dictionary2():
    personal_details = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    for i in personal_details:
        personal_details[i] = personal_details[i].lower().count('t')
    print(personal_details)
    
def sets1():
    s2 = set(range(0, 21, 2))
    print(s2)
    s3 = set(range(0, 21, 3))
    print(s3)
    s4 = set(range(0, 21, 4))
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))
    
def sets2():
    letters = set('Python')
    print(letters)
    letters.add('i')
    print(letters)
    letters2 = frozenset('marathon')
    print(letters.union(letters2))
    print(letters.intersection(letters2))