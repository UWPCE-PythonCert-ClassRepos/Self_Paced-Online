# python 3

# dict_lab.py

# https://uwpce-pythoncert.github.io/PythonCertDevel/modules/DictsAndSets.html#dicts-and-sets


def dict1(keys, values):

    # Create a dictionary containing “name”, “city”, and “cake” for “Chris” from
    # “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and
    # values: “Chris”, etc.)

    d1 = dict(zip(keys, values))
    # Display the dictionary.
    print("\n\nd1: ", d1)
    # Delete the entry for “cake”.
    del d1["cake"]
    # Display the dictionary.
    print("\nd1: ", d1)
    # Add an entry for “fruit” with “Mango”
    d1["fruit"] = "Mango"
    # display the dictionary.
    print("\nd1: ", d1)
    # Display the dictionary keys.
    print("\nd1.keys(): ", d1.keys())
    print("\nlist(d1): ", list(d1))
    # Display the dictionary values.
    print("\nd1.values(): ", d1.values())
    print("\nlist(d1.values()): ", list(d1.values()))
    # Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    print("\n'cake' in d1: ", "cake" in d1)
    # Display whether or not “Mango” is a value in the dictionary (i.e. True).
    print("\n'Mango' in d1.values(): ", "Mango" in d1.values())
    print("\n'Mango' in list(d1.values()): ", "Mango" in list(d1.values()))


def dict2(keys, values):
    """
    Using the dictionary from item 1: Make a dictionary using the same keys
    but with the number of ‘t’s in each value as the value
    (consider upper and lower case?).
    For fun doing the same for "c".
    """
    d2t = {}
    d2c = {}
    for i in range(len(keys)):
        d2t.setdefault(keys[i], values[i].lower().count("t"))
        d2c.setdefault(keys[i], values[i].lower().count("c"))
    print("d2t: ", d2t)
    print("d2c: ", d2c)



k = ["name", "city", "cake"]
v = ["Chris", "Seattle", "Chocolate"]

# dict1(k, v)
# dict2(k, v)

# *********************  sets  *********************
# *********************  set_1  *********************

def set1(div, n):
    """
    div: divisor, integer, range of divisors starting from 2, up to div + 1.
    n: dividend, integer, range dividends starting from 0, up to n + 1.
    returns list of (div - 2) lists of quotients where j % i == 0,
        list[lists][1] is the divisor.
    """
    s = []
    for i in range(2, div + 1):
        ss = []
        for j in range(n + 1):
            if j % i == 0:
                ss.append(j)
        s.append(ss)

    return s

# create dictionary keys. not sure the usage of c_letter is a good fit for set()
def set1_dict_keys(c_letter, div):
    """
    create dictionary keys
    c_letter: a letter common for all the keys.
    div: integer, range from 2 up to div + 1
    returns list of string, c_letter + div[i]
    """
    s1 = set()
    for i in range(2, div + 1):
        s1.add(c_letter + str(i))
    return s1

def set1_dict(keys, sets):
    """
    keys: list of string values used as keys in dictionary of length a.
    sets: list of sub-lists of length a.
    returns dictionary of key: sub-list
    """
    l_s = []
    temp = sorted(sets, key = lambda set_n: set_n[1])
    for item in temp:
        l_s.append(set(item))

    return dict(zip(sorted(keys), l_s))


def set1_run(div, n, letter):

    # Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    # divisible by 2, 3 and 4.

    # set11 = set1(div, n)
    # set11_dict_keys = set1_dict_keys(letter, div)
    dict_sets = set1_dict(set1_dict_keys(letter, div), set1(div, n))
    print()
    # Display the sets.
    for k, v in dict_sets.items():
        print(k, " : ", v)
    # or to ensure ordered output:
    print()
    for k in sorted(dict_sets.keys()):
        print(k, " : ", dict_sets[k])

    # Display if s3 is a subset of s2 (False)
    print("\ns3 is a subset of s2: ", dict_sets["s3"].issubset(dict_sets["s2"]))

    # Display if s4 is a subset of s2 (True)
    print("s4 is a subset of s2: ", dict_sets["s4"].issubset(dict_sets["s2"]))



n = 20
div = 4
letter = "s"

# set1_run(div, n, letter)

# *********************  set_2  *********************

def set2():

    # Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    s = "Python"
    my_set = set(s)
    print(my_set)
    my_set.add("i")
    print(my_set)

    # Create a frozenset with the letters in ‘marathon’.
    s = "marathon"
    my_frozenset = frozenset(s)

    # display the union
    print(my_set.union(my_frozenset))
    print(my_set | my_frozenset)

    # and intersection of the two sets.
    print(my_set.intersection(my_frozenset))
    print(sorted(my_set & my_frozenset))


set2()
