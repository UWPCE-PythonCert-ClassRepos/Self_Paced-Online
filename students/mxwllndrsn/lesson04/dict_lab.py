#!/usr/bin/env python3

#uw python 210
#lesson 04
#max anderson

#dictionary lab / set lab

if __name__ == "__main__":

#dictionaries 1
    first_dict = {
                  'Name': 'Chris',
                  'City': 'Seattle',
                  'Cake': 'Chocolate'
                 }

    print('\n', first_dict.items())
    first_dict.pop('Cake')
    print(first_dict.items())
    first_dict.update({'Fruit': 'Mango'})
    print(first_dict.items())
    print(first_dict.keys())
    print(first_dict.values())
    print('Cake' in first_dict.keys())
    print('Mango' in first_dict.values())

#dictionaries 2
    first_dict['Name'] = (first_dict['Name'].count('t')
                       + first_dict['Name'].count('T'))
    first_dict['City'] = (first_dict['City'].count('t')
                       + first_dict['City'].count('T'))
    first_dict['Fruit'] = (first_dict['Fruit'].count('t')
                        + first_dict['Fruit'].count('T'))
    print(first_dict)

#sets 1
    s2, s3, s4 = set(), set(), set()
    for i in range(21):
        if i % 2 == 0:
            s2.update({i})
            if i % 4 == 0:
                s4.update({i})
        elif i % 3 == 0:
            s3.update({i})
    print('\n', s2, s3, s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

#sets 2
    pyset = set('Python')
    pyset.update({'i'})
    print('\n', pyset)
    marset = frozenset('Marathon')
    print(pyset.intersection(marset))
    print(pyset.union(marset))

