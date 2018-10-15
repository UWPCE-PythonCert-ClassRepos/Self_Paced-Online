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