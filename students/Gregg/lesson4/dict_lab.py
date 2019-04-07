#!/usr/bin/env python3
"""Demonstrate python dictionary and set features"""

exist_str = "Is {} in the {}? {}".format


def chris_attributes():
    """Name, city and cake attributes for chris"""
    chris_dict = {
    'name ': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
    }
    return chris_dict

def value_ts(dict_in):
    """"Create a dictionary counting the ts in each of dict_in values"""
    t_dict = {}
    for key, value in dict_in.items():
        t_dict[key] = value.lower().count('t')
    return t_dict

def twenty_divisors(x):
    """A set that contains the numbers between 0 and 20 divisible by x"""
    divisors_set = set()
    for i in range(21):
        if i%x == 0:
            divisors_set.add(i)
    return divisors_set

def exist_thing(item, descriptor, iter_in):
    """Return string describing the existance of key_in in dict_in"""
    exists = item in iter_in
    str_form = exist_str(item, descriptor, exists)
    return str_form

def tests():
    """Test the ________ functions"""
    pass

def exercise_demo(func_in):
    print(f'LessonX: _______ Exercise - {func_in.__doc__}')
    print(f'Demo of {func_in()}')
    print('')

if __name__ == "__main__":
    tests()
    print('Lesson4: Dict Lab Exercise')
    print('Lesson4: Dict Lab Exercise - Dictionaries 1')
    print(
        'Create a dictionary containing “name”, “city”, and “cake” for '
        '“Chris” from “Seattle” who likes “Chocolate” (so the keys should'
        ' be: “name”, etc, and values: “Chris”, etc.'
    )
    chris_dict = chris_attributes()
    print('Display the dictionary.')
    print(chris_dict)
    print('\nDelete the entry for “cake”.')
    del(chris_dict['cake'])
    # prefer this to pop when I'm not using the popped value
    print('\nDisplay the dictionary.')
    print(chris_dict)
    print(
        '\nAdd an entry for “fruit” with “Mango” and display the dictionary.'
    )
    chris_dict['fruit'] = 'Mango'
    print(chris_dict)
    print('\nDisplay the dictionary keys.')
    print(chris_dict.keys())
    print('\nDisplay the dictionary values.')
    print(chris_dict.values())
    print(
        '\nDisplay whether or not “cake” is a key in the '
        'dictionary (i.e. False) (now).'
    )
    print(exist_thing('cake', 'dictionary', chris_dict))
    print(
        '\nDisplay whether or not “Mango” is a value in the '
        'dictionary (i.e. True).'
    )
    print(exist_thing('Mango', 'values', chris_dict.values()))
    print('\nLesson4: Dict Lab Exercise - Dictionaries 2')
    print(
        'Using the dictionary from item 1: Make a dictionary using the same '
        'keys but with the number of ‘t’s in each value as the value (consider '
        'upper and lower case?).'
    )
    print(value_ts(chris_attributes()))
    print('\nLesson4: Set Lab Exercise - Set 1')
    print(
        'Create sets s2, s3 and s4 that contain numbers from zero through '
        'twenty, divisible by 2, 3 and 4.'
    )
    s2 = twenty_divisors(2)
    s3 = twenty_divisors(3)
    s4 = twenty_divisors(4)
    print('Display the sets.')
    print(s2)
    print(s3)
    print(s4)
    print('\nDisplay if s3 is a subset of s2 (False)')
    print(s3.issubset(s2))
    print('\nand if s4 is a subset of s2 (True).')
    print(s4.issubset(s2))

