#Dictionaries 1
def dictionaries1():
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d)
    d.pop('cake')
    print(d)
    d['fruit']= 'Mango'
    print(d)
    print(d.keys())
    print(d.values())
    print('cake' in d)
    print('Mango' in d.values())
