
def dictionary1(person_dict):
    """function to test basic functionality of dictionaries"""
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
    """function to update values of dict with count of letter t in each existing value"""
    for k,v in person_dict.items():
        person_dict[k] = v.lower().count('t')

    print(person_dict)     

def set1():
    """function to test set functionality with three sets of integers"""
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(1,21):
        if i % 2 == 0:
           s2.add(i)
        if i % 3 == 0:
           s3.add(i)
        if i % 4 == 0:
           s4.add(i)

    print("s2")
    print(s2)
    print("s3")
    print(s3)
    print("s4")
    print(s4)

    print("Is s3 a subset of s2? {}".format(s3.issubset(s2)))
    print("Is s4 a subset of s2? {}".format(s4.issubset(s2)))

def set2():
    """function to test sets and frozensets"""
    py_set = set(list('python'))
    py_set.add('i')
    mar_set = frozenset('marathon')
    print('python set :' + str(py_set))
    print('marathon_set :' + str(mar_set))
    print('union of the two sets: {}'.format(py_set.union(mar_set)))
    print('intersection of the two sets: {}'.format(py_set.intersection(mar_set)))

if __name__ == '__main__':

    person_dict = { 'name':'Chris', 'city':'Seattle', 'cake':'Chocolate' }
    dictionary1(person_dict.copy())
    dictionary2(person_dict.copy())
    set1()
    set2()

