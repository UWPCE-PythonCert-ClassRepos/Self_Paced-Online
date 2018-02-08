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
    return


def set1():
    s2 = set((list(range(21)))[::2])
    s3 = set((list(range(21)))[::3])
    s4 = set((list(range(21)))[::4])
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))
    return


def set2():
    pythoni = set('Python')
    pythoni.update('i')
    marathon = frozenset('marathon')
    print(pythoni.union(marathon))
    print(pythoni.intersection(marathon))
    return


dictionary1()
dictionary2()
set1()
set2()
