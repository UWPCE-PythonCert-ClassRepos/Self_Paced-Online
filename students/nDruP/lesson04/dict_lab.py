def dictionary1():
    dating_profile = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
    print(dating_profile)
    dating_profile.pop('cake')
    print(dating_profile)
    dating_profile['fruit']='Mango'
    print(dating_profile.keys())
    print(dating_profile.values())
    print('cake' in dating_profile)
    print('Mango' in dating_profile.values())

dictionary1()
