def dictionary1():
    dating_profile = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
    print(dating_profile)
    dating_profile.pop('cake')
    print(dating_profile)
    dating_profile['fruit'] = 'Mango'
    print(dating_profile.keys())
    print(dating_profile.values())
    print('cake' in dating_profile)
    print('Mango' in dating_profile.values())
    return dating_profile

def dictionary2():
    t_profile = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
    for x,y in t_profile.items():
        t_profile[x] = (y.lower()).count('t')
    print(t_profile)

def set1():
    s2 = set([0:20:2])
    
dictionary1()
dictionary2()
