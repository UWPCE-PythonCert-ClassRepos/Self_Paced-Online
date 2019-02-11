#Lesson 4 Activities
#Jason Virtue 02/05/2019
#UW Self Paced Python Course


#Create Dictionary for lab
db = {
    'name': 'chris',
    'city': 'seattle',
    'cake': 'chocolate',
    'color': 'red',
    'degree': 'computer science',
}

#Display dictionary
dict(db)

#Delete cake from dictionary
del db['cake']
print(dict(db))
db['fruit'] = 'mango'
print(dict(db))
print(db.keys())
print(db.values())

if 'cake' in db.keys():
    print('yes, cake is in the dictionary')
else:
    print('sorry, no cake in this dictionary')
if 'mango' in db.values():
    print('yes, there is a mango in the dictionary')
else:
    print('NO, mango is not in the dictionary')

def dict_2(data):
    db2 = {}
    for k, v in data.items():
        t_count = v.lower().count('t')
        db2[k] = t_count
    return db2

print(dict_2(db))

def set_1():
    s2 = set()
    for i in range(1, 21):
        if i % 2 == 0:
            s2.update([i])

    s3 = set()
    for i in range(1, 21):
        if i % 3 == 0:
            s3.update([i])

    s4 = set()
    for i in range(1, 21):
        if i % 4 == 0:
            s4.update([i])

    print(s2)
    print(s3)
    print(s4)

    if s3.issubset(s2):
        print('True')
    else:
        print('false')

    if s4.issubset(s2):
        print('Yes, s4 is in s2.')
    else:
        print('negative')

print(set_1())

def set_2():
    sp = set()
    for c in 'python':
        sp.update(c)
    print(sp)
    sp.add('i')
    print()
    print(sp)

    fr_set = set()

    for c in 'marathon':
        fr_set.update(c)
    print(fr_set)
    new = fr_set.intersection(sp)
    print(new)
    new2 = sp.union(fr_set)
    print(new2)

print(set_2())